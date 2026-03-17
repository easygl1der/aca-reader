import fitz

def get_fig_2_11_precise():
    doc = fitz.open('PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf')
    page = doc[83]
    width = page.rect.width
    height = page.rect.height
    
    # Find the caption
    text_instances = page.search_for('Figure 2-11')
    if not text_instances:
        print("Figure 2-11 not found")
        return
    
    caption_rect = text_instances[0]
    
    # Figure 2-11 is usually above the caption
    # Let's look for drawings and text "S" above it
    
    # Search for "S" near the figure
    s_instances = page.search_for('S')
    # Filter "S" that are near the caption
    # The figure is above the caption (y=571)
    relevant_s = [r for r in s_instances if 500 < r.y1 < 580 and 150 < r.x1 < 250]
    
    # Get drawings
    drawings = page.get_drawings()
    relevant_drawings = []
    for d in drawings:
        # Check if the drawing is in the vicinity of Figure 2-11
        # Based on the caption location (165, 572)
        # Be more generous with the range
        if 500 < d['rect'].y1 < 580 and 150 < d['rect'].x1 < 250:
            relevant_drawings.append(d['rect'])
            
    # Also check for images
    images = page.get_image_info()
    relevant_images = []
    for img in images:
        if 500 < img['bbox'][1] < 580 and 150 < img['bbox'][0] < 250:
            relevant_images.append(fitz.Rect(img['bbox']))            
    # Combine all rects
    all_rects = [caption_rect] + relevant_s + relevant_drawings
    
    if not all_rects:
        print("No elements found for Figure 2-11")
        return
        
    x1 = min(r.x0 for r in all_rects)
    y1 = min(r.y0 for r in all_rects)
    x2 = max(r.x1 for r in all_rects)
    y2 = max(r.y1 for r in all_rects)
    
    # Add 0.02 margin (relative)
    # 0.02 of width and height
    margin_x = 0.02 * width
    margin_y = 0.02 * height
    
    x1 = max(0, x1 - margin_x)
    y1 = max(0, y1 - margin_y)
    x2 = min(width, x2 + margin_x)
    y2 = min(height, y2 + margin_y)
    
    # Normalize
    print(f"Figure: 2-11")
    print(f"Bounding Box: x1={x1/width:.2f}, y1={y1/height:.2f}, x2={x2/width:.2f}, y2={y2/height:.2f}")
    
    doc.close()

if __name__ == "__main__":
    get_fig_2_11_precise()
