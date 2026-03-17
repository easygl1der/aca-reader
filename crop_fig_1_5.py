import fitz

pdf_path = "PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf"
doc = fitz.open(pdf_path)
page = doc.load_page(19)
w = page.rect.width
h = page.rect.height

# Coordinates found
x1, y1, x2, y2 = 0.1237, 0.2864, 0.6331, 0.4575

# Convert back to points
rect = fitz.Rect(x1*w, y1*h, x2*w, y2*h)

# Add a tiny bit of padding (2 points)
rect.x0 -= 2
rect.y0 -= 2
rect.x1 += 2
rect.y1 += 2

pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(2, 2))
pix.save("/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png")

print(f"Figure: 1-5, Bounding Box: x1={x1:.4f}, y1={y1:.4f}, x2={x2:.4f}, y2={y2:.4f} /Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png")
