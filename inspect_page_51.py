import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 50 # Page 51
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

print(f"Page size: {w} x {h}")

text_instances = page.search_for("Figure 1-24")
for inst in text_instances:
    print(f"Text 'Figure 1-24' at: {inst}")
    print(f"Normalized: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")

# Look for drawings
drawings = page.get_drawings()
print(f"Found {len(drawings)} drawings")
for i, d in enumerate(drawings):
    r = d["rect"]
    # Filter out very small or very large (like page borders)
    if r.width < 5 or r.height < 5:
        continue
    # Filter out header/footer
    if r.y0 < 50 or r.y1 > h - 50:
        continue
    # Look for things above the text label
    if r.y1 < 600 and r.y1 > 200:
        print(f"Drawing {i}: {r}")
        print(f"Normalized: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f}")

# Look for images
images = page.get_image_info()
print(f"Found {len(images)} images")
for i, img in enumerate(images):
    r = fitz.Rect(img["bbox"])
    print(f"Image {i}: {r}")
    print(f"Normalized: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f}")
