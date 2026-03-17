#!/usr/bin/env python3
"""
从 Do Carmo 教材提取 Chapter 1 和 Chapter 2 的所有 Figure
使用 Gemini CLI 检测边界框 + 正确编号命名 + 保存裁剪位置到 CSV
"""
import os
import re
import subprocess
import time
import fitz
from PIL import Image

# ========== 配置区 ==========
PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
BASE_DIR = "/Users/yueyh/Projects/aca-workflow/notes/differential-geometry/do-carmo-curves-surfaces/figures"

# Gemini 临时目录
GEMINI_TEMP_DIR = "/Users/yueyh/.gemini/tmp/figure-extractor"

# Chapter 配置
CHAPTER_PAGE_RANGES = {
    1: (19, 70),   # Chapter 1: pages 19-70
    2: (71, 151),  # Chapter 2: pages 71-151
}

def get_figure_list(chapter):
    """从 PDF 解析指定 Chapter 的所有 Figure 编号和页码"""
    doc = fitz.open(PDF_PATH)
    start_page, end_page = CHAPTER_PAGE_RANGES[chapter]

    figures = {}
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        text = page.get_text()
        # 匹配 Figure 1-XX 或 Figure 2-XX
        matches = re.findall(r'Figure\s*(\d+)[-](\d+)', text, re.IGNORECASE)
        for ch, num in matches:
            if int(ch) == chapter:
                fig_id = f"{ch}-{num}"
                if fig_id not in figures:
                    figures[fig_id] = page_num + 1  # 1-based 页码

    doc.close()
    return figures


def extract_page(page_num, output_dir, dpi=400):
    """提取指定页面的 400 DPI 图片"""
    os.makedirs(output_dir, exist_ok=True)
    page_path = os.path.join(output_dir, f"page-{page_num:03d}.png")

    if not os.path.exists(page_path):
        doc = fitz.open(PDF_PATH)
        page = doc[page_num - 1]  # 0-based
        scale = dpi / 72
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
        pix.save(page_path)
        doc.close()
        print(f"  提取页面 {page_num}")

    return page_path


def call_gemini(image_path, figure_ids_on_page):
    """调用 Gemini CLI 识别 Figure 位置"""
    figures_str = ", ".join([f"Figure {fid}" for fid in figure_ids_on_page])
    prompt = f'''找出 {figures_str} 的精确位置。

输出格式（每个 Figure 必须输出一行）：
Figure: X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 "Figure X-Y"
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02 边距'''

    # 复制到临时目录
    temp_path = os.path.join(GEMINI_TEMP_DIR, "temp_page.png")
    os.makedirs(GEMINI_TEMP_DIR, exist_ok=True)
    import shutil
    shutil.copy(image_path, temp_path)

    # 使用 gemini CLI，-y 自动确认
    cmd = f'gemini -y "{prompt}" "{temp_path}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
    return result.stdout + result.stderr


def parse_bboxes(text, figure_ids_on_page):
    """解析 Gemini 输出的边界框"""
    results = {}
    for fig_id in figure_ids_on_page:
        # 匹配: Figure: 1-1 ... Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
        pattern = rf'Figure:\s*{re.escape(fig_id)}.*?Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)'
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            x1, y1, x2, y2 = float(match.group(1)), float(match.group(2)), float(match.group(3)), float(match.group(4))
            # 修正坐标顺序
            if x1 > x2: x1, x2 = x2, x1
            if y1 > y2: y1, y2 = y2, y1
            results[fig_id] = (x1, y1, x2, y2)
    return results


def crop_and_save(figure_id, page_num, bbox, pages_dir, output_dir):
    """裁剪并保存 Figure"""
    page_path = os.path.join(pages_dir, f"page-{page_num:03d}.png")
    img = Image.open(page_path)
    W, H = img.size

    x1, y1, x2, y2 = bbox
    box = (int(W * x1), int(H * y1), int(W * x2), int(H * y2))
    crop = img.crop(box)

    out_path = os.path.join(output_dir, f"fig_{figure_id}.png")
    crop.save(out_path, quality=95)
    return out_path, box


def process_chapter(chapter):
    """处理单个 Chapter"""
    output_dir = f"{BASE_DIR}/chapter{chapter}"
    pages_dir = f"{output_dir}/pages_400dpi"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(pages_dir, exist_ok=True)

    print(f"\n{'='*50}")
    print(f"处理 Chapter {chapter}")
    print(f"{'='*50}\n")

    # 1. 获取 Figure 列表
    figures = get_figure_list(chapter)
    print(f"Chapter {chapter}: 找到 {len(figures)} 个 Figure")
    for fig_id in sorted(figures.keys(), key=lambda x: (int(x.split('-')[0]), int(x.split('-')[1]))):
        print(f"  Figure {fig_id}: Page {figures[fig_id]}")

    # 2. 提取页面
    figure_pages = set(figures.values())
    print(f"\n提取 {len(figure_pages)} 个页面...")
    for page_num in figure_pages:
        extract_page(page_num, pages_dir)

    # 3. 按页处理：每页调用一次 Gemini
    results = []
    crop_positions = []

    for page_num in sorted(figure_pages):
        page_figs = [k for k, v in figures.items() if v == page_num]
        if not page_figs:
            continue

        # 按编号排序
        page_figs.sort(key=lambda x: int(x.split('-')[1]))

        print(f"\n[Page {page_num}] 处理 {len(page_figs)} 个 figures: {page_figs}")
        page_path = os.path.join(pages_dir, f"page-{page_num:03d}.png")

        try:
            text = call_gemini(page_path, page_figs)
            bboxes = parse_bboxes(text, page_figs)
            print(f"  识别到 {len(bboxes)} 个边界框")
            # 调试输出
            if len(bboxes) != len(page_figs):
                print(f"  ⚠️ 原始输出:\n{text[:500]}")
        except Exception as e:
            print(f"  错误: {e}")
            bboxes = {}

        for fig_id in page_figs:
            if fig_id in bboxes:
                out_path, box = crop_and_save(fig_id, page_num, bboxes[fig_id], pages_dir, output_dir)
                print(f"  ✓ fig_{fig_id}.png: {box}")
                results.append((fig_id, "OK"))
                crop_positions.append({
                    "figure": f"fig_{fig_id}",
                    "source_page": page_num,
                    "left": box[0], "top": box[1],
                    "right": box[2], "bottom": box[3]
                })
            else:
                print(f"  ⚠️ fig_{fig_id} 未识别")
                results.append((fig_id, "MISSING"))

        time.sleep(2)  # 避免 API 限流

    # 4. 保存 CSV
    csv_path = os.path.join(output_dir, "figure_crop_positions.csv")
    with open(csv_path, "w") as f:
        f.write("figure,source_page,left,top,right,bottom\n")
        for pos in crop_positions:
            f.write(f"{pos['figure']},{pos['source_page']},{pos['left']},{pos['top']},{pos['right']},{pos['bottom']}\n")

    print(f"\n{'='*50}")
    print(f"Chapter {chapter} 完成!")
    print(f"成功: {sum(1 for r in results if r[1] == 'OK')}/{len(results)}")
    print(f"CSV: {csv_path}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    # 处理 Chapter 1
    process_chapter(1)

    # 处理 Chapter 2
    process_chapter(2)

    print("\n=== 所有 Chapter 处理完成 ===")
