import pymupdf

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = pymupdf.open(pdf_path)
# Based on figure_list.json ("1-28": 57) and get_fig_1_27_precise.py (page_idx=55 for "1-27": 56)
page_idx = 56 
page = doc[page_idx]

# Search for Figure 1-28
text_res = page.search_for("Figure 1-28")
if not text_res:
    text_res = page.search_for("Fig. 1-28")

if not text_res:
    print("Figure text not found")
    exit()

print(f"Found {len(text_res)} occurrences of the text:")
for i, rect in enumerate(text_res):
    print(f"  [{i}] {rect}")

# The caption is usually the one that is NOT inside a paragraph.
# Or just the first one if there's only one.
# On page 57, there might be a reference in the text and the caption.
# Let's assume the caption is the one with the largest y-coordinate among those that are likely captions.
# Actually, in this book, the caption "Figure 1-28" is usually below the figure.
caption_rect = text_res[-1] # Let's try the last one
print(f"Using caption_rect: {caption_rect}")

# Get all drawings
drawings = page.get_drawings()

# Get all images
images = page.get_image_info()

# Find elements that belong to the figure
# We assume the figure is above the caption
fig_elements = []

for d in drawings:
    # Filter out page borders or very large rectangles if any
    if d["rect"].width > page.rect.width * 0.9 and d["rect"].height > page.rect.height * 0.9:
        continue
    if d["rect"].y1 < caption_rect.y1 + 10 and d["rect"].y1 > 50: # Above or near caption
        fig_elements.append(pymupdf.Rect(d["rect"]))

for img in images:
    img_rect = pymupdf.Rect(img["bbox"])
    if img_rect.y1 < caption_rect.y1 + 10 and img_rect.y1 > 50:
        fig_elements.append(img_rect)

if not fig_elements:
    # If no graphics found above, maybe it's just text or we missed it
    total_rect = caption_rect
else:
    total_rect = fig_elements[0]
    for el in fig_elements[1:]:
        total_rect = total_rect | el
    total_rect = total_rect | caption_rect

# Normalize coordinates
w = page.rect.width
h = page.rect.height

x1 = total_rect.x0 / w
y1 = total_rect.y0 / h
x2 = total_rect.x1 / w
y2 = total_rect.y1 / h

# Apply 0.02 margin
print(f"Figure: 1-28")
print(f"Bounding Box: x1={max(0, x1-0.02):.2f}, y1={max(0, y1-0.02):.2f}, x2={min(1, x2+0.02):.2f}, y2={min(1, y2+0.02):.2f}")
