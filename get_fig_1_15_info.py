import fitz
import json

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")

for page_num in [33, 34]:
    page = doc.load_page(page_num)
    w = page.rect.width
    h = page.rect.height
    print(f"--- Page {page_num + 1} ---")
    
    # Search for text
    text_instances = page.search_for("Figure 1-15")
    if text_instances:
        print(f"Found 'Figure 1-15'")
    else:
        text_instances = page.search_for("Fig. 1-15")
        if text_instances:
            print(f"Found 'Fig. 1-15'")
        
    for inst in text_instances:
        print(f"Text 'Figure 1-15' found at: {inst}")
        print(f"Normalized: x1={inst.x0/w:.4f}, y1={inst.y0/h:.4f}, x2={inst.x1/w:.4f}, y2={inst.y1/h:.4f}")

    # Search for drawings
    drawings = page.get_drawings()
    print(f"Number of drawings: {len(drawings)}")
    
    # Search for images
    images = page.get_images()
    print(f"Number of images: {len(images)}")
