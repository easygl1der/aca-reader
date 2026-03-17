import fitz
doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
for i, page in enumerate(doc):
    text = page.get_text()
    if "Figure 1-38" in text or "1-38" in text:
         print(f"Page {i+1}: {text.splitlines()[:5]}")
