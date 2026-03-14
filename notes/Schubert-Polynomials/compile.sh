#!/bin/bash
# 编译 LaTeX 文档（运行三次以确保交叉引用正确）
#
# xelatex: XeLaTeX 编译器，支持 Unicode 和中文字符
# -interaction=nonstopmode: 遇到错误继续运行，不等待用户交互
# -synctex=1: 启用 SyncTeX，实现 PDF 与源码双向同步

FILE="schubert-positivity-notes"

echo "=== 第一次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 第二次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 第三次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 编译完成 ==="
ls -la ${FILE}.pdf
