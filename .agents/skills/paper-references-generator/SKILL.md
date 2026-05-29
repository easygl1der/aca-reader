---
name: paper-references-generator
description: 自动从论文 md 转录文件中提取参考文献列表，使用 CrossRef API 搜索每篇论文，获取 DOI 并生成 BibTeX 引用格式，方便添加到笔记中。
argument-hint: "<md文件路径>"
---

# Paper References Generator

自动从论文的 md 转录文件中提取参考文献，使用 CrossRef API 搜索并生成 BibTeX 引用。

## Arguments

`$ARGUMENTS` 是 md 文件的路径。

## 使用方法

```bash
python ~/.Codex/skills/paper-references-generator/scripts/paper_references_generator.py <md文件路径>
```

## 工作流程

### 步骤 1：提取参考文献
读取 md 文件，查找 `REFERENCES` 或 `Bibliography` 部分，提取所有参考文献条目。

### 步骤 2：使用 CrossRef API 搜索
对每篇参考文献，使用 CrossRef API 搜索获取完整信息：
```
https://api.crossref.org/works?query=<关键词>
```

### 步骤 3：生成 BibTeX
根据获取的信息生成 BibTeX 格式引用。

## 输出示例

```
处理文件: paper.md
找到 22 篇参考文献

处理 [1] Author1...
  ✓ 找到: Paper Title

============================================================
BibTeX 参考文献
============================================================

### [1] Paper Title
BibTeX key: author2023
```bibtex
@article{author2023,
  author = {Author, First},
  title = {Paper Title},
  year = {2023},
  doi = {10.xxx/xxx}
}
```

### 未找到的参考文献（需手动处理）
- [X] 搜索关键词
```

## 注意事项

- CrossRef API 完全免费，无需 API key
- 有速率限制，每秒最多几个请求
- 如果 API 失败，标记为"待手动处理"
