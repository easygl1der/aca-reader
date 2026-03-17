import fitz
import json

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 63
page = doc.load_page(page_num)

text_dict = page.get_text("dict")
print(json.dumps(text_dict["blocks"], indent=2))
