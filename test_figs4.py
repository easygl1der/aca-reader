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

paths = page.get_drawings()
for p in paths:
    r = p["rect"]
    if r.width < 5 and r.height < 5:
        continue
    if r.y0 < 0 or r.y1 > h or r.width > w * 0.9:
        continue
    
    if r.y1 < 200:
        if r.x1 < 220:
            figs["1-38"]["elements"].append(("drawing", r))
        else:
            figs["1-39"]["elements"].append(("drawing", r))
    elif r.y0 > 200 and r.y1 < 360:
        if r.x1 < 210:
            figs["1-40"]["elements"].append(("drawing", r))
        else:
            figs["1-41"]["elements"].append(("drawing", r))

words = page.get_text("words")
for w_info in words:
    x0, y0, x1, y1, text = w_info[:5]
    r = fitz.Rect(x0, y0, x1, y1)
    if y1 < 200:
        if x1 < 220:
            figs["1-38"]["elements"].append(("text: " + text, r))
        else:
            figs["1-39"]["elements"].append(("text: " + text, r))
    elif y0 > 200 and y1 < 360:
        if x1 < 210:
            figs["1-40"]["elements"].append(("text: " + text, r))
        else:
            figs["1-41"]["elements"].append(("text: " + text, r))

for f_id, data in figs.items():
    print(f"\n--- {f_id} ---")
    for el in data["elements"]:
        if isinstance(el, tuple):
            print(f"{el[0]}: {el[1]}")
        else:
            print(f"MAIN TEXT: {el}")
