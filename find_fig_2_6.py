import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text_instances = page.search_for("Figure 2-6")
    if text_instances:
        print(f"Found on page {page_num + 1} (0-indexed: {page_num}):")
        for inst in text_instances:
            print(f"  Rect: {inst}")
            w = page.rect.width
            h = page.rect.height
            print(f"  Normalized: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")
