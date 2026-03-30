# Content Curator Agent

## Role
从教材章节提取并改写内容，填充 curriculum-planner 生成的 slide 大纲。

## Input
- Slide 大纲：`.claude/workspace/applied-linear-regression/chapter04/outline.json`
- 教材章节：`PDFs/applied-linear-regression/chapters/chapter04_gauss.tex`
- 风格规范：`.claude/skills/textbook-slides/style_spec.md`

## Tasks

### Task 1: 读取教材内容
按 slide 大纲的需求，从 chapter04_gauss.tex 提取：
- 定理陈述（Theorem 4.1）
- 直观解释（误差椭圆几何）
- 例子内容
- 动机引入段落

### Task 2: 内容改写
将教材内容改写为 slide 友好的格式：
- 公式精简：保留核心公式，去除冗余符号
- 文字压缩：将段落压缩为要点（每点 ≤20 字）
- 层次结构：提取 2-3 层嵌套结构
- 术语统一：使用风格规范中的术语表

### Task 3: 生成 slide_contents.md
输出到 `.claude/workspace/applied-linear-regression/chapter04/slide_contents.md`：

```markdown
# Chapter 04: Gauss-Markov Theorem - Slide Contents

## Slide gm_01 (title)
- **标题**: Gauss-Markov Theorem
- **副标题**: Best Linear Unbiased Estimation
- **内容**: [封面设计素材]

## Slide gm_02 (motivation)
- **标题**: Why BLUE?
- **要点**:
  - OLS 是自然的，但不一定是"最佳"的
  - "最佳" = 所有线性估计中方差最小
  - 关键问题：OLS 在线性类中是否最优？

## Slide gm_03 (review)
- **标题**: OLS 回顾
- **公式**: $\hat{\beta} = (X^TX)^{-1}X^Ty$
- **要点**:
  - 最小化残差平方和
  - 几何解释：投影

## Slide gm_04 (theorem)
- **标题**: Gauss-Markov Theorem
- **定理陈述**: [完整定理文本]
- **直观解释**: [误差椭圆示意图描述]
```

### Task 4: 识别需手动填写内容
在 slide_contents.md 中标注：
- `[需手动添加图片]`
- `[需手动输入数值例子]`
- `[参考文献：教材 p.XX]`

## Output
- `.claude/workspace/applied-linear-regression/chapter04/slide_contents.md`
- `.claude/workspace/applied-linear-regression/chapter04/compilation_notes.md`（需手动填写的内容清单）
