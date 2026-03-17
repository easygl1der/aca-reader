import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 63 # Page 64 is index 63
page = doc.load_page(page_num)

print("--- Images ---")
image_list = page.get_images(full=True)
for img in image_list:
    print(img)

print("\n--- Drawings ---")
drawings = page.get_drawings()
for i, d in enumerate(drawings):
    if i < 10 or i > len(drawings) - 10:
        print(f"Drawing {i}: {d['rect']}")

print(f"\nTotal drawings: {len(drawings)}")

print("\n--- Text Blocks ---")
blocks = page.get_text("blocks")
for b in blocks:
    print(f"Bbox: {b[:4]}, Text: {b[4].strip()}")
