import fitz

PDF_PATH = "/Users/yueyh/Projects/aca-workflow/PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(PDF_PATH)
page_num = 34 # 0-indexed is 33? Wait, figure_list says 34, let's check if it's 1-indexed or 0-indexed.
# Usually these lists are 1-indexed if they come from a human or a simple script.
# Let's check page 34 (1-indexed) which is doc[33] and doc[34].

for p in [33, 34]:
    page = doc[p]
    print(f"--- Page {p+1} ---")
    text_instances = page.search_for("Figure 1-14")
    for inst in text_instances:
        print(f"Found 'Figure 1-14' at: {inst}")
    
    # Also look for drawings
    paths = page.get_drawings()
    print(f"Number of drawings: {len(paths)}")
    
    # Get image size
    pix = page.get_pixmap()
    print(f"Page size: {page.rect.width} x {page.rect.height}")
