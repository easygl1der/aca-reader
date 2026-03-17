#!/usr/bin/env python3
"""
提取缺失的 Chapter 1 Figures - 逐个处理
"""
import os
import re
import subprocess
import time
import fitz
from PIL import Image

# ========== 配置区 ==========
PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
OUTPUT_DIR = "/Users/yueyh/Projects/aca-workflow/notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter1"
PAGES_DIR = f"{OUTPUT_DIR}/pages_400dpi"
GEMINI_TEMP_DIR = "/Users/yueyh/.gemini/tmp/figure-extractor"

# 缺失的 Figures (figure_id, page_num)
MISSING_FIGURES = [
    ("1-5", 20),
    ("1-8", 24),
    ("1-9", 24),
    ("1-14", 34),
    ("1-15", 35),
    ("1-23", 51),
    ("1-24", 51),
    ("1-28", 57),
    ("1-30", 59),
    ("1-31", 59),
    ("1-34", 63),
]

def extract_page(page_num):
    """提取指定页面的 400 DPI 图片"""
    os.makedirs(PAGES_DIR, exist_ok=True)
    page_path = os.path.join(PAGES_DIR, f"page-{page_num:03d}.png")

    if not os.path.exists(page_path):
        doc = fitz.open(PDF_PATH)
        page = doc[page_num - 1]  # 0-based
        scale = 400 / 72
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
        pix.save(page_path)
        doc.close()
        print(f"  提取页面 {page_num}")

    return page_path


def call_gemini(image_path, figure_id):
    """调用 Gemini CLI 识别单个 Figure 位置"""
    prompt = f'''找出 Figure {figure_id} 的精确位置。

输出格式（必须精确）：
Figure: {figure_id}
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 "Figure {figure_id}"
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02 边距'''

    # 复制到临时目录
    temp_path = os.path.join(GEMINI_TEMP_DIR, "temp_page.png")
    os.makedirs(GEMINI_TEMP_DIR, exist_ok=True)
    import shutil
    shutil.copy(image_path, temp_path)

    # 使用 gemini CLI，-y 自动确认
    cmd = f'gemini -y "{prompt}" "{temp_path}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=180)
    return result.stdout + result.stderr


def parse_bbox(text, figure_id):
    """解析 Gemini 输出的边界框"""
    pattern = rf'Figure:\s*{re.escape(figure_id)}.*?Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)'
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        x1, y1, x2, y2 = float(match.group(1)), float(match.group(2)), float(match.group(3)), float(match.group(4))
        # 修正坐标顺序
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        return (x1, y1, x2, y2)
    return None


def crop_and_save(figure_id, page_num, bbox):
    """裁剪并保存 Figure"""
    page_path = os.path.join(PAGES_DIR, f"page-{page_num:03d}.png")
    img = Image.open(page_path)
    W, H = img.size

    x1, y1, x2, y2 = bbox
    box = (int(W * x1), int(H * y1), int(W * x2), int(H * y2))
    crop = img.crop(box)

    out_path = os.path.join(OUTPUT_DIR, f"fig_{figure_id}.png")
    crop.save(out_path, quality=95)
    return out_path, box


def main():
    print("=== 提取缺失的 Chapter 1 Figures ===\n")

    # 按页面分组处理
    pages_with_missing = {}
    for fig_id, page_num in MISSING_FIGURES:
        if page_num not in pages_with_missing:
            pages_with_missing[page_num] = []
        pages_with_missing[page_num].append(fig_id)

    crop_positions = []

    for page_num in sorted(pages_with_missing.keys()):
        figure_ids = pages_with_missing[page_num]
        print(f"\n[Page {page_num}] 处理: {figure_ids}")

        # 提取页面
        page_path = extract_page(page_num)

        for figure_id in figure_ids:
            print(f"  处理 Figure {figure_id}...", end=" ")

            try:
                text = call_gemini(page_path, figure_id)
                bbox = parse_bbox(text, figure_id)

                if bbox:
                    out_path, box = crop_and_save(figure_id, page_num, bbox)
                    print(f"✓ ({box})")
                    crop_positions.append({
                        "figure": f"fig_{figure_id}",
                        "source_page": page_num,
                        "left": box[0], "top": box[1],
                        "right": box[2], "bottom": box[3]
                    })
                else:
                    print(f"⚠️ 无法解析")
                    print(f"   原始输出: {text[:200]}")
            except subprocess.TimeoutExpired:
                print(f"⚠️ 超时")
            except Exception as e:
                print(f"⚠️ 错误: {e}")

            time.sleep(3)  # 避免 API 限流

    # 更新 CSV
    csv_path = os.path.join(OUTPUT_DIR, "figure_crop_positions.csv")
    print(f"\n更新 CSV: {csv_path}")

    # 读取现有 CSV
    existing = {}
    if os.path.exists(csv_path):
        with open(csv_path, "r") as f:
            lines = f.readlines()[1:]  # skip header
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) >= 6:
                    existing[parts[0]] = line.strip()

    # 添加新的
    for pos in crop_positions:
        key = pos["figure"]
        line = f"{pos['figure']},{pos['source_page']},{pos['left']},{pos['top']},{pos['right']},{pos['bottom']}"
        existing[key] = line

    # 写入
    with open(csv_path, "w") as f:
        f.write("figure,source_page,left,top,right,bottom\n")
        for key in sorted(existing.keys(), key=lambda x: (int(x.split('-')[0]), int(x.split('-')[1]))):
            f.write(existing[key] + "\n")

    print(f"\n完成! 新增 {len(crop_positions)} 个 Figures")
    print(f"总共存入 {len(existing)} 个 Figures")


if __name__ == "__main__":
    main()
