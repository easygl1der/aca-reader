import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(76) # Page 77
text = page.get_text("text")
import re
figs = re.findall(r'Figure\s+\d+-\d+', text)
print(f"Figures found on page 77: {set(figs)}")

# Also search for "Fig."
figs2 = re.findall(r'Fig\.\s+\d+-\d+', text)
print(f"Fig. found on page 77: {set(figs2)}")
