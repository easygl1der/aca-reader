import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)

for page_num in [62, 63]: # 0-indexed
    print(f"--- Page {page_num + 1} ---")
    page = doc.load_page(page_num)
    text = page.get_text("blocks")
    for block in text:
        if "Figure 1-34" in block[4]:
            print(f"Bbox: {block[:4]}")
            print(f"Text: {block[4]}")
            print("-" * 10)
