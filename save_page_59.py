import fitz
import sys

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(58)  # page index 58 is page 59
pix = page.get_pixmap()
pix.save("page_59.png")
print("Saved page 59 to page_59.png")
