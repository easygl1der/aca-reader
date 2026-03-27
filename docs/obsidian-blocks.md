# Obsidian Callout Blocks

Obsidian 使用 `> [!type]` 语法创建 callout 块，用于标注不同类型的内容。

## 常用 Block 类型

| 类型 | 用途 | 颜色倾向 |
|------|------|---------|
| `note` | 普通笔记、说明 | 蓝/灰 |
| `info` | 信息提示 | 蓝 |
| `tip` | 技巧、提示 | 绿 |
| `warning` | 警告 | 黄/橙 |
| `danger` | 危险、错误 | 红 |
| `example` | 示例 | 紫 |
| `quote` | 引用 | 灰 |
| `question` | 问题 | 蓝 |
| `success` | 成功 | 绿 |

## 学术/作业专用 Block 类型

| 类型 | 用途 | 使用场景 |
|------|------|---------|
| `exr` | 习题/作业题 | 每个题目单独一个 block |
| `solution` | 解答 | 习题解答放在 `> [!exr]` 后，独立成 block |
| `def` | 定义 | 关键概念定义 |
| `thm` | 定理 | 重要定理 |
| `lemma` | 引理 | 辅助性定理 |
| `proof` | 证明 | 完整证明过程 |
| `rmk` | remark 备注 | 补充说明、解释 |
| `cor` | 推论 | 定理的推论 |

## 基本语法

```
> [!type] 标题（可选）
> 内容...
```

## 示例

### 习题格式

```markdown
> [!exr] Problem 3.4
> **Section 3.4** — *Fisher's exact test*
>
> Consider a CRE with a binary outcome...
```

### 解答格式

```markdown
> [!solution] Solution to Problem 3.4
>
> **Step 1:** ...
>
> Therefore, the distribution is...
```

### 定义格式

```markdown
> [!def] Hypergeometric Distribution
> A random variable $X$ follows a **Hypergeometric distribution** with parameters $(N, K, n)$ if
> $$\mathbb{P}(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}.$$
```

### 备注格式

```markdown
> [!rmk]
> **为什么 $Y$ 是给定的？** 在 FRT 框架下...
```

### 定理格式

```markdown
> [!thm] Theorem 7.1 (Matched-Pairs)
> Under matched-pairs randomization with $n/2$ pairs, the variance of $\hat{\tau}$ is...
```

## 作业文件模板

对于作业文件，每个题目使用以下结构：

```markdown
> [!exr] Problem X.X
> **Section X.X** — *Title*
>
> 题目内容...

> [!solution] Solution to Problem X.X
>
> 解答内容（直觉 + 推导 + 结论，全部放在这里）...
```

### 多部分题目

```markdown
> [!exr] Part 2 · (a)
> 子问题内容...

> [!solution] Solution to Part 2(a)
> 解答...

---

> [!exr] Part 2 · (b)
> ...

> [!solution] Solution to Part 2(b)
> ...
```

## 图片嵌入

使用 `![[path/to/image.png]]` 语法嵌入图片：

```markdown
![[R/coef_histogram.png]]
```

## 代码块

使用三个反引号包裹代码：

~~~markdown
```r
# R code here
lm(y ~ x, data = df)
```
~~~

## 注意事项

1. **Block 之间用 `---` 分隔** - 在视觉上区分不同题目
2. **标题使用粗体** - `**Section 3.4** — *Title*`
3. **公式使用 LaTeX** - `$...$` 行内公式，`$$...$$` 独立公式
4. **避免 Unicode** - 下标用 `$x_1$` 而非 `x₁`
5. **解答完整放 solution block 内** - 整道题的解答（直觉、真值表、推导、结论）全部放在 `> [!solution]` block 内
6. **长公式必须折行** - 公式太长时，在 `∨`、`∧`、`→` 等逻辑断点处用 `\\` 手动换行，禁止让公式溢出屏幕或页面
