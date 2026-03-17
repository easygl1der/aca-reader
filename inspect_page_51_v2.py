import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 50 # Page 51
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

for fig_label in ["Figure 1-23", "Figure 1-24"]:
    text_instances = page.search_for(fig_label)
    for inst in text_instances:
        print(f"Text '{fig_label}' at: {inst}")
        print(f"Normalized: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")

drawings = page.get_drawings()
for i, d in enumerate(drawings):
    r = d["rect"]
    if r.width < 5 or r.height < 5: continue
    if r.y0 < 50 or r.y1 > h - 50: continue
    print(f"Drawing {i}: {r}, Normalized: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f}")
