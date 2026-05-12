# Textbook Notes Workflow Skill

## 功能

从教材源材料生成高质量章节笔记，支持：知识点提取、习题处理、Stein 写作风格、多轮修订、LaTeX 编译、QA 记录、以及 Agent Team 协作。

## 触发条件

- 用户说"生成第 X 章笔记"、"写 chapters/chapterX"
- 用户说"润色 .tex"、"写作任务"
- 用户要求生成教材章节笔记

---

## 核心原则

### 源材料优先级（绝对规则）

| 优先级 | 来源 | 说明 |
|--------|------|------|
| **1** | `chapters/chapterX.tex` | 如果已存在，直接读取修改 |
| **2** | `PDFs/<主题>/transcript/**/*.md` | MinerU 转录本（优先） |
| **3** | `PDFs/<主题>/transcript/**/*.tex` | 教材章节 tex |
| **4** | 原始 PDF | 仅限需要视觉确认时，使用 `pages` 参数限制 |

> ⚠️ **永远不要**优先扫描原始 PDF！Transcript 是首选。

### LaTeX 格式红线（禁止违反）

| 禁止 ❌ | 正确 ✅ |
|---------|---------|
| `\bm`（向量） | `\mathbf` 或 `\boldsymbol` |
| `\I`（单位矩阵） | `\mathbb{I}` |
| Unicode 下标 `$n₁$` | `$n_1$` |
| `\ref{xxx}` | `\cref{xxx}` |
| `\include{chapterX}` | `\input{chapterX}` |
| 章节文件末尾 `\end{document}` | **禁止** |
| Markdown 语法、\tag{} | 标准 LaTeX 引用 |

### 空括号记号（用户偏好）

- 空方括号：`[\cdot]`
- 空圆括号：`(\cdot)`

---

## 工作流程

### Step 1: 确定任务范围

1. 读取 `.claude/writer-round-robin.json` 确定 writer pair
2. 从 prompt 提取章节编号（"第 3 章" → `chapter3`）
3. 确定笔记目标目录：`notes/<主题>/chapters/`
4. 确定源材料路径（见上方优先级）

### Step 2: 分析源材料

```
使用 Agent tool (subagent_type: content-curator) 读取教材章节：
- 提取知识框架（定理、定义、引理）
- 标记关键公式和图
- 标注难点和直观理解
```

### Step 3: 生成笔记初稿（Primary Writer）

**写作风格**：Stein 风格（详见下方）

**结构**：
```latex
\section{章节标题}
\subsection{引入}
% 动机、历史背景、为什么重要

\subsection{主要内容}
% 定义 → 定理 → 证明思路 → 例子

\subsection{习题}
\begin{exercise}{题号}
题目内容...
\end{exercise}
\begin{solution}
解答内容...
\end{solution}
% 重复所有习题
```

**关键格式**：
- 每个定义/定理/引理都要有 `\label{eq:名称}` 或 `\labelthm{df:名称}`
- 证明结尾加 `\qed` 或 `\qedash`
- 习题和解答**必须严格成对**（begin/end 数量相等）
- **禁止**在章节文件末尾写 `\end{document}`

### Step 4: 评审修订（Reviewer）

Reviewer 执行**挑战式评审**：

1. **逻辑完整性**：证明步骤是否跳步？
2. **直观理解**：是否有动机说明和几何直观？
3. **习题平衡**：begin/end 是否匹配？
4. **格式合规**：是否违反 LaTeX 红线？
5. **引用完备**：定理引用是否附上原文 footnote？

至少 **2 轮讨论**，每轮 Reviewer 提出质疑，Primary Writer 回应修订。

### Step 5: Exercise + Solution 平衡验证

**必须验证**（生成后检查）：
```python
import re
content = open('chapterX.tex').read()
ex_begins = len(re.findall(r'\\begin\{exercise\}', content))
ex_ends = len(re.findall(r'\\end\{exercise\}', content))
sol_begins = len(re.findall(r'\\begin\{solution\}', content))
sol_ends = len(re.findall(r'\\end\{solution\}', content))
assert ex_begins == ex_ends, f"Exercise 失衡: {ex_begins} begins vs {ex_ends} ends"
assert sol_begins == sol_ends, "Solution 失衡"
```

**常见错误**：
- Agent 删除 exercise begin 但保留 end → 产生孤立 `\end{exercise}`
- 重复的 solution block 残留
- 修复：使用 `git checkout HEAD~2` 恢复后重新处理

### Step 6: QA 记录（每问必录）

1. 用户提问 → 口语化回答
2. 记录到 `appendix/qa.tex`
3. 正文加 footnote：`\footnote{问：...？见附录 \cref{sec:qa-xxx}}`
4. 重新编译

**格式**：
```latex
\subsection{标题}\label{sec:qa-xxx}
\textbf{问：}...？
\textbf{答：}...
```

### Step 7: 编译验证

```bash
cd notes/<主题>/
bash compile.sh  # xelatex 3 次
```

**检查项**：
- overfull hbox 警告
- undefined reference 警告
- PDF 页数是否合理

---

## Stein 写作风格

### 核心原则

| 原则 | 说明 |
|------|------|
| **动机优先** | 先讲"为什么"，再讲"是什么" |
| **历史语境** | 定理谁提出的？解决什么问题？ |
| **直观连接** | 抽象概念配几何/物理直观 |
| **有机组织** | 章节之间互引，形成网络 |

### 实践指南

**引入部分**：
```
在引入概念 X 之前，先问：为什么需要 X？
（例：黎曼度量 → 为了定义弧长和角度，与内积联系）
```

**定理呈现**：
```
[直觉层面]
[形式陈述]
[证明思路（为什么有效）]
[形式证明]
[补充说明（推广、例外）]
```

**例子优先**：
```
讲"曲率"之前，先给一个具体曲面的例子，
让读者建立直觉，再抽象化。
```

---

## Agent Team 协作模式

### TeamCreate（当需要多 agent 时）

```json
{
  "team_name": "<主题>-writing-team",
  "description": "生成第 X 章笔记"
}
```

### Writer Pair 轮询

| Round | 主笔 | 评审 |
|-------|------|------|
| 1 | ch1-writer | ch1-writer-2 |
| 2 | ch2-writer | ch2-writer-2 |
| 3 | ch3-writer | ch3-writer-2 |
| 循环→ | ... | ... |

### 协作流程

1. **第一轮**：Primary 起草 → Reviewer 挑战
2. **第二轮**：Primary 修订 → Reviewer 最终确认
3. **汇报**：Team Lead 汇总，向用户交付

### PUA 注入要求

Spawn sub-agent 时，prompt 末尾注入：
```
开工前用 Read 工具读取以下文件，按其中的行为协议执行：
- 核心行为：找到 pua 插件目录下的 skills/pua/SKILL.md（用 Glob 搜索 **/pua/skills/pua/SKILL.md）
- 如果是 P7 模式：同目录下的 references/p7-protocol.md
```

---

## Skill 触发 Subagent 能力

**可以的**。使用 `Agent` tool 即可 spawn 任意 subagent：

| 场景 | Agent Type | 说明 |
|------|------------|------|
| 内容提取 | `content-curator` | 从教材提取内容 |
| 写作 | `writing-expert` | 润色/修改已有草稿 |
| LaTeX 检查 | `latex-checker` | QA 检查 |
| Agent Team | `pua:tech-lead-p9` | 协调多 agent |
| 单任务执行 | `executor` | 复杂但独立的任务 |

**示例**：
```json
Agent({
  "description": "生成微分几何 chapter4 初稿",
  "prompt": "使用 content-curator 读取教材...",
  "subagent_type": "content-curator"
})
```

---

## 常见错误与修复

| 症状 | 原因 | 修复 |
|------|------|------|
| 编译后章节不出现 | 章节文件末尾有 `\end{document}` | `sed -i '' '$ d' chapterX.tex` |
| Exercise 失衡 | Agent 删除 begin 但保留 end | `git checkout HEAD~2` 恢复，重新处理 |
| 重复 solution block | 之前修订残留 | 定位并删除重复 block |
| overfull hbox | 公式太长 | 调整断行或使用 `\!` 压缩 |
| undefined ref | 标签名拼写错误 | 搜索并修正 |

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
