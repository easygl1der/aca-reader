import PIL.Image

def crop_figures(image_path, bboxes):
    img = PIL.Image.open(image_path)
    w, h = img.size
    for name, bbox in bboxes.items():
        x1, y1, x2, y2 = bbox
        left = x1 * w
        top = y1 * h
        right = x2 * w
        bottom = y2 * h
        cropped = img.crop((left, top, right, bottom))
        cropped.save(f"crop_{name}.png")
        print(f"Saved crop_{name}.png")

bboxes = {
    "1-30": [0.15, 0.05, 0.73, 0.32],
    "1-31": [0.70, 0.06, 0.98, 0.32]
}

crop_figures("page_59.png", bboxes)
