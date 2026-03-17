import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 50 # Page 51
page = doc.load_page(page_num)
w = page.rect.width
h = page.rect.height

# Label boundaries
y_min_limit = 330 
y_max_limit = 583.18 

x_coords = []
y_coords = []

# Check drawings
drawings = page.get_drawings()
for d in drawings:
    r = d["rect"]
    # Skip if too large or outside our y-range
    if r.y1 < y_min_limit or r.y0 > y_max_limit: continue
    if r.width > w * 0.9 or r.height > h * 0.9: continue
    if r.width < 1 or r.height < 1: continue
    
    x_coords.extend([r.x0, r.x1])
    y_coords.extend([r.y0, r.y1])

# Check text blocks
blocks = page.get_text("blocks")
for b in blocks:
    r = fitz.Rect(b[:4])
    if r.y1 < y_min_limit or r.y0 > y_max_limit: continue
    if len(b[4].strip()) > 100: continue # Likely main text
    
    # Check if it's one of our labels or inside the range
    if "Figure 1-24" in b[4] or (r.x0 > 100 and r.x1 < 400):
        x_coords.extend([r.x0, r.x1])
        y_coords.extend([r.y0, r.y1])

if x_coords:
    x1, y1, x2, y2 = min(x_coords), min(y_coords), max(x_coords), max(y_coords)
    print(f"Absolute BBox: x1={x1}, y1={y1}, x2={x2}, y2={y2}")
    print(f"Normalized: x1={x1/w:.4f}, y1={y1/h:.4f}, x2={x2/w:.4f}, y2={y2/h:.4f}")
else:
    print("No components found")
