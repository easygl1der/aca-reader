import fitz

PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(PDF_PATH)
page = doc[33] # Page 34

image_info = page.get_image_info(hashes=False)
for info in image_info:
    print(f"Image bbox: {info['bbox']}")

# Also check for any other hidden elements
text_dict = page.get_text("dict")
for block in text_dict["blocks"]:
    if block["type"] == 1: # image block
        print(f"Image block bbox: {block['bbox']}")
