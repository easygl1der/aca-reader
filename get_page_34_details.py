import fitz

PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(PDF_PATH)
page = doc[33] # Page 34

print(f"Page size: {page.rect}")

# Find Figure 1-14 text again
text_instances = page.search_for("Figure 1-14")
print(f"Figure 1-14 text rect: {text_instances}")

# Get all drawings
paths = page.get_drawings()
for i, path in enumerate(paths):
    print(f"Drawing {i}: rect={path['rect']}")

# Get images
images = page.get_images(full=True)
for i, img in enumerate(images):
    print(f"Image {i}: {img}")
    # Get image rect
    img_info = page.get_image_info(hashes=False)
    for info in img_info:
        print(f"Image info: {info['bbox']}")
