import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text_instances = page.search_for("Figure 1-5")
    if text_instances:
        print(f"Page {page_num + 1}: Found 'Figure 1-5'")
        w = page.rect.width
        h = page.rect.height
        for inst in text_instances:
            print(f"  Coordinates: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")
