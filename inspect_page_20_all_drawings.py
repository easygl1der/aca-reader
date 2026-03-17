import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 19 # Page 20
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

print("All Drawings:")
drawings = page.get_drawings()
for i, d in enumerate(drawings):
    r = d["rect"]
    print(f"Drawing {i}: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f} (w={r.width:.1f}, h={r.height:.1f})")
