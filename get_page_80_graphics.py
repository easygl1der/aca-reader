import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page_idx = 79 
page = doc.load_page(page_idx)
w = page.rect.width
h = page.rect.height

drawings = page.get_drawings()
print(f"Total drawings: {len(drawings)}")

# Group drawings by proximity or just list their bboxes
for i, d in enumerate(drawings):
    r = d["rect"]
    # Only print drawings that are reasonably large or in the middle of the page
    if r.width > 2 or r.height > 2:
        print(f"Drawing {i}: x1={r.x0/w:.4f}, y1={r.y0/h:.4f}, x2={r.x1/w:.4f}, y2={r.y1/h:.4f}")

# Also check for images
images = page.get_image_info()
for i, img in enumerate(images):
    r = img["bbox"]
    print(f"Image {i}: x1={r[0]/w:.4f}, y1={r[1]/h:.4f}, x2={r[2]/w:.4f}, y2={r[3]/h:.4f}")
