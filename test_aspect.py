from PIL import Image
import fitz

img = Image.open("/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png")
print(f"Image size: {img.size}, aspect ratio: {img.size[0]/img.size[1]:.4f}")

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(66)
print(f"PDF page size: {page.rect.width}x{page.rect.height}, aspect ratio: {page.rect.width/page.rect.height:.4f}")
