import fitz
doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(23)
blocks = page.get_text("blocks")
for b in blocks:
    if "Figure 1-8" in b[4]:
        print(f"Block: {b[4].strip()}")
        print(f"BBox: {b[:4]}")
doc.close()
