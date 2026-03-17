import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(58)  # Page 59
blocks = page.get_text("blocks")

for b in blocks:
    # b = (x0, y0, x1, y1, "text", block_no, block_type)
    if "Figure 1-30" in b[4] or "Figure 1-31" in b[4]:
        print(f"Block: {b[4].strip()}")
        print(f"Coords: {b[0]:.2f}, {b[1]:.2f}, {b[2]:.2f}, {b[3]:.2f}")
        w = page.rect.width
        h = page.rect.height
        print(f"Normalized: x1={b[0]/w:.4f}, y1={b[1]/h:.4f}, x2={b[2]/w:.4f}, y2={b[3]/h:.4f}")
        print("-" * 20)
