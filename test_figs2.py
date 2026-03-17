import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(66)
w = page.rect.width
h = page.rect.height

for f_id in ["1-38", "1-39", "1-40", "1-41"]:
    for inst in page.search_for(f"Figure {f_id}"):
        print(f"{f_id} text: x0={inst.x0}, y0={inst.y0}, x1={inst.x1}, y1={inst.y1}")

paths = page.get_drawings()
for p in paths:
    r = p["rect"]
    # only print big ones or those in upper half to avoid spam
    if r.y0 < 400 and r.width > 5 and r.height > 5:
        print(f"Drawing: x0={r.x0:.1f}, y0={r.y0:.1f}, x1={r.x1:.1f}, y1={r.y1:.1f}")
