# 图片处理规范

本文档定义微分几何笔记中图片的处理标准，包括引用格式和排版布局规则。

---

## 一、图片源路径

教材图片位于：
```
PDFs/differential-geometry/transcript/Do Carmo - Differential Geometry of Curves and Surfaces/hybrid_ocr/images/
```

笔记中引用时使用相对路径（从 `.tex` 文件位置出发）：
```latex
../../../../PDFs/differential-geometry/transcript/Do Carmo - Differential Geometry of Curves and Surfaces/hybrid_ocr/images/fig_1-X.png
```

---

## 二、图片引用格式（强制要求）

**每处图片引用必须同时包含 `\cref{}` 和"教材 Figure X-X"**：

```latex
% 单图引用
如图 \cref{fig:helix}（教材 Figure 1-1）所示
见 \cref{fig:fig1-6}，教材 Figure 1-6

% 多图引用
见 \cref{fig:isoperimetric-config}、\cref{fig:isoperimetric-proof}，教材 Figure 1-23、1-24
```

**格式规则**：
- `\cref{}` 放在前面，使用中文括号 `（...）`
- "教材 Figure X-X" 紧跟其后
- 多图引用：用`、`分隔 label，用`、`分隔 figure 编号

---

## 三、图片排版流程

处理新图片时，按以下步骤操作：

### Step 1: 分析纵横比

用 Python 分析图片尺寸：
```python
from PIL import Image
img = Image.open("path/to/image.png")
width, height = img.size
ratio = width / height
print(f"尺寸: {width}x{height}, 纵横比: {ratio:.2f}")
```

### Step 2: 根据纵横比分类

| 分类 | 纵横比范围 | 排版规则 |
|------|-----------|---------|
| Portrait（竖向） | < 0.7 | 可并排 |
| Square（方形） | 0.7 ~ 1.5 | 可并排 |
| Landscape（横向） | 1.5 ~ 2.5 | 可并排，需控制宽度 |
| **Ultra-wide（超宽）** | **> 2.5** | **必须单独一行** |

### Step 3: 决定布局

**核心原则**：
1. **Ultra-wide 图片（ratio > 2.5）必须单独一行**，绝不能并排
2. **不同类型混排时分开**：Portrait + Landscape → 分开单独行
3. **相似类型可以并排**：Portrait + Portrait，或 Landscape + Landscape

**宽度设置**：
- 单图单独行：0.70 ~ 0.85
- 双图并排：0.35:0.35 或 0.40:0.40 或 0.30:0.35
- 总宽度控制在 0.85 以内

### Step 4: 写入 LaTeX

根据布局选择对应的 minipage 模板。

---

## 四、minipage 模板

### 模板 A：单独行（适合 ultra-wide 或混合类型）

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}{0.80\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image.png}
    \caption{图注}
    \label{fig:xxx}
  \end{minipage}
\end{figure}
```

### 模板 B：并排双图（适合相似纵横比）

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}{0.35\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image1.png}
    \caption{图注1}
    \label{fig:xxx1}
  \end{minipage}
  \hfill
  \begin{minipage}{0.30\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image2.png}
    \caption{图注2}
    \label{fig:xxx2}
  \end{minipage}
\end{figure}
```

### 模板 C：三图并排

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}{0.30\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image1.png}
    \caption{图注1}
    \label{fig:xxx1}
  \end{minipage}
  \hfill
  \begin{minipage}{0.30\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image2.png}
    \caption{图注2}
    \label{fig:xxx2}
  \end{minipage}
  \hfill
  \begin{minipage}{0.30\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image3.png}
    \caption{图注3}
    \label{fig:xxx3}
  \end{minipage}
\end{figure}
```

---

## 五、常见图片纵横比（do Carmo Chapter 1）

| 图片 | 尺寸 | 纵横比 | 分类 | 排版 |
|------|------|--------|------|------|
| fig_1-1 (helix) | 305x394 | 0.77 | Portrait | 可并排 |
| fig_1-2 (trace) | 467x231 | 2.02 | Ultra-wide | **单独一行** |
| fig_1-7 (cycloid) | 809x248 | 3.26 | Ultra-wide | **单独一行** |
| fig_1-8 (cissoid) | 352x683 | 0.52 | Portrait | 可并排 |
| fig_1-9 (tractrix) | 317x661 | 0.48 | Portrait | 可并排 |
| fig_1-27b | 734x288 | 2.55 | Ultra-wide | **单独一行** |
| fig_1-27c | 669x248 | 2.70 | Ultra-wide | **单独一行** |
| fig_1-28a | 808x195 | 4.14 | Ultra-wide | **单独一行** |
| fig_1-28b | 525x172 | 3.05 | Ultra-wide | **单独一行** |

---

## 六、Label 命名规范

```latex
\label{fig:helix}      % helix 螺旋线
\label{fig:cycloid}    % 旋轮线
\label{fig:fig1-4}     % 教材原图编号（当原名更清晰时）
```

---

## 七、编译注意事项

- 使用 `xeCJK` 支持中文
- 图片路径中避免中文名
- 编译脚本使用各目录的 `compile.sh`
- 使用 `[H]` 强制固定图片位置
