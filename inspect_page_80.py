import fitz
import json

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_idx = 79 # Absolute page 80
page = doc.load_page(page_idx)
w = page.rect.width
h = page.rect.height

print(f"Page size: {w} x {h}")

# Get text blocks
blocks = page.get_text("blocks")
for b in blocks:
    if "Figure 2-8" in b[4] or "Figure 2-9" in b[4]:
        print(f"Text Block: {b[4].strip()}")
        print(f"Normalized: x1={b[0]/w:.4f}, y1={b[1]/h:.4f}, x2={b[2]/w:.4f}, y2={b[3]/h:.4f}")

# Get drawings to find the visual parts of the figures
drawings = page.get_drawings()
# We might need to filter drawings near the text blocks
