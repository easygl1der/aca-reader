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
../../../../PDFs/differential-geometry/transcript/Do Carmo - Differential Geometry of Curves and Surfaces/hybrid_ocr/images/<filename>.jpg
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

## 三、排版核心原则

### 黄金法则

1. **相似比例的图片可以并排，不同比例必须分开**
2. **Ultra-wide 图片（ratio > 2.5）必须单独一行**
3. **不要让图片被过度拉伸或压缩**

### 纵横比分类

| 分类 | 纵横比范围 | 排版规则 |
|------|-----------|---------|
| Portrait（竖向） | < 0.7 | 可并排 |
| Square（方形） | 0.7 ~ 1.5 | 可并排 |
| Landscape（横向） | 1.5 ~ 2.5 | 可并排，需控制宽度 |
| **Ultra-wide（超宽）** | **> 2.5** | **必须单独一行** |

---

## 四、排版决策流程

### Step 1: 分析每张图片的纵横比

用 Python 分析图片尺寸：
```python
from PIL import Image
img = Image.open("path/to/image.jpg")
width, height = img.size
ratio = width / height
print(f"尺寸: {width}x{height}, 纵横比: {ratio:.2f}")
```

### Step 2: 根据比例决定布局

**常见问题及解决方案**：

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 4张图竖向堆叠太长 | 都是小比例图 | 改成 2x2 网格 |
| 并排效果差 | 不同类型的图混排 | 分开单独行 |
| 图片被压缩/拉伸 | minipage 宽度不合适 | 调整宽度比例 |

**具体规则**：
- 2张图：都用 Square 或 Portrait → 并排（0.35:0.35 或 0.40:0.40）
- 2张图：一个 Square 一个 Ultra-wide → 分开单独行
- 3张图：比例接近 → 三并排（0.30:0.30:0.30）
- 4张图：都是 Square → 2x2 网格
- 4张图：混合类型 → 分成两个并排或四个单独行

### Step 3: 选择 minipage 宽度

- 单图单独行：0.70 ~ 0.85
- 双图并排：0.35:0.35 或 0.40:0.40 或 0.45:0.40
- 三图并排：0.30:0.30:0.30
- 总宽度控制在 0.85 以内

### Step 4: 检查是否需要分开

**必须分开的情况**：
1. 任何一张图 ratio > 2.5（ultra-wide）
2. Portrait 和 Landscape 混合
3. 4张以上的图堆叠

---

## 五、常见问题修复

### 问题1：4张图竖向堆叠
**原因**：都是 Square 类型但用了 `\newline` 竖排
**解决**：改成 2x2 网格
```latex
% 错误 ❌
\begin{minipage}{0.8\textwidth}
\subfloat[...]{\label{fig:1}}\newline
\subfloat[...]{\label{fig:2}}\newline
\subfloat[...]{\label{fig:3}}\newline
\subfloat[...]{\label{fig:4}}
\end{minipage}

% 正确 ✅
\begin{minipage}{0.45\textwidth}
\subfloat[...]{\label{fig:1}}
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
\subfloat[...]{\label{fig:2}}
\end{minipage}
% 第二行...
```

### 问题2：不同比例图片并排
**原因**：Square 和 Ultra-wide 混排
**解决**：Ultra-wide 必须单独一行
```latex
% 错误 ❌ - Ultra-wide 和 Square 并排
\begin{minipage}{0.35\textwidth} ... 1.36 ratio \end{minipage}
\hfill
\begin{minipage}{0.30\textwidth} ... 2.55 ultra-wide \end{minipage}

% 正确 ✅ - 分开
\begin{minipage}{0.45\textwidth} ... Square \end{minipage}
\end{figure}
\begin{figure}[H]
\begin{minipage}{0.80\textwidth} ... Ultra-wide \end{minipage}
```

### 问题3：helix 和 trace 并排效果差
**原因**：Portrait (0.77) 和 Landscape (2.02) 视觉不协调
**解决**：调整宽度比例或分开
```latex
% 调整后效果更好
\begin{minipage}{0.40\textwidth} ... Portrait \end{minipage}
\hfill
\begin{minipage}{0.50\textwidth} ... Landscape \end{minipage}
```

---

## 六、minipage 模板

### 模板 A：单独行（适合 ultra-wide 或混合类型）

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}{0.80\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image.jpg}
    \caption{图注}
    \label{fig:xxx}
  \end{minipage}
\end{figure}
```

### 模板 B：并排双图（适合相似纵横比）

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}{0.40\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image1.jpg}
    \caption{图注1}
    \label{fig:xxx1}
  \end{minipage}
  \hfill
  \begin{minipage}{0.40\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image2.jpg}
    \caption{图注2}
    \label{fig:xxx2}
  \end{minipage}
\end{figure}
```

### 模板 C：2x2 网格（适合4张 Square 图）

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}{0.45\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image1.jpg}
    \caption{图注1}
    \label{fig:xxx1}
  \end{minipage}
  \hfill
  \begin{minipage}{0.45\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image2.jpg}
    \caption{图注2}
    \label{fig:xxx2}
  \end{minipage}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{minipage}{0.45\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image3.jpg}
    \caption{图注3}
    \label{fig:xxx3}
  \end{minipage}
  \hfill
  \begin{minipage}{0.45\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image4.jpg}
    \caption{图注4}
    \label{fig:xxx4}
  \end{minipage}
\end{figure}
```

### 模板 D：三图并排

```latex
\begin{figure}[H]
  \centering
  \begin{minipage}{0.30\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image1.jpg}
    \caption{图注1}
    \label{fig:xxx1}
  \end{minipage}
  \hfill
  \begin{minipage}{0.30\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image2.jpg}
    \caption{图注2}
    \label{fig:xxx2}
  \end{minipage}
  \hfill
  \begin{minipage}{0.30\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image3.jpg}
    \caption{图注3}
    \label{fig:xxx3}
  \end{minipage}
\end{figure}
```

---

## 七、常见图片纵横比（do Carmo Chapter 1）

| 图片 | 尺寸 | 纵横比 | 分类 | 排版建议 |
|------|------|--------|------|---------|
| fig_1-1 (helix) | 305x394 | 0.77 | Portrait | 可并排 |
| fig_1-2 (trace1) | 467x231 | 2.02 | Landscape | 可并排 |
| fig_1-3 (trace2) | 553x384 | 1.44 | Square | 可并排 |
| fig_1-4 | 359x178 | 2.02 | Landscape | 可并排 |
| fig_1-5 | 434x311 | 1.40 | Square | 可并排 |
| fig_1-6 | ~500x300 | ~1.67 | Landscape | 可并排 |
| fig_1-7 (cycloid) | 809x248 | 3.26 | **Ultra-wide** | **单独一行** |
| fig_1-8 (cissoid) | 352x683 | 0.52 | Portrait | 可并排 |
| fig_1-9 (tractrix) | 317x661 | 0.48 | Portrait | 可并排 |
| fig_1-10 | 755x530 | 1.42 | Square | 可并排 |
| fig_1-11 | 620x486 | 1.28 | Square | 可并排 |
| fig_1-27a | 795x583 | 1.36 | Square | 可并排 |
| **fig_1-27b** | **734x288** | **2.55** | **Ultra-wide** | **单独一行** |
| **fig_1-27c** | **669x248** | **2.70** | **Ultra-wide** | **单独一行** |
| fig_1-28a | 808x195 | 4.14 | **Ultra-wide** | **单独一行** |
| fig_1-28b | 525x172 | 3.05 | **Ultra-wide** | **单独一行** |
| fig_1-29a | 270x359 | 0.75 | Square | 可并排 |
| **fig_1-29b** | **477x148** | **3.22** | **Ultra-wide** | **单独一行** |

---

## 八、Label 命名规范

```latex
\label{fig:helix}           % helix 螺旋线
\label{fig:cycloid}         % 旋轮线
\label{fig:fig1-4}          % 教材原图编号（当原名更清晰时）
\label{fig:trace1}          % trace 图1
\label{fig:local-canonical-projections}  % 描述性名称
```

---

## 九、编译注意事项

- 使用 `xeCJK` 支持中文
- 图片路径中避免中文名
- 编译脚本使用各目录的 `compile.sh`
- 使用 `[H]` 强制固定图片位置
- `\subfloat` 的 caption 中写 "Figure X-X" 便于识别

---

## 十、检查清单

添加图片后，自查以下问题：

- [ ] 所有 ultra-wide 图片（ratio > 2.5）都单独一行？
- [ ] 不同类型的图片没有混在一起并排？
- [ ] 4张 Square 图是否用了 2x2 网格而非竖向堆叠？
- [ ] minipage 总宽度是否控制在 0.85 以内？
- [ ] 文本中的引用是否同时有 `\cref{}` 和"教材 Figure X-X"？
- [ ] label 命名是否清晰可读？
