---
name: tex-figure-insert
description: 将教材图片插入 LaTeX 笔记，按照纵横比自动排版，检查布局问题，生成正确的引用格式
---

# Tex Figure Insert - 教材图片插入工具

## 功能

将教材中的图片插入 LaTeX 笔记，自动处理：
- 纵横比分析
- 排版布局决策
- 正确的引用格式（含 `\cref{}` 和"教材 Figure X-X"）

## 使用方式

```
插入教材图片：Figure 1-18, 1-19, 1-20
```

## 工作流程

### Step 1: 分析图片纵横比

```python
from PIL import Image
import os

# 图片源路径
IMAGE_DIR = "PDFs/differential-geometry/transcript/Do Carmo - Differential Geometry of Curves and Surfaces/hybrid_ocr/images/"

def analyze_image(filename):
    img = Image.open(os.path.join(IMAGE_DIR, filename))
    w, h = img.size
    ratio = w / h
    if ratio > 2.5:
        category = "ULTRA-WIDE"
    elif ratio > 1.5:
        category = "Landscape"
    elif ratio < 0.7:
        category = "Portrait"
    else:
        category = "Square"
    return {"width": w, "height": h, "ratio": ratio, "category": category}
```

### Step 2: 决定布局

| 情况 | 布局方案 |
|------|---------|
| 单张 Square/Landscape/Portrait | 单独一行，宽度 0.70~0.85 |
| 单张 Ultra-wide (ratio>2.5) | 单独一行，宽度 0.80~0.85 |
| 2张 Square 并排 | 双列，0.35:0.35 或 0.40:0.40 |
| 2张 Portrait 并排 | 双列，0.35:0.35 |
| 3张比例接近 | 三列，0.30:0.30:0.30 |
| 4张 Square | 2x2 网格 |
| 任何 Ultra-wide | **必须单独一行** |
| 不同类型混合 | 分开单独行 |

### Step 3: 生成 LaTeX 代码

```latex
% 单独行模板
\begin{figure}[H]
  \centering
  \begin{minipage}{0.80\textwidth}
    \centering
    \includegraphics[width=\textwidth]{../../../../PDFs/differential-geometry/transcript/Do Carmo - Differential Geometry of Curves and Surfaces/hybrid_ocr/images/<filename>.jpg}
    \caption{Figure X-X. 图注}
    \label{fig:xxx}
  \end{minipage}
\end{figure}

% 双列模板
\begin{figure}[H]
  \centering
  \begin{minipage}{0.40\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image1.jpg}
    \caption{Figure X-X (a). 图注1}
    \label{fig:xxx1}
  \end{minipage}
  \hfill
  \begin{minipage}{0.40\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image2.jpg}
    \caption{Figure X-X (b). 图注2}
    \label{fig:xxx2}
  \end{minipage}
\end{figure}
```

### Step 4: 文本引用格式

```latex
% 单图
如图 \cref{fig:helix}（教材 Figure 1-1）所示

% 多图
见 \cref{fig:fig1-27b}、\cref{fig:fig1-27c}，教材 Figure 1-27 (b)、(c)
```

## 常见问题修复

### 问题：4张图竖向堆叠
**解决**：改成 2x2 网格
```latex
% 错误
\begin{minipage}{0.8\textwidth}
\subfloat[...]\newline
\subfloat[...]\newline
\subfloat[...]\newline
\subfloat[...]

% 正确
\begin{minipage}{0.45\textwidth}...\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}...\end{minipage}
% 第二行同理
```

### 问题：Ultra-wide 和 Square 并排
**解决**：Ultra-wide 必须单独一行
```latex
% 错误 - ultra-wide 被压缩
\begin{minipage}{0.35\textwidth} ... 1.36 \end{minipage}
\begin{minipage}{0.30\textwidth} ... 2.55 ultra-wide \end{minipage}

% 正确
\begin{minipage}{0.45\textwidth} ... Square \end{minipage}
\end{figure}
\begin{figure}[H]
\begin{minipage}{0.80\textwidth} ... Ultra-wide \end{minipage}
```

## 纵横比速查表

### do Carmo Chapter 1

| Figure | Ratio | Category | Recommended Layout |
|--------|-------|---------|-------------------|
| 1-1 (helix) | 0.77 | Portrait | 并排 |
| 1-2 (trace) | 2.02 | Landscape | 并排 |
| 1-3 | 1.44 | Square | 并排 |
| 1-4 | 2.02 | Landscape | 并排 |
| 1-7 (cycloid) | 3.26 | **Ultra-wide** | **单独一行** |
| 1-8 (cissoid) | 0.52 | Portrait | 并排 |
| 1-9 (tractrix) | 0.48 | Portrait | 并排 |
| 1-27b | 2.55 | **Ultra-wide** | **单独一行** |
| 1-27c | 2.70 | **Ultra-wide** | **单独一行** |
| 1-28a | 4.14 | **Ultra-wide** | **单独一行** |
| 1-28b | 3.05 | **Ultra-wide** | **单独一行** |
| 1-29b | 3.22 | **Ultra-wide** | **单独一行** |

## 检查清单

添加图片后必须检查：

- [ ] 所有 Ultra-wide 图片（ratio > 2.5）都单独一行？
- [ ] 不同类型的图片没有混在一起并排？
- [ ] 4张 Square 图是否用了 2x2 网格？
- [ ] minipage 总宽度控制在 0.85 以内？
- [ ] 文本引用同时有 `\cref{}` 和"教材 Figure X-X"？
- [ ] label 命名清晰可读？

## 相关文档

详细规范见：`docs/image-handling.md`
