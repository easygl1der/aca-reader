# Footnote 与 QA 附录引用不一致问题

**日期**: 2026-03-31
**检查范围**: notes/Schubert-Polynomials/ 目录下所有 chapter*.tex 文件

---

## 问题概述

在检查脚注引用 `\footnote{...见附录 \cref{sec:XXX}}` 与 `appendix/qa.tex` 中实际内容时，发现以下不一致情况：

---

## 一、严重问题：sec:appendix-* 类型引用指向正文附录而非 QA

以下脚注引用指向的是**正文附录章节**（chapter*.tex 中的 `\section{附录：...}`），而不是 **qa.tex 中的问答条目**：

| 脚注引用 | 出现位置 | 问题描述 |
|---------|---------|---------|
| `sec:appendix-ch2-proof` | chapter2.tex:102, 188 | "乘积公式的完整推导" / "详细推导" |
| `sec:appendix-ch2-path` | chapter2.tex:117 | "Path 图的详细定义与权重公式" |
| `sec:appendix-ch2-dominant` | chapter2.tex:217 | "Dominant approximation 的完整证明" |
| `sec:appendix-eqc-proof` | chapter4.tex:222 | "量子 Schubert 演算 positivity 定理的完整证明" |

**这4个标签在 qa.tex 中都不存在！**

### 格式分析

这些脚注的格式是：
- `\footnote{XXX的完整推导见附录 \cref{sec:appendix-xxx}。}`
- `\footnote{详细推导见附录 \cref{sec:appendix-xxx}。}`

**没有"问："前缀**，与其他 QA 脚注格式不一致：
- QA 格式：`\footnote{问：XXX？见附录 \cref{sec:qa-xxx}。}`

### 修复方向

**选项 A**：如果这些内容确实应该是正文附录（完整证明/推导），而不是 QA 问答：
- 保持现有指向
- 建议统一格式：`\footnote{完整证明见附录 \cref{sec:appendix-xxx}。}`（去掉"问："暗示）

**选项 B**：如果这些应该指向 QA：
- 需要在 qa.tex 中创建对应的 `\section{问题}\label{sec:appendix-xxx}` 条目
- 或将这些内容重命名为 `sec:qa-appendix-xxx` 以区分

---

## 二、轻度问题：脚注问题描述与附录实际内容不完全匹配

脚注中的问题描述通常比附录中的**实际问题**更简化：

### 2.1 sec:GW-invariant

| 来源 | 内容 |
|------|------|
| 脚注 (ch4:374) | "问：什么是 Gromov-Witten 不变量？" |
| qa.tex (sec:GW-invariant) | "什么是 Gromov-Witten 不变量？**它计数的是什么？**" |

**差异**：脚注遗漏了"它计数的是什么"这一深层问题

**修复建议**：脚注改为"问：什么是 Gromov-Witten 不变量？它计数的是什么？"

### 2.2 sec:EquivariantCohomologyClass

| 来源 | 内容 |
|------|------|
| 脚注 (ch1:522, ch4:87) | "问：$H_T^*(pt)$ 是什么意思？等变上同调类如何定义？" |
| qa.tex (sec:EquivariantCohomologyClass) | "等变量子上同调类是如何定义的？" |

**差异**：脚注具体问了 $H_T^*(pt)$ 和上标 T 的含义，但 qa.tex 的问题更宽泛

**分析**：脚注问题更具体，可能超出了附录回答的范围

### 2.3 sec:q-formal-variable

| 来源 | 内容 |
|------|------|
| 脚注 (ch4:60) | "问：$q^d$ 是形式变量是什么意思？" |
| qa.tex (sec:q-formal-variable) | "$\sigma(u) \star \sigma(v) = \sum_d \sum_w q^d c_{u,v}^{w,d} \sigma(w)$ 这个公式中，$q^d$ 是形式变量，$q$ 是什么？求和是对什么？$u, v, w$ 是什么？" |

**差异**：脚注简化了问题，遗漏了"求和是对什么？$u, v, w$ 是什么？"

**修复建议**：脚注可以改为"问：$q^d$ 是形式变量是什么意思？量子乘积公式中各项是什么？"

### 2.4 sec:unipotent-radical

| 来源 | 内容 |
|------|------|
| 脚注 (ch4:444) | "问：什么是幂幺根基？" |
| qa.tex (sec:unipotent-radical) | "在 Borel 子群分解 $B = T \cdot U$ 中，$U$ 称为'幂幺根基'，这是什么意思？" |

**差异**：脚注过于简化，遗漏了"Borel 子群分解"的具体语境

**修复建议**：脚注改为"问：$U$（幂幺根基）在 Borel 子群分解 $B = T \cdot U$ 中是什么意思？"

### 2.5 sec:GrahamPositivityCoefficientMeaning

| 来源 | 内容 |
|------|------|
| 脚注 (ch4:49) | "问：Graham Positivity 中展开系数的'非负性'具体是什么含义？" |
| qa.tex (sec:GrahamPositivityCoefficientMeaning) | "在 Graham Positivity 定理中，为什么说展开系数 $c^w_{u,v}(\mathbf{y}, \mathbf{t})$ 是 $t_j - y_i$ 的非负整数系数多项式？**展开式中明明有负项（如 $-x_1t_2$）？**" |

**差异**：脚注遗漏了"展开式中明明有负项"这个关键疑问

**修复建议**：脚注改为"问：Graham Positivity 中展开系数的'非负性'具体是什么含义？展开式中明明有负项？"

---

## 三、正确的引用（未发现问题）

以下脚注引用与 qa.tex 内容**匹配良好**：

| sec:label | 脚注问题 | qa.tex 问题 | 状态 |
|-----------|---------|-------------|------|
| sec:sigma-u-T | "$\sigma(u)^T$ 是什么意思？" | "$\sigma(u)^T$ 是什么意思？上标 $T$ 代表什么？" | OK |
| sec:EquivariantvsQuantum | "等变量子上同调与量子上同调有什么区别？" | "是量子同调吗？" | OK |
| sec:graded-Lambda-q-algebra | "什么是分次 $\Lambda[q]$-代数？$q$ 变量代表什么？" | "什么是分次 $\Lambda[q]$-代数？$q$ 变量代表什么？" | OK |
| sec:P1-to-X | "$f: \mathbb{P}^1 \to X$ 中的 $X$ 是什么？" | "这里的 $X$ 是什么？$\mathbb{P}^1$ 又是什么？" | OK |
| sec:EQLR-Definition | (在 ch4 中未直接作为脚注出现) | "EQLR 系数是什么？..." | N/A |

---

## 四、经验教训总结

### 4.1 脚注引用规范

1. **QA 脚注必须指向 qa.tex**：所有"问：XXX？见附录"的脚注引用，label 必须在 qa.tex 中存在
2. **正文附录引用需明确区分**：如果引用的是正文附录（完整证明），应使用不同格式，如 `\footnote{完整证明见附录 \cref{sec:appendix-xxx}。}`
3. **避免混用**：同一个项目中不应出现既指向 qa.tex 又指向正文附录的"见附录"引用

### 4.2 脚注问题描述规范

1. **脚注问题应与 qa.tex 问题一致**：脚注中的问题描述应准确反映附录中的实际**问题**
2. **不要过度简化**：脚注问题是读者产生疑问的第一个入口，不应遗漏关键信息
3. **保持一致性**：如果附录问题有多个层次，脚注问题也应相应完整

### 4.3 修复优先级

| 优先级 | 问题类型 | 修复方式 |
|--------|---------|---------|
| **P0** | sec:appendix-* 引用不存在于 qa.tex | 确认是否为正文附录引用，若是则统一格式 |
| **P1** | 脚注与附录问题描述不一致 | 更新脚注文本以匹配附录实际内容 |

---

## 五、后续行动建议

1. **确认 sec:appendix-* 的性质**：与作者确认这些引用是否有意指向正文附录
2. **统一脚注格式**：如果确认是正文附录，修改脚注格式以区分 QA 引用
3. **更新脚注文本**：按上述"修复建议"修改 P1 级问题
4. **建立检查机制**：在 QA 工作流中增加脚注引用验证步骤
