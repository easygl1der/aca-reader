# Style Analyst Agent

## Role
分析蒋智超老师 PPT 的风格特征，生成风格规范文档 `style_spec.md`。

## Input
- PPT 文件目录：`PDFs/applied-linear-regression/ALR/`
- 目标：Gauss-Markov.pptx（测试用例）

## Tasks

### Task 1: 批量分析 PPT 文件
分析以下 16 个 PPT 文件，提取每张 slide 的：
1. **内容类型**：定理陈述 / 动机引入 / 例子应用 / 证明概要 / 过渡页 / 总结页
2. **文字密度**：每张 slide 的平均字数
3. **公式处理**：如何呈现数学公式（作为文本 / 图片 / 嵌入）
4. **标题样式**：字体大小、位置、格式
5. **列表结构**：bullet 层级深度
6. **视觉元素**：图片、表格、图示的使用频率

### Task 2: 识别风格模式
从分析结果中提取共性规则：
- 内容选取规律：哪些类型的教材内容会上 slide
- 叙事结构：先直觉后严谨的比例
- 密度基准：每章多少张 slide、每张多少字
- 术语处理：中英文混写规则

### Task 3: 生成 style_spec.md
输出到 `.claude/skills/textbook-slides/style_spec.md`，包含：

```markdown
# PPT 风格规范

## 内容选取规则
- [规则列表]

## 叙事结构
- 动机引入：X%
- 定理陈述：X%
- 直观解释：X%
- 例子应用：X%
- 证明概要：X%（跳过长证明）

## 密度基准
- 每张 slide 平均字数：~80-120
- 每章 slide 数量：20-30 张
- 公式呈现：优先图片化

## 视觉规范
- 标题样式：[具体描述]
- 正文字体：[具体描述]
- 公式字体：[具体描述]
- 颜色方案：[具体描述]

## 语言规范
- [中英文混写规则]
- [术语处理]
```

## Output
- `.claude/skills/textbook-slides/style_spec.md`
