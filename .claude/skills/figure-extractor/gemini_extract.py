#!/usr/bin/env python3
"""
Gemini Vision Figure Extractor
使用 Gemini 3.1 Pro 视觉模型直接从页面图片中提取 figures
"""

import os
import sys
import json
import base64
import argparse
import urllib.request
import urllib.error
import ssl
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# 忽略 SSL 证书验证
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 配置
# 可用模型: gemini-2.5-flash-image, gemini-3.1-pro-preview, gemini-3.1-flash-image-preview
DEFAULT_MODEL = "gemini-3.1-pro-preview"  # 默认使用 gemini-3.1-pro
API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def encode_image(image_path):
    """将图片编码为 base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')


def extract_figures_with_gemini(image_path: str, api_key: str, model: str = DEFAULT_MODEL) -> list:
    """
    使用 Gemini 提取页面中的 figures
    返回: [{"figure_id": "1-1", "bbox": [x1, y1, x2, y2]}, ...]
    """
    url = f"{API_BASE_URL}/{model}:generateContent"

    # 读取图片并编码
    image_base64 = encode_image(image_path)

    prompt = """你是一个专业的教材图像内容提取助手。我会给你提供一张或多张微分几何教材（do Carmo《曲线与曲面微分几何》）的扫描页面图片。

你的任务是：
1. 识别图片中所有的数学插图（Figure），每张插图都有格式为"Figure X-XX"的图注标签。
2. 对每张插图的位置，用相对坐标（left, upper, right, lower，以图片宽高的百分比表示）精确标定其边界框（bounding box)。
3. 对每张 Figure，给出：
   - 图注编号（如 Figure 1-5）
   - 图在页面中的大致位置（左上/右上/左下/右下/居中/全宽）
   - 图的内容简述（用1-2句中文描述其数学含义或所表达的几何概念）
   - 相对坐标 bounding box（格式：x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX）

注意：
- 忽略文字段落、公式和页眉页码，只关注由线条、坐标轴、曲线构成的图形。
- 如果一张页面包含多张紧邻的小图（如左右并排），请分别单独标定每张。
- bounding box 应留有少量边距，不要截断坐标轴标签和图注文字。

请按如下格式输出（每张图一个块）：

---
编号: Figure X-XX
位置: [左上 / 右上 / 居中 / 全宽 等]
内容简述: [1-2句中文描述]
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
---

如果页面中没有 Figure，请输出"无 Figure"。"""

    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {
                    "inlineData": {
                        "mimeType": "image/png",
                        "data": image_base64
                    }
                }
            ]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 4096
        }
    }

    data = json.dumps(payload).encode('utf-8')

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'Content-Type': 'application/json',
            'x-goog-api-key': api_key
        },
        method='POST'
    )

    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
            result = json.loads(response.read().decode('utf-8'))

            # 提取文本响应
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    text = candidate['content']['parts'][0].get('text', '')

                    # 检查是否无 Figure
                    if '无 Figure' in text or '没有Figure' in text:
                        return []

                    # 解析新格式
                    # 格式：编号: Figure X-XX, 位置: xxx, 内容简述: xxx, Bounding Box: x1=0.XX...
                    import re
                    figures = []

                    # 按 --- 分割多个块
                    blocks = text.split('---')

                    for block in blocks:
                        block = block.strip()
                        if not block or '编号:' not in block:
                            continue

                        # 提取 figure_id
                        id_match = re.search(r'编号:\s*Figure\s*(\d+[-\s]\d+|\d+)', block)
                        if not id_match:
                            continue
                        figure_id = id_match.group(1).replace(' ', '-')

                        # 提取 bounding box (相对坐标 0.XX)
                        bbox_match = re.search(r'Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)', block)
                        if bbox_match:
                            # 转换为绝对坐标（百分比）
                            x1 = float(bbox_match.group(1))
                            y1 = float(bbox_match.group(2))
                            x2 = float(bbox_match.group(3))
                            y2 = float(bbox_match.group(4))
                            bbox = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
                        else:
                            bbox = {'x1': 0.1, 'y1': 0.1, 'x2': 0.9, 'y2': 0.9}

                        figures.append({
                            'figure_id': figure_id,
                            'caption': f'Figure {figure_id}',
                            'bbox': bbox
                        })

                    if figures:
                        return figures

                    print(f"⚠️ 无法解析格式，原始响应: {text[:800]}")
                    return []

            print(f"❌ API 响应格式异常: {result}")
            return []

    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"❌ HTTP 错误 {e.code}:")
        try:
            error_json = json.loads(error_body)
            print(json.dumps(error_json, indent=2, ensure_ascii=False))
        except:
            print(error_body)
        return []
    except Exception as e:
        print(f"❌ 错误: {e}")
        return []


def crop_and_save(image_path: str, bbox: dict, output_path: str) -> bool:
    """根据边界框裁剪并保存图片"""
    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"❌ 无法读取图片: {image_path}")
            return False

        h, w = img.shape[:2]

        # 边界框坐标
        x1 = max(0, int(bbox.get('x1', 0)))
        y1 = max(0, int(bbox.get('y1', 0)))
        x2 = min(w, int(bbox.get('x2', w)))
        y2 = min(h, int(bbox.get('y2', h)))

        # 裁剪
        crop = img[y1:y2, x1:x2]

        # 保存
        cv2.imwrite(output_path, crop)
        return True

    except Exception as e:
        print(f"❌ 裁剪失败: {e}")
        return False


def process_page(image_path: str, output_dir: str, api_key: str, model: str = DEFAULT_MODEL):
    """处理单张页面，提取所有 figures"""
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n{'='*50}")
    print(f"📄 处理: {os.path.basename(image_path)}")
    print(f"{'='*50}")

    # 调用 Gemini 提取 figures
    print("⏳ 正在用 Gemini 分析页面...")
    figures = extract_figures_with_gemini(image_path, api_key, model)

    if not figures:
        print("⚠️ 未找到任何 Figure")
        return []

    print(f"✅ 找到 {len(figures)} 个 figures")

    # 裁剪并保存
    saved = []
    for fig in figures:
        fig_id = fig.get('figure_id', 'unknown')
        bbox = fig.get('bbox', {})

        # 生成输出文件名
        output_path = os.path.join(output_dir, f"fig_{fig_id}.png")

        # 处理重复文件名
        if os.path.exists(output_path):
            base, ext = os.path.splitext(output_path)
            counter = 1
            while os.path.exists(f"{base}_{counter}{ext}"):
                counter += 1
            output_path = f"{base}_{counter}{ext}"

        # 裁剪保存
        if crop_and_save(image_path, bbox, output_path):
            print(f"  ✓ fig_{fig_id}.png")
            saved.append(output_path)
        else:
            print(f"  ✗ fig_{fig_id}.png (失败)")

    return saved


def main():
    parser = argparse.ArgumentParser(description='Gemini Vision 图表提取器')
    parser.add_argument("input", help="输入页面图片路径")
    parser.add_argument("-o", "--output", default="figures_output", help="输出目录")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL, help="Gemini 模型")
    parser.add_argument("-k", "--api-key", default=None, help="API Key")

    args = parser.parse_args()

    # 获取 API Key
    api_key = args.api_key or os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("❌ 请设置 GEMINI_API_KEY 环境变量或使用 -k 参数")
        sys.exit(1)

    if not os.path.exists(args.input):
        print(f"❌ 文件不存在: {args.input}")
        sys.exit(1)

    print(f"🤖 使用模型: {args.model}")
    print(f"📁 输出目录: {args.output}")

    # 处理页面
    saved = process_page(args.input, args.output, api_key, args.model)

    print(f"\n{'='*50}")
    print(f"✅ 完成！共提取 {len(saved)} 个 figures")
    print(f"📁 输出目录: {args.output}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
