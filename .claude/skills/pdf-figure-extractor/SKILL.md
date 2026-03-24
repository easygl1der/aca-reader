---
name: pdf-figure-extractor
description: 从教材 PDF 或图片中自动提取数学插图。支持 PDF（600 DPI 高清渲染）和 PNG（400 DPI）两种输入模式，自动使用 Gemini Vision API 识别 figure 边界框并裁剪。具备断点续传（detection_results.json）、独立裁剪模式（--crop-only）、强制重刷（--force）等工业级功能。触发条件：提取教材插图、裁剪 PDF 页面 figure、批量提取 chapter X figures。
---

# PDF 教材插图智能提取工具

## 核心功能

### 1. 双模式支持
- **PDF 模式** (`USE_PDF = True`): 直接处理 PDF 页面，600 DPI 高清渲染
- **图片模式** (`USE_PDF = False`): 处理 400 DPI PNG/JPG 图片

### 2. 智能识别
使用 Gemini Vision API 识别 figure 边界框，精确裁剪

### 3. 断点续传
- 自动保存检测结果到 `detection_results.json`
- 跳过已成功处理的页面
- 自动重试之前失败的页面

### 4. 独立裁剪模式
不调用 API，根据已有坐标重新生成高清图片

---

## 使用方法

### 准备工作

1. 安装依赖：
```bash
uv pip install pymupdf pillow google-genai
```

2. 设置 API Key：
```bash
export GEMINI_API_KEY="your-api-key"
```

### 脚本配置

编辑 `figure_extractor.py` 中的配置区：

```python
# 模式选择
USE_PDF = True  # True: PDF 模式; False: 图片模式

if USE_PDF:
    INPUT_DIR = "chapter2/pages_pdf"      # PDF 页面目录
    OUTPUT_DIR = "chapter2/output_pdf"     # 输出目录
else:
    INPUT_DIR = "chapter2/pages_400dpi"    # 图片目录
    OUTPUT_DIR = "chapter2/output"         # 输出目录

# 指定处理特定文件（为空则处理整个目录）
IMAGE_FILES = []
```

### 运行命令

```bash
# 方式一：使用 --chapter 快速选择章节（推荐）
uv run figure_extractor.py --chapter 2      # 提取 Chapter 2
uv run figure_extractor.py -c 3             # 提取 Chapter 3

# 方式二：手动指定输入输出目录
uv run figure_extractor.py -i ./pages_pdf -o ./output

# 强制重刷所有页面（忽略缓存）
uv run figure_extractor.py --chapter 2 --force

# 仅裁剪模式（不调用 API，使用已有坐标）
uv run figure_extractor.py --chapter 2 --crop-only

# 使用 PNG/图片模式（而非 PDF）
uv run figure_extractor.py --chapter 2 --png

# 查看帮助
uv run figure_extractor.py --help
```

### 命令行参数

| 参数 | 简写 | 说明 |
|------|------|------|
| `--chapter` | `-c` | 快速选择章节（1-5），自动设置路径 |
| `--input` | `-i` | 输入目录（PDF 页面或图片目录） |
| `--output` | `-o` | 输出目录 |
| `--pdf` | - | 使用 PDF 模式（默认） |
| `--png` | - | 使用 PNG/图片模式 |
| `--force` | - | 强制重刷所有页面 |
| `--crop-only` | - | 仅裁剪模式（不调用 API） |

---

## 输出结构

```
chapter2/
├── pages_pdf/           # PDF 源页面
│   ├── page-070.pdf
│   └── ...
├── output_pdf/          # 裁剪结果
│   ├── detection_results.json  # 检测数据
│   ├── Figure_2-1.png
│   ├── Figure_2-2.png
│   └── ...
└── pages_400dpi/        # 备用图片源
```

### detection_results.json 格式
```json
{
  "page-070.pdf": {
    "status": "success",
    "figures": [
      {
        "id": "Figure 2-1",
        "description": "曲线示例",
        "bbox": {"x1": 0.02, "y1": 0.08, "x2": 0.50, "y2": 0.38}
      }
    ],
    "tokens": 1500,
    "time": "2026-03-17 10:30:00"
  }
}
```

---

### 章节信息查询工具

配套提供 `chapter_analyzer.py`，可查询 Figure 信息：

```bash
# 列出章节所有 Figure
python chapter_analyzer.py <pdf路径> --chapter 2 --list

# 查看特定 Figure 上下文
python chapter_analyzer.py <pdf路径> --chapter 2 --figure 2-1

# 查看特定页码上下文
python chapter_analyzer.py <pdf路径> --chapter 2 --page 70

# 导出页面到指定目录
python chapter_analyzer.py <pdf路径> --chapter 2 --extract ./output
```

### 高级配置

### 切换章节

处理不同章节时，修改配置：

```python
# Chapter 1
INPUT_DIR = "chapter1/pages_pdf"
OUTPUT_DIR = "chapter1/output_pdf"

# Chapter 2
INPUT_DIR = "chapter2/pages_pdf"
OUTPUT_DIR = "chapter2/output_pdf"
```

### 提取 PDF 页面

先从教材 PDF 提取带 figure 的页面：

```python
# 从 PDF 提取 Chapter X 的页面
import re
from pypdf import PdfReader, PdfWriter

PDF_PATH = "book.pdf"
OUTPUT_DIR = "chapter2/pages_pdf"

reader = PdfReader(PDF_PATH)

# 查找 Figure 2.xx 的页面
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    if re.search(r'Figure\s*2[\.\-]\d+', text):
        # 提取为单页 PDF
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{OUTPUT_DIR}/page-{i+1:03d}.pdf", "wb") as f:
            writer.write(f)
```

---

## 提示词工程

内置高精度提示词，确保：
1. **元素完整性**：坐标轴箭头、曲线、标签完整
2. **禁止触边**：图形与边缘有白边间隙
3. **并排图处理**：允许重叠，宁可多余不要截断
4. **图注完整**：包含 "Figure X-X" 描述文字
