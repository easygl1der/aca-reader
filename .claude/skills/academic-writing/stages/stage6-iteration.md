# 阶段 6：AI 迭代优化

## 目的

根据用户反馈，迭代优化章节，生成 V2、V3 等版本，直到用户批准。

## 输入

- 当前版本 `drafts/v{N}_chapter{N}.tex`
- 用户反馈 `drafts/feedback/review_v{N}.md`

## 输出

- 优化版本 `drafts/v{N+1}_chapter{N}.tex`
- 更新后的 `drafts/feedback/review_v{N+1}.md`

## 迭代循环

```
V1 → 用户审阅 → 反馈 → V2 → 用户审阅 → 反馈 → V3 → ... → 用户批准
```

## 执行步骤

### Step 1：读取反馈

```bash
cat drafts/feedback/review_v1.md
```

### Step 2：解析反馈为可执行项

将用户反馈转换为具体的修改任务：

| 反馈类型 | 处理方式 |
|----------|----------|
| 内容问题 | 直接修改对应位置 |
| 结构问题 | 调整章节结构 |
| 风格问题 | 使用 `writing-expert` 润色 |
| 符号问题 | 检查并修正符号使用 |
| 附录问题 | 移动推导到/移出附录 |
| 新增内容 | 按 Stein 风格添加 |
| 删除内容 | 精简不必要内容 |

### Step 3：创建新版本

```bash
cp drafts/v1_chapter5.tex drafts/v2_chapter5.tex
```

### Step 4：应用修改

根据反馈类型执行相应修改：

#### 4.1 内容修改

```latex
% 找到问题位置，直接修改
% 例如：修改引言第二段
Old: "这个问题由 Rubin 首先提出..."
New: "这个问题由 Rubin (1974) 在其经典论文中首次提出..."
```

#### 4.2 结构修改

调整章节顺序或添加新节：
```latex
% 添加新的小节
\section{协变量平衡的诊断方法}\label{sec:5-4}
```

#### 4.3 风格润色

调用 `writing-expert` agent 进行 Stein 风格润色：

```bash
# 使用 SendMessage 联系 writing-expert
SendMessage(to: writing-expert, content: "请润色 drafts/v2_chapter5.tex 的引言部分，使其更符合 Stein 动机优先风格。")
```

#### 4.4 符号修正

检查并修正符号使用：
```bash
# 使用 latex-writing-check 检查符号问题
grep -rn "var(" --include="*.tex" drafts/v2_chapter5.tex
grep -rn "text{Var" --include="*.tex" drafts/v2_chapter5.tex
```

#### 4.5 附录调整

移动推导：
```latex
% 从正文移除证明，添加到附录
% 正文保留：
\begin{Proof}[概要]
证明的核心思想是... \done
\par\Notes{完整证明见附录 \cref{sec:appendix-5-1}。}
\end{Proof}

% 附录添加：
\section{附录：定理的完整证明}\label{sec:appendix-5-1}
```

#### 4.6 新增内容

按 Stein 风格添加新内容：
```latex
% 添加新例子
\begin{Example}[协变量不平衡的后果]\label{ex:5-6}
考虑一个极端情况：处理组全部为男性，对照组全部为女性...
\end{Example}
```

#### 4.7 删除内容

精简冗余：
```latex
% 删除重复的动机说明
% 删除过于琐碎的推导步骤
```

### Step 5：验证修改

#### 5.1 编译验证

```bash
cd notes/<topic>
./compile.sh
```

#### 5.2 格式检查

```bash
Skill latex-writing-check
Skill latex-label-ref-verifier
```

#### 5.3 内容验证（如有必要）

```bash
Skill note-content-verifier
```

### Step 6：生成审阅报告

创建 `drafts/feedback/review_v2.md` 的前身——记录已执行的修改：

```markdown
# V2 修改记录

## 已执行的修改

### 1. 引言第二段（用户反馈 1.2）
**修改前**：这个问题由 Rubin 首先提出...
**修改后**：这个问题由 Rubin (1974) 在其经典论文中首次提出...

### 2. 新增 Example 5.6（用户反馈 新增内容-1）
**新增内容**：协变量不平衡的后果的例子

### 3. 定理 5.2 证明移至附录（用户反馈 附录-1）
**修改**：完整证明移至 appendix/derivations.tex
**正文**：保留证明概要

## 未执行的修改及原因

### 1. 用户反馈 2.3（删除第三章内容回顾）
**原因**：为保持内容完整性，保留此回顾段落，但缩短了长度

## 下一步
请审阅 V2 版本...
```

### Step 7：发送审阅请求

向用户报告修改情况，并请求再次审阅：

---

## 📄 V2 审阅请求

根据 V1 反馈，已执行以下主要修改：

### 已修改
- ✅ 引言增加 Rubin (1974) 引用
- ✅ 新增 Example 5.6（协变量不平衡后果）
- ✅ 定理 5.2 证明移至附录
- ✅ 删除重复段落

### 请审阅
V2 版本已生成，请再次审阅并提供反馈...

---

## 迭代终止条件

循环继续直到：

1. **用户批准**：用户明确表示"V2 可以"或"不需要再修改"
2. **达到最大迭代次数**：V5 之后强制停止，请求用户最终决定

## 版本命名规范

```
drafts/
├── v1_chapter5.tex          # 初始版本
├── v2_chapter5.tex          # 第一轮迭代
├── v3_chapter5.tex          # 第二轮迭代
├── ...
└── final_chapter5.tex       # 最终版本（用户批准后）
```

## 最终版本处理

用户批准后：

1. 复制最终版本到主目录：
   ```bash
   cp drafts/final_chapter5.tex chapters/chapter5.tex
   ```

2. 更新 `appendix/derivations.tex`（如有必要）

3. 提交 git：
   ```bash
   git add chapters/chapter5.tex appendix/derivations.tex
   git commit -m "feat: complete Chapter 5 draft"
   ```

## 验证清单（每次迭代）

- [ ] 所有用户反馈已处理
- [ ] 编译成功
- [ ] 无 Markdown 格式
- [ ] 符号使用正确
- [ ] label/ref 一致
- [ ] 审阅报告已生成

## 集成 Skill

| Skill | 用途 |
|-------|------|
| `writing-expert` | 风格润色 |
| `latex-writing-check` | 格式检查 |
| `latex-label-ref-verifier` | 引用检查 |
| `latex-debug` | 编译错误修复 |
| `note-content-verifier` | 内容验证 |
