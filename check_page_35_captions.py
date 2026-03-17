import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_num = 34 # Page 35
page = doc.load_page(page_num)

text_instances = page.search_for("Figure")
if not text_instances:
    text_instances = page.search_for("Fig.")

w = page.rect.width
h = page.rect.height

for inst in text_instances:
    # Get the whole line
    line = page.get_text("text", clip=fitz.Rect(0, inst.y0, w, inst.y1+5))
    print(f"Found text: {line.strip()} at y1={inst.y0/h:.4f}")
