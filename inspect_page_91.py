import fitz

def inspect_page(pdf_path, page_num):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)
    
    text_blocks = page.get_text("blocks")
    drawings = page.get_drawings()
    
    width = page.rect.width
    height = page.rect.height
    
    print(f"Page Size: width={width}, height={height}")
    
    print("\nText Blocks:")
    for b in text_blocks:
        print(f"Bbox: {b[:4]}, Text: {b[4].strip()}")
        
    print("\nDrawings count:", len(drawings))
    # Filter and group drawings to find the figure
    for i, d in enumerate(drawings):
        if i < 10: # Just show first few
             print(f"Drawing {i} Bbox: {d['rect']}")
            
    doc.close()

if __name__ == "__main__":
    pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
    inspect_page(pdf_path, 90)
