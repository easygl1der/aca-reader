#!/bin/bash
# 编译 LaTeX 文档（使用 BibTeX）

FILE="schubert-positivity-notes"

echo "=== 第一次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 运行 BibTeX ==="
bibtex ${FILE}.aux

echo "=== 第二次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 第三次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 编译完成 ==="
ls -la ${FILE}.pdf
