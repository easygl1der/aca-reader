import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")

def get_bboxes(page_num):
    page = doc.load_page(page_num)
    w = page.rect.width
    h = page.rect.height
    print(f"\nPage {page_num+1} (w={w}, h={h}):")
    
    for f_id in ["1-38", "1-39", "1-40", "1-41"]:
        instances = page.search_for(f"Figure {f_id}")
        for inst in instances:
            print(f"Text 'Figure {f_id}': y1={inst.y0/h:.4f}")
            # get drawings around this text
            y_text = inst.y0
            paths = page.get_drawings()
            min_x, min_y, max_x, max_y = w, h, 0, 0
            found = False
            for p in paths:
                r = p["rect"]
                if r.y1 < y_text and r.y0 > y_text - 300: # drawing above text
                    if r.x0 < min_x: min_x = r.x0
                    if r.y0 < min_y: min_y = r.y0
                    if r.x1 > max_x: max_x = r.x1
                    if r.y1 > max_y: max_y = r.y1
                    found = True
            
            if found:
                # Add text box into bounding box
                min_x = min(min_x, inst.x0)
                min_y = min(min_y, inst.y0)
                max_x = max(max_x, inst.x1)
                max_y = max(max_y, inst.y1)
                
                # Expand by 0.02
                print(f"Figure {f_id}: x1={max(0, min_x/w - 0.02):.4f}, y1={max(0, min_y/h - 0.02):.4f}, x2={min(1, max_x/w + 0.02):.4f}, y2={min(1, max_y/h + 0.02):.4f}")

get_bboxes(65)
get_bboxes(66)
