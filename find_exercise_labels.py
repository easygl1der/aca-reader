import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(23)
blocks = page.get_text("dict")["blocks"]

for b in blocks:
    if "lines" in b:
        for l in b["lines"]:
            text = "".join([s["text"] for s in l["spans"]])
            if text.strip() in ["a.", "b.", "c."]:
                print(f"Label '{text}' at {l['bbox']}")

doc.close()
