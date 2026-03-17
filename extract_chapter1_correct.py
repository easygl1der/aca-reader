#!/usr/bin/env python3
"""
从教材页面提取 Figure - 使用 CV 方法 + 正确编号
"""
import os
import re
import fitz
import cv2
import numpy as np
from PIL import Image
from collections import defaultdict

# 配置
PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
OUTPUT_DIR = "/Users/yueyh/Projects/aca-workflow/notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter1"
DPI = 400

# 第一步：从 PDF 找出所有 Figure 及其页面
doc = fitz.open(PDF_PATH)

figures = {}  # figure_num -> page_num
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    # 匹配 Figure 1-XX 或 Figure 2-XX
    matches = re.findall(r'Figure\s*(\d+)[-](\d+)', text, re.IGNORECASE)
    for ch, num in matches:
        fig_id = f"{ch}-{num}"
        if fig_id not in figures:
            figures[fig_id] = page_num + 1  # 1-based

doc.close()

print(f"找到 {len(figures)} 个 Figure")
print("前10个:", list(sorted(figures.items(), key=lambda x: (int(x[0].split('-')[0]), int(x[0].split('-')[1])))[:10]))

# 第二步：提取页面图片
pages_dir = os.path.join(OUTPUT_DIR, "pages_400dpi")
os.makedirs(pages_dir, exist_ok=True)

doc = fitz.open(PDF_PATH)
scale = DPI / 72

# 只提取有 figure 的页面
figure_pages = set(figures.values())
for page_num in figure_pages:
    page = doc[page_num - 1]  # 0-based
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
    pix.save(os.path.join(pages_dir, f"page-{page_num:03d}.png"))

doc.close()
print(f"\n提取了 {len(figure_pages)} 个页面到 {pages_dir}")

# 第三步：使用 figure_extractor 提取每页的 figures
# 然后匹配正确的编号
import subprocess

page_figures = defaultdict(list)  # page_num -> [(fig_id, bbox), ...]

for page_num in sorted(figure_pages):
    page_path = os.path.join(pages_dir, f"page-{page_num:03d}.png")

    # 运行 figure_extractor
    result = subprocess.run(
        ["python3", "/Users/yueyh/Projects/aca-workflow/figure_extractor.py",
         page_path, "-o", OUTPUT_DIR, "--no-gemini"],
        capture_output=True, text=True
    )

    # 解析输出，获取裁剪位置
    debug_csv = os.path.join(OUTPUT_DIR, f"page-{page_num:03d}_debug.csv")
    if os.path.exists(debug_csv):
        with open(debug_csv) as f:
            lines = f.readlines()[1:]  # skip header
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) >= 6 and parts[5] == "True":  # cv_keep
                    left, right, top, bottom = parts[2], parts[3], parts[4], parts[5]
                    page_figures[page_num].append({
                        "left": int(left), "right": int(right),
                        "top": int(top), "bottom": int(bottom)
                    })

# 第四步：为每页的 figures 分配正确的编号
# 假设每页的 figures 按从上到下顺序对应该页的第一个 Figure 编号
for page_num in sorted(page_figures.keys()):
    page_figs = page_figures[page_num]
    # 找到该页第一个 figure 编号
    page_fig_ids = [k for k, v in figures.items() if v == page_num]
    page_fig_ids.sort(key=lambda x: int(x.split('-')[1]))

    if page_fig_ids:
        start_num = int(page_fig_ids[0].split('-')[1])
        for i, fig_data in enumerate(page_figs):
            fig_id = f"1-{start_num + i}"
            if fig_id in figures:
                # 裁剪图片
                page_path = os.path.join(pages_dir, f"page-{page_num:03d}.png")
                img = Image.open(page_path)
                box = (fig_data["left"], fig_data["top"], fig_data["right"], fig_data["bottom"])
                crop = img.crop(box)

                out_path = os.path.join(OUTPUT_DIR, f"fig_{fig_id}.png")
                crop.save(out_path, quality=95)
                print(f"✓ fig_{fig_id}.png (Page {page_num})")

print("\n完成!")
