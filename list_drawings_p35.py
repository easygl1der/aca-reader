import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_num = 34 # Page 35
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

drawings = page.get_drawings()
print(f"Page {page_num+1} drawings:")
for i, d in enumerate(drawings):
    r = d["rect"]
    print(f"Drawing {i}: {r}, Normalized: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f}")

text_instances = page.search_for("Figure 1-15")
for inst in text_instances:
    print(f"Caption 'Figure 1-15': {inst}, Normalized: y1={inst.y0/h:.4f}")
