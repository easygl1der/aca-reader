from PIL import Image

img = Image.open("/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png")
w, h = img.size

# Based on PDF units (432x648)
# x1=66.5, y1=208.2, x2=188.1, y2=451.1
nx1, ny1, nx2, ny2 = 66.5/432, 208.2/648, 188.1/432, 451.1/648

left = nx1 * w
top = ny1 * h
right = nx2 * w
bottom = ny2 * h

crop = img.crop((left, top, right, bottom))
crop.save("verify_fig_1_8_precise.png")
print(f"Crop saved. Normalized: x1={nx1:.4f}, y1={ny1:.4f}, x2={nx2:.4f}, y2={ny2:.4f}")
