import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 62
page = doc.load_page(page_num)

print("--- Drawings ---")
drawings = page.get_drawings()
for i, d in enumerate(drawings):
    if d['rect'].width > 50 and d['rect'].height > 50:
        print(f"Drawing {i}: {d['rect']}")

print("--- Images ---")
images = page.get_images()
for img in images:
    print(img)
