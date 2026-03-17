import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page = doc.load_page(23)
w, h = page.rect.width, page.rect.height

blocks = page.get_text("blocks")
for b in blocks:
    print(f"Text: {b[4].strip()}")
    print(f"Rect: {b[:4]}")

drawings = page.get_drawings()
for i, d in enumerate(drawings):
    print(f"Drawing {i}: {d['rect']}")

doc.close()
