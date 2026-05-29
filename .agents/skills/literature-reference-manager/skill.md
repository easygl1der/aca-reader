---
name: literature-reference-manager
description: 文献引用管理器 - 扫描文献库，提取参考文献，自动从 CrossRef/Google Scholar 获取标准 BibTeX 引用，保存到文献库。
argument-hint: "<文献主题或PDF文件路径>"
---

# Literature Reference Manager

文献引用管理器 - 自动化的参考文献处理工作流。

## 功能

1. **扫描文献库** - 查看指定主题的文献列表
2. **提取参考文献** - 从 PDF/md 转录文件中提取参考文献
3. **自动搜索** - 使用 CrossRef API 和 Google Scholar 获取 BibTeX
4. **保存引用** - 生成并保存 BibTeX 文件到文献库

## 使用方法

### 方式一：扫描文献库
```bash
# 查看某个主题下的文献
/文献引用管理器 bayesian
/文献引用管理器 causal-inference
```

### 方式二：处理指定文献
```bash
# 处理指定文件
/文献引用管理器 PDFs/bayesian/textbook/Bayesian_Data_Analysis_Carlin.pdf
```

### 方式三：生成引用库
```bash
# 为整个主题生成引用库
/文献引用管理器 bayesian --generate-bib
```

## 工作流程

### 步骤 1：扫描文献库
列出指定主题目录下的所有 PDF 文献，显示：
- 文件名
- 文件大小
- 转录状态（是否已有 md）

### 步骤 2：选择文献
用户选择要处理的文献（可多选）

### 步骤 3：提取参考文献
- 如果有 md 转录文件，从 md 中提取
- 如果只有 PDF，使用 PDF 解析提取参考文献页面

### 步骤 4：自动搜索
对每篇参考文献：
1. 先尝试 CrossRef API（免费，无需 key）
2. 如果失败，使用 Google Scholar 搜索
3. 如果都失败，标记为"待手动"

### 步骤 5：保存引用
- 生成 `references.bib` 文件
- 保存到文献目录
- 可选：更新笔记中的引用

## 输出

```
============================================================
文献引用管理器
============================================================

📁 当前目录: PDFs/bayesian/
📚 文献数量: 5

[1] Bayesian Data Analysis (Gelman)
    - 转录状态: ✅ 已完成
    - 参考文献: 45 篇

[2] Markov Chain Monte Carlo in Practice
    - 转录状态: ✅ 已完成
    - 参考文献: 28 篇

选择要处理的文献 (输入编号，多选用逗号分隔): 1,2

============================================================
正在处理: Bayesian Data Analysis
============================================================

找到 45 篇参考文献

[1/45] Gelman et al. (1995) - 搜索中...
  ✓ 找到: Bayesian Data Analysis
  DOI: 10.1201/9780203887204

[2/45] Carlin and Louis (2008) - 搜索中...
  ✓ 找到: Bayes and Empirical Bayes
  DOI: 10.1007/978-0-387-35666-5

...

============================================================
生成完成
============================================================

📁 输出文件: PDFs/bayesian/references.bib
📚 成功获取: 42/45 篇
⚠️ 待手动: 3 篇
```

## 配置文件

首次使用会自动创建 `~/.literature-refs/config.json`：
```json
{
  "default_format": "bibtex",
  "citation_style": "authoryear",
  "auto_save": true,
  "crossref_email": "your@email.com"
}
```

## 注意事项

- CrossRef API 需要提供邮箱（可选但推荐）
- 有速率限制，不要同时处理大量文献
- 未找到的参考文献会列出，方便手动查找
- 支持多种文献格式：教材、论文、arXiv
