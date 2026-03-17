import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_num = 34 # Page 35
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

# Get text in the upper part of the page
text = page.get_text("blocks")
for b in text:
    r = b[:4]
    print(f"Block: {b[4].strip()}, Rect: {r}, Normalized: y1={r[1]/h:.4f}")
