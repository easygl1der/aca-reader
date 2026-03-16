import cv2
import numpy as np
from PIL import Image
import sys
import os

def extract_figures(image_path, output_dir="."):
    # 1. 加载图像与二值化
    img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img_cv is None:
        print(f"Error: Cannot load {image_path}")
        return

    # 获取动态尺寸
    img_h, img_w = img_cv.shape
    _, thresh = cv2.threshold(img_cv, 200, 255, cv2.THRESH_BINARY_INV)
    row_sums = np.sum(thresh, axis=1)

    # 动态阈值 1：Y轴段落间距（设为图片高度的 1.5%，保底20像素）
    y_gap_threshold = max(20, int(img_h * 0.015))
    
    # 动态阈值 2：最小图表高度（设为图片高度的 5%，保底80像素）
    MIN_FIGURE_HEIGHT = max(80, int(img_h * 0.05))

    # 2. Y 轴水平投影
    y_blocks = []
    in_block = False
    start_y = 0
    zero_count = 0

    for y, val in enumerate(row_sums):
        if val > 1000:
            if not in_block:
                in_block = True
                start_y = y
            zero_count = 0
        else:
            zero_count += 1
            if in_block and zero_count >= y_gap_threshold:
                y_blocks.append([start_y, y - zero_count])
                in_block = False
    if in_block:
        y_blocks.append([start_y, len(row_sums) - 1])

    # 3. Y 轴块过滤与图注合并
    merged_blocks = []
    skip_next = False

    for i in range(len(y_blocks)):
        if skip_next:
            skip_next = False
            continue
            
        top, bottom = y_blocks[i]
        height = bottom - top
        
        if height > MIN_FIGURE_HEIGHT:
            if i + 1 < len(y_blocks):
                next_top, next_bottom = y_blocks[i+1]
                gap = next_top - bottom
                next_height = next_bottom - next_top
                # 图注间距和高度，使用类似比例
                if gap < int(img_h * 0.04) and next_height < int(img_h * 0.04):
                    bottom = next_bottom
                    skip_next = True
            
            merged_blocks.append((max(0, top-20), min(img_h, bottom+20)))

    # 4. X 轴垂直投影：切除白边 & 劈开并排图
    img_pil = Image.open(image_path)
    extracted_count = 0
    
    # 动态阈值 3：X轴并排图片间距（设为图片宽度的 8%，保底40像素）
    # 真正并排的两张图，间距通常在 15% 以上；而同一个图内的元素间距很少超过 8%
    x_gap_threshold = max(40, int(img_w * 0.08))

    for top, bottom in merged_blocks:
        block_thresh = thresh[top:bottom, :]
        col_sums = np.sum(block_thresh, axis=0)
        
        x_blocks = []
        in_content = False
        start_x = 0
        zero_count = 0

        for x, val in enumerate(col_sums):
            if val > 500:
                if not in_content:
                    in_content = True
                    start_x = x
                zero_count = 0
            else:
                zero_count += 1
                if in_content and zero_count >= x_gap_threshold:
                    x_blocks.append((max(0, start_x-20), x - zero_count + 20))
                    in_content = False
        if in_content:
            x_blocks.append((max(0, start_x-20), len(col_sums) - 1))
            
        for left, right in x_blocks:
            if right - left < int(img_w * 0.05): # 忽略极窄的噪点（小于宽度的5%）
                continue
            extracted_count += 1
            out_name = os.path.join(output_dir, f"extracted_figure_{extracted_count}.png")
            cropped = img_pil.crop((left, top, right, bottom))
            cropped.save(out_name)
            print(f"-> 成功提取: {out_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python figure_extractor.py <图片路径>")
    else:
        extract_figures(sys.argv[1])
