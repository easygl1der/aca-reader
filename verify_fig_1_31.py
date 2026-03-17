from PIL import Image
import os

image_path = "/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png"
output_path = "/Users/yueyh/.gemini/tmp/figure-extractor/verify_fig_1_31.png"

# Gemini coordinates
x1, y1, x2, y2 = 0.58, 0.06, 0.87, 0.29

with Image.open(image_path) as img:
    width, height = img.size
    left = x1 * width
    top = y1 * height
    right = x2 * width
    bottom = y2 * height
    
    crop = img.crop((left, top, right, bottom))
    crop.save(output_path)
    print(f"Saved crop to {output_path}")
    print(f"Crop size: {crop.size}")
