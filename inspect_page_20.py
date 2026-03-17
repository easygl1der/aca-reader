import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 19 # Page 20
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

print(f"Page {page_num+1} size: {w}x{h}")

# Text Figure 1-5
text_instances = page.search_for("Figure 1-5")
for inst in text_instances:
    print(f"Text 'Figure 1-5': x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")

print("Drawings:")
drawings = page.get_drawings()
for i, d in enumerate(drawings):
    r = d["rect"]
    # Filter out very small drawings or headers
    if r.width > 5 and r.height > 5:
        print(f"Drawing {i}: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f} (w={r.width:.1f}, h={r.height:.1f})")

print("Images:")
image_info = page.get_image_info()
for i, img in enumerate(image_info):
    r = img["bbox"]
    print(f"Image {i}: x1={r[0]/w:.4f}, y1={r[1]/h:.4f}, x2={r[2]/w:.4f}, y2={r[3]/h:.4f}")
