import fitz
import json

doc = fitz.open('PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf')
page = doc[91] # Page 92 is index 91

# Get text instances for Figure 2-16
text_instances = page.search_for("Figure 2-16")
print(f"Text instances: {text_instances}")

# Get all drawings
drawings = page.get_drawings()

# Get image resolution
pix = page.get_pixmap()
width = page.rect.width
height = page.rect.height

print(f"Page size: {width} x {height}")

# Find drawings near the text instance
if text_instances:
    fig_text_rect = text_instances[0]
    # Look for drawings above the text (typical for these figures)
    # or text that belongs to the figure labels
    
    # Let's find all text blocks on the page to see context
    blocks = page.get_text("blocks")
    for b in blocks:
        if "Figure 2-16" in b[4]:
            print(f"Block containing Figure 2-16: {b[:4]}")
            print(f"Text: {b[4]}")

# Export drawings to check their positions
drawings_summary = []
for d in drawings:
    drawings_summary.append({
        "rect": [d["rect"].x0, d["rect"].y0, d["rect"].x1, d["rect"].y1],
        "items": len(d["items"])
    })

with open("page_92_drawings.json", "w") as f:
    json.dump(drawings_summary, f)
