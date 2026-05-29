---
name: skim-jump
description: 使用 Skim displayline 跳转到 PDF 对应 TeX 行号
user-invocable: true
---

# Skim Jump Skill

## 功能
通过 Skim 的 `displayline` 命令实现 PDF 与 TeX 源码的同步跳转。

## 命令格式
```bash
/Applications/Skim.app/Contents/SharedSupport/displayline -r -g <line> "<pdf-file>" "<tex-file>"
```

## 参数说明
- `-r`: 重新加载 PDF
- `-g`: 跳转到指定位置并聚焦窗口

## 使用流程

### 1. 定位目标行号
```bash
grep -n "目标内容" /path/to/chapters/chapter1.tex
```

### 2. 执行跳转
```bash
/Applications/Skim.app/Contents/SharedSupport/displayline -r -g <行号> "<PDF路径>" "<TeX路径>"
```

## 示例

跳转到 chapter1.tex 第 650 行（李代数定义）：
```bash
/Applications/Skim.app/Contents/SharedSupport/displayline -r -g 650 "/Users/yueyh/Projects/aca-workflow/notes/Schubert-Polynomials/schubert-positivity-notes.pdf" "/Users/yueyh/Projects/aca-workflow/notes/Schubert-Polynomials/chapters/chapter1.tex"
```

跳转到 appendix/qa.tex 第 114 行：
```bash
/Applications/Skim.app/Contents/SharedSupport/displayline -r -g 114 "/Users/yueyh/Projects/aca-workflow/notes/Schubert-Polynomials/schubert-positivity-notes.pdf" "/Users/yueyh/Projects/aca-workflow/notes/Schubert-Polynomials/appendix/qa.tex"
```

## 注意事项
- 使用子文件路径（如 `chapters/chapter1.tex`），不要用主文件
- 每次修改 TeX 后需要重新编译才能生成正确的 synctex
- PDF 和 TeX 文件路径必须是绝对路径
