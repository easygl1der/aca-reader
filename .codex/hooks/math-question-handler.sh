#!/bin/bash
# math-question-handler.sh - 处理数学问题的 hook
# 当用户询问数学问题时，自动使用 gemini-browser-chat 并调研笔记上下文

# 检查是否是数学问题（包含数学关键词）
TEXT="$1"

if echo "$TEXT" | grep -E "(计算|证明|为什么|是什么|如何|例题|定理|命题|引理|展开|系数)" > /dev/null 2>&1; then
    echo "检测到数学问题，建议使用 /gemini-browser-chat 进行深入研究"
    echo "相关上下文："
    echo "  - 当前章节：chapters/chapter1.tex (Graham Positivity)"
    echo "  - 关键定义：FlagVariety, SymmetricGroup, DividedDifference"
    echo "  - 关键定理：GrahamPositivity, Samuel, Kirillov"
    echo "  - QA 记录：appendix/qa.tex"
    exit 0
fi

exit 0
