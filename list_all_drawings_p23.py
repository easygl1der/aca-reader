import fitz
doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(23)
drawings = page.get_drawings()
for i, d in enumerate(drawings):
    print(f"Drawing {i}: {d['rect']}")
doc.close()
