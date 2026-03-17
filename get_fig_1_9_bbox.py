import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page = doc.load_page(23)
w, h = page.rect.width, page.rect.height

# Figure 1-9 label: BBox: (265.372802734375, 457.4308166503906, 369.7392883300781, 469.2527160644531)
label_x0 = 265.37
label_y0 = 457.43

x_min, y_min, x_max, y_max = w, h, 0, 0

# Include label
x_min = min(x_min, label_x0)
x_max = max(x_max, 369.74)
y_min = min(y_min, label_y0)
y_max = max(y_max, 469.25)

# Check drawings on the right
drawings = page.get_drawings()
for d in drawings:
    r = d["rect"]
    # Only pick drawings that are horizontally aligned with the label and above it
    if r.x1 > label_x0 - 10 and r.x0 < label_x0 + 150:
        if r.y1 < label_y0 and r.y0 > 200: # Above label, below equation
            if r.width > 400: continue
            x_min = min(x_min, r.x0)
            x_max = max(x_max, r.x1)
            y_min = min(y_min, r.y0)
            y_max = max(y_max, r.y1)

# Check text on the right
dict = page.get_text("dict")
for block in dict["blocks"]:
    if "lines" in block:
        for line in block["lines"]:
            r = fitz.Rect(line["bbox"])
            text = "".join([span["text"] for span in line["spans"]]).strip()
            if r.x1 > label_x0 - 10 and r.x0 < label_x0 + 150:
                if r.y1 < label_y0 + 20 and r.y0 > 200:
                    if len(text) > 50: continue
                    x_min = min(x_min, r.x0)
                    x_max = max(x_max, r.x1)
                    y_min = min(y_min, r.y0)
                    y_max = max(y_max, r.y1)

# Add some margin
padding = 10
x_min -= padding
y_min -= padding
x_max += padding
y_max += padding

print(f"Absolute BBox: x1={x_min}, y1={y_min}, x2={x_max}, y2={y_max}")
print(f"Normalized: x1={x_min/w:.4f}, y1={y_min/h:.4f}, x2={x_max/w:.4f}, y2={y_max/h:.4f}")

# Draw and save
pix = page.get_pixmap()
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
draw = ImageDraw.Draw(img)
draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)
img.save("verify_fig_1_9.png")

doc.close()
