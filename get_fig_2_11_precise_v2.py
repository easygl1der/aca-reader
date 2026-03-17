import fitz

def get_fig_2_11_precise_v2():
    doc = fitz.open('PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf')
    page = doc[83]
    width = page.rect.width
    height = page.rect.height
    
    # 1. Caption
    text_instances = page.search_for('Figure 2-11')
    caption_rect = text_instances[0]
    
    # 2. Drawings in the vicinity
    drawings = page.get_drawings()
    relevant_drawings = []
    # Search for drawings around the caption and to its left
    for d in drawings:
        r = d['rect']
        # The figure is to the left or above the caption
        if 480 < r.y1 < 600 and 40 < r.x1 < 250:
            relevant_drawings.append(r)
            
    # 3. Text labels like "S"
    s_instances = page.search_for('S')
    relevant_text = [r for r in s_instances if 480 < r.y1 < 600 and 40 < r.x1 < 250]
    
    # 4. Images
    image_info = page.get_image_info()
    relevant_images = [fitz.Rect(img['bbox']) for img in image_info if 480 < img['bbox'][3] < 600 and 40 < img['bbox'][0] < 250]
    
    # Combine all
    all_rects = [caption_rect] + relevant_drawings + relevant_text + relevant_images
    
    x1 = min(r.x0 for r in all_rects)
    y1 = min(r.y0 for r in all_rects)
    x2 = max(r.x1 for r in all_rects)
    y2 = max(r.y1 for r in all_rects)
    
    # Margin 0.02 relative
    margin_x = 0.02 * width
    margin_y = 0.02 * height
    
    x1 = max(0, x1 - margin_x)
    y1 = max(0, y1 - margin_y)
    x2 = min(width, x2 + margin_x)
    y2 = min(height, y2 + margin_y)
    
    print(f"Figure: 2-11")
    print(f"Bounding Box: x1={x1/width:.2f}, y1={y1/height:.2f}, x2={x2/width:.2f}, y2={y2/height:.2f}")
    
    doc.close()

if __name__ == "__main__":
    get_fig_2_11_precise_v2()
