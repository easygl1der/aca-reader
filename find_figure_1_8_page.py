import fitz
import sys

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)

target = "Figure 1-8"

found = False
for i in range(len(doc)):
    page = doc.load_page(i)
    text = page.get_text()
    if target in text:
        print(f"Found '{target}' on PDF page index {i} (printed page maybe {i+1}?)")
        found = True
        # Let's also print the context
        blocks = page.get_text("blocks")
        for b in blocks:
            if target in b[4]:
                print(f"Block: {b[4].strip()}")
                print(f"BBox: {b[:4]}")
        break

if not found:
    print(f"'{target}' not found in the PDF.")
doc.close()
