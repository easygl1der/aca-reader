# 阶段 1+2：AI 精读定位

## 目的

定位并精读目标章节，提取关键内容，为后续大纲生成和初稿写作提供素材。

## 输入

用户指定的主题，例如：
- "Chapter 5 covariate balance in CRE"
- "Chapter 3 potential outcomes"

## 执行步骤

### Step 1：定位教材章节

根据主题确定对应的教材和章节：

**主题目录映射**：
| 主题 | 教材路径 | 笔记路径 |
|------|----------|----------|
| 因果推断 | `PDFs/causal-inference/transcript/A First Course in Causal Inference/` | `notes/A-First-Course-in-Causal-Inference/` |
| 微分几何 | `PDFs/differential-geometry/Do Carmo/` | `notes/differential-geometry/do-carmo-curves-surfaces/` |
| 贝叶斯 | `PDFs/bayesian/` | `notes/bayesian/` |
| 信息几何 | `PDFs/information-geometry/` | `notes/information-geometry/` |

### Step 2：读取章节内容

优先读取 `.tex` 转录版本（支持 label 跳转）：

```bash
# 示例：读取因果推断 Chapter 5
ls PDFs/causal-inference/transcript/A\ First\ Course\ in\ Causal\ Inference/
# 找到 chapter5.tex 或对应 md 文件
```

### Step 3：提取关键内容

对章节内容进行结构化提取：

#### 3.1 核心定义（Definitions）
- 定义编号和名称
- 完整定义内容
- 定义之前的动机/背景

#### 3.2 重要定理（Theorems）
- 定理编号和名称
- 完整定理内容
- 定理条件和结论
- 是否需要附录推导

#### 3.3 关键公式（Equations）
- 公式编号和名称
- 完整公式
- 公式的含义和用途

#### 3.4 示例（Examples）
- 示例编号和描述
- 示例的动机（为什么需要这个例子）
- 示例的完整计算/推导

#### 3.5 动机背景（Motivation）
- 这个章节解决什么问题
- 历史脉络和重要人物
- 与前面章节的联系

### Step 4：标注 Stein 风格

为每个关键内容标注：

```
【动机】这个定义从何而来？为什么要引入？
【历史】这个概念由谁提出？何时提出？
【联系】与哪些已学内容相关？
【应用】这个定理/公式有什么用？
【注意】这里容易犯什么错误？
【推导】这个证明的核心思想是什么？
```

### Step 5：识别附录内容

标记需要放到附录的复杂推导：

```
【附录候选】
- 定理 5.2 的完整证明（太长，影响正文流畅）
- 公式 (5.7) 的详细推导（包含多步代数运算）
- 性质 5.4 的验证（技术性较强）
```

### Step 6：记录问答

如果精读过程中有疑问：

1. 先尝试自行解答
2. 如果无法解答，使用 `qa-specialist` skill 记录问题
3. 调用 `gemini-browser-chat` 获取更深入的解释（如需要）

## 输出格式

创建 `close-reading-notes.md`：

```markdown
# Close Reading Notes: Chapter 5 - Covariate Balance in CRE

## 基本信息
- **主题**: Chapter 5 - Covariate Balance in Confounded Regression
- **字数**: ~5000 words
- **核心概念**: covariate balance, confounded regression

## 动机背景

**这个章节解决什么问题？**

在上一章我们学习了...，但是遇到了...问题。
本章引入...来解决这个问题。

**历史脉络**：
- [历史人物] 在 [年份] 首次提出...
- [后续发展]

## 核心定义

### Definition 5.1: [名称]
**原文**：
> 完整定义内容

**动机**：为什么要引入这个定义？
**联系**：与之前哪个概念相关？

## 重要定理

### Theorem 5.2: [名称]
**完整内容**：
> 定理完整表述

**条件**：
- 条件 1
- 条件 2

**结论**：
- 结论 1
- 结论 2

**核心思想**：证明的关键是什么？
**附录标记**：⚠️ 完整证明见附录

## 关键公式

### Equation (5.3): [名称]
**完整公式**：
$$\mathbb{E}(Y | X) = ...$$

**含义**：
**用途**：
**附录标记**：⚠️ 推导见附录

## 示例

### Example 5.4: [名称]
**动机**：为什么要举这个例子？

**设定**：
- $X$ = ...
- $Y$ = ...

**计算**：
[详细计算过程]

## 章节结构图

```
Section 5.1: 引入
    ↓
Section 5.2: [核心定义]
    ↓
Section 5.3: [主要定理] → Appendix A
    ↓
Section 5.4: [应用例子]
    ↓
Section 5.5: [小结]
```

## 待解答问题

1. [问题 1] — 状态：❓ 待研究
2. [问题 2] — 状态：✅ 已解答（见 qa.tex）

## 附录候选清单

| 内容 | 位置 | 原因 |
|------|------|------|
| Theorem 5.2 证明 | Appendix A.1 | 步骤太多，影响正文流畅 |
| (5.7) 推导 | Appendix A.2 | 多步代数运算 |
| Example 5.6 计算 | Appendix A.3 | 数值计算，非概念核心 |
```

## 集成 Skill

| Skill | 用途 |
|-------|------|
| `qa-specialist` | 记录精读中的问答 |
| `gemini-browser-chat` | 复杂数学问题深入解答 |

## 验证

完成精读后，确认：
- [ ] 已定位正确的章节
- [ ] 所有关键定义/定理/公式已提取
- [ ] 动机背景已标注
- [ ] 附录候选已标记
- [ ] 疑问已记录或解答
