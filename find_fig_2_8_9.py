import fitz
doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
for i, page in enumerate(doc):
    text = page.get_text()
    if "Figure 2-8" in text:
         print(f"Figure 2-8 found on absolute page {i+1}")
    if "Figure 2-9" in text:
         print(f"Figure 2-9 found on absolute page {i+1}")
