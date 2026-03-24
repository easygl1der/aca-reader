import os, csv, json
import cv2, numpy as np
from PIL import Image

# Unified bbox order: (left, right, top, bottom)


def detect_footer_caption_blocks(thresh, top, bottom, img_w):
    """Detect caption blocks in the footer area using projection profile."""
    footer_h = max(50, int((bottom - top) * 0.12))
    footer_top = max(top, bottom - footer_h)
    footer = thresh[footer_top:bottom, :]
    col_sums = np.sum(footer, axis=0)
    ranges, in_text = [], False
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
    return [r for r in merged if (r[1] - r[0]) >= min_caption_width]


def is_graphic_block(thresh, top, bottom, img_w):
    """Check if a block is likely a graphic (not text)."""
    blk = thresh[top:bottom, :]
    col_sums = np.sum(blk, axis=0)
    nz = np.where(col_sums > 500)[0]
    if len(nz) == 0:
        return False
    first, last = int(nz[0]), int(nz[-1])
    span_ratio = (last - first) / img_w
    gaps, zero_count = [], 0
    for v in col_sums[first:last + 1]:
        if v < 500:
            zero_count += 1
        else:
            if zero_count > 0:
                gaps.append(zero_count)
            zero_count = 0
    max_gap = max(gaps) if gaps else 0
    return (max_gap >= max(70, int(img_w * 0.10))) or (span_ratio < 0.72 and (bottom - top) >= 140)


def is_caption_anchor(thresh, top, bottom, img_w):
    """Check if this block has a single centered caption - likely a compound figure."""
    caps = detect_footer_caption_blocks(thresh, top, bottom, img_w)
    if len(caps) != 1:
        return False
    a, b = caps[0]
    center = (a + b) / 2
    width_ratio = (b - a) / img_w
    top_part_bottom = max(top + 1, bottom - max(60, int((bottom - top) * 0.22)))
    return (img_w * 0.40 <= center <= img_w * 0.60) and (width_ratio <= 0.16) and is_graphic_block(thresh, top, top_part_bottom, img_w)


def build_prelim_blocks(thresh, img_h):
    """Build preliminary blocks using row projection profile."""
    row_sums = np.sum(thresh, axis=1)
    y_gap_threshold = max(20, int(img_h * 0.015))
    min_figure_height = max(80, int(img_h * 0.05))
    raw_blocks, in_block, zero_count = [], False, 0
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
    return raw_blocks, prelim


def split_x_blocks(thresh, top, bottom, img_w):
    """Split blocks horizontally using column projection."""
    blk = thresh[top:bottom, :]
    col_sums = np.sum(blk, axis=0)
    x_gap_threshold = max(40, int(img_w * 0.08))
    min_width = int(img_w * 0.05)
    blocks, in_content, zero_count = [], False, 0
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
    """Calculate CV metrics to filter out non-figure content."""
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
    return {"fg_ratio": fg_ratio, "edge_density": edge_density, "cc_big": cc_big, "x_span_ratio": x_span_ratio}


def is_probably_figure_relaxed(gray):
    """First-pass filter: likely a figure based on CV metrics."""
    m = figure_filter_metrics(gray)
    keep = (
        (m["fg_ratio"] < 0.055 and m["edge_density"] < 0.055)
        or (m["cc_big"] < 120 and m["fg_ratio"] < 0.05)
        or (m["fg_ratio"] < 0.04 and m["x_span_ratio"] < 0.97)
    )
    return keep, m


def bottom_caption_groups(gray_crop):
    """
    Detect multiple caption anchors at the bottom of the crop.
    Only inspect bottom 35% to avoid counting figures as captions.
    Returns list of caption anchors with positions.
    """
    h, w = gray_crop.shape
    _, th = cv2.threshold(gray_crop, 200, 255, cv2.THRESH_BINARY_INV)
    footer_top = int(h * 0.65)
    footer = th[footer_top:h, :]
    row_sums = np.sum(footer, axis=1)
    min_row = max(350, int(w * 0.35))

    lines = []
    in_line = False
    for y, v in enumerate(row_sums):
        if v > min_row:
            if not in_line:
                ys = y
                in_line = True
        else:
            if in_line:
                lines.append((ys, y - 1, int(row_sums[ys:y].max())))
                in_line = False
    if in_line:
        lines.append((ys, footer.shape[0] - 1, int(row_sums[ys:].max())))

    candidates = []
    for y1, y2, strength in lines:
        band = footer[max(0, y1 - 3):min(footer.shape[0], y2 + 4), :]
        col_sums = np.sum(band, axis=0)
        segs = []
        in_seg = False
        for x, v in enumerate(col_sums):
            if v > 180:
                if not in_seg:
                    xs = x
                    in_seg = True
            else:
                if in_seg:
                    segs.append((xs, x - 1))
                    in_seg = False
        if in_seg:
            segs.append((xs, band.shape[1] - 1))

        merged = []
        for a, b in segs:
            if not merged or a - merged[-1][1] > max(20, int(w * 0.03)):
                merged.append([a, b])
            else:
                merged[-1][1] = b

        anchors = []
        for a, b in merged:
            ww = b - a
            if max(70, int(w * 0.08)) <= ww <= int(w * 0.22):
                anchors.append({
                    'cx': (a + b) / 2,
                    'cy': footer_top + (y1 + y2) / 2,
                    'bbox': (a, footer_top + y1, b, footer_top + y2),
                    'width': ww,
                })

        # Good caption line: 2-4 moderate-width groups, prefer bottom-most
        if len(anchors) >= 2:
            candidates.append({'line': (y1, y2), 'strength': strength, 'anchors': anchors})

    if not candidates:
        return []

    # Choose bottom-most valid line
    chosen = sorted(candidates, key=lambda x: x['line'][1])[-1]
    anchors = chosen['anchors']

    # De-duplicate close anchors
    uniq = []
    for a in sorted(anchors, key=lambda z: z['cx']):
        if not any(abs(a['cx'] - b['cx']) < max(45, int(w * 0.05)) for b in uniq):
            uniq.append(a)

    # If too many anchors, keep two widest/rightmost-separated
    if len(uniq) > 2:
        uniq = sorted(uniq, key=lambda z: z['width'], reverse=True)[:2]
        uniq = sorted(uniq, key=lambda z: z['cx'])

    return uniq


def split_bbox_by_anchors(bbox, anchors, crop_w, crop_h, pad=24):
    """Split a bounding box based on caption anchor positions."""
    left, right, top, bottom = bbox
    if len(anchors) <= 1:
        return [bbox]
    xs = np.array([a['cx'] for a in anchors], dtype=np.float32)
    ys = np.array([a['cy'] for a in anchors], dtype=np.float32)
    x_spread = float(xs.max() - xs.min())
    y_spread = float(ys.max() - ys.min())
    boxes = []
    if x_spread >= y_spread:
        # Horizontal split
        anchors = sorted(anchors, key=lambda a: a['cx'])
        cuts = [0]
        for i in range(len(anchors) - 1):
            cuts.append(int((anchors[i]['cx'] + anchors[i + 1]['cx']) / 2))
        cuts.append(crop_w)
        for i in range(len(cuts) - 1):
            l = max(0, cuts[i] - (pad if i > 0 else 0))
            r = min(crop_w, cuts[i + 1] + (pad if i < len(cuts) - 2 else 0))
            boxes.append((left + l, left + r, top, bottom))
    else:
        # Vertical split
        anchors = sorted(anchors, key=lambda a: a['cy'])
        cuts = [0]
        for i in range(len(anchors) - 1):
            cuts.append(int((anchors[i]['cy'] + anchors[i + 1]['cy']) / 2))
        cuts.append(crop_h)
        for i in range(len(cuts) - 1):
            t = max(0, cuts[i] - (pad if i > 0 else 0))
            b = min(crop_h, cuts[i + 1] + (pad if i < len(cuts) - 2 else 0))
            boxes.append((left, right, top + t, top + b))
    return boxes


def refine_candidates_by_internal_captions(pil_img, candidates):
    """
    Second-pass refinement: detect multiple captions within each candidate.
    This prevents "two figures stuck together" issue.
    """
    refined, debug = [], []
    for left, right, top, bottom, mode in candidates:
        crop = pil_img.crop((left, top, right, bottom))
        gray_crop = cv2.cvtColor(np.array(crop), cv2.COLOR_RGB2GRAY)
        anchors = bottom_caption_groups(gray_crop)
        if len(anchors) >= 2:
            # Split into multiple boxes
            boxes = split_bbox_by_anchors((left, right, top, bottom), anchors, gray_crop.shape[1], gray_crop.shape[0], pad=24)
            for b in boxes:
                refined.append((b[0], b[1], b[2], b[3], 'multi_caption_split'))
            debug.append({'mode': mode, 'left': left, 'right': right, 'top': top, 'bottom': bottom,
                          'caption_anchor_count': len(anchors), 'split': True, 'caption_source': 'bottom_visual'})
        else:
            refined.append((left, right, top, bottom, mode))
            debug.append({'mode': mode, 'left': left, 'right': right, 'top': top, 'bottom': bottom,
                          'caption_anchor_count': len(anchors), 'split': False, 'caption_source': 'bottom_visual'})
    return refined, debug


def extract_figures(image_path, output_dir):
    """
    Main extraction function: page image -> candidate blocks -> refine -> filter -> output.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f'Cannot load image: {image_path}')
    img_h, img_w = img.shape
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
    raw_blocks, prelim = build_prelim_blocks(thresh, img_h)
    used = [False] * len(prelim)
    candidates = []

    # Phase 1: detect compound figures (caption anchor)
    for i, (top, bottom) in enumerate(prelim):
        if used[i]:
            continue
        if is_caption_anchor(thresh, top, bottom, img_w):
            merged_top, merged_bottom = top, bottom
            j = i - 1
            while j >= 0 and not used[j]:
                prev_top, prev_bottom = prelim[j]
                gap = merged_top - prev_bottom
                if gap <= max(60, int(img_h * 0.06)) and is_graphic_block(thresh, prev_top, prev_bottom, img_w):
                    merged_top = prev_top
                    used[j] = True
                    j -= 1
                else:
                    break
            used[i] = True
            candidates.append((0, img_w - 1, merged_top, merged_bottom, 'compound_keep'))

    # Phase 2: normal split
    for i, (top, bottom) in enumerate(prelim):
        if used[i]:
            continue
        for left, right in split_x_blocks(thresh, top, bottom, img_w):
            candidates.append((left, right, top, bottom, 'split'))
        used[i] = True

    pil_img = Image.open(image_path)

    # Phase 3: refine candidates by detecting multiple captions
    refined_candidates, refine_debug = refine_candidates_by_internal_captions(pil_img, candidates)

    os.makedirs(output_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(image_path))[0]
    results, debug_rows = [], []

    # Phase 4: CV filter
    for cand_idx, (left, right, top, bottom, mode) in enumerate(refined_candidates, 1):
        crop = pil_img.crop((left, top, right, bottom))
        gray_crop = cv2.cvtColor(np.array(crop), cv2.COLOR_RGB2GRAY)
        keep, metrics = is_probably_figure_relaxed(gray_crop)
        candidate_path = os.path.join(output_dir, f'{stem}_candidate_{cand_idx}.png')
        crop.save(candidate_path)
        debug_rows.append({'source': image_path, 'candidate_index': cand_idx, 'mode': mode,
                           'left': left, 'right': right, 'top': top, 'bottom': bottom,
                           'keep': keep, 'fg_ratio': round(metrics['fg_ratio'], 6),
                           'edge_density': round(metrics['edge_density'], 6),
                           'cc_big': metrics['cc_big'], 'x_span_ratio': round(metrics['x_span_ratio'], 6)})
        if keep:
            out_name = os.path.join(output_dir, f'{stem}_figure_{len(results)+1}.png')
            crop.save(out_name)
            results.append({'output': out_name, 'mode': mode, 'left': left, 'right': right, 'top': top, 'bottom': bottom})

    # Save debug CSVs
    debug_csv = os.path.join(output_dir, f'{stem}_debug.csv')
    if debug_rows:
        with open(debug_csv, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=list(debug_rows[0].keys()))
            writer.writeheader()
            writer.writerows(debug_rows)
    refine_csv = os.path.join(output_dir, f'{stem}_refine_debug.csv')
    if refine_debug:
        with open(refine_csv, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=list(refine_debug[0].keys()))
            writer.writeheader()
            writer.writerows(refine_debug)

    return {'image': image_path, 'raw_blocks': raw_blocks, 'prelim_blocks': prelim,
            'initial_candidates': candidates, 'refined_candidates': refined_candidates,
            'results': results, 'debug_csv': debug_csv, 'refine_csv': refine_csv}


# ========== PDF Processing ==========

def pdf_to_images(pdf_path, output_dir, dpi=150):
    """Convert PDF pages to images using PyMuPDF."""
    try:
        import fitz
    except ImportError:
        print("Error: PyMuPDF not installed. Run: pip install PyMuPDF")
        return []

    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    page_paths = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72))
        out_path = os.path.join(output_dir, f"page_{page_num+1:03d}.png")
        pix.save(out_path)
        page_paths.append(out_path)

    doc.close()
    return page_paths


def process_pdf(pdf_path, output_dir, dpi=150):
    """Process entire PDF: convert to images, extract figures from each page."""
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    work_dir = os.path.join(output_dir, f"{pdf_name}_figures")
    pages_dir = os.path.join(work_dir, "pages")

    print(f"Converting PDF to images...")
    page_paths = pdf_to_images(pdf_path, pages_dir, dpi)
    print(f"Extracted {len(page_paths)} pages")

    all_results = []
    for page_path in page_paths:
        page_num = os.path.basename(page_path).replace("page_", "").replace(".png", "")
        print(f"Processing page {page_num}...")

        try:
            result = extract_figures(page_path, work_dir)
            for item in result['results']:
                # Rename with page number
                src = item['output']
                dst = src.replace("_figure_", f"_p{page_num}_")
                if os.path.exists(src):
                    os.rename(src, dst)
                    item['output'] = dst
            all_results.extend(result['results'])
            print(f"  -> Found {len(result['results'])} figures")
        except Exception as e:
            print(f"  -> Error: {e}")

    print(f"\nTotal figures extracted: {len(all_results)}")
    return all_results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract figures from PDF or image")
    parser.add_argument("input", help="Input PDF or image path")
    parser.add_argument("-o", "--output", default="figure_output", help="Output directory")
    parser.add_argument("--pdf", action="store_true", help="Treat input as PDF")
    parser.add_argument("--dpi", type=int, default=150, help="PDF to image DPI")

    args = parser.parse_args()

    if args.pdf:
        process_pdf(args.input, args.output, args.dpi)
    else:
        result = extract_figures(args.input, args.output)
        print(f"Extracted {len(result['results'])} figures")
        for item in result['results']:
            print(f"  {item['output']}")
