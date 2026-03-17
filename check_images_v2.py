import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 63
page = doc.load_page(page_num)

print("--- Image Info ---")
images = page.get_image_info(xrefs=True)
for img in images:
    print(img)

print("--- XObjects ---")
xobjects = page.get_xobjects()
for x in xobjects:
    print(x)
