import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(23)
w, h = page.rect.width, page.rect.height

# Figure 1-8 vicinity: x [0, 230], y [100, 480]
blocks = page.get_text("dict")["blocks"]
for b in blocks:
    if "lines" in b:
        for l in b["lines"]:
            for s in l["spans"]:
                r = s["bbox"]
                if r[0] < 230 and r[1] > 100 and r[3] < 480:
                    print(f"Text: '{s['text']}' at {r}")

doc.close()
