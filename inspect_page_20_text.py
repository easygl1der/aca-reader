import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 19 # Page 20
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

print("Text Blocks:")
blocks = page.get_text("blocks")
for b in blocks:
    r = b[:4]
    text = b[4].strip()
    if "Figure" in text or "1-5" in text:
        print(f"Block: x1={r[0]/w:.4f}, y1={r[1]/h:.4f}, x2={r[2]/w:.4f}, y2={r[3]/h:.4f}")
        print(f"Content: {text}")

print("Search results:")
text_instances = page.search_for("Figure 1-5")
for inst in text_instances:
    # Get surrounding text
    rect = inst + (-50, -50, 50, 50) # Expand search area
    surrounding_text = page.get_text("text", clip=rect)
    print(f"Text 'Figure 1-5' at {inst}")
    print(f"Surrounding: {surrounding_text.strip()}")
