import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(76)
w = page.rect.width
h = page.rect.height

# Get all drawings
drawings = page.get_drawings()
if drawings:
    # Find the union of all drawing rectangles
    bbox = drawings[0]["rect"]
    for d in drawings[1:]:
        bbox |= d["rect"]
    
    print(f"Total drawings bbox: {bbox}")
    print(f"Normalized: x1={bbox.x0/w:.4f}, y1={bbox.y0/h:.4f}, x2={bbox.x1/w:.4f}, y2={bbox.y1/h:.4f}")

# Get images
images = page.get_image_info()
for i, img in enumerate(images):
    bbox = fitz.Rect(img["bbox"])
    print(f"Image {i} bbox: {bbox}")
    print(f"Normalized: x1={bbox.x0/w:.4f}, y1={bbox.y0/h:.4f}, x2={bbox.x1/w:.4f}, y2={bbox.y1/h:.4f}")
