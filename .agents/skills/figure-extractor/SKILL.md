# 📘 Skill: 教材插图自动提取流程（完整版）

> 从教材扫描图片中系统化提取数学插图的完整工作流

## 触发词

- 提取插图
- 提取数学图形
- figure extraction
- 教材图片提取
- 批量裁剪 figures
- 提取 chapter X figures

---

## 核心流程

```
原始 PDF
   │
   ▼
【第一步】从 PDF 解析所有 Figure 编号和页码
   │
   ▼
【第二步】用 400 DPI 提取页面 PNG
   │
   ▼
【第三步】用 Gemini 识别 Figure 边界框
   │
   ▼
【第四步】裁剪并保存（按正确编号命名）
   │
   ▼
【第五步】保存裁剪位置到 CSV
```

---

## 第一步：从 PDF 解析 Figure 列表

```python
import fitz
import re

pdf_path = "/path/to/book.pdf"
doc = fitz.open(pdf_path)

# 找所有 Figure 及其页码
figures = {}  # "1-1" -> page_num
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    # 匹配 Figure 1-XX 或 Figure 2-XX
    matches = re.findall(r'Figure\s*(\d+)[-](\d+)', text, re.IGNORECASE)
    for ch, num in matches:
        fig_id = f"{ch}-{num}"
        if fig_id not in figures:
            figures[fig_id] = page_num + 1  # 1-based 页码

print(f"共找到 {len(figures)} 个 Figure")
for fig_id in sorted(figures.keys(), key=lambda x: (int(x.split('-')[0]), int(x.split('-')[1]))):
    print(f"Figure {fig_id}: Page {figures[fig_id]}")

doc.close()
```

---

## 第二步：提取 400 DPI 页面图片

```python
import fitz
import os

pdf_path = "/path/to/book.pdf"
output_dir = "./pages_400dpi"
os.makedirs(output_dir, exist_ok=True)

dpi = 400
scale = dpi / 72
doc = fitz.open(pdf_path)

# 只提取有 figure 的页面
figure_pages = set(figures.values())
for page_num in figure_pages:
    page = doc[page_num - 1]  # 0-based
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
    pix.save(os.path.join(output_dir, f"page-{page_num:03d}.png"))

doc.close()
print(f"提取了 {len(figure_pages)} 个页面")
```

---

## 第三步：Gemini 识别 Figure 位置

### 批量提取脚本

```python
#!/usr/bin/env python3
"""
从教材页面批量提取所有 Figure
使用 Gemini 视觉识别 + 正确编号匹配
"""
import os
import json
import base64
import urllib.request
import ssl
import re
from PIL import Image
import time

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# ========== 配置区 ==========
PDF_PATH = "/path/to/book.pdf"           # PDF 路径
PAGES_DIR = "./pages_400dpi"            # 页面图片目录
OUTPUT_DIR = "./figures"                  # 输出目录
API_KEY = os.environ.get('GEMINI_API_KEY')  # 或直接填写 API Key
MODEL = 'gemini-2.0-flash-exp'          # 支持视觉的模型

# ========== 第一步：从 PDF 解析 Figure 列表 ==========
def get_figure_list():
    doc = fitz.open(PDF_PATH)
    figures = {}
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        matches = re.findall(r'Figure\s*(\d+)[-](\d+)', text, re.IGNORECASE)
        for ch, num in matches:
            fig_id = f"{ch}-{num}"
            if fig_id not in figures:
                figures[fig_id] = page_num + 1
    doc.close()
    return figures

# ========== 第二步：Gemini 识别 ==========
def call_gemini(image_path, figure_ids_on_page):
    """调用 Gemini 识别页面中的 figures"""
    with open(image_path, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('utf-8')

    # 构建 prompt，包含该页所有 figure 编号
    figures_str = ", ".join([f"Figure {fid}" for fid in figure_ids_on_page])
    PROMPT = f"""看这张教材原图，找出以下 figures 的精确位置：{figures_str}

对每个 Figure 输出：
Figure: Figure X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字
- 四周留 0.02 边距，确保完整"""

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'
    payload = {
        'contents': [{
            'parts': [
                {'text': PROMPT},
                {'inlineData': {'mimeType': 'image/png', 'data': image_base64}}
            ]
        }],
        'generationConfig': {'temperature': 0.1, 'maxOutputTokens': 4096}
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={
        'Content-Type': 'application/json',
        'x-goog-api-key': API_KEY
    }, method='POST')

    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'candidates' in result:
                return result['candidates'][0]['content']['parts'][0].get('text', '')
    except Exception as e:
        print(f'  Error: {e}')
    return None

def parse_bboxes(text, figure_ids_on_page):
    """解析 Gemini 输出的边界框"""
    results = {}
    for fig_id in figure_ids_on_page:
        # 匹配特定 figure 的坐标
        pattern = rf'Figure\s*{fig_id.replace("-", "[-~]")}.*?Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)'
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            x1, y1, x2, y2 = float(match.group(1)), float(match.group(2)), float(match.group(3)), float(match.group(4))
            # 修正顺序
            if x1 > x2: x1, x2 = x2, x1
            if y1 > y2: y1, y2 = y2, y1
            results[fig_id] = (x1, y1, x2, y2)
    return results

def crop_and_save(figure_id, page_num, bbox):
    """裁剪并保存图片"""
    page_path = os.path.join(PAGES_DIR, f"page-{page_num:03d}.png")
    img = Image.open(page_path)
    W, H = img.size

    x1, y1, x2, y2 = bbox
    box = (int(W * x1), int(H * y1), int(W * x2), int(H * y2))
    crop = img.crop(box)

    out_name = f"fig_{figure_id}.png"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    crop.save(out_path, quality=95)
    return out_path, box

# ========== 主流程 ==========
os.makedirs(PAGES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. 获取 Figure 列表
figures = get_figure_list()
print(f"共 {len(figures)} 个 Figure")

# 2. 提取页面图片（只提取有 figure 的页面）
doc = fitz.open(PDF_PATH)
scale = 400 / 72
figure_pages = set(figures.values())
for page_num in figure_pages:
    page_path = os.path.join(PAGES_DIR, f"page-{page_num:03d}.png")
    if not os.path.exists(page_path):
        page = doc[page_num - 1]
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
        pix.save(page_path)
doc.close()

# 3. 按页处理：每页调用一次 Gemini
results = []
crop_positions = []

for page_num in sorted(figure_pages):
    # 该页所有 figure 编号
    page_figs = [k for k, v in figures.items() if v == page_num]
    if not page_figs:
        continue

    print(f"\n[Page {page_num}] 处理 {len(page_figs)} 个 figures...")
    page_path = os.path.join(PAGES_DIR, f"page-{page_num:03d}.png")

    text = call_gemini(page_path, page_figs)
    if not text:
        print(f"  ⚠️ Gemini 调用失败")
        continue

    bboxes = parse_bboxes(text, page_figs)
    print(f"  识别到 {len(bboxes)} 个边界框")

    for fig_id in page_figs:
        if fig_id in bboxes:
            out_path, box = crop_and_save(fig_id, page_num, bboxes[fig_id])
            print(f"  ✓ fig_{fig_id}.png: {box}")
            results.append((fig_id, "OK"))
            crop_positions.append({
                "figure": f"fig_{fig_id}",
                "source_page": page_num,
                "left": box[0], "top": box[1],
                "right": box[2], "bottom": box[3]
            })
        else:
            print(f"  ⚠️ fig_{fig_id} 未识别到")
            results.append((fig_id, "MISSING"))

    time.sleep(0.3)  # 避免 API 限流

# 4. 保存裁剪位置到 CSV
csv_path = os.path.join(OUTPUT_DIR, "figure_crop_positions.csv")
with open(csv_path, "w") as f:
    f.write("figure,source_page,left,top,right,bottom\n")
    for pos in crop_positions:
        f.write(f"{pos['figure']},{pos['source_page']},{pos['left']},{pos['top']},{pos['right']},{pos['bottom']}\n")

print(f"\n\n=== 完成 ===")
print(f"成功: {sum(1 for r in results if r[1] == 'OK')}/{len(results)}")
print(f"裁剪位置: {csv_path}")
```

---

## 第四步：手动提取单个 Figure

如果批量提取失败，可以单独提取：

```python
import os, json, base64, urllib.request, ssl, re
from PIL import Image

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL = 'gemini-2.0-flash-exp'

# 配置
image_path = "./pages_400dpi/page-019.png"
output_path = "./figures/fig_1-1.png"
figure_id = "1-1"

img = Image.open(image_path)
W, H = img.size

PROMPT = f'''看这张教材原图，找出 Figure {figure_id} 的精确位置。

输出格式：
Figure: Figure {figure_id}
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 "Figure {figure_id}"
- 四周留 0.02 边距'''

with open(image_path, 'rb') as f:
    image_base64 = base64.b64encode(f.read()).decode('utf-8')

url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'
payload = {
    'contents': [{
        'parts': [
            {'text': PROMPT},
            {'inlineData': {'mimeType': 'image/png', 'data': image_base64}}
        ]
    }],
    'generationConfig': {'temperature': 0.1, 'maxOutputTokens': 4096}
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={
    'Content-Type': 'application/json',
    'x-goog-api-key': API_KEY
}, method='POST')

with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
    result = json.loads(response.read().decode('utf-8'))
    text = result['candidates'][0]['content']['parts'][0].get('text', '')
    print(text)

    bbox_match = re.search(r'Bounding Box:\s*x1=(0\.\d+),\s*y1=(0\.\d+),\s*x2=(0\.\d+),\s*y2=(0\.\d+)', text)
    if bbox_match:
        x1, y1, x2, y2 = float(bbox_match.group(1)), float(bbox_match.group(2)), float(bbox_match.group(3)), float(bbox_match.group(4))
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        box = (int(W * x1), int(H * y1), int(W * x2), int(H * y2))
        crop = img.crop(box)
        crop.save(output_path, quality=95)
        print(f'✓ 已保存: {output_path}')
        print(f'  裁剪位置: left={box[0]}, top={box[1]}, right={box[2]}, bottom={box[3]}')
```

---

## 第五步：查找缺失的 Figure

```python
import fitz
import re

pdf_path = '/path/to/book.pdf'
doc = fitz.open(pdf_path)

# 找所有 Figure
figures = {}
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    matches = re.findall(r'Figure\s*(\d+)[-](\d+)', text, re.IGNORECASE)
    for ch, num in matches:
        fig_id = f"{ch}-{num}"
        if fig_id not in figures:
            figures[fig_id] = page_num + 1

# 读取已提取的图片
import os
extracted = set()
for f in os.listdir('./figures'):
    if f.startswith('fig_') and f.endswith('.png'):
        # fig_1-1.png -> 1-1
        extracted.add(f[4:-4])

# 对比
missing = set(figures.keys()) - extracted
print(f"缺失 {len(missing)} 个 Figure:")
for fig_id in sorted(missing, key=lambda x: (int(x.split('-')[0]), int(x.split('-')[1]))):
    print(f"  Figure {fig_id}: Page {figures[fig_id]}")

doc.close()
```

---

## 快速开始

```bash
# 1. 修改脚本中的配置
# PDF_PATH = "/path/to/Do Carmo.pdf"
# PAGES_DIR = "./pages_400dpi"
# OUTPUT_DIR = "./figures"

# 2. 运行批量提取
python3 extract_figures.py

# 3. 检查结果
ls figures/fig_*.png | wc -l

# 4. 检查裁剪位置
cat figures/figure_crop_positions.csv
```

---

## 重要提醒

1. **必须先解析 Figure 列表**：用 PDF 文本分析得到正确编号，不要让 Gemini 自由识别
2. **400 DPI**：使用 `fitz.Matrix(400/72, 400/72)` 而不是 `fitz.Matrix(2, 2)`
3. **保存裁剪位置**：提取后必须保存 CSV，记录 figure、页码、left、top、right、bottom
4. **直接覆盖**：同名文件直接覆盖，不要生成 fig_1-1_1.png
5. **检查完整性**：提取后检查图片是否包含完整的图注和坐标轴标签

---

## 输出格式

### figures/ 目录
```
figures/
├── fig_1-1.png
├── fig_1-2.png
├── fig_1-3.png
└── ...
```

### figure_crop_positions.csv
```csv
figure,source_page,left,top,right,bottom
fig_1-1,19,100,200,500,600
fig_1-2,19,150,250,450,550
...
```

---

> 更新于 2026-03-17：修复了 DPI 配置、添加了 Figure 编号解析、添加了裁剪位置保存
