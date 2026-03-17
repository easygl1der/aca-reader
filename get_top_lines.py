import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(58)
w = page.rect.width
h = page.rect.height
d = page.get_text("dict")

for b in d["blocks"]:
    if "lines" in b:
        for l in b["lines"]:
            text = "".join([s["text"] for s in l["spans"]])
            r = l["bbox"]
            if r[1]/h < 0.1:  # Top 10% of page
                print(f"Line: {text}")
                print(f"Normalized: x1={r[0]/w:.4f}, y1={r[1]/h:.4f}, x2={r[2]/w:.4f}, y2={r[3]/h:.4f}")
