from PIL import Image

img = Image.open("temp_page_23.png")
w, h = img.size

# Much larger crop for investigation
nx1, ny1, nx2, ny2 = 0.10, 0.20, 0.50, 0.80

left = nx1 * w
top = ny1 * h
right = nx2 * w
bottom = ny2 * h

crop = img.crop((left, top, right, bottom))
crop.save("crop_fig_1_8_v2.png")
print(f"Saved crop to crop_fig_1_8_v2.png at ({left}, {top}, {right}, {bottom})")
