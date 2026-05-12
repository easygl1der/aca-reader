# Textbook Notes Workflow Skill

## 功能

从教材源材料生成/修复高质量章节笔记，支持：源材料分析、Agent Team 协作、Stein 写作风格、多轮修订、Exercise+Solution 配平、LaTeX 编译、QA 记录。

## 触发条件

- 用户说"生成第 X 章笔记"、"写 chapters/chapterX"
- 用户说"润色 .tex"、"写作任务"
- 用户要求生成/修复教材章节笔记

---

## 源材料优先级（绝对规则）

| 优先级 | 来源 | 说明 |
|--------|------|------|
| **1** | `chapters/chapterX.tex` | 如果已存在，**直接读取修改** |
| **2** | `PDFs/<主题>/transcript/**/*.tex` | LaTeX 源文件（优先） |
| **3** | `PDFs/<主题>/transcript/**/*.md` | MinerU 转录本 |
| **4** | 原始 PDF | 仅限需要**视觉确认**时，使用 `pages` 参数限制 |

> ⚠️ **永远不要**优先扫描原始 PDF！

---

## LaTeX 格式红线（禁止违反，碰了就是 3.25）

| 禁止 ❌ | 正确 ✅ |
|---------|---------|
| `\bm`（向量） | `\mathbf` 或 `\boldsymbol` |
| `\I`（单位矩阵） | `\mathbb{I}` |
| Unicode 下标 `$n₁$` | `$n_1$` |
| `\ref{xxx}` | `\cref{xxx}` |
| `\include{chapterX}` | `\input{chapterX}` |
| **章节文件末尾 `\end{document}`** | **禁止！会导致后续章节完全消失！** |
| Markdown 语法、`\tag{}` | 标准 LaTeX 引用 |
| 中文摘要替代英文原文 | **习题内容必须与 transcript 原文完全一致（英文）** |

### 空括号记号（用户偏好）

- 空方括号：`[\cdot]`
- 空圆括号：`(\cdot)`

---

## 核心要求（必须严格遵守）

### R1: 习题内容必须与 transcript 英文原文完全一致

- 习题题号、内容一个字都不能改
- 格式：`\begin{exercise}{2-2, 1 — do Carmo, Exercise 2-2, 1}`
- subagent 不得擅自改写为中文摘要

### R2: 习题数量必须与教材 transcript 完全一致

生成/修复前，必须先从 transcript 确认每节习题数量：
```
Do Carmo 微分几何教材示例：
2-2: 16题, 2-3: 16题, 2-4: 28题, 2-5: 15题, 2-6: 7题, 2-7: 0题, 2-8: 22题
```
不得靠猜，必须逐节与 transcript 比对。

### R3: 每张图片都要确认并插入正确位置

- 从 transcript markdown 中识别图片引用（如 `![](fig/xxx.jpg)`）
- 确认图片路径和内容
- 在对应位置插入 LaTeX 图片环境
- 习题中引用的图片必须出现在正确位置

### R4: 习题引用的 Proposition/Theorem 必须在正文存在

- 如果习题引用了 Proposition 1 和 Proposition 2
- **必须**确保正文中有这两个命题
- 附 `\label{prop:xxx}` 和 `\cref{prop:xxx}`
- 并加 footnote 注明原文位置

### R5: Solution 格式（详细程度）

```
Solution 格式（三层）：
1. 直观理解：几何直觉 + 思路概述
2. 严格证明：形式化推导
3. LaTeX 推导：完整公式序列
```

---

## 工作流程

### Phase 1: 任务启动 — 对齐目标

1. 读取 `.claude/writer-round-robin.json` 确定 writer pair（轮询机制）
2. 从 prompt 提取章节编号（"第 3 章" → `chapter3`）
3. 确定笔记目标目录：`notes/<主题>/chapters/`
4. 确定源材料路径（按上方优先级）

### Phase 2: 内容分析（Content Analysis）

使用 `content-curator` agent 读取源材料，提取：
- 知识框架（定义、定理、引理、命题、性质）
- 关键公式和图（Figma/SVG 路径引用）
- **习题列表（题号、内容、数量）** — 必须与 transcript 完全一致
- 难点和直观理解
- 约定了哪些符号体系
- **每张图片的内容和位置**

### Phase 3: 写作（Primary Writer）

**写作风格**：Stein 风格
- 动机优先：先讲"为什么"，再讲"是什么"
- 历史语境：定理谁提出？解决什么问题？
- 直观连接：抽象概念配几何/物理直观
- 有机组织：章节之间互引，形成网络

**LaTeX 结构**：
```latex
\section{章节标题}
\subsection{引入}
% 动机、历史背景、为什么重要

\subsection{主要内容}
% 定义 → 定理 → 证明思路 → 例子

\subsection{习题}
\begin{exercise}{2-2, 1 — do Carmo, Exercise 2-2, 1}
题目内容（英文原文）...
\end{exercise}
\begin{solution}
直观理解...
严格证明...
LaTeX推导...
\end{solution}
```

**关键格式**：
- 每个定义/定理/引理都要有 `\label{eq:名称}` 或 `\label{df:名称}`
- 证明结尾加 `\qed`
- 习题和解答**必须严格成对**（begin/end 数量相等）
- **禁止**在章节文件末尾写 `\end{document}`

### Phase 4: 评审修订（Reviewer）

至少 **2 轮讨论**：

**第一轮**：
- Reviewer 挑战：逻辑完整性、直观理解、习题平衡、格式合规、引用完备
- Primary Writer 回应修订

**第二轮**：
- Primary Writer 修订后发回
- Reviewer 最终确认

### Phase 5: Exercise + Solution 配平验证（必须执行！）

**Python 脚本验证**：
```python
import re
content = open('chapterX.tex').read()
ex_begins = len(re.findall(r'\\begin\{exercise\}', content))
ex_ends = len(re.findall(r'\\end\{exercise\}', content))
sol_begins = len(re.findall(r'\\begin\{solution\}', content))
sol_ends = len(re.findall(r'\\end\{solution\}', content))
assert ex_begins == ex_ends, f"Exercise 失衡: {ex_begins} begins vs {ex_ends} ends"
assert sol_begins == sol_ends, f"Solution 失衡: {sol_begins} vs {sol_ends}"
assert ex_begins == sol_begins, f"Exercise/Solution 不配平: {ex_begins} exercises vs {sol_begins} solutions"
```

**Exercise 数量必须与 transcript 完全一致**。使用 `grep` 逐节统计题号。

### Phase 6: 质量检查（针对已有章节的修复任务）

当任务是**修复**而非新写时，必须执行全面质量检查：

#### 6.1 习题数量检查（逐节与 transcript 比对）

```bash
# 统计当前章节每节习题数
grep -n "begin{exercise}" chapterX.tex | sed 's/.*begin{exercise}{//' | sed 's/}.*//' | cut -d',' -f1 | sort | uniq -c

# 对比 transcript 中的习题数量（必须已知每节正确数量）
```

#### 6.2 正文内容完整性检查

- 是否有遗漏的 Proposition/Definition/Theorem/Property/Lemma？
- **习题引用的 Proposition 是否在正文中存在？**
- 如果习题引用了 Proposition 1 和 Proposition 2 → 必须确保笔记中有这两个命题，且有 `\label{prop:xxx}` 和 `\cref{prop:xxx}`

#### 6.3 图片引用检查

- 习题中引用的图片是否在正确位置？
- transcript 中提到的 Figure 是否都已插入？

#### 6.4 正文内容忠实度检查

- 内容是否与 transcript 原文一致？（英文内容不能变成中文摘要）
- 是否有漏写知识点？

### Phase 7: Solution 添加（针对缺解的章节）

当章节存在但 solution 缺失时：

1. 参考同教材其他章节的 solution 格式（例如 chapter1.tex）
2. 使用 `executor` agent **并行处理每节**（可用 10+ agents）
3. Solution 格式：直观理解 → 严格证明 → LaTeX 推导

### Phase 8: QA 记录（每问必录）

1. 用户提问 → 口语化回答
2. 记录到 `appendix/qa.tex`
3. 正文加 footnote：`\footnote{问：...？见附录 \cref{sec:qa-xxx}}`
4. 重新编译

### Phase 9: 编译验证

```bash
cd notes/<主题>/
bash compile.sh  # xelatex 3 次
```

**检查项**：
- overfull hbox 警告
- undefined reference 警告
- PDF 页数是否合理（章节是否出现）

---

## 已知坑与修复 SOP

### 🚨 严重问题（3.25 级）

| 症状 | 原因 | 修复 |
|------|------|------|
| 编译后章节完全消失（PDF 页数不增） | 章节文件末尾有 `\end{document}` | `sed -i '' '$ d' chapters/chapterX.tex` |
| exercise begins = 60 但 ends = 68 | Agent 只删 begin 没删 end | `git checkout HEAD~2` 恢复，重新处理 |
| exercises 数量 84 而非 64 | Agent 重复插入 exercises | 定位重复 block，删除多余部分 |
| solution blocks 数量多于 exercises | 之前修订残留重复 solution | 找到重复 block，删除 |
| 习题内容变中文 | Agent 擅自改写英文原文 | 逐题对照 transcript 修复 |
| 习题引用 Proposition 但正文没有 | 漏写了命题 | 补充命题内容 + `\label` + `\cref` |

### ⚠️ 中等问题

| 症状 | 原因 | 修复 |
|------|------|------|
| exercise/solution 不配平 | 添加 solution 时没有同步加 | 用 Phase 5 Python 脚本验证 |
| 图片缺失 | 没有从 transcript 插入图片 | 手动补充图片路径 |

### 📝 Exercise 题号格式（严格遵守）

```
\begin{exercise}{2-2, 1 — do Carmo, Exercise 2-2, 1}
```

---

## Agent Team 协作模式

### Writer Pair 轮询（Round Robin）

读取 `.claude/writer-round-robin.json`，每轮交替使用 writer pair。

### 并行化策略

**场景：多章节同时处理**
- 每章节一个独立的 Agent Team
- 章节内部每节可并行（**可用 10+ agents 同时处理**）
- 使用 `TaskCreate` 追踪所有并行任务

**Subagent 启动时必须注入 PUA**：
```
开工前用 Read 工具读取以下文件，按其中的行为协议执行：
- 核心行为：找到 pua 插件目录下的 skills/pua/SKILL.md（用 Glob 搜索 **/pua/skills/pua/SKILL.md）
- 如果是 P7 模式：同目录下的 references/p7-protocol.md
```

### 修复任务的 Agent 策略

| 任务类型 | Agent 数量 | 并行策略 |
|---------|-----------|---------|
| 新章节写作 | 2（主笔+评审） | 串行（主笔→评审→确认） |
| 已有章节质量检查 | 10+ | **每节一个 agent，并行** |
| Solution 添加 | 5+ | 每节一个 agent，并行 |
| 零散修复 | 1 | executor 单任务 |

---

## 输出路径规范

```
notes/<主题>/
├── <主题>-notes.tex    # 主入口（\input{chapterX}）
├── compile.sh          # 编译脚本
├── chapters/
│   ├── chapter0.tex    # 引言
│   ├── chapter1.tex
│   └── ...
└── appendix/
    └── qa.tex          # QA 记录
```

---

## 附录：Skill 能力确认

**Q: Skill 能否触发 subagent？**
**A: 可以。** 使用 `Agent` tool 直接 spawn，支持所有 subagent_type。

**Q: Skill 能否触发 Agent Team？**
**A: 可以。** 使用 `TeamCreate` 创建 team，再用 `Agent` 的 `team_name` 参数 spawn 成员。

**Q: Skill 能否自己执行写作？**
**A: 可以但不推荐。** 写作任务应该路由到 `writing-expert` agent 或 Writer Team，确保多轮修订和质量把关。

**Q: 修复已有章节用什么策略？**
**A: 质量检查 + 并行修复。** 先用 Python 脚本诊断问题（exercise/solution 数量、begin/end 平衡），然后用多个 subagent 并行处理每节的修复/补充。

**Q: subagent 数量上限？**
**A: 可用 10+ 并行。** 每节一个 agent 是最小颗粒度。
