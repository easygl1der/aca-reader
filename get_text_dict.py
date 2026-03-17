import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(58)
w = page.rect.width
h = page.rect.height
d = page.get_text("dict")

for b in d["blocks"]:
    contains_fig = False
    if "lines" in b:
        for l in b["lines"]:
            text = "".join([s["text"] for s in l["spans"]])
            if "Figure 1-30" in text or "Figure 1-31" in text:
                contains_fig = True
        if contains_fig:
            for l in b["lines"]:
                text = "".join([s["text"] for s in l["spans"]])
                print(f"Line: {text}")
                r = l["bbox"]
                print(f"Normalized: x1={r[0]/w:.4f}, y1={r[1]/h:.4f}, x2={r[2]/w:.4f}, y2={r[3]/h:.4f}")

