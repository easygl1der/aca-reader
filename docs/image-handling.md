# 图片处理规范

本文档定义微分几何笔记中图片的处理标准。

## 图片源路径

教材图片位于：
```
PDFs/differential-geometry/transcript/Do Carmo - Differential Geometry of Curves and Surfaces/hybrid_ocr/images/
```

笔记中引用时使用相对路径：
```latex
../../../../PDFs/differential-geometry/transcript/Do Carmo - Differential Geometry of Curves and Surfaces/hybrid_ocr/images/fig_1-X.png
```

## 图片引用格式

**强制要求**：每处图片引用必须同时包含 `\cref{}` 和"教材 Figure X-X"：

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
- 如果引用多张图片，用`、`分隔 label，用`、`分隔 figure 编号

## 图片排版规则

### 1. 纵横比分析

首先分析图片的纵横比（宽高比）：
- **Portrait**（竖向）: ratio < 0.7
- **Landscape**（横向）: ratio > 1.5
- **Ultra-wide**（超宽）: ratio > 2.5
- **Square**（方形）: 0.7 ≤ ratio ≤ 1.5

### 2. 排版策略

| 纵横比组合 | 排版方式 |
|-----------|---------|
| Portrait + Portrait | 并排，使用 0.35:0.35 或 0.40:0.40 |
| Portrait + Landscape | 分开单独行，避免并排 |
| Landscape + Landscape | 并排，但需控制总宽度 ≤ 0.9 |
| Ultra-wide（>2.5） | **必须单独一行**，不使用并排 |
| 多图（3张） | 根据纵横比选择并排或分开 |

### 3. 宽度设置

- 单图单独行：0.70 ~ 0.85
- 双图并排：0.35:0.35 或 0.40:0.40 或 0.45:0.40
- 宽度总和控制在 0.85 以内

### 4. 分组原则

将**相似纵横比**的图片组合在一起：
- 相似的 aspect ratio 可以并排
- 差异大的 aspect ratio 必须分开

## minipage 结构模板

```latex
% 单独行（适合 ultra-wide 或 portrait+landscape 混合）
\begin{figure}[H]
  \centering
  \begin{minipage}{0.80\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image.png}
    \caption{图注}
    \label{fig:xxx}
  \end{minipage}
\end{figure}

% 并排（适合相似纵横比）
\begin{figure}[H]
  \centering
  \begin{minipage}{0.40\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image1.png}
    \caption{图注1}
    \label{fig:xxx1}
  \end{minipage}
  \hfill
  \begin{minipage}{0.40\textwidth}
    \centering
    \includegraphics[width=\textwidth]{path/to/image2.png}
    \caption{图注2}
    \label{fig:xxx2}
  \end{minipage}
\end{figure}
```

## 常见图片纵横比（do Carmo Chapter 1）

| 图片 | 尺寸 | 纵横比 | 分类 | 排版建议 |
|------|------|--------|------|---------|
| fig_1-1 (helix) | 305x394 | 0.77 | Portrait | 可并排 |
| fig_1-2 (trace) | 467x231 | 2.02 | Ultra-wide | **单独一行** |
| fig_1-7 (cycloid) | 809x248 | 3.26 | Ultra-wide | **单独一行** |
| fig_1-8 (cissoid) | 352x683 | 0.52 | Portrait | 可并排 |
| fig_1-9 (tractrix) | 317x661 | 0.48 | Portrait | 可并排 |
| fig_1-27b | 734x288 | 2.55 | Ultra-wide | **单独一行** |
| fig_1-27c | 669x248 | 2.70 | Ultra-wide | **单独一行** |
| fig_1-28a | 808x195 | 4.14 | Ultra-wide | **单独一行** |
| fig_1-28b | 525x172 | 3.05 | Ultra-wide | **单独一行** |

## 图片 Label 命名规范

使用清晰、可读的 label：
```latex
\label{fig:helix}      % helix 螺旋线
\label{fig:cycloid}    % 旋轮线
\label{fig:fig1-4}     % 教材原图编号
```

## 编译注意事项

- 使用 `xeCJK` 支持中文
- 图片路径中避免中文名
- 编译脚本使用各目录的 `compile.sh`
