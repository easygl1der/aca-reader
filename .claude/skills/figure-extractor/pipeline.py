#!/usr/bin/env python3
"""
Complete Figure Extraction Pipeline:
1. Extract candidates using CV (v4)
2. Verify with Gemini for Figure caption
3. Rename and organize output
"""

import os
import subprocess
import re
from pathlib import Path

def call_gemini_verify(image_path):
    """Use Gemini to verify if image has Figure caption"""
    prompt = """只输出JSON: {"has_figure": true/false, "figure_id": "1-1"}"""

    # Gemini CLI must run in skill directory
    skill_dir = os.path.dirname(os.path.abspath(__file__))

    # Copy image to skill temp dir if not already there
    filename = os.path.basename(image_path)
    temp_path = os.path.join(skill_dir, filename)

    if not os.path.exists(temp_path):
        import shutil
        shutil.copy2(image_path, temp_path)

    cmd = f'echo "{prompt}" | gemini "{filename}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
    output = result.stdout + result.stderr

    # 解析 JSON
    try:
        import json
        json_match = re.search(r'\{[^}]+\}', output)
        if json_match:
            data = json.loads(json_match.group())
            return data
    except:
        pass

    return {"has_figure": False, "figure_id": None, "caption": None}


def process_image(image_path, output_dir):
    """Complete pipeline: extract -> verify -> organize"""

    image_path = os.path.abspath(image_path)
    base_name = Path(image_path).stem
    work_dir = os.path.join(output_dir, f"{base_name}_extracted")
    figures_dir = os.path.join(work_dir, "figures")
    os.makedirs(figures_dir, exist_ok=True)

    print(f"=== Step 1: Extract candidates with CV (v4) ===")

    # Step 1: Run CV extraction
    from figure_extractor_v4 import extract_figures

    result = extract_figures(image_path, work_dir)

    print(f"CV extracted {len(result['results'])} candidates")

    print(f"\n=== Step 2: Verify with Gemini ===")

    verified = []
    for i, item in enumerate(result['results'], 1):
        cand_path = item['output']
        print(f"  Checking: {Path(cand_path).name}...", end=" ")

        gemini_result = call_gemini_verify(cand_path)

        if gemini_result.get('has_figure', False):
            fig_id = gemini_result.get('figure_id', f'fig_{i}')
            # Clean figure ID
            fig_id = fig_id.replace('Figure ', '').replace('Fig.', '').strip()

            # Rename
            new_name = f"fig_{fig_id}.png"
            new_path = os.path.join(figures_dir, new_name)

            # Handle duplicates
            if os.path.exists(new_path):
                base, ext = os.path.splitext(new_name)
                new_path = os.path.join(figures_dir, f"{base}_{i}{ext}")

            os.rename(cand_path, new_path)
            verified.append({
                'original': cand_path,
                'output': new_path,
                'figure_id': fig_id,
                'caption': gemini_result.get('caption', '')
            })
            print(f"✓ Figure {fig_id}")
        else:
            # Delete non-figure
            os.remove(cand_path)
            print(f"✗ Not a figure, deleted")

    print(f"\n=== Step 3: Summary ===")
    print(f"Total candidates: {len(result['results'])}")
    print(f"Verified figures: {len(verified)}")

    if verified:
        print(f"\nFinal figures:")
        for v in verified:
            print(f"  {Path(v['output']).name}")

    # Cleanup: delete debug files and remaining candidates
    for f in Path(work_dir).glob("*.csv"):
        f.unlink()
    for f in Path(work_dir).glob("*_candidate_*.png"):
        f.unlink()

    print(f"\nOutput directory: {figures_dir}")

    return verified


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Figure Extraction Pipeline: CV + Gemini")
    parser.add_argument("input", help="Input page image path")
    parser.add_argument("-o", "--output", default="figure_output", help="Output directory")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    process_image(args.input, args.output)
