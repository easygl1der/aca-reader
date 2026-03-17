import fitz
import json

def get_figure_bbox(pdf_path, page_num, figure_label):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num - 1)  # 0-indexed
    
    width = page.rect.width
    height = page.rect.height
    
    print(f"Page size: {width} x {height}")
    
    # Find figure label
    text_instances = page.search_for(figure_label)
    if not text_instances:
        print(f"Could not find label {figure_label}")
        return
    
    label_rect = text_instances[0]
    print(f"Label rect: {label_rect}")
    
    # Find all text blocks to see the full caption
    blocks = page.get_text("blocks")
    caption_block = None
    for b in blocks:
        if figure_label in b[4]:
            caption_block = fitz.Rect(b[:4])
            print(f"Caption block text: {b[4].strip()}")
            print(f"Caption block rect: {caption_block}")
            break
            
    # Find graphics/images near the label
    # Usually the figure is above the label
    
    # Get all drawings
    drawings = page.get_drawings()
    # Get all images
    images = page.get_image_info()
    
    relevant_rects = []
    if caption_block:
        relevant_rects.append(caption_block)
    else:
        relevant_rects.append(label_rect)
        
    # Look for items above the label
    for d in drawings:
        d_rect = fitz.Rect(d['rect'])
        # If it's above the label and not too far
        if d_rect.y1 < label_rect.y0 and d_rect.y1 > label_rect.y0 - 400:
            relevant_rects.append(d_rect)
            
    for img in images:
        img_rect = fitz.Rect(img['bbox'])
        if img_rect.y1 < label_rect.y0 and img_rect.y1 > label_rect.y0 - 400:
            relevant_rects.append(img_rect)

    if not relevant_rects:
        print("No relevant graphics found")
        return

    # Compute bounding box that covers all relevant parts
    x1 = min(r.x0 for r in relevant_rects)
    y1 = min(r.y0 for r in relevant_rects)
    x2 = max(r.x1 for r in relevant_rects)
    y2 = max(r.y1 for r in relevant_rects)
    
    # Add 0.02 margin (of total width/height)
    margin_x = 0.02 * width
    margin_y = 0.02 * height
    
    x1 = max(0, x1 - margin_x)
    y1 = max(0, y1 - margin_y)
    x2 = min(width, x2 + margin_x)
    y2 = min(height, y2 + margin_y)
    
    # Normalize
    nx1 = x1 / width
    ny1 = y1 / height
    nx2 = x2 / width
    ny2 = y2 / height
    
    print(f"Figure: {figure_label}")
    print(f"Bounding Box: x1={nx1:.2f}, y1={ny1:.2f}, x2={nx2:.2f}, y2={ny2:.2f}")

get_figure_bbox('PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf', 86, 'Figure 2-12')
