#!/usr/bin/env python3
"""
从教材 PDF 批量提取所有 Figure
使用 Gemini CLI + 正确编号匹配 + 400 DPI
"""
import os
import re
import subprocess
import time
from PIL import Image
import fitz

# ========== 配置区 ==========
PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
BASE_DIR = "/Users/yueyh/Projects/aca-workflow/notes/differential-geometry/do-carmo-curves-surfaces/figures"
CHAPTER = 1  # 1 或 2

# 工作区临时目录
GEMINI_TEMP_DIR = "/Users/yueyh/.gemini/tmp/figure-extractor"

CHAPTER_PAGE_RANGES = {
    1: (19, 70),
    2: (71, 151),
}

OUTPUT_DIR = f"{BASE_DIR}/chapter{CHAPTER}"
PAGES_DIR = f"{OUTPUT_DIR}/pages_400dpi"


def get_figure_list():
    """从 PDF 解析 Figure 列表"""
    doc = fitz.open(PDF_PATH)
    start_page, end_page = CHAPTER_PAGE_RANGES[CHAPTER]

    figures = {}
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        text = page.get_text()
        matches = re.findall(r'Figure\s*(\d+)[-](\d+)', text, re.IGNORECASE)
        for ch, num in matches:
            if int(ch) == CHAPTER:
                fig_id = f"{ch}-{num}"
                if fig_id not in figures:
                    figures[fig_id] = page_num + 1

    doc.close()
    print(f"Chapter {CHAPTER}: {len(figures)} figures")
    return figures


def extract_pages(figure_pages):
    """提取 400 DPI 页面"""
    os.makedirs(PAGES_DIR, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    scale = 400 / 72

    for page_num in figure_pages:
        page_path = f"{PAGES_DIR}/page-{page_num:03d}.png"
        if not os.path.exists(page_path):
            page = doc[page_num - 1]
            pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
            pix.save(page_path)
            print(f"  提取页面 {page_num}")
    doc.close()


def call_gemini(image_path, figure_ids_on_page):
    """调用 Gemini CLI - 使用 -y 自动确认"""
    figures_str = ", ".join([f"Figure {fid}" for fid in figure_ids_on_page])
    prompt = f'找出 {figures_str} 的位置，只输出：Figure: X-Y, Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX'

    # 复制到临时目录
    temp_path = os.path.join(GEMINI_TEMP_DIR, "temp_page.png")
    os.makedirs(GEMINI_TEMP_DIR, exist_ok=True)
    import shutil
    shutil.copy(image_path, temp_path)

    # 使用 -y 自动确认，不指定模型
    cmd = f'gemini -y "{prompt}" "{temp_path}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
    return result.stdout + result.stderr


def parse_bboxes(text, figure_ids_on_page):
    """解析边界框"""
    results = {}
    for fig_id in figure_ids_on_page:
        pattern = rf'Figure:\s*{fig_id}.*?Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)'
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            x1, y1, x2, y2 = float(match.group(1)), float(match.group(2)), float(match.group(3)), float(match.group(4))
            if x1 > x2: x1, x2 = x2, x1
            if y1 > y2: y1, y2 = y2, y1
            results[fig_id] = (x1, y1, x2, y2)
    return results


def crop_and_save(figure_id, page_num, bbox):
    """裁剪并保存"""
    page_path = f"{PAGES_DIR}/page-{page_num:03d}.png"
    img = Image.open(page_path)
    W, H = img.size

    x1, y1, x2, y2 = bbox
    box = (int(W * x1), int(H * y1), int(W * x2), int(H * y2))
    crop = img.crop(box)

    out_path = os.path.join(OUTPUT_DIR, f"fig_{figure_id}.png")
    crop.save(out_path, quality=95)
    return out_path, box


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n=== Chapter {CHAPTER} Figure 提取 ===\n")

    # 1. 获取 Figure 列表
    figures = get_figure_list()
    figure_pages = set(figures.values())

    # 2. 提取页面
    print("\n提取页面...")
    extract_pages(figure_pages)

    # 3. 按页处理
    print("\n识别 Figure...")
    results = []
    crop_positions = []

    for page_num in sorted(figure_pages):
        page_figs = [k for k, v in figures.items() if v == page_num]
        if not page_figs:
            continue

        print(f"\n[Page {page_num}] {len(page_figs)} figures...")
        page_path = f"{PAGES_DIR}/page-{page_num:03d}.png"

        try:
            text = call_gemini(page_path, page_figs)
            bboxes = parse_bboxes(text, page_figs)
            print(f"  识别到 {len(bboxes)} 个")
        except Exception as e:
            print(f"  错误: {e}")
            bboxes = {}

        for fig_id in page_figs:
            if fig_id in bboxes:
                out_path, box = crop_and_save(fig_id, page_num, bboxes[fig_id])
                print(f"  ✓ fig_{fig_id}.png")
                results.append((fig_id, "OK"))
                crop_positions.append({
                    "figure": f"fig_{fig_id}", "source_page": page_num,
                    "left": box[0], "top": box[1], "right": box[2], "bottom": box[3]
                })
            else:
                print(f"  ⚠️ fig_{fig_id} 未识别")
                results.append((fig_id, "MISSING"))

        time.sleep(2)

    # 4. 保存 CSV
    csv_path = os.path.join(OUTPUT_DIR, "figure_crop_positions.csv")
    with open(csv_path, "w") as f:
        f.write("figure,source_page,left,top,right,bottom\n")
        for pos in crop_positions:
            f.write(f"{pos['figure']},{pos['source_page']},{pos['left']},{pos['top']},{pos['right']},{pos['bottom']}\n")

    print(f"\n=== 完成 ===")
    print(f"成功: {sum(1 for r in results if r[1] == 'OK')}/{len(results)}")
    print(f"CSV: {csv_path}")


if __name__ == "__main__":
    main()
