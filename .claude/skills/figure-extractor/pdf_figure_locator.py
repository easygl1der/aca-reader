#!/usr/bin/env python3
"""
PDF Figure Locator - 根据图注定位提取图片

直接从 PDF 中根据 Figure 标注定位并提取图片。
"""

import os
import re
import argparse
from pathlib import Path

# 尝试导入 PDF 库
try:
    import fitz  # PyMuPDF
    PDF_LIB = "pymupdf"
except ImportError:
    try:
        import pdfplumber
        PDF_LIB = "pdfplumber"
    except ImportError:
        PDF_LIB = None


# Figure 标注匹配模式
FIGURE_PATTERNS = [
    # Figure 1-1, Figure 1.1, Figure 1
    (re.compile(r'Figure\s+(\d+)[-.\s]?(\d*)', re.IGNORECASE), 'Figure'),
    # Fig. 1-1, Fig. 1.1
    (re.compile(r'Fig\.\s*(\d+)[-.\s]?(\d*)', re.IGNORECASE), 'Fig.'),
    # Fig 1-1 (无点号)
    (re.compile(r'Fig\s+(\d+)[-.\s]?(\d*)', re.IGNORECASE), 'Fig'),
]


def find_figure_captions(pdf_path, page_nums=None):
    """找到 PDF 中所有 Figure 标注及其位置"""

    figures = []

    if PDF_LIB == "pymupdf":
        doc = fitz.open(pdf_path)
        total_pages = len(doc)

        for page_num in range(total_pages):
            if page_nums and (page_num + 1) not in page_nums:
                continue

            page = doc[page_num]
            text = page.get_text("text")

            # 搜索每种模式
            for pattern, label in FIGURE_PATTERNS:
                for match in pattern.finditer(text):
                    fig_num = match.group(1)
                    sub_num = match.group(2)

                    if sub_num:
                        figure_id = f"{fig_num}-{sub_num}"
                    else:
                        figure_id = fig_num

                    # 获取匹配位置
                    match_pos = match.start()

                    # 尝试获取坐标（近似）
                    # 在 fitz 中精确获取坐标比较复杂，这里用近似方法
                    rect = find_caption_rect(page, match.group(0))

                    figures.append({
                        "figure_id": figure_id,
                        "label": label,
                        "page": page_num + 1,  # 1-based
                        "caption": match.group(0),
                        "rect": rect,  # (x0, y0, x1, y1)
                        "match_pos": match_pos
                    })

        doc.close()

    elif PDF_LIB == "pdfplumber":
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                if page_nums and (page_num + 1) not in page_nums:
                    continue

                text = page.extract_text()
                if not text:
                    continue

                for pattern, label in FIGURE_PATTERNS:
                    for match in pattern.finditer(text):
                        fig_num = match.group(1)
                        sub_num = match.group(2)

                        if sub_num:
                            figure_id = f"{fig_num}-{sub_num}"
                        else:
                            figure_id = fig_num

                        # 尝试获取字符位置
                        chars = page.chars
                        rect = find_caption_rect_plumber(chars, match.group(0))

                        figures.append({
                            "figure_id": figure_id,
                            "label": label,
                            "page": page_num + 1,
                            "caption": match.group(0),
                            "rect": rect,
                            "match_pos": match.start()
                        })

    return figures


def find_caption_rect(page, caption_text):
    """使用 PyMuPDF 找到caption的坐标"""
    # 搜索包含 caption 文本的所有区域
    areas = page.search_for(caption_text)
    if areas:
        return areas[0]  # 返回第一个匹配
    return None


def find_caption_rect_plumber(chars, caption_text):
    """使用 pdfplumber 找到 caption 的坐标"""
    # 找到所有匹配的字符
    matching_chars = [c for c in chars if caption_text in c.get('text', '')]
    if matching_chars:
        # 计算边界框
        min_x = min(c['x0'] for c in matching_chars)
        min_y = min(c['top'] for c in matching_chars)
        max_x = max(c['x1'] for c in matching_chars)
        max_y = max(c['bottom'] for c in matching_chars)
        return (min_x, min_y, max_x, max_y)
    return None


def extract_figure_image(pdf_path, figure_info, output_dir, dpi=150):
    """根据 figure 位置提取图片"""

    os.makedirs(output_dir, exist_ok=True)
    figure_id = figure_info['figure_id']
    page_num = figure_info['page']  # 1-based

    if PDF_LIB == "pymupdf":
        doc = fitz.open(pdf_path)
        page = doc[page_num - 1]  # 0-based

        page_width = page.rect.width
        page_height = page.rect.height

        # 默认页边距
        margin_left = page_width * 0.05
        margin_right = page_width * 0.95
        margin_top = page_height * 0.05

        # Figure 高度比例（图片通常占页面一定比例）
        figure_height_ratio = 0.45

        # 估算图片区域
        # 图注在底部，所以图片在上方
        if figure_info.get('rect'):
            caption_rect = figure_info['rect']
            # 图片底部 = 图注顶部 - 一些间距
            figure_bottom = caption_rect.y0 - 10
            # 图片顶部 = 页面顶部 + 边距
            figure_top = margin_top
        else:
            # 如果没找到图注位置，用默认比例
            figure_bottom = page_height * 0.9
            figure_top = margin_top

        figure_height = figure_bottom - figure_top
        if figure_height < page_height * 0.2:
            figure_height = page_height * figure_height_ratio
            figure_bottom = figure_top + figure_height

        # 图片左右范围
        figure_left = margin_left
        figure_right = page_width - margin_left

        # 创建裁剪区域
        clip_rect = fitz.Rect(figure_left, figure_top, figure_right, figure_bottom)

        # 提取图片
        pix = page.get_pixmap(clip=clip_rect, dpi=dpi)

        output_path = os.path.join(output_dir, f"fig_{figure_id}.png")
        pix.save(output_path)

        doc.close()

        return output_path

    return None


def process_pdf(pdf_path, output_dir, page_nums=None, figure_ids=None, verbose=False):
    """处理 PDF，提取所有 figures"""

    if not Path(pdf_path).exists():
        print(f"Error: PDF not found: {pdf_path}")
        return

    if PDF_LIB is None:
        print("Error: No PDF library available. Install PyMuPDF: pip install PyMuPDF")
        return

    print(f"Processing: {pdf_path}")
    print(f"Using library: {PDF_LIB}")

    # 找到所有 figure 标注
    figures = find_figure_captions(pdf_path, page_nums)

    # 过滤指定 figure
    if figure_ids:
        figures = [f for f in figures if f['figure_id'] in figure_ids]

    if verbose:
        print(f"\nFound {len(figures)} figures:")
        for f in figures:
            print(f"  - Figure {f['figure_id']} (page {f['page']}): {f['caption']}")

    # 提取每个 figure
    print(f"\nExtracting figures...")
    extracted = []
    report_lines = ["figure_id,page,caption,output_path"]

    for fig in figures:
        output_path = extract_figure_image(pdf_path, fig, output_dir)
        if output_path and Path(output_path).exists():
            extracted.append(output_path)
            print(f"  ✓ fig_{fig['figure_id']}.png (page {fig['page']})")

            # 添加到报告
            rel_path = Path(output_path).name
            report_lines.append(f"fig_{fig['figure_id']},{fig['page']},{fig['caption']},{rel_path}")
        else:
            print(f"  ✗ fig_{fig['figure_id']}.png (failed)")

    # 保存汇总报告
    report_path = os.path.join(output_dir, "figures_summary.csv")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))

    print(f"\n{'='*50}")
    print(f"Complete! Extracted {len(extracted)} figures")
    print(f"Output: {output_dir}")
    print(f"Summary: {report_path}")
    print(f"{'='*50}")

    return extracted


def main():
    parser = argparse.ArgumentParser(
        description="Extract figures from PDF by locating Figure captions"
    )
    parser.add_argument("pdf", help="Input PDF path")
    parser.add_argument("-o", "--output", default="figures_output", help="Output directory")
    parser.add_argument("-p", "--pages", type=int, nargs="+", help="Process only these pages")
    parser.add_argument("-f", "--figures", type=str, nargs="+", help="Extract only these figure IDs (e.g., 1-1 1-2)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    process_pdf(
        args.pdf,
        args.output,
        page_nums=args.pages,
        figure_ids=args.figures,
        verbose=args.verbose
    )


if __name__ == "__main__":
    main()
