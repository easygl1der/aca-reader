import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(23)
drawings = page.get_drawings()

# Figure 1-8 x-range: [50, 210]
for i, d in enumerate(drawings):
    r = d['rect']
    if r[0] < 220 and r[2] > 40:
        print(f"Drawing {i}: {r}")

doc.close()
