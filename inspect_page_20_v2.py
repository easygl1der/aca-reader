import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 19 # Page 20
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

for fig_name in ["Figure 1-4", "Figure 1-5", "Figure 1-6"]:
    text_instances = page.search_for(fig_name)
    if text_instances:
        for inst in text_instances:
            print(f"Text '{fig_name}': x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")
    else:
        print(f"'{fig_name}' not found on this page.")

print("Drawings (y < 0.6):")
drawings = page.get_drawings()
for i, d in enumerate(drawings):
    r = d["rect"]
    if r.width > 5 and r.height > 5 and r.y1/h < 0.6:
        print(f"Drawing {i}: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f} (w={r.width:.1f}, h={r.height:.1f})")
