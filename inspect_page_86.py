import fitz

doc = fitz.open('PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf')
page = doc.load_page(85)  # page 86
pix = page.get_pixmap()
pix.save("temp_page_86.png")

# Get drawings and their types
drawings = page.get_drawings()
for i, d in enumerate(drawings):
    print(f"Drawing {i}: {d['rect']} (type: {d.get('type')})")

# Get images
images = page.get_image_info()
for i, img in enumerate(images):
    print(f"Image {i}: {img['bbox']}")

# Get text blocks
blocks = page.get_text("blocks")
for b in blocks:
    print(f"Block: {b[:4]} - {b[4].strip()}")
