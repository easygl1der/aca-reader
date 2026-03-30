# Curriculum Planner Agent

## Role
**核心思考 agent**。基于风格规范和 topic 映射，规划每章 slide 大纲（JSON 格式）。

## Input
- 风格规范：`.claude/skills/textbook-slides/style_spec.md`
- Topic 映射：`.claude/skills/textbook-slides/topic_map.md`
- 教材章节：`PDFs/applied-linear-regression/chapters/chapter04_gauss.tex`
- 用户指令：生成 Gauss-Markov 章节 slides

## Tasks

### Task 1: 理解知识地图
分析 Chapter 04 的概念依赖图：
- 前置知识：Chapter 02 (OLS), Chapter 03 (Gauss-Markov 背景)
- 核心定理：Gauss-Markov Theorem
- 延伸概念：BLUE, 最小方差性, 几何解释
- 应用场景：线性模型的参数估计

### Task 2: 设计教学叙事
按照"先直觉后严谨"的原则组织 slide 顺序：
1. 动机引入（5%）：为什么需要 BLUE？
2. 概念铺垫（15%）：OLS 回顾、最小二乘几何
3. 定理陈述（10%）：Gauss-Markov Theorem
4. 直观解释（30%）：误差椭圆、最佳性几何
5. 例子应用（20%）：简单线性回归例子
6. 总结回顾（10%）：核心要点
7. 过渡页（10%）：下一章预览

### Task 3: 生成 slide 大纲 JSON
输出到 `.claude/workspace/applied-linear-regression/chapter04/outline.json`：

```json
{
  "chapter": "04",
  "title": "Gauss-Markov Theorem",
  "topic": "Gauss-Markov",
  "total_slides": 25,
  "slides": [
    {
      "slide_id": "gm_01",
      "type": "title",
      "title": "Gauss-Markov Theorem",
      "subtitle": "Best Linear Unbiased Estimation",
      "source": "教材 §4.1",
      "notes": "封面页"
    },
    {
      "slide_id": "gm_02",
      "type": "motivation",
      "title": "Why BLUE?",
      "content_source": "教材 §4.1 motivation",
      "teaching_intent": "引出最佳估计的动机",
      "key_elements": ["OLS is natural but not unique", "Best = lowest variance among linear estimators"],
      "depends_on": [],
      "skip_elements": []
    },
    {
      "slide_id": "gm_03",
      "type": "review",
      "title": "OLS 回顾",
      "content_source": "教材 §2.2, §3.1",
      "teaching_intent": "铺垫：最小二乘估计的推导",
      "key_elements": ["$\\hat{\\beta} = (X^TX)^{-1}X^Ty$", "几何解释"],
      "depends_on": [],
      "skip_elements": ["矩阵演算细节"]
    },
    {
      "slide_id": "gm_04",
      "type": "theorem",
      "title": "Gauss-Markov Theorem",
      "content_source": "教材 §4.1, Theorem 4.1",
      "teaching_intent": "建立 OLS 是 BLUE 的结论",
      "key_elements": [
        "定理陈述：$\\text{Var}(\\tilde{\\beta}) - \\text{Var}(\\hat{\\beta}) \\geq 0$",
        "直观解释（误差椭圆）"
      ],
      "depends_on": ["gm_02", "gm_03"],
      "skip_elements": ["完整证明（见教材 p.45-47）"]
    }
  ]
}
```

### Slide Type 枚举
- `title`: 封面页
- `motivation`: 动机引入
- `review`: 回顾铺垫
- `theorem`: 定理陈述
- `intuition`: 直观解释
- `example`: 例子应用
- `summary`: 总结页
- `transition`: 过渡页

## Output
- `.claude/workspace/applied-linear-regression/chapter04/outline.json`
