import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page = doc.load_page(19)
w = page.rect.width
h = page.rect.height

blocks = page.get_text("blocks")
for b in blocks:
    print(f"Block: x1={b[0]/w:.4f}, y1={b[1]/h:.4f}, x2={b[2]/w:.4f}, y2={b[3]/h:.4f} | Text: {b[4].strip()}")
