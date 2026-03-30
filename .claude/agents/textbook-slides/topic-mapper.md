# Topic Mapper Agent

## Role
建立 PPT topic 与教材 chapter 的映射关系，生成 `topic_map.md`。

## Input
- PPT 文件：`PDFs/applied-linear-regression/ALR/*.pptx`
- 教材章节：`PDFs/applied-linear-regression/chapters/`

## Tasks

### Task 1: 分析 Gauss-Markov PPT
针对测试用例 `Gauss-Markov.pptx`：
1. 提取 slide 标题列表
2. 识别每张 slide 对应的教材内容来源
3. 建立 slide → 教材段落/章节的映射

### Task 2: 建立完整映射表
为所有 16 个 PPT 建立映射关系：

| PPT 文件 | 核心 Topic | 对应教材章节 | Slide 数量 | 核心内容 |
|----------|-----------|-------------|------------|----------|
| Gauss-Markov.pptx | BLUE, 最佳线性无偏估计 | Chapter 04 | ~25 | Gauss-Markov 定理 |

### Task 3: 生成 topic_map.md
输出到 `.claude/skills/textbook-slides/topic_map.md`：

```markdown
# Topic ↔ Chapter 映射

## Gauss-Markov (测试用例)
- **PPT**: `Gauss-Markov.pptx`
- **对应教材**: Chapter 04 (Gauss-Markov Theorem)
- **Slide 数量**: ~25 张
- **核心内容**:
  - OLS 回顾
  - BLUE 条件
  - Gauss-Markov 定理陈述
  - 直观解释（误差椭圆几何）
  - 例子
- **跳过的内容**:
  - 完整证明（见教材 p.45-47）
  - 有限样本性质细节

## 完整映射表
[16 个 PPT 的映射关系]
```

## Output
- `.claude/skills/textbook-slides/topic_map.md`
