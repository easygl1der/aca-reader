#!/usr/bin/env python3
"""
批量从教材页面提取所有 Figure
用法: python3 batch_extract.py [pages_dir] [output_dir]
"""
import os
import sys
import json
import base64
import urllib.request
import ssl
import re
from PIL import Image

# 配置（可通过命令行参数覆盖）
PAGES_DIR = sys.argv[1] if len(sys.argv) > 1 else './pages'
OUTPUT_DIR = sys.argv[2] if len(sys.argv) > 2 else './figures'

API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL = 'gemini-3.1-flash-image-preview'

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

PROMPT = '''分析以下教材页面图片，识别所有数学插图（Figure）。

**重要要求：**
- bounding box 必须包含图注文字（Figure X-XX）
- 四周留适当边距（约 0.02-0.03），确保完整包含坐标轴标签和图注
- 如果图注在图形下方，y2 要延伸到包含图注

对每张 Figure 输出：
编号: Figure X-XX
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 只识别图形，忽略纯文字段落'''

def extract_figures(image_path):
    """调用 Gemini 识别图片中的 figures"""
    with open(image_path, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('utf-8')

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'
    payload = {
        'contents': [{
            'parts': [
                {'text': PROMPT},
                {'inlineData': {'mimeType': 'image/png', 'data': image_base64}}
            ]
        }],
        'generationConfig': {'temperature': 0.1, 'maxOutputTokens': 4096}
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={
        'Content-Type': 'application/json',
        'x-goog-api-key': API_KEY
    }, method='POST')

    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'candidates' in result:
                return result['candidates'][0]['content']['parts'][0].get('text', '')
    except Exception as e:
        print(f'  Error: {e}')
    return None

def parse_coordinates(text, img_w=0, img_h=0):
    """解析 Gemini 输出，提取坐标"""
    figures = []
    # 按 --- 或空行分割
    blocks = re.split(r'---+|\n\n', text)
    for block in blocks:
        # 提取编号
        id_match = re.search(r'Figure\s*(\d+[-~]\d+|\d+)', block, re.IGNORECASE)
        # 先尝试匹配相对坐标 (0.XX)
        bbox_match = re.search(r'Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)', block)
        if id_match and bbox_match:
            fig_id = id_match.group(1).replace('~', '-')
            coords = {
                'x1': float(bbox_match.group(1)),
                'y1': float(bbox_match.group(2)),
                'x2': float(bbox_match.group(3)),
                'y2': float(bbox_match.group(4))
            }
            # 修正坐标顺序（如果 x1>x2 或 y1>y2）
            if coords['x1'] > coords['x2']:
                coords['x1'], coords['x2'] = coords['x2'], coords['x1']
            if coords['y1'] > coords['y2']:
                coords['y1'], coords['y2'] = coords['y2'], coords['y1']
            # 验证坐标有效性
            if coords['x1'] < coords['x2'] and coords['y1'] < coords['y2']:
                figures.append({'id': fig_id, 'coords': coords})
            continue

        # 如果没有相对坐标，尝试匹配绝对坐标 (如 x1=129, y1=548)
        abs_bbox_match = re.search(r'Bounding Box:\s*x1=(\d+),\s*y1=(\d+),\s*x2=(\d+),\s*y2=(\d+)', block)
        if id_match and abs_bbox_match and img_w > 0 and img_h > 0:
            fig_id = id_match.group(1).replace('~', '-')
            # 转换为相对坐标
            coords = {
                'x1': int(abs_bbox_match.group(1)) / img_w,
                'y1': int(abs_bbox_match.group(2)) / img_h,
                'x2': int(abs_bbox_match.group(3)) / img_w,
                'y2': int(abs_bbox_match.group(4)) / img_h
            }
            # 验证坐标有效性
            if coords['x1'] < coords['x2'] and coords['y1'] < coords['y2']:
                figures.append({'id': fig_id, 'coords': coords})
    return figures

def crop_figures(page_name, figures):
    """裁剪并保存 figures"""
    page_path = os.path.join(PAGES_DIR, page_name)
    img = Image.open(page_path)
    W, H = img.size

    saved = []
    for fig in figures:
        fig_id = fig['id']
        c = fig['coords']
        box = (int(W * c['x1']), int(H * c['y1']), int(W * c['x2']), int(H * c['y2']))
        crop = img.crop(box)

        # 文件名: fig_2-1.png, fig_2-2.png 等（直接覆盖）
        out_name = f'fig_{fig_id}.png'
        out_path = os.path.join(OUTPUT_DIR, out_name)

        crop.save(out_path, quality=95)
        saved.append(out_name)
        print(f'  ✓ {out_name}: {box}')

    return saved

# 主循环：处理所有页面
pages = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith('.png')])

# 只处理还没处理过的页面（ch-001 到 ch-040）
for page in pages:
    page_num = page.replace('ch-', '').replace('.png', '')
    page_num = int(page_num)
    if page_num > 40:
        break

    print(f'\n[{page}] 识别中...')
    page_path = os.path.join(PAGES_DIR, page)

    # 获取图片尺寸用于坐标转换
    img = Image.open(page_path)
    W, H = img.size

    text = extract_figures(page_path)
    if not text:
        print(f'  ⚠️ 识别失败')
        continue

    # 检查是否有 "无 Figure" 或 "没有"
    if '无Figure' in text or '没有Figure' in text or '没有图' in text:
        print(f'  ⚠️ 本页无插图')
        continue

    figures = parse_coordinates(text, W, H)
    if figures:
        print(f'  找到 {len(figures)} 个 figures')
        crop_figures(page, figures)
    else:
        print(f'  ⚠️ 无法解析坐标')
        print(f'  原始输出: {text[:200]}')
