import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page_num = 50 # Page 51
page = doc.load_page(page_num)
pix = page.get_pixmap()
pix.save("page_51.png")

# Figure 1-23 label is at Normalized: x1=0.4441, y1=0.4899, x2=0.5616, y2=0.5079
# Drawing 6 is at Normalized: x1=0.3936, y1=0.2654, x2=0.6886, y2=0.4583

# Let's crop a bit more to be sure
# x1=0.3, y1=0.2, x2=0.7, y2=0.52
w = page.rect.width
h = page.rect.height

rect = fitz.Rect(0.3*w, 0.2*h, 0.7*w, 0.52*h)
pix = page.get_pixmap(clip=rect)
pix.save("crop_fig_1_23.png")

print("Saved page_51.png and crop_fig_1_23.png")
