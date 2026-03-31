# 教学风格规范（蒋智超老师 - 应用回归分析 2025 秋）

> 基于 16 个 PPT 文件、383 张 slide 的系统分析

---

## 分析概览

| 指标 | 数值 |
|------|------|
| PPT 文件数 | 16 |
| 总 slide 数 | 383 |
| 平均每 PPT slide 数 | ~24 |
| 平均每 slide 字数 | ~27 |
| MathML 公式覆盖率 | 46.2%（177/383 slides） |
| 图片使用率 | 88.0%（337/383 slides） |
| 主要形状 | rect (1572), line (350) |

---

## 内容选取规则

### 1. 内容覆盖面
- **线性模型**：Gauss-Markov 定理、Normal 线性模型、OLS 渐近性、偏回归、部分回归
- **正则化**：Ridge、Lasso、Overfitting
- **模型诊断**：Model checking、Transformation、Weighted OLS
- **广义线性模型**：Logistic（binary/categorical）、Count outcomes、GLM
- **复习**：覆盖所有主题的总结复习 PPT

### 2. 每主题内容组织
典型结构：**动机 → 定义/框架 → 核心内容 → 证明/推导 → 练习题**

- 先用 **Motivation** slide 点明问题背景（为什么学这个）
- 用 **Definition/Framework** 建立概念框架
- 核心内容讲解定理和性质
- 适当插入 proof slides
- 以 **多选题/练习题** 结尾检验理解

### 3. 习题设计
- 大量使用**多选题**（每题 1 分）检验学生理解
- 题目简短有力，如 "Which of the following will change?"
- 答案通常在后续 slide 揭晓

---

## 知识组织模式

### 5 类内容组织方式

| 模式 | 占比 | 示例 |
|------|------|------|
| **Motivation → Content** | 5.7% | "Ridge works well for prediction, but Lasso is better for interpretability" |
| **Definition → Theorem → Proof** | 13.3% | 定理证明三连 |
| **Properties → Implications** | 10.4% | 讲解定理后说明其含义 |
| **Code → Output → Interpretation** | ~20% | 复习 PPT 专用结构 |
| **Example → Generalization** | 5.7% | 从具体例子引出一般结论 |

### 典型 slide 类型目录

| Slide 类型 | 占比 | 典型用途 |
|------------|------|----------|
| **Title/Cover** | 26.6% | 封面、章节标题页 |
| **Explanation** | 44.4% | 核心教学内容 |
| **Theorem/Property** | 10.4% | 定理陈述 |
| **Proof/Derivation** | 7.3% | 证明推导 |
| **Motivation/Example** | 5.7% | 动机引入 |
| **Definition** | 2.9% | 概念定义 |
| **Exercise** | 1.0% | 习题多选 |
| **Summary** | 0.8% | 小结 |
| **Transition** | 0.8% | 过渡页 |

---

## 密度基准

### 文字密度
- **平均每 slide 27 个英文单词**（或 15-20 个中文词）
- **平均每 slide 5.5 个 bullet point**
- 最多不超过 50 字/slide，避免信息过载

### 密度节奏
```
Motivation slide:    低密度（15-20 词）
Definition slide:    中密度（25-35 词）
Theorem slide:       中高密度（30-40 词）
Proof slide:         高密度（公式为主，文字辅助）
Exercise slide:      低密度（10-15 词，仅题目）
```

### 公式密度
- **46.2% 的 slides 含 MathML 公式**
- 公式与文字比例约 1:2（1 个公式配 2 行解释）
- 核心定理类 slide 公式密度最高

---

## 视觉习惯

### 配色方案
| 颜色 | 色值 | 用途 |
|------|------|------|
| 金黄 | `#FFC000` | 强调色、重点标注 |
| 深蓝 | `#0563C1` | 主色调、标题 |
| 绿色 | `#70AD47` | 积极/正确指示 |
| 橙色 | `#ED7D31` | 警示/注意 |
| 灰蓝 | `#44546A` | 正文文字 |
| 浅灰 | `#A5A5A5` | 次要文字 |
| 深灰 | `#000000` | 纯文字页 |

### 形状使用
- **矩形 (rect)**: 1583 个 — 主要内容容器
- **线条 (line)**: 350 个 — 分隔、连接
- **圆角矩形 (roundRect)**: 36 个 — 特殊标注框
- **椭圆 (ellipse)**: 4 个 — 装饰性

### 布局特征
- **几乎不用渐变**（仅 16 slides 有渐变）
- **几乎不用阴影**（0 slides 有 shadow）
- **几乎不用表格**（仅 2 slides 有表格）
- **大量使用图片/图示**（88% slides 含图片）

---

## 公式呈现

### MathML 使用
- **177/383 slides（46.2%）使用 Office MathML**
- 仅 2 个 PPT 未使用 MathML（复习 PPT 使用较少）
- 公式嵌入为 Office 原生公式对象

### 公式呈现原则
1. **公式居中**，上下留白
2. 公式后**紧跟解释文字**
3. 关键符号用**颜色标注**（如金色标注重点系数）
4. 长公式**分段展示**，不堆砌

### 常见公式模式
```
统计量：β_hat, σ_hat, RSS, R²
检验量：t-value, p-value, z-value
概率：P(Y=1|X), E[Y|X], Var(Y|X)
```

---

## 语言风格

### 问句引导（启发式教学）
- "Why should we focus on the OLS estimator?"
- "Why not use other functions of 'misfits'?"
- "Is it optimal in some sense?"
- "How robust is the result?"

### 动词使用频率
| 动词 | 用途 |
|------|------|
| Show / Prove | 定理推导 |
| Compute / Calculate | 计算演示 |
| Estimate | 估计方法 |
| Check / Verify | 模型验证 |
| Interpret | 结果解释 |

### 语气特征
- **简洁直接**：少用冗余词汇
- **问题驱动**：以问题引导思考
- **中英混合**：英文术语 + 中文辅助
- **学术规范**：引用原文 (Tibshirani 1996, Zou and Hastie 2005)

---

## 典型 Slide 类型目录

### 1. Cover Slide（封面）
```
- 标题居中，大字体
- 副标题/章节名
- 作者：蒋智超
- 时间：2025 年 秋
- 简洁背景，无多余装饰
```

### 2. Motivation Slide（动机引入）
```
- 左上角 "Motivation" + 编号
- 问题陈述（1-2 句）
- 背景说明
- 引入核心矛盾/需求
```

### 3. Definition Slide（定义）
```
- 顶部 "Definition" 标签
- 核心定义框（矩形背景）
- 变量符号说明
- 编号（如 "Condition (C1)"）
```

### 4. Theorem Slide（定理）
```
- 顶部 "Theorem" 标签 + 编号
- 定理陈述框
- 关键假设条件列表
- 可选：简短直观解释
```

### 5. Proof Slide（证明）
```
- 顶部 "Proof:" 标签
- 分步推导
- 每步简短解释
- 结尾 QED 或省略
```

### 6. Example Slide（例题）
```
- "Example:" 标签
- 具体数值/数据
- 逐步求解过程
- 结果解释
```

### 7. Exercise Slide（多选题）
```
- 顶部 "多选题" + 分值
- 选项 A/B/C/D
- 简洁题目
- 答案在后续 slide
```

### 8. Summary Slide（小结）
```
- "主要结论" 或 "Key Takeaways"
- 3-5 个核心点
- 简短回顾
```

---

## 附录：数据来源

分析文件列表：
```
1. 应用回归分析复习.pptx (23 slides)
2. 应用回归分析复习 [自动保存的].pptx (22 slides)
3. count outcomes.pptx (23 slides)
4. Gauss-Markov.pptx (20 slides)
5. GLM.pptx (17 slides)
6. Lasso.pptx (20 slides)
7. logistic regression （binary）.pptx (30 slides)
8. logistic regression （categorical）.pptx (32 slides)
9. model checking.pptx (37 slides)
10. Normal linear.pptx (23 slides)
11. OLS asymptotics.pptx (28 slides)
12. overfitting.pptx (21 slides)
13. partial regression.pptx (34 slides)
14. ridge regression.pptx (21 slides)
15. transformation.pptx (15 slides)
16. weighted OLS.pptx (17 slides)
```

---

*本规范基于 2026-03-31 的 PPT 分析生成*
