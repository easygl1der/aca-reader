import os
import csv
import argparse
import cv2
import numpy as np
from PIL import Image
import subprocess
import json


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

    return raw_blocks, prelim


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
    """第一道筛选：CV 方法初筛"""
    m = figure_filter_metrics(gray)

    keep = (
        (m["fg_ratio"] < 0.055 and m["edge_density"] < 0.055)
        or (m["cc_big"] < 120 and m["fg_ratio"] < 0.05)
        or (m["fg_ratio"] < 0.04 and m["x_span_ratio"] < 0.97)
    )

    return keep, m


def verify_with_gemini(image_path):
    """第二道筛选：用 Gemini 严格验证是否是真正的 Figure"""
    prompt = """你是一个严格的学术页面图片分类器。你的任务是判断"这张裁剪图片是否是一个真正的 figure"，而不是正文、公式块、空白块、标题、段落或普通排版内容。

【硬规则1：图注优先】
如果没有明确图注/图号（如 Figure 1-8, Fig. 3 等），直接 is_figure = false

【硬规则2：公式块不是 figure】
主体是数学公式、公式推导、参数表达式，等式，判 false

【硬规则3：正文块不是 figure】
段落文字、题目、定理、证明、练习、小节标题，判 false

【硬规则4：空白块不是 figure】
大部分空白，无图形主体，无图注，判 false

【成为 true 的必要条件】
1. 有明确图注/图号
2. 主体是图形内容（曲线图、几何图、示意图、坐标轴图、多子图等）

只输出严格JSON：
{"is_figure": true或false, "confidence": 0.0到1.0, "reason": "一句中文理由"}"""

    cmd = f'echo "{prompt}" | gemini "{image_path}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)

    output = result.stdout + result.stderr

    # 解析 JSON 结果
    try:
        import re
        # 尝试提取 JSON
        json_match = re.search(r'\{[^}]+\}', output)
        if json_match:
            gemini_data = json.loads(json_match.group())
            is_figure = gemini_data.get("is_figure", False)
            reason = gemini_data.get("reason", "")

            # 如果判定为 figure，尝试提取图号
            if is_figure:
                fig_match = re.search(r'Figure\s*(\d+)[-.]?(\d*)', reason)
                if fig_match:
                    if fig_match.group(2):
                        figure_num = f"{fig_match.group(1)}-{fig_match.group(2)}"
                    else:
                        figure_num = f"{fig_match.group(1)}"
                    return "HAS_FIGURE", figure_num, output[:200]
                else:
                    return "HAS_FIGURE", None, output[:200]
            else:
                return "NOT_FIGURE", None, output[:200]
    except:
        pass

    return "UNKNOWN", None, output[:200]


def extract_figures(image_path, output_dir, use_gemini=True):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Cannot load image: {image_path}")

    img_h, img_w = img.shape
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

    raw_blocks, prelim = build_prelim_blocks(thresh, img_h)

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

    pil_img = Image.open(image_path)

    os.makedirs(output_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(image_path))[0]

    cv_results = []
    gemini_results = []
    final_results = []

    # 第一道筛选：CV 方法
    for cand_idx, (left, right, top, bottom, mode) in enumerate(candidates, 1):
        crop = pil_img.crop((left, top, right, bottom))
        gray_crop = cv2.cvtColor(np.array(crop), cv2.COLOR_RGB2GRAY)

        keep, metrics = is_probably_figure_relaxed(gray_crop)

        cv_results.append({
            "candidate_index": cand_idx,
            "mode": mode,
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom,
            "cv_keep": keep,
            "fg_ratio": round(metrics["fg_ratio"], 6),
            "edge_density": round(metrics["edge_density"], 6),
            "cc_big": metrics["cc_big"],
            "x_span_ratio": round(metrics["x_span_ratio"], 6),
        })

        if not keep:
            continue

        # 保存临时文件用于 Gemini 验证
        temp_path = os.path.join(output_dir, f"{stem}_temp_{cand_idx}.png")
        crop.save(temp_path)

        # 第二道筛选：Gemini 验证
        if use_gemini:
            gemini_result, figure_num, gemini_output = verify_with_gemini(temp_path)
            gemini_results.append({
                "candidate_index": cand_idx,
                "gemini_result": gemini_result,
                "figure_num": figure_num,
                "gemini_output": gemini_output,
            })

            if gemini_result == "HAS_FIGURE" and figure_num:
                final_path = os.path.join(output_dir, f"fig_{figure_num}.png")
                crop.save(final_path)
                final_results.append({
                    "output": final_path,
                    "figure_num": figure_num,
                    "mode": mode,
                })
                print(f"✓ {final_path} <- Figure {figure_num}")
            else:
                print(f"✗ {temp_path} <- {gemini_result}")
                os.remove(temp_path)
        else:
            # 不使用 Gemini，直接保留
            final_idx = len(final_results) + 1
            out_name = f"{stem}_figure_{final_idx}.png"
            out_path = os.path.join(output_dir, out_name)
            crop.save(out_path)
            final_results.append({
                "output": out_path,
                "mode": mode,
            })

    # 保存调试 CSV
    debug_csv = os.path.join(output_dir, f"{stem}_debug.csv")
    with open(debug_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "candidate_index", "mode", "left", "right", "top", "bottom",
            "cv_keep", "fg_ratio", "edge_density", "cc_big", "x_span_ratio",
            "gemini_result", "figure_num"
        ])
        writer.writeheader()
        for i, row in enumerate(cv_results):
            row["gemini_result"] = gemini_results[i]["gemini_result"] if i < len(gemini_results) else "N/A"
            row["figure_num"] = gemini_results[i]["figure_num"] if i < len(gemini_results) else "N/A"
            writer.writerow(row)

    # 保存裁剪位置汇总 CSV（包含所有最终提取的图片坐标）
    crop_positions = []
    for i, row in enumerate(cv_results):
        if row["cv_keep"] and (not use_gemini or (i < len(gemini_results) and gemini_results[i].get("gemini_result") == "HAS_FIGURE")):
            crop_positions.append({
                "figure_num": row.get("figure_num", f"{final_results[len([r for r in crop_positions if r.get('output')]):03d}"),
                "left": row["left"],
                "right": row["right"],
                "top": row["top"],
                "bottom": row["bottom"],
            })

    if crop_positions:
        positions_csv = os.path.join(output_dir, "figure_crop_positions.csv")
        with open(positions_csv, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["figure_num", "left", "top", "right", "bottom", "width", "height"])
            writer.writeheader()
            for pos in crop_positions:
                # 获取图片尺寸
                fig_path = os.path.join(output_dir, f"fig_{pos['figure_num']}.png")
                if os.path.exists(fig_path):
                    with Image.open(fig_path) as img:
                        pos["width"], pos["height"] = img.size
                writer.writerow(pos)

    summary = {
        "image": image_path,
        "raw_blocks": raw_blocks,
        "prelim_blocks": prelim,
        "candidate_count": len(candidates),
        "cv_kept_count": sum(1 for r in cv_results if r["cv_keep"]),
        "final_count": len(final_results),
        "debug_csv": debug_csv,
        "crop_positions_csv": positions_csv if crop_positions else None,
        "results": final_results,
    }

    return summary


def main():
    import sys
    if len(sys.argv) < 2:
        print("用法: python figure_extractor.py <图片路径> [-o <输出目录>] [--no-gemini]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_dir = "figure_output"
    use_gemini = True

    # 解析参数
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "-o" and i + 1 < len(sys.argv):
            output_dir = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--no-gemini":
            use_gemini = False
            i += 1
        else:
            i += 1

    summary = extract_figures(image_path, output_dir, use_gemini=use_gemini)

    print(f"\n=== 提取结果 ===")
    print(f"图片: {summary['image']}")
    print(f"原始块: {len(summary['raw_blocks'])}")
    print(f"预筛选块: {len(summary['prelim_blocks'])}")
    print(f"候选数: {summary['candidate_count']}")
    print(f"CV初筛保留: {summary['cv_kept_count']}")
    print(f"最终保留 (含Gemini): {summary['final_count']}")
    print(f"调试CSV: {summary['debug_csv']}")
    if summary.get('crop_positions_csv'):
        print(f"裁剪位置CSV: {summary['crop_positions_csv']}")

    if summary['results']:
        print("\n最终结果:")
        for item in summary["results"]:
            print(f"  {item['output']}")


if __name__ == "__main__":
    main()
