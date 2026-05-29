#!/bin/bash
# skim-jump.sh - 跳转到 PDF 对应位置
# 用法: skim-jump <line> [tex-file]
# 示例: skim-jump 890 /path/to/file.tex

LINE=$1
TEX_FILE=$2

if [ -z "$LINE" ]; then
    echo "用法: skim-jump <line> [tex-file]"
    exit 1
fi

# 查找 PDF 文件（向上搜索）
PDF_PATH=""
SEARCH_DIR=$(pwd)
while [ "$SEARCH_DIR" != "/" ]; do
    if ls "$SEARCH_DIR"/*.pdf 1> /dev/null 2>&1; then
        PDF_PATH=$(ls "$SEARCH_DIR"/*.pdf | head -1)
        break
    fi
    SEARCH_DIR=$(dirname "$SEARCH_DIR")
done

if [ -z "$PDF_PATH" ]; then
    echo "错误: 找不到 PDF 文件"
    exit 1
fi

# 构建 displayline 命令 (使用 Skim 完整路径)
SKIM_DISPLAYLINE="/Applications/Skim.app/Contents/SharedSupport/displayline"
if [ -n "$TEX_FILE" ]; then
    CMD="\"$SKIM_DISPLAYLINE\" -r -g $LINE \"$PDF_PATH\" \"$TEX_FILE\""
else
    CMD="\"$SKIM_DISPLAYLINE\" -r -g $LINE \"$PDF_PATH\""
fi

# 执行跳转
eval "$CMD"
