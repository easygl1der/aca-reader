from PIL import Image

img = Image.open("/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png")
w, h = img.size

# Wider crop for final check
nx1, ny1, nx2, ny2 = 0.05, 0.20, 0.60, 0.80

left = nx1 * w
top = ny1 * h
right = nx2 * w
bottom = ny2 * h

crop = img.crop((left, top, right, bottom))
crop.save("final_check_p23.png")
print(f"Wide crop saved for manual inspection (mental).")
