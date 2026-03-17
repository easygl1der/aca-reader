import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 50 # Page 51
page = doc.load_page(page_num)
blocks = page.get_text("blocks")
w = page.rect.width
h = page.rect.height

for b in blocks:
    print(f"Block: {b[4].strip()}")
    print(f"Coords: {b[0]:.2f}, {b[1]:.2f}, {b[2]:.2f}, {b[3]:.2f}")
    print(f"Normalized: x1={b[0]/w:.4f}, y1={b[1]/h:.4f}, x2={b[2]/w:.4f}, y2={b[3]/h:.4f}")
    print("-" * 20)
