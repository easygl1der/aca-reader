import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(58)  # Page 59
text_instances_30 = page.search_for("Figure 1-30")
text_instances_31 = page.search_for("Figure 1-31")

print("Figure 1-30 text instances:")
for inst in text_instances_30:
    print(inst)

print("Figure 1-31 text instances:")
for inst in text_instances_31:
    print(inst)

# Get normalized coordinates
w = page.rect.width
h = page.rect.height

print("\nNormalized (x1, y1, x2, y2):")
for inst in text_instances_30:
    print(f"1-30: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")
for inst in text_instances_31:
    print(f"1-31: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")
