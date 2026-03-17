import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)

target = "Figure 1-9"
found_page = -1

for i in range(len(doc)):
    page = doc.load_page(i)
    text = page.get_text()
    if target in text:
        found_page = i
        break

if found_page == -1:
    print(f"'{target}' not found.")
    doc.close()
    exit()

print(f"Found '{target}' on page {found_page}")
page = doc.load_page(found_page)
w = page.rect.width
h = page.rect.height

# Find the label bbox
blocks = page.get_text("blocks")
label_rect = None
for b in blocks:
    if target in b[4]:
        label_rect = fitz.Rect(b[:4])
        print(f"Label found: {b[4].strip()} at {label_rect}")

# Typically the figure is above or near the label.
# In Do Carmo, figures are often to the side or above.
# Let's look for drawings nearby.
drawings = page.get_drawings()
x_min, y_min, x_max, y_max = w, h, 0, 0

# Based on previous knowledge (Figure 1-8 and 1-9 are together), 
# they might be in a specific region.
# Let's just gather all drawings that are somewhat close to the label.
for d in drawings:
    r = d["rect"]
    # If the drawing is within some vertical range of the label or just above it
    if r.y1 > label_rect.y0 - 200 and r.y0 < label_rect.y1 + 50:
        if r.x0 > label_rect.x0 - 50 and r.x1 < label_rect.x1 + 100: # Heuristic
            x_min = min(x_min, r.x0)
            x_max = max(x_max, r.x1)
            y_min = min(y_min, r.y0)
            y_max = max(y_max, r.y1)

# Include the label itself in the bbox if needed, or just for reference.
# The user usually wants the whole thing including the caption.
x_min = min(x_min, label_rect.x0)
x_max = max(x_max, label_rect.x1)
y_min = min(y_min, label_rect.y0)
y_max = max(y_max, label_rect.y1)

print(f"BBox: x1={x_min}, y1={y_min}, x2={x_max}, y2={y_max}")
print(f"Normalized: x1={x_min/w:.4f}, y1={y_min/h:.4f}, x2={x_max/w:.4f}, y2={y_max/h:.4f}")

doc.close()
