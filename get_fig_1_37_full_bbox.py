import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(65)  # Page 66
w = page.rect.width
h = page.rect.height

print(f"Page Size: {w} x {h}")

# Search for the text
text_instances = page.search_for("Figure 1-37")
if text_instances:
    fig_text_rect = text_instances[0]
    print(f"Figure Text Rect: {fig_text_rect}")
else:
    print("Figure 1-37 text not found")
    exit()

# Get drawings
drawings = page.get_drawings()
print(f"Number of drawings: {len(drawings)}")

# Find drawings near the figure text
# Usually figures are above the text
fig_bbox = fitz.Rect(fig_text_rect)

for dw in drawings:
    r = dw['rect']
    # If the drawing is above the text and within reasonable horizontal range
    if r.y1 < fig_text_rect.y0 and r.y1 > fig_text_rect.y0 - 200:
        fig_bbox.include_rect(r)

print(f"Combined Figure BBox (Drawings + Text): {fig_bbox}")
print(f"Normalized: x1={fig_bbox.x0/w:.4f}, y1={fig_bbox.y0/h:.4f}, x2={fig_bbox.x1/w:.4f}, y2={fig_bbox.y1/h:.4f}")

# Check images too
images = page.get_image_info()
print(f"Number of images: {len(images)}")
for img in images:
    r = fitz.Rect(img['bbox'])
    print(f"Image BBox: {r}")
    if r.y1 < fig_text_rect.y0 and r.y1 > fig_text_rect.y0 - 300:
        fig_bbox.include_rect(r)

print(f"Final Figure BBox: {fig_bbox}")
print(f"Final Normalized: x1={fig_bbox.x0/w:.4f}, y1={fig_bbox.y0/h:.4f}, x2={fig_bbox.x1/w:.4f}, y2={fig_bbox.y1/h:.4f}")
