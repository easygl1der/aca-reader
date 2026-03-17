import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_num = 33 # Page 34
page = doc.load_page(page_num)

text_instances = page.search_for("Figure 1-15")
print(f"Searching for 'Figure 1-15': {len(text_instances)} found")

text_instances_all = page.search_for("Figure")
print(f"Searching for 'Figure': {len(text_instances_all)} found")
for inst in text_instances_all:
    line = page.get_text("text", clip=fitz.Rect(0, inst.y0, page.rect.width, inst.y1+5))
    print(f"Found: {line.strip()} at y0={inst.y0}")
