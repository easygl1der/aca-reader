import fitz
import json

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)

search_term = "Figure 1-34"
results = []

for page_num in range(50, 80):
    page = doc.load_page(page_num)
    text_instances = page.search_for(search_term)
    if text_instances:
        for inst in text_instances:
            results.append({
                "page": page_num + 1,
                "bbox": [inst.x0, inst.y0, inst.x1, inst.y1],
                "text": search_term
            })

print(json.dumps(results, indent=2))
