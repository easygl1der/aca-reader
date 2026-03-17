import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(23)
drawings = page.get_drawings()

for i, d in enumerate(drawings):
    r = d['rect']
    print(f"Drawing {i}: x1={r[0]:.4f}, y1={r[1]:.4f}, x2={r[2]:.4f}, y2={r[3]:.4f}")

doc.close()
