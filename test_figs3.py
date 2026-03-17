import fitz

doc = fitz.open("PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.pdf")
page = doc.load_page(66)
w = page.rect.width
h = page.rect.height

figs = {
    "1-38": {"text": None, "elements": []},
    "1-39": {"text": None, "elements": []},
    "1-40": {"text": None, "elements": []},
    "1-41": {"text": None, "elements": []},
}

for f_id in figs.keys():
    for inst in page.search_for(f"Figure {f_id}"):
        figs[f_id]["text"] = inst
        figs[f_id]["elements"].append(inst)

# Get all drawings
paths = page.get_drawings()
for p in paths:
    r = p["rect"]
    if r.width < 5 and r.height < 5:
        continue
    if r.y0 < 0 or r.y1 > h or r.width > w * 0.9:
        continue
    
    # Assign to figure based on position
    if r.y1 < 200: # 1-38 or 1-39
        if r.x1 < 220:
            figs["1-38"]["elements"].append(r)
        else:
            figs["1-39"]["elements"].append(r)
    elif r.y0 > 200 and r.y1 < 360: # 1-40 or 1-41
        if r.x1 < 210:
            figs["1-40"]["elements"].append(r)
        else:
            figs["1-41"]["elements"].append(r)

# Get all text words
words = page.get_text("words")
for w_info in words:
    x0, y0, x1, y1, text = w_info[:5]
    r = fitz.Rect(x0, y0, x1, y1)
    if y1 < 200:
        if x1 < 220:
            figs["1-38"]["elements"].append(r)
        else:
            figs["1-39"]["elements"].append(r)
    elif y0 > 200 and y1 < 360:
        if x1 < 210:
            figs["1-40"]["elements"].append(r)
        else:
            figs["1-41"]["elements"].append(r)

for f_id, data in figs.items():
    if not data["elements"]:
        continue
    
    min_x = min(e.x0 for e in data["elements"])
    min_y = min(e.y0 for e in data["elements"])
    max_x = max(e.x1 for e in data["elements"])
    max_y = max(e.y1 for e in data["elements"])
    
    # Add text box explicitly again just in case
    t = data["text"]
    if t:
        min_x = min(min_x, t.x0)
        min_y = min(min_y, t.y0)
        max_x = max(max_x, t.x1)
        max_y = max(max_y, t.y1)
    
    nx1 = max(0.0, min_x/w - 0.02)
    ny1 = max(0.0, min_y/h - 0.02)
    nx2 = min(1.0, max_x/w + 0.02)
    ny2 = min(1.0, max_y/h + 0.02)
    
    print(f"Figure: {f_id}")
    print(f"Bounding Box: x1={nx1:.4f}, y1={ny1:.4f}, x2={nx2:.4f}, y2={ny2:.4f}")

