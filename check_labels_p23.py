import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page = doc.load_page(23)

# Get detailed text info
dict = page.get_text("dict")
for block in dict["blocks"]:
    if "lines" in block:
        for line in block["lines"]:
            text = "".join([span["text"] for span in line["spans"]])
            if "Figure 1-9" in text or "Figure 1-8" in text:
                print(f"Line: {text}")
                print(f"BBox: {line['bbox']}")

doc.close()
