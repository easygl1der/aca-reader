import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 19 # Page 20
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

print("Text in Figure Area (y: 0.25 - 0.50):")
rect = fitz.Rect(0, 0.25 * h, w, 0.50 * h)
text_dict = page.get_text("dict", clip=rect)

for block in text_dict["blocks"]:
    if "lines" in block:
        for line in block["lines"]:
            for span in line["spans"]:
                r = span["bbox"]
                print(f"Text: '{span['text']}' at x1={r[0]/w:.4f}, y1={r[1]/h:.4f}, x2={r[2]/w:.4f}, y2={r[3]/h:.4f}")
