import fitz

def save_page_image(pdf_path, page_num, output_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)
    pix = page.get_pixmap()
    pix.save(output_path)
    doc.close()

if __name__ == "__main__":
    pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
    save_page_image(pdf_path, 90, "temp_page_91.png")
