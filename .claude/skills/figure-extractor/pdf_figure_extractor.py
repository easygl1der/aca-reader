import os
import csv
import json
import argparse
import base64
from pathlib import Path
import cv2
import numpy as np
from PIL import Image

# PDF to image conversion
try:
    from pdf2image import convert_from_path
    PDF_BACKEND = 'pdf2image'
except ImportError:
    try:
        import fitz  # PyMuPDF
        PDF_BACKEND = 'pymupdf'
    except ImportError:
        PDF_BACKEND = None


# ========== Figure extraction logic ==========

def detect_footer_caption_blocks(thresh, top, bottom, img_w):
    footer_h = max(50, int((bottom - top) * 0.12))
    footer_top = max(top, bottom - footer_h)
    footer = thresh[footer_top:bottom, :]
    col_sums = np.sum(footer, axis=0)

    ranges = []
    in_text = False
    start = 0

    for x, v in enumerate(col_sums):
        if v > 500:
            if not in_text:
                start = x
                in_text = True
        else:
            if in_text:
                ranges.append((start, x - 1))
                in_text = False

    if in_text:
        ranges.append((start, img_w - 1))

    merge_gap = max(15, int(img_w * 0.01))
    min_caption_width = max(30, int(img_w * 0.03))

    merged = []
    for a, b in ranges:
        if not merged or a - merged[-1][1] >= merge_gap:
            merged.append([a, b])
        else:
            merged[-1][1] = b

    merged = [r for r in merged if (r[1] - r[0]) >= min_caption_width]
    return merged


def is_graphic_block(thresh, top, bottom, img_w):
    blk = thresh[top:bottom, :]
    col_sums = np.sum(blk, axis=0)
    nz = np.where(col_sums > 500)[0]

    if len(nz) == 0:
        return False

    first, last = int(nz[0]), int(nz[-1])
    span_ratio = (last - first) / img_w

    gaps = []
    zero_count = 0
    for v in col_sums[first:last + 1]:
        if v < 500:
            zero_count += 1
        else:
            if zero_count > 0:
                gaps.append(zero_count)
            zero_count = 0

    max_gap = max(gaps) if gaps else 0

    return (
        max_gap >= max(70, int(img_w * 0.10))
        or (span_ratio < 0.72 and (bottom - top) >= 140)
    )


def is_caption_anchor(thresh, top, bottom, img_w):
    caps = detect_footer_caption_blocks(thresh, top, bottom, img_w)
    if len(caps) != 1:
        return False

    a, b = caps[0]
    center = (a + b) / 2
    width_ratio = (b - a) / img_w

    top_part_bottom = max(top + 1, bottom - max(60, int((bottom - top) * 0.22)))

    return (
        img_w * 0.40 <= center <= img_w * 0.60
        and width_ratio <= 0.16
        and is_graphic_block(thresh, top, top_part_bottom, img_w)
    )


def build_prelim_blocks(thresh, img_h):
    row_sums = np.sum(thresh, axis=1)

    y_gap_threshold = max(20, int(img_h * 0.015))
    min_figure_height = max(80, int(img_h * 0.05))

    raw_blocks = []
    in_block = False
    zero_count = 0
    start_y = 0

    for y, val in enumerate(row_sums):
        if val > 1000:
            if not in_block:
                start_y = y
                in_block = True
            zero_count = 0
        else:
            zero_count += 1
            if in_block and zero_count >= y_gap_threshold:
                raw_blocks.append((start_y, y - zero_count))
                in_block = False

    if in_block:
        raw_blocks.append((start_y, img_h - 1))

    prelim = []
    i = 0
    while i < len(raw_blocks):
        top, bottom = raw_blocks[i]

        if bottom - top > min_figure_height:
            if i + 1 < len(raw_blocks):
                next_top, next_bottom = raw_blocks[i + 1]
                gap = next_top - bottom
                next_height = next_bottom - next_top

                if gap < int(img_h * 0.04) and next_height < int(img_h * 0.04):
                    bottom = next_bottom
                    i += 1

            prelim.append([max(0, top - 20), min(img_h, bottom + 20)])

        i += 1

    return prelim


def split_x_blocks(thresh, top, bottom, img_w):
    blk = thresh[top:bottom, :]
    col_sums = np.sum(blk, axis=0)

    x_gap_threshold = max(40, int(img_w * 0.08))
    min_width = int(img_w * 0.05)

    blocks = []
    in_content = False
    zero_count = 0
    start_x = 0

    for x, val in enumerate(col_sums):
        if val > 500:
            if not in_content:
                start_x = x
                in_content = True
            zero_count = 0
        else:
            zero_count += 1
            if in_content and zero_count >= x_gap_threshold:
                left = max(0, start_x - 20)
                right = x - zero_count + 20
                if right - left >= min_width:
                    blocks.append((left, right))
                in_content = False

    if in_content:
        left = max(0, start_x - 20)
        right = img_w - 1
        if right - left >= min_width:
            blocks.append((left, right))

    return blocks


def figure_filter_metrics(gray):
    _, th = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    fg_ratio = float((th > 0).mean())

    edges = cv2.Canny(gray, 80, 180)
    edge_density = float((edges > 0).mean())

    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(th, 8)
    areas = stats[1:, cv2.CC_STAT_AREA] if nlabels > 1 else np.array([])
    cc_big = int((areas >= 20).sum()) if len(areas) else 0

    col_sums = np.sum(th, axis=0)
    nz = np.where(col_sums > 500)[0]
    x_span_ratio = float((nz[-1] - nz[0]) / gray.shape[1]) if len(nz) else 0.0

    return {
        "fg_ratio": fg_ratio,
        "edge_density": edge_density,
        "cc_big": cc_big,
        "x_span_ratio": x_span_ratio,
    }


def is_probably_figure_relaxed(gray):
    m = figure_filter_metrics(gray)

    keep = (
        (m["fg_ratio"] < 0.055 and m["edge_density"] < 0.055)
        or (m["cc_big"] < 120 and m["fg_ratio"] < 0.05)
        or (m["fg_ratio"] < 0.04 and m["x_span_ratio"] < 0.97)
    )

    return keep, m


def extract_candidates_from_page(page_image_path, output_dir, page_num):
    """Extract candidate figure blocks from a single page image"""

    img = cv2.imread(page_image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return []

    img_h, img_w = img.shape
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

    prelim = build_prelim_blocks(thresh, img_h)

    used = [False] * len(prelim)
    candidates = []

    # Phase 1: compound figure anchor first
    for i, (top, bottom) in enumerate(prelim):
        if used[i]:
            continue

        if is_caption_anchor(thresh, top, bottom, img_w):
            merged_top, merged_bottom = top, bottom
            j = i - 1

            while j >= 0 and not used[j]:
                prev_top, prev_bottom = prelim[j]
                gap = merged_top - prev_bottom

                if gap <= max(60, int(img_h * 0.06)) and is_graphic_block(
                    thresh, prev_top, prev_bottom, img_w
                ):
                    merged_top = prev_top
                    used[j] = True
                    j -= 1
                else:
                    break

            used[i] = True
            candidates.append((0, img_w - 1, merged_top, merged_bottom, "compound_keep"))

    # Phase 2: normal split
    for i, (top, bottom) in enumerate(prelim):
        if used[i]:
            continue

        x_blocks = split_x_blocks(thresh, top, bottom, img_w)
        for left, right in x_blocks:
            candidates.append((left, right, top, bottom, "split"))

        used[i] = True

    pil_img = Image.open(page_image_path)

    results = []
    for cand_idx, (left, right, top, bottom, mode) in enumerate(candidates, 1):
        crop = pil_img.crop((left, top, right, bottom))
        gray_crop = cv2.cvtColor(np.array(crop), cv2.COLOR_RGB2GRAY)

        keep, metrics = is_probably_figure_relaxed(gray_crop)

        if keep:
            # Save candidate to temp location
            temp_name = f"page{page_num:03d}_candidate{cand_idx:02d}.png"
            temp_path = os.path.join(output_dir, "candidates", temp_name)
            os.makedirs(os.path.dirname(temp_path), exist_ok=True)
            crop.save(temp_path)

            results.append({
                "page": page_num,
                "candidate_id": cand_idx,
                "temp_path": temp_path,
                "mode": mode,
                "bbox": (left, top, right, bottom),
                "metrics": metrics,
            })

    return results


# ========== PDF processing ==========

def pdf_to_images(pdf_path, output_dir):
    """Convert PDF to page images"""

    os.makedirs(output_dir, exist_ok=True)

    if PDF_BACKEND == 'pdf2image':
        pages = convert_from_path(pdf_path, dpi=200)
        page_paths = []
        for i, page in enumerate(pages, 1):
            page_path = os.path.join(output_dir, f"page_{i:03d}.png")
            page.save(page_path, 'PNG')
            page_paths.append(page_path)
        return page_paths

    elif PDF_BACKEND == 'pymupdf':
        doc = fitz.open(pdf_path)
        page_paths = []
        for i, page in enumerate(doc, 1):
            pix = page.get_pixmap(matrix=fitz.Matrix(200/72, 200/72))
            page_path = os.path.join(output_dir, f"page_{i:03d}.png")
            pix.save(page_path)
            page_paths.append(page_path)
        doc.close()
        return page_paths

    else:
        raise RuntimeError("No PDF backend available. Install pdf2image or PyMuPDF.")


# ========== Gemini integration ==========

def call_gemini_judge(image_path, api_key=None):
    """
    Call Gemini API to judge if candidate is a real figure.
    Uses Gemini CLI if no API key provided.
    """

    # Try Gemini CLI first (no API key needed)
    if api_key is None:
        prompt = """你是一个严格的学术页面图片分类器。请判断这张裁剪图片是不是"真正的 figure"。

严格规则：
1. 如果没有明确图注或图号（如 Figure 1-8、Fig. 2），直接判定不是 figure。
2. 如果主体是公式、推导、正文、标题、练习文字、空白区域，也不是 figure。
3. 只有当"存在明确图注"且"主体明显是图形/示意图/坐标图/几何图/复合子图"时，才判定为 figure。
4. 复合图如果只有一个总图注，也算一个 figure。
5. 不要因为图片周围空白很多、内容居中、排版像插图，就把公式块误判成 figure。
6. 正文中提到 Figure，不代表该块本身就是 figure。

只输出严格JSON：
{"is_figure": true或false, "confidence": 0.0到1.0, "reason": "一句中文理由"}"""

        import subprocess
        cmd = f'echo "{prompt}" | gemini "{image_path}"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        output = result.stdout + result.stderr

        try:
            import re
            json_match = re.search(r'\{[^}]+\}', output)
            if json_match:
                data = json.loads(json_match.group())
                return data
        except:
            pass

        return {"is_figure": False, "confidence": 0.0, "reason": "解析失败"}

    # Use Google Generative AI SDK if API key provided
    import google.generativeai as genai

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = """你是一个严格的学术页面图片分类器。请判断这张裁剪图片是不是"真正的 figure"。

严格规则：
1. 如果没有明确图注或图号（如 Figure 1-8、Fig. 2），直接判定不是 figure。
2. 如果主体是公式、推导、正文、标题、练习文字、空白区域，也不是 figure。
3. 只有当"存在明确图注"且"主体明显是图形/示意图/坐标图/几何图/复合子图"时，才判定为 figure。
4. 复合图如果只有一个总图注，也算一个 figure。

只输出 JSON：
{"is_figure": true或false, "confidence": 0.0到1.0, "reason": "一句中文理由"}"""

    try:
        img = Image.open(image_path)
        response = model.generate_content([prompt, img])

        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

        result = json.loads(text)
        return result

    except Exception as e:
        return {"is_figure": False, "confidence": 0.0, "reason": f"API调用失败: {str(e)}"}


# ========== Main pipeline ==========

def process_pdf_with_gemini(pdf_path, output_dir, gemini_api_key=None):
    """
    Full pipeline: PDF -> pages -> candidates -> Gemini judgment -> final figures
    """

    pdf_name = Path(pdf_path).stem
    work_dir = os.path.join(output_dir, pdf_name)

    print(f"[1/4] Converting PDF to images...")
    pages_dir = os.path.join(work_dir, "pages")
    page_paths = pdf_to_images(pdf_path, pages_dir)
    print(f"  -> {len(page_paths)} pages extracted")

    print(f"\n[2/4] Extracting candidate figure blocks...")
    all_candidates = []
    for i, page_path in enumerate(page_paths, 1):
        candidates = extract_candidates_from_page(page_path, work_dir, i)
        all_candidates.extend(candidates)
        print(f"  -> Page {i}: {len(candidates)} candidates")

    print(f"\n[3/4] Judging candidates with Gemini...")
    final_figures = []
    for cand in all_candidates:
        print(f"  -> Judging page {cand['page']} candidate {cand['candidate_id']}...", end=" ")

        judgment = call_gemini_judge(cand['temp_path'], gemini_api_key)
        cand['judgment'] = judgment

        if judgment.get('is_figure', False):
            # Extract figure number from reason if available
            import re
            fig_match = re.search(r'Figure\s*(\d+)[-.]?(\d*)', judgment.get('reason', ''))
            if fig_match:
                if fig_match.group(2):
                    fig_num = f"{fig_match.group(1)}-{fig_match.group(2)}"
                else:
                    fig_num = f"{fig_match.group(1)}"
            else:
                fig_num = f"p{cand['page']:03d}_{len(final_figures)+1:02d}"

            # Rename and move to final output
            final_name = f"{pdf_name}_figure_{fig_num}.png"
            final_path = os.path.join(work_dir, "figures", final_name)
            os.makedirs(os.path.dirname(final_path), exist_ok=True)

            img = Image.open(cand['temp_path'])
            img.save(final_path)

            final_figures.append({
                "output": final_path,
                "figure_num": fig_num,
                "page": cand['page'],
                "bbox": cand['bbox'],
                "judgment": judgment
            })
            print(f"✓ KEPT ({judgment.get('confidence', 0):.2f}): {judgment.get('reason', '')}")
        else:
            print(f"✗ SKIP ({judgment.get('confidence', 0):.2f}): {judgment.get('reason', '')}")

    print(f"\n[4/4] Saving results...")

    # Save detailed report
    report_path = os.path.join(work_dir, f"{pdf_name}_report.csv")
    with open(report_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'page', 'candidate_id', 'is_figure', 'confidence',
            'reason', 'output_path'
        ])
        writer.writeheader()

        for cand in all_candidates:
            j = cand['judgment']
            writer.writerow({
                'page': cand['page'],
                'candidate_id': cand['candidate_id'],
                'is_figure': j.get('is_figure', False),
                'confidence': j.get('confidence', 0),
                'reason': j.get('reason', ''),
                'output_path': next((f['output'] for f in final_figures
                                   if f['page'] == cand['page'] and
                                   f['bbox'] == cand['bbox']), '')
            })

    print(f"\n{'='*60}")
    print(f"✓ Processing complete!")
    print(f"  Total candidates: {len(all_candidates)}")
    print(f"  Final figures: {len(final_figures)}")
    print(f"  Report: {report_path}")
    print(f"  Figures: {os.path.join(work_dir, 'figures')}")
    print(f"{'='*60}")

    return {
        'pdf': pdf_path,
        'pages': len(page_paths),
        'candidates': len(all_candidates),
        'figures': len(final_figures),
        'report': report_path,
        'output_dir': os.path.join(work_dir, "figures")
    }


def main():
    parser = argparse.ArgumentParser(description="Extract figures from PDF using OpenCV + Gemini")
    parser.add_argument("pdf", help="Input PDF path")
    parser.add_argument("-o", "--output", default="pdf_figures_output", help="Output directory")
    parser.add_argument("-k", "--api-key", default=None, help="Gemini API key (optional, uses CLI if not provided)")

    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"Error: PDF not found: {args.pdf}")
        return

    result = process_pdf_with_gemini(args.pdf, args.output, args.api_key)

    print(f"\nSummary:")
    print(f"  PDF: {result['pdf']}")
    print(f"  Pages: {result['pages']}")
    print(f"  Candidates extracted: {result['candidates']}")
    print(f"  Final figures: {result['figures']}")
    print(f"  Output: {result['output_dir']}")


if __name__ == "__main__":
    main()
