import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_idx = 58
page = doc.load_page(page_idx)
w = page.rect.width
h = page.rect.height
d = page.get_text("dict")

# Find lines for Figure 1-30 caption
caption_lines = []
for b in d["blocks"]:
    if "lines" in b:
        for l in b["lines"]:
            span_text = "".join([s["text"] for s in l["spans"]])
            if "Figure 1-30" in span_text or "corresponding straight line" in span_text:
                caption_lines.append(l["bbox"])

cx1 = min(l[0] for l in caption_lines)
cy1 = min(l[1] for l in caption_lines)
cx2 = max(l[2] for l in caption_lines)
cy2 = max(l[3] for l in caption_lines)

# Find drawings and labels for Figure 1-30
drawings = page.get_drawings()
fig_elements = []
for dw in drawings:
    db = dw["rect"]
    if db[3] < cy1 and db[0] < 250 and db[1] > 50:
        fig_elements.append(db)

# Find "n =" labels
for b in d["blocks"]:
    if "lines" in b:
        for l in b["lines"]:
            span_text = "".join([s["text"] for s in l["spans"]])
            if "n =" in span_text and l["bbox"][3] < cy1 and l["bbox"][0] < 250:
                fig_elements.append(l["bbox"])
            if "C" in span_text and len(span_text.strip()) == 1 and l["bbox"][3] < cy1 and l["bbox"][0] < 250:
                # Also include the 'C' label
                fig_elements.append(l["bbox"])

if fig_elements:
    fx1 = min(min(e[0] for e in fig_elements), cx1)
    fy1 = min(min(e[1] for e in fig_elements), cy1)
    fx2 = max(max(e[2] for e in fig_elements), cx2)
    fy2 = max(max(e[3] for e in fig_elements), cy2)

    # Apply 0.02 margin
    margin = 0.02
    nx1 = max(0, fx1/w - margin)
    ny1 = max(0, fy1/h - margin)
    nx2 = min(1, fx2/w + margin)
    ny2 = min(1, fy2/h + margin)
    
    print(f"Figure: 1-30")
    print(f"Bounding Box: x1={nx1:.2f}, y1={ny1:.2f}, x2={nx2:.2f}, y2={ny2:.2f}")
