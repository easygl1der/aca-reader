---
name: pdf-reader
description: 解析 PDF 文献，提取章节结构，理解内容框架
user-invocable: true
---

# PDF 解析 Skill

## 功能

1. 读取 PDF 文件内容
2. 提取章节结构（章、节、小节标题）
3. 识别核心定理/定义
4. 生成章节概览

## 使用方式

- 加载 PDF："帮我解析这个 PDF"
- 查看结构："这本书的章节结构是什么"
- 章节概览："第3章讲了什么"

## 输出

- 章节结构树
- 每章的核心目标
- 核心定义/定理列表

## 注意事项

- 使用 OCR 或 PDF 解析工具读取内容
- 提取标题作为章节标记
- 识别数学定理和定义（通常有编号如 Theorem 1.1, Definition 2.3）

## 实现

使用 Python 脚本进行 PDF 解析：

### 安装依赖

```bash
pip install pymupdf  # 推荐
# 或
pip install pdfplumber
```

### 使用方法

```bash
python src/pdf_parser.py <pdf_file>
```

### 输出格式

```json
{
  "pdf_path": "book.pdf",
  "structure": [
    {"type": "chapter", "number": "1", "title": "Introduction"},
    {"type": "section", "number": "1.1", "title": "Basic Concepts"},
    {"type": "theorem", "theorem_type": "Theorem", "number": "1.1"}
  ]
}
```
