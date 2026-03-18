# Label 和 Cross-reference 规范

## 命名规范
- 定理：\label{def:TheoremXX}
- 引理：\label{def:LemmaXX}
- 定义：\label{def:名称}
- 章节：\label{sec:名称}
- 公式：\label{eq:名称}
- 图片：\label{fig:描述性名称}

## 引用方式
- **必须使用 `\cref{标签名}`**（需要 cleveref 宏包）
- 禁止硬编码数字引用，如"定理1.2"
- 禁止模糊指代，如"前述"、"前文"、"上述条件"

## 示例
```latex
\begin{Theorem}[Neyman's Theorem]\label{def:NeymanTheorem}
...
根据 \cref{def:NeymanTheorem}，...

\begin{equation}\label{eq:ATE}
\tau = \bar{Y}(1) - \bar{Y}(0)
\end{equation}
见 \cref{eq:ATE}。
```

## 符号定义规则

### 常见约定
- 带 hat (^) = 样本估计量（从数据计算）
- 不带 hat = 总体真值/有限总体量
- 例如：$\hat{\bar{Y}}(1)$ 是样本均值，$\bar{Y}(1)$ 是有限总体均值

### 符号第一次出现时
- 必须先定义符号含义
- 使用 `\sqrt{}`、`\frac{}{}` 等标准 LaTeX 命令
