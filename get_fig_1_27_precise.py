import pymupdf

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = pymupdf.open(pdf_path)
page_idx = 55
page = doc[page_idx]

# Search for Figure 1-27
text_res = page.search_for("Figure 1-27")
if not text_res:
    print("Figure text not found")
    exit()

text_rect = text_res[0]

# Get all drawings
drawings = page.get_drawings()

# Find drawings that are part of Figure 1-27
# Assuming they are above the text and within a reasonable range
# The text is at y ~ 496. Let's look for drawings between y=50 and y=490
fig_drawings = [d for d in drawings if d["rect"].y1 < text_rect.y0 and d["rect"].y1 > 50]

if not fig_drawings:
    print("No drawings found above text")
    # Maybe it's an image?
    images = page.get_image_info()
    if images:
        fig_rect = pymupdf.Rect(images[0]["bbox"])
        for img in images[1:]:
             if img["bbox"][1] < text_rect.y0:
                 fig_rect = fig_rect | pymupdf.Rect(img["bbox"])
    else:
        # If no drawings or images, just use the text rect for now or fail
        fig_rect = text_rect
else:
    fig_rect = pymupdf.Rect(fig_drawings[0]["rect"])
    for d in fig_drawings[1:]:
        fig_rect = fig_rect | pymupdf.Rect(d["rect"])

# Union with text rect
total_rect = fig_rect | text_rect

# Normalize coordinates
w = page.rect.width
h = page.rect.height

x1 = total_rect.x0 / w
y1 = total_rect.y0 / h
x2 = total_rect.x1 / w
y2 = total_rect.y1 / h

# Apply 0.02 margin as requested
print(f"Figure: 1-27")
print(f"Bounding Box: x1={max(0, x1-0.02):.2f}, y1={max(0, y1-0.02):.2f}, x2={min(1, x2+0.02):.2f}, y2={min(1, y2+0.02):.2f}")
