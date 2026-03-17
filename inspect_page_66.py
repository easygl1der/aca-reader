import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(65)  # Page 66
w = page.rect.width
h = page.rect.height

text_instances = page.search_for("Figure 1-37")
fig_text_rect = text_instances[0]

print(f"Figure Text Rect: {fig_text_rect}")

drawings = page.get_drawings()
for i, dw in enumerate(drawings):
    print(f"Drawing {i}: {dw['rect']}")

# Let's see if there's text nearby
# Figure 1-37 is usually preceded by some graphics.
# Let's look at all text on the page to see where "Problem 7" is.
page_text = page.get_text("blocks")
for b in page_text:
    print(f"Block: {b[:4]} - Text: {b[4][:50].strip()}")
