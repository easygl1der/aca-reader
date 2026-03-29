# Homework Workflow Skill

## 功能

从 homework PDF 中提取作业题目，并在教材转录本中找到对应内容，生成 Obsidian callout 格式的作业笔记。

## 触发条件

- 用户说"读取作业"、"解析 homework"、"帮我看作业有哪些"
- 用户提供了 homework PDF 路径
- 用户要求生成作业笔记

## 工作流程

### Step 1: 检查教材 transcript / tex

**优先使用已有 .md 或 .tex 文件**，不要重复从 PDF 提取。

1. 搜索是否有对应教材的 transcript (.md) 或笔记 (.tex)：
   ```
   Glob: PDFs/<主题>/transcript/**/*.md
   Glob: notes/<主题>/**/*.tex
   ```

2. 如果有 .tex 文件 → 读取 .tex（更好的 `\label` / `\cref` 跳转）
3. 如果只有 .md 文件 → 读取 .md 转录本
4. **只有当没有 transcript 也没有 tex 时**，才从 PDF 解析

### Step 2: 解析 Homework PDF

使用 `pymupdf` (fitz) 提取 PDF 文本：

```python
import fitz
doc = fitz.open('/path/to/homework.pdf')
for page in doc:
    print(page.get_text())
```

### Step 3: 分析作业结构

识别：
- 教材习题编号（如 "Chapter 2: 2.1", "Chapter 3: 3.4, 3.5, 3.6"）
- 实证分析题目（LaLonde 数据等）

### Step 3: 在教材 transcript / tex 中查找习题内容

教材路径优先级：
1. **优先使用 .tex 版本**（如果有的话）- 因为 tex 里面有更好的 `\label` 和 `\cref` 引用跳转功能
2. 否则使用 .md 转录本

教材转录本路径：
```
PDFs/causal-inference/transcript/A First Course in Causal Inference - Peng Ding/hybrid_ocr/A First Course in Causal Inference - Peng Ding.md
```

**注意**：如果同一目录有 .tex 文件，优先使用 .tex 文件。

查找方法：
1. 搜索 "X.X Homework Problems" 标题
2. 提取该 section 下所有 numbered problems
3. 注意习题引用（如 "Section 3.4"、"Problem 3.6"）

### Step 4: 生成 Obsidian Callout 格式

**必须遵循的格式规则：**

1. **Callout 类型**：
   - 作业题用 `> [!exr]`
   - 被引用的背景内容用 `> [!example]`
   - 信息说明用 `> [!info]`
   - 数据说明用 `> [!note]`

2. **结构规则**：
   - `> [!exr]` callout 里面**只有习题题目**（不包含被引用内容）
   - 被引用的背景内容在**外部**用 `> [!example]` callout 补充
   - 每个题目单独一个 callout block

3. **Unicode 禁止规则**：
   - ❌ 禁止使用 `n₁`, `n₀`, `₁`, `₀` 等 unicode 下标
   - ✅ 必须使用 `$n_1$`, `$n_0$` 等 LaTeX 格式

4. **引用处理**：
   - 如果习题引用了前面章节内容（如 "Recall the example in Section 3.5.2"）
   - 在 `.tex` 文件中找到对应的章节，提取完整内容
   - 用 `> [!example]` callout 补充在习题 callout 的**外部**
   - **重要**: 如果习题要求 "Verify (3.7)" 或 "Show that (X.Y)" 等，必须：
     1. 在 .tex 文件中找到对应的 `\label{eq::...}` 或章节
     2. 提取完整的 equation 内容并写出
     3. 将被引用的 equation 完整写出，不能只写引用编号

## 模板格式

```markdown
```
Reading: 2.1 · 3.4 · 3.5 · 3.6 · 3.8 · A.1 · A.6 · C.1 · C.2
Data: nsw_cps.dta
```

---

> [!info] Part 1: Textbook Reading
> Read the following sections from *A First Course in Causal Inference* by Peng Ding:

| Chapter | Section | Title |
|---------|---------|-------|
| Chapter 2 | 2.1 | ... |

---

> [!exr] Problem X.X
> **Section X.X** — *Title*
>
> 完整习题内容（包括所有条件、假设、公式）
>
> *Remark: 如果有 remark 或引用，包含它们*

> [!example] Referenced Background: Section X.X
> 被引用的背景内容（外部补充）

---

> [!exr] Part 2 · (a)
> 题目内容

---

> [!note] Data Information
> 数据变量说明...
```

## 输出路径

作业文件保存到：
```
/Users/yueyh/Library/CloudStorage/GoogleDrive-easyglider458@gmail.com/My Drive/homework/<课程名>/hw<N>.md
```

## 注意事项

- 习题内容要完整提取，不能只提取标题
- 两个习题之间的内容都算第一个习题的
- `> [!exr]` 里面只有习题题目，被引用内容在外部用 `> [!example]` 补充
- 变量表格使用 markdown table 格式
- 数学公式使用 `$$...$$` 或 `$...$`
