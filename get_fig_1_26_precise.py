import pymupdf

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = pymupdf.open(pdf_path)
page = doc[53]

drawings = page.get_drawings()
# Filter drawings that are part of the figure (above the text)
# The text is at y ~ 187
figure_drawings = [d for d in drawings if d["rect"].y1 < 185 and d["rect"].y1 > 40]

if figure_drawings:
    rect = figure_drawings[0]["rect"]
    for d in figure_drawings[1:]:
        rect = rect | d["rect"]
    print(f"Drawings BBox: {rect}")
else:
    print("No drawings found in the specified range.")

text_res = page.search_for("Figure 1-26")
print(f"Text BBox: {text_res}")
