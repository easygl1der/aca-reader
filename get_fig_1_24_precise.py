import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 50 # Page 51
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

# Label boundaries
y_sep = 330 # Just below Figure 1-23 label
y_end = 583.18 # Bottom of Figure 1-24 label

x_min = w
x_max = 0
y_min = h
y_max = 0

# Check drawings
drawings = page.get_drawings()
for d in drawings:
    r = d["rect"]
    if r.y1 > y_sep and r.y0 < y_end:
        if r.width < 5 or r.height < 5: continue
        x_min = min(x_min, r.x0)
        x_max = max(x_max, r.x1)
        y_min = min(y_min, r.y0)
        y_max = max(y_max, r.y1)

# Check text blocks
blocks = page.get_text("blocks")
for b in blocks:
    r = fitz.Rect(b[:4])
    if r.y1 > y_sep and r.y0 < y_end:
        # Exclude main text blocks if any
        if "Figure 1-24" in b[4]:
             x_min = min(x_min, r.x0)
             x_max = max(x_max, r.x1)
             y_min = min(y_min, r.y0)
             y_max = max(y_max, r.y1)
             continue
        if len(b[4].strip()) > 50: continue # Likely main text
        
        x_min = min(x_min, r.x0)
        x_max = max(x_max, r.x1)
        y_min = min(y_min, r.y0)
        y_max = max(y_max, r.y1)

print(f"Absolute BBox: x1={x_min}, y1={y_min}, x2={x_max}, y2={y_max}")
print(f"Normalized: x1={x_min/w:.4f}, y1={y_min/h:.4f}, x2={x_max/w:.4f}, y2={y_max/h:.4f}")
