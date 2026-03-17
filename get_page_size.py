import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 63
page = doc.load_page(page_num)
rect = page.rect
print(f"Page size: {rect.width} x {rect.height}")
