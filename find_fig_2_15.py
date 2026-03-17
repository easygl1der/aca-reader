import fitz

def find_figure_page(pdf_path, figure_label):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_instances = page.search_for(figure_label)
        if text_instances:
            print(f"Found {figure_label} on PDF page {page_num + 1}")
            for inst in text_instances:
                print(f"Coordinates: {inst}")
    doc.close()

if __name__ == "__main__":
    pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
    find_figure_page(pdf_path, "Figure 2-15")
