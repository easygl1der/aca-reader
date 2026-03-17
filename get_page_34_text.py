import fitz

PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(PDF_PATH)
page = doc[33] # Page 34

blocks = page.get_text("blocks")
for b in blocks:
    # b = (x0, y0, x1, y1, "text", block_no, block_type)
    if b[6] == 0: # text block
        print(f"Block: {b[:4]}, text: {repr(b[4])}")
