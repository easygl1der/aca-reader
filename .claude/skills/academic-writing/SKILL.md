# Academic Writing Skill

## Purpose

实现六阶段 AI 自动学术写作工作流，通过人机协作迭代循环，最终生成高质量的课程讲义。

**核心理念**：人不直接改任何一个字，却参与到每一个字、每一幅图的创作之中。

## 六阶段工作流概览

| 阶段 | 名称 | 输出 | 等待用户 |
|------|------|------|----------|
| 1+2 | AI 精读定位 | `close-reading-notes.md` | ❌ |
| 3 | AI 大纲生成 | `chapter-outline.tex` | ❌ |
| 4 | AI 初稿 V1 | `drafts/v1_chapter{N}.tex` | ❌ |
| 5 | 人工审阅 | PDF + 反馈请求 | ✅ |
| 6 | AI 迭代优化 | V2, V3, ... | 循环 5-6 |

## 触发条件

当用户说以下命令时启动此 skill：
- "帮我写 Chapter X 关于 Y 的讲义"
- "开始六阶段学术写作"
- "用工作流写 Chapter X"
- "Write a chapter about X"

## 阶段执行

### 阶段 1+2：AI 精读定位

**执行文件**: `stages/stage1-close-reading.md`

- 定位教材对应章节
- 提取关键定义、定理、公式、例子
- 按 Stein 风格标注动机背景
- 识别需要附录推导的复杂证明
- 如有疑问，自动调用 qa-specialist 记录到 `appendix/qa.tex`

### 阶段 3：AI 大纲生成

**执行文件**: `stages/stage3-outline-generation.md`

- 生成章节骨架（动机优先结构）
- 预分配 label（`eq:balance-CRE`, `thm:5-1` 等）
- 标记需要放到附录的推导
- 输出 `chapter-outline.tex`（~30% 填充度）

### 阶段 4：AI 初稿 V1

**执行文件**: `stages/stage4-first-draft.md`

- 扩充大纲为完整章节
- 严格遵循 Stein 动机风格
- LaTeX 格式检查（无 Markdown）
- 符号规范（$\mathbb{E}X$, $\mathbf{x}$, $\boldsymbol{X}$）
- 示例放定义后，复杂推导放附录
- 输出 `drafts/v1_chapter{N}.tex`

**自动验证**：
- `latex-label-ref-verifier` — 引用一致性检查
- `latex-writing-check` — 格式检查
- `note-content-verifier` — 内容防幻觉

### 阶段 5：人工审阅 ⏸️

**执行文件**: `stages/stage5-human-review.md`

1. 编译 PDF：`cd notes/<topic> && ./compile.sh`
2. 提示用户审阅并提供结构化反馈
3. **Skill 暂停**，等待用户反馈
4. 用户提供 `feedback/review_vN.md`

### 阶段 6：AI 迭代优化

**执行文件**: `stages/stage6-iteration.md`

- 解析用户反馈为可执行项
- 应用修复（内容/风格/LaTeX）
- 生成 V{N+1} 版本
- 重新编译验证
- 循环直到用户批准

## 输出目录结构

```
notes/<topic>/
├── <topic>-notes.tex           # 主文件
├── compile.sh                   # 编译脚本
├── chapters/
│   └── chapter{N}.tex         # 最终定稿
├── appendix/
│   ├── qa.tex                 # QA 记录
│   └── derivations.tex        # 公式推导
├── drafts/
│   ├── v1_chapter{N}.tex
│   ├── v2_chapter{N}.tex
│   └── feedback/
│       ├── review_v1.md
│       └── review_v2.md
├── close-reading-notes.md
└── chapter-outline.tex
```

## 集成已有 Skill/Agent

| 现有 Skill/Agent | 在流程中的用途 |
|------------------|---------------|
| `qa-specialist` | 精读和写作中的问答记录 |
| `latex-writing-check` | V1/V2 阶段的格式检查 |
| `latex-label-ref-verifier` | 引用一致性检查 |
| `latex-debug` | 编译错误自动修复 |
| `note-content-verifier` | 内容真实性验证 |
| `writing-expert` (agent) | Stein 风格润色 |
| `figure-extractor` | 提取书中图形 |
| `paper-references-generator` | 生成参考文献 BibTeX |
| `literature-experts` team | 领域专家确认技术细节 |

## 领域专家团队

当精读或写作中遇到专业知识问题时，通过 `SendMessage` 咨询：

| Agent | 角色 |
|-------|------|
| `causal-expert` | 因果推断（Peng Ding 书籍） |
| `geometry-expert` | 微分几何（Do Carmo） |
| `bayesian-expert` | 贝叶斯统计（Gelman） |
| `info-geo-expert` | 信息几何（Amari） |
| `schubert-expert` | Schubert 计数几何 |

## 符号规范

严格遵循 `docs/writing-guide.md`：

| 概念 | 符号 |
|------|------|
| 概率 | `\mathbb{P}(A)` |
| 期望（单变量） | `\mathbb{E}X` |
| 期望（多变量） | `\mathbb{E}(XY)` |
| 方差 | `\text{var}` |
| 协方差 | `\text{cov}` |
| 向量 | `\mathbf{x}` |
| 矩阵 | `\boldsymbol{X}` |
| 示性函数 | `\mathbb{I}` |
| 独立性 | `A \Perp B` |

**禁止**：`\bm` 命令（用 `\mathbf` 或 `\boldsymbol` 替代）

## LaTeX 格式规范

- ❌ 禁止 Markdown 格式
- ✅ 必须使用 `\begin{enumerate}`, `\textbf{}`, `\textit{}`
- ✅ 引言简洁流畅，避免冗长脚注打断叙述
- ✅ 详细定义放到背景知识章节

## 写作风格

遵循 **Stein 动机优先风格**：

1. **动机明确**：先解释"为什么需要它"
2. **历史脉络**：注重概念的起源
3. **有机联系**：强调不同领域的相互关联
4. **叙事流畅**：避免干巴巴的罗列
5. **循序渐进**：从简单到复杂

详见 `docs/stein-writing-style.md`
