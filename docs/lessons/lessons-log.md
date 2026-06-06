
## 2026-04-03: 空洞脚注引用不能删除，必须找到正确位置

**问题**：ch6 有两处脚注写着"见附录"但内容空洞（没有具体推导）：
- Line 101: "Laplace 分布 MLE 的完整推导见附录"
- Line 409: "指数分布似然比检验的详细推导见附录"

**错误做法**：我先盲目添加了 `\cref{sec:mle-asymptotic-proof}`，但 appendix 中根本没有 Laplace MLE 和指数 LRT 的对应章节，造成虚假引用。然后我直接删除了这两条脚注——**比原来更糟**，因为读者失去了追溯推导细节的导航。

**正确做法（三步走）**：

1. **搜索现有 appendix 章节**：`grep "\\label\{sec:" chapters/chapter6.tex`，找内容最相关的已有章节

2. **存在相关章节** → 修改脚注指向正确位置

3. **不存在相关章节** → **必须在 appendix 中补充内容**，然后再引用
   - **绝不能删除脚注**——脚注是读者追溯推导的唯一导航

**正确修复**：
- Laplace MLE 脚注 → 指向 `sec:mle-asymptotic-proof`（MLE 渐近正态是同类内容）
- 指数 LRT 脚注 → 同样指向 `sec:mle-asymptotic-proof`
- 或在 appendix 新增专门的小节

**教训**：修复"见附录"空洞脚注前，**绝不能删除**。先搜现有 appendix，找不到则补充内容，绝不断开读者追溯的链条。

---

## 2026-04-03: LaTeX 修复不记录到 qa.tex

**问题**：把 LaTeX 语法修复记录到了 `appendix/qa.tex`，但 qa.tex 是用于记录"用户提问"的，不应记录内部修复。

**正确路由**：
- **用户提问** → 记录到 `appendix/qa.tex`
- **内部修复 / 经验教训** → 记录到 `docs/lessons/lessons-log.md`

**教训**：区分"用户问题回答"和"内部经验教训"，前者进 qa.tex，后者进 lessons-log.md。


## 2026-03-31: bash heredoc 导致 LaTeX 命令损坏

**问题**：使用 `echo '...' >> file.tex` 或 heredoc 追加内容时，反斜杠 `\`，导致 `\textbf`、`\begin{itemize}` 等 LaTeX 命令被损坏（变成 `extbf`、`egin{itemize}`）。

**原因**：bash heredoc/echo 默认不处理反斜杠转义字符。

**解决方案**：
1. 使用 Python 写入文件，避免 bash 转义问题
2. 或在 heredoc 中使用单引号并确保内容不包含会转义的字符

**教训**：追加 LaTeX 内容到 .tex 文件时，优先使用 Python 而非 bash heredoc/echo。


## 2026-03-31: 添加附录解释后必须在正文中加 footnote 引用

**问题**：在 appendix 添加了解释，但漏了正文中某处的 footnote 引用。

**检查清单**：每次在 qa.tex 添加新内容后，必须检查：
1. 正文是否有多处提到这个概念？
2. 每处是否都已添加 footnote 引用？

**本次教训**：Gromov-Witten 不变量在正文第 15 行和第 237 行都出现了，我只给第 15 行加了 footnote，漏了第 237 行。

**正确流程**：
1. 在 appendix 添加解释
2. grep 正文中所有提到该概念的位置
3. 每个位置都要添加 \footnote{问：xxx？见附录 \cref{sec:xxx}。}


## 2026-03-31: Proofread 时 AI 报告的问题需用户视觉确认

**问题**：AI 报告了 4 个问题，但经用户逐个确认后，只有 2 个是真正需要修复的。

**本次确认结果**：
| 问题 | 结论 |
|------|------|
| 行202 孤立等式残留 | ❌ 不是问题（Theorem 后的推导等式是正常表述）|
| 行44 脚注在 Theorem 内 | ❌ 不是问题（技术上可行）|
| 行150 `\ref`→`\cref` | ✅ 确实需要修复 |
| 行308 `\ref`→`\cref` | ✅ 确实需要修复 |

**教训**：
1. **AI 报告 ≠ 必须修复** — 必须逐个跳转让用户视觉确认
2. **Theorem 后的等式** — 可能是正常数学表述，不是编辑残留
3. **脚注在 Theorem 内** — 在 LaTeX 中技术上是合法的，不算错误

**正确流程**：
1. AI 生成问题列表
2. **逐个 Skim 跳转**，每个停留 5 秒
3. 用户确认哪些需要修复
4. 只修复用户同意的问题
5. 记录"不是问题"的经验到 CLAUDE.md


## 2026-03-31: Claude Code permissions 配置不支持文件后缀细粒度控制

**问题**：用户想配置 `rm -f *.aux *.bbl *.blg ...` 不询问，但 `rm` 本身需要询问。

**尝试方案**：
- 添加 `Bash(rm -f:*)` → ❌ 失败（会绕过所有 rm -f 的询问）
- 去掉 `Bash(rm -f:*)` → 用户不需要这种粗粒度控制

**结论**：Claude Code 的 `settings.local.json` permissions 目前不支持基于文件后缀的细粒度控制。

**教训**：
1. 权限配置只有通配符级别（如 `rm:*`、`rm -f:*`），无法细化到 `rm -f *.aux`
2. 如果无法做到精确控制，就不要添加该权限
3. 用户对"特定后缀免确认"的需求暂时无法满足

**替代方案**：
- 使用项目内的 compile wrapper script 处理辅助文件删除
- 或每次手动确认

---

## 2026-04-04: 定理引用时同时标注文献和笔记交叉引用

**情境**：用户引用 Theorem 5.1 (Classical Double Schubert Positivity) 时，表示引用文献时如果该内容在笔记中已有对应位置，则**不仅加 `\cite{}` 文献引用，也要加 `\cref{}` 指向笔记内的对应位置**。

**用户习惯**：
> 定理引用时，如果该文献/定理已经在笔记中有对应内容，**不仅要加文献引用 `\cite{...}`，也要加 `\cref{...}` 指向笔记内的对应位置**。格式为在同一括号内同时写 citation 和 cref。

**示例**：
```latex
% 原文
The proof follows the strategy of Gao--Xiong \cite[Section 2]{GX2025}...

% 改为：文献引用 + 笔记交叉引用（双管齐下）
The proof follows the strategy of Gao--Xiong \cite[Section 2]{GX2025}\footnote{详见\cref{sec:GX2025-Section2}（\cite[Section 2]{GX2025}）}，which extends Graham's positivity framework \cite{Gr}\footnote{详见\cref{def:GrahamPositivity}（\cite[Section 2.2]{Gr}）}...
```

**适用场景**：
- 定理证明中引用他人工作时
- 引用已在本笔记中定义的概念（如 `\cref{def:DoubleSchubertPolynomial}`）
- 引用已在本笔记中证明的定理（如 `\cref{th:GrahamPositivityRefined}`）

**本次操作**：
- Theorem 5.1 证明中：
  - `\cite[Section 2]{GX2025}` → 加 `\footnote{详见\cref{sec:GX2025-Section2}（\cite[Section 2]{GX2025}）}`
  - `\cite{Gr}` → 加 `\footnote{详见\cref{def:GrahamPositivity}（\cite[Section 2.2]{Gr}）}`
  - $\mathfrak{S}_w(\mathbf{x}; \mathbf{y})$ → 加 `\footnote{双Schubert多项式定义见\cref{def:DoubleSchubertPolynomial}}`
  - Graham positivity theorem → 加 `\footnote{详见\cref{th:GrahamPositivityRefined}（\cite[Corollary 2.4]{GX2025}）}`

**待办**：
- [ ] 检查 Lemma 2.5 是否在笔记中有对应位置
- [ ] 检查 moment graph 相关定义是否有 label
- [ ] 检查其他章节是否有类似需要补充双引用的情况

---

## 2026-04-08: rewrite chapter 导致 qa.tex 1300 行内容被删除

**问题**：commit `7aee6ae07`（chore: update chapter5）重写 chapter5 时，意外删除了 qa.tex 的 28 个 QA 条目（从 1875 行骤降到 566 行）。

**事故链条**：
1. `dfd5d29b5` — qa.tex 已有 1875 行，包含 28 个精心撰写的 QA 条目
2. `7aee6ae07` — update chapter5 时，agent 对 qa.tex 做了大幅重写/替换
3. 结果：qa.tex 变成 566 行，删除了 1309 行内容，包括：
   - EQLR 系数定义与意义
   - Skew 除差算子与除差算子的关系
   - 逆除差算子的定义
   - 双重与三重 Schubert 多项式的区别
   - 等变量子上同调类的定义
   - Hilbert 第十五问题与 Schubert 演算
   - 量子上同调的定义
   - Theorem 1.1 的例子：Triple Schubert Positivity
   - Knutson-Tao (2003) 展开系数的几何意义
   - Graham Positivity 中 Grassmannian 限制的作用
   - Littlewood-Richardson 系数为何非负
   - ... 共 28 个条目

**恢复方法**：`git show dfd5d29b5:notes/Schubert-Polynomials/appendix/qa.tex > notes/Schubert-Polynomials/appendix/qa.tex`

**Root cause**：agent 在 rewrite 一个章节时，没有意识到 qa.tex 也在被同时处理，且没有检查 qa.tex 是否有未提交的宝贵内容。

**教训**：
1. **qa.tex 是高价值内容库** — 每次 rewrite 章节内容前，必须先检查 qa.tex 是否有相关的新内容
2. **rewrite 时要 grep 检查** — 搜所有 .tex 文件中是否有对新内容的引用，确保没有遗漏
3. **commit 前用 `git diff` 确认** — 确认只改了你意图改的文件，没有意外副作用
4. **qa.tex 应该有独立的 commit** — 不应与其他章节内容混在同一个 commit 里

## 2026-06-06: 项目 Codex 目录统一使用小写 `.codex`

**问题/场景**：用户纠正我把项目规则目录说成 `.Codex/`，实际项目约定应为小写 `.codex/`。

**教训**：本项目内所有 Codex 配置、hooks、rules、agents 路径统一写作 `.codex/`。即使 macOS 上 `.Codex` 和 `.codex` 可能指向同一个目录，也必须在文档和回答中使用小写路径，避免跨平台和心智模型混乱。

**检查清单**：
- [ ] 回答项目路径时统一写 `.codex/`
- [ ] 新增规则文件时放入 `.codex/rules/`
- [ ] 修改索引文档时避免重新引入 `.Codex/`
