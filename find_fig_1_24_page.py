import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text_instances = page.search_for("Figure 1-24")
    if text_instances:
        print(f"Found on page {page_num + 1}")
        for inst in text_instances:
            print(f"BBox: {inst}")
        break
