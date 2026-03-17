#!/usr/bin/env python3
"""
从教材页面提取所有 Figure - 使用 Gemini 视觉识别
"""
import os
import json
import base64
import urllib.request
import ssl
import re
from PIL import Image
import time

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# ========== 配置区 ==========
PAGES_DIR = "/Users/yueyh/Projects/aca-workflow/notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter1/pages_400dpi"
OUTPUT_DIR = "/Users/yueyh/Projects/aca-workflow/notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter1"
API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL = 'gemini-2.5-flash-preview-05-20'

# Figure 列表（从 PDF 分析得到）
FIGURES = {
    # (figure_id, page_num)
    ("1-1", 19), ("1-2", 19), ("1-3", 19), ("1-4", 19),
    ("1-5", 20), ("1-6", 21), ("1-7", 23),
    ("1-8", 24), ("1-9", 24), ("1-10", 25), ("1-11", 26),
    ("1-12", 27), ("1-13", 30), ("1-14", 34), ("1-15", 35),
    ("1-16", 38), ("1-17", 41), ("1-18", 45), ("1-19", 46),
    ("1-20", 48), ("1-21", 48), ("1-22", 50), ("1-23", 51),
    ("1-24", 51), ("1-25", 53), ("1-26", 54), ("1-27", 56),
    ("1-28", 57), ("1-29", 58), ("1-30", 59), ("1-31", 59),
    ("1-32", 60), ("1-33", 62), ("1-34", 63), ("1-35", 65),
    ("1-36", 65), ("1-37", 66), ("1-38", 67), ("1-39", 67),
    ("1-40", 67), ("1-41", 67),
}

PROMPT = '''看这张教材原图，找出 Figure {figure_id} 的精确位置。

输出格式（必须精确）：
Figure: {figure_id}
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 "Figure {figure_id}"
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02-0.03 边距，确保完整'''

def call_gemini(image_path, figure_id):
    """调用 Gemini 识别单个 figure"""
    with open(image_path, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('utf-8')

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'
    prompt = PROMPT.format(figure_id=figure_id)
    payload = {
        'contents': [{
            'parts': [
                {'text': prompt},
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

def parse_bbox(text):
    """解析 Gemini 输出的边界框"""
    bbox_match = re.search(r'Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)', text)
    if bbox_match:
        x1, y1, x2, y2 = float(bbox_match.group(1)), float(bbox_match.group(2)), float(bbox_match.group(3)), float(bbox_match.group(4))
        # 修正坐标顺序
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        return x1, y1, x2, y2
    return None

def crop_and_save(figure_id, page_num, bbox):
    """裁剪并保存图片"""
    page_path = os.path.join(PAGES_DIR, f"page-{page_num:03d}.png")
    img = Image.open(page_path)
    W, H = img.size

    x1, y1, x2, y2 = bbox
    box = (int(W * x1), int(H * y1), int(W * x2), int(H * y2))
    crop = img.crop(box)

    out_name = f"fig_{figure_id}.png"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    crop.save(out_path, quality=95)
    return out_path

# 主循环
os.makedirs(OUTPUT_DIR, exist_ok=True)

results = []
for figure_id, page_num in sorted(FIGURES, key=lambda x: (int(x[0].split('-')[0]), int(x[0].split('-')[1]))):
    print(f"\n[{figure_id}] Page {page_num} 识别中...")
    page_path = os.path.join(PAGES_DIR, f"page-{page_num:03d}.png")

    text = call_gemini(page_path, figure_id)
    if not text:
        print(f'  ⚠️ 识别失败')
        results.append((figure_id, page_num, "FAILED", None))
        continue

    bbox = parse_bbox(text)
    if bbox:
        out_path = crop_and_save(figure_id, page_num, bbox)
        print(f'  ✓ {out_path}: {bbox}')
        results.append((figure_id, page_num, "OK", bbox))
    else:
        print(f'  ⚠️ 无法解析坐标')
        print(f'  原始输出: {text[:300]}')
        results.append((figure_id, page_num, "PARSE_ERROR", text[:300]))

    time.sleep(0.5)  # 避免 API 限流

# 保存结果到 CSV
csv_path = os.path.join(OUTPUT_DIR, "figure_extraction_results.csv")
with open(csv_path, "w") as f:
    f.write("figure_id,page_num,status,bbox\n")
    for figure_id, page_num, status, bbox in results:
        f.write(f"{figure_id},{page_num},{status},{bbox}\n")

print(f"\n\n完成！结果保存到: {csv_path}")
print(f"成功提取: {sum(1 for r in results if r[2] == 'OK')}/{len(results)}")
