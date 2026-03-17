import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 50 # Page 51
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

# Target Figure 1-23
# We know the label is at y ~ 320
label_rect = fitz.Rect(191.85899353027344, 317.43780517578125, 242.60714721679688, 329.1353759765625)

# Find all drawings and text in the upper half of the page
drawings = page.get_drawings()
text_blocks = page.get_text("dict")["blocks"]

fig_rects = []

# Filter drawings
for d in drawings:
    r = d["rect"]
    if r.y1 < 315 and r.y0 > 50: # Above the caption
        if r.width > 2 or r.height > 2:
            fig_rects.append(r)

# Filter text
for b in text_blocks:
    if "bbox" in b:
        r = fitz.Rect(b["bbox"])
        # Check if it's near the figure (e.g. y, x, E, 0, p(t), a(t))
        if r.y1 < 315 and r.y0 > 100:
            # We want to exclude the main text above
            # The main text ends around y=100
            if r.x0 > 100 and r.x1 < 400: # Figures are usually centered
                fig_rects.append(r)
    if "lines" in b:
        for l in b["lines"]:
            r = fitz.Rect(l["bbox"])
            if r.y1 < 315 and r.y0 > 150:
                 fig_rects.append(r)

if fig_rects:
    x0 = min(r.x0 for r in fig_rects)
    y0 = min(r.y0 for r in fig_rects)
    x1 = max(r.x1 for r in fig_rects)
    y1 = max(r.y1 for r in fig_rects)
    
    # Include the caption label too? The prompt says "Precise location of Figure 1-23". 
    # Usually it includes the caption.
    x0 = min(x0, label_rect.x0)
    y0 = min(y0, label_rect.y0)
    x1 = max(x1, label_rect.x1)
    y1 = max(y1, label_rect.y1)

    # Margin
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5

    print(f"Figure 1-23 Bounding Box: x1={x0/w:.4f}, y1={y0/h:.4f}, x2={x1/w:.4f}, y2={y1/h:.4f}")
    
    # Save final crop
    rect = fitz.Rect(x0, y0, x1, y1)
    pix = page.get_pixmap(clip=rect)
    pix.save("fig_1_23_final.png")
