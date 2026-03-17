import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 19 # Page 20
page = doc.load_page(page_num)
pix = page.get_pixmap()
pix.save("temp_page_20.png")
print("Saved temp_page_20.png")
