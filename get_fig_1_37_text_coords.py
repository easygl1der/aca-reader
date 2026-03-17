import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(65)  # Page 66
text_instances = page.search_for("Figure 1-37")

print("Figure 1-37 text instances:")
for inst in text_instances:
    print(inst)

w = page.rect.width
h = page.rect.height

print(f"Page size: {w} x {h}")

for inst in text_instances:
    print(f"Normalized: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")
