import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(58)
drawings = page.get_drawings()
w = page.rect.width
h = page.rect.height

for d in drawings:
    r = d["rect"]
    if r.y1/h < 0.4: # Only interested in top part
        # Check if it's not the header or border
        if r.y0/h > 0.065:
            print(f"Drawing Rect: {r}")
            print(f"Normalized: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f}")
