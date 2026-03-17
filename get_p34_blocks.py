import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_num = 33 # Page 34
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

text = page.get_text("blocks")
for b in text:
    r = b[:4]
    print(f"Block: {b[4].strip()}, Rect: {r}, Normalized: y1={r[1]/h:.4f}")
