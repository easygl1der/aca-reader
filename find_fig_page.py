import pymupdf

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = pymupdf.open(pdf_path)

found_pages = []
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    if "Figure 1-15" in text or "Fig. 1-15" in text:
        found_pages.append(i + 1)

print(f"Figure 1-15 found on pages: {found_pages}")
