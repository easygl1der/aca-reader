# 因果推断专家教训记忆

**适用对象**: causal-expert, causal-expert-2
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L101 | Potential Outcomes 符号约定 | 2 |
| L102 | Peng Ding 习题格式 | 3 |
| L103 | 平衡性条件推导 | 1 |
| L104 | IV 估计量的正确表述 | 1 |

---

## L101: Potential Outcomes 符号约定

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
混淆了 Potential Outcomes 的符号表示，如用 `$Y_i(1)$` vs `$Y_i(0)$` vs `$Y_i$`。

**正确做法**:
- $Y_i(1)$：单元 $i$ 接受 treatment 后的潜在结果
- $Y_i(0)$：单元 $i$ 接受 control 后的潜在结果
- $Y_i$：观测结果（可能是 $Y_i(1)$ 或 $Y_i(0)$，取决于实际分配）
- $\tau_i = Y_i(1) - Y_i(0)$：单元因果效应

**符号规范**:
```latex
% 正确写法
Y_i(1) - Y_i(0)  % 单元因果效应
\mathbb{E}[Y_i(1) - Y_i(0)]  % ATE
```

**防止措施**:
- 始终区分观测值和潜在结果
- 引用 Peng Ding 原书符号

---

## L102: Peng Ding 习题格式

**日期**: 2026-03-29
**经历次数**: 3 次 (累计)

**错误描述**:
习题中硬编码公式编号（如"证明 (5.2)"），而不是用 `\eqref{}` 引用。

**正确做法**:
```latex
% 1. 先给公式加 label
\begin{equation}
\label{eq:balance-discrete-CRE}
\frac{1}{n} \sum_{i=1}^n \mathbb{I}(X_i = x) (\tau_i - \hat{\tau}_{CATE}(x)) = 0
\end{equation}

% 2. 习题中用 \eqref{} 引用
\begin{Exercise}{\ref{exr:5-1} Consistency of OLS}\label{exr:5-1}
Show that \eqref{eq:ols-estimator} is consistent...
\end{Exercise}
```

**环境**: `Exercise`（首字母大写）
**Label 命名**: `exr:{章号}-{题号}`

**防止措施**:
- 写习题前先检查是否已有 label 定义
- 用 `\eqref{}` 替代硬编码编号

---

## L103: 平衡性条件推导

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
在正文中写了完整的平衡性条件推导，导致正文过于冗长。

**正确做法**:
- 推导放附录 `\section{附录：公式推导}`
- 正文用脚注引用：`\footnote{推导见附录 \cref{sec:derivation-balance-discrete-CRE}。}`

**附录结构**:
```latex
\subsection{平衡性条件的推导}\label{sec:derivation-balance-discrete-CRE}
\textbf{背景}：...
\textbf{目标}：证明 \eqref{eq:balance-discrete-CRE}
\textbf{推导步骤}：
1. 首先...
```

**防止措施**:
- 推导一律放附录
- 正文只写结论和直观解释

---

## L104: IV 估计量的正确表述

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆 IV 估计的不同形式（2SLS、IPW、LM 形式等）。

**正确做法**:
- 2SLS：第一阶段 + 第二阶段
- 控制函数法：用 reduced form 残差
- Local Average Treatment Effect (LATE)：前提是单调性

**防止措施**:
- 明确说明是哪种 IV 估计量
- 引用 Peng Ding Chapter 7

---

## 领域专属符号表

```latex
% 因果推断核心符号
Potential Outcomes: Y_i(1), Y_i(0)
ATE: \mathbb{E}[Y_i(1) - Y_i(0)]
CATE: \tau(x) = \mathbb{E}[Y_i(1) - Y_i(0) | X_i = x]
SUTVA: Y_i = Z_i Y_i(1) + (1-Z_i)Y_i(0)
RCT: Z_i \Perp (Y_i(1), Y_i(0))
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/causal-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是因果推断专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
