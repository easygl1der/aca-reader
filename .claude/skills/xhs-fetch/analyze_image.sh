#!/bin/bash
# 分析小红书图文内容 - 使用 Gemini 2.5 Flash API
# 用法:
#   ./analyze_image.sh <图片文件> <文案文件> [输出文件]
#   ./analyze_image.sh <文件夹> <文案文件> [输出文件]   # 自动分析文件夹中所有图片

set -e

INPUT_PATH="$1"
TEXT_FILE="$2"
OUTPUT_FILE="$3"

if [ -z "$INPUT_PATH" ] || [ -z "$TEXT_FILE" ]; then
    echo "用法: $0 <图片或文件夹> <文案文件> [输出文件]"
    echo "示例: $0 ~/tmp/xhs/01_笔记/image_01.webp ~/tmp/xhs/01_笔记/info.txt"
    echo "       $0 ~/tmp/xhs/01_笔记/ ~/tmp/xhs/01_笔记/info.txt"
    exit 1
fi

if [ ! -f "$TEXT_FILE" ]; then
    echo "错误: 文案文件不存在: $TEXT_FILE"
    exit 1
fi

# 读取文案内容
TEXT_CONTENT=$(cat "$TEXT_FILE")

# API 配置
API_KEY="${GEMINI_API_KEY}"
MODEL="gemini-2.5-flash"
API_URL="https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent"

# 构建 prompt
PROMPT="你是一名小红书内容分析专家。根据以下内容进行分析：

## 分析要求：
1. 内容总结（200字内）
2. 内容结构拆解：开头钩子，信息块章节、结尾设计
3. 评论区洞察：高频观点、典型支持/质疑点
4. 给创作者的优化建议
5. 话题标签（3-5个）

## 输出格式：
===
【内容总结】
xxx

【内容结构】
- 开头钩子：xxx
- 信息块：xxx
- 结尾设计：xxx

【评论区洞察】
- 高频观点：xxx
- 典型观点：xxx

【优化建议】
xxx

【话题标签】
#标签1 #标签2 #标签3
===

## 内容如下：
$TEXT_CONTENT"

# 判断是文件还是文件夹
declare -a IMAGE_FILES

if [ -f "$INPUT_PATH" ]; then
    # 单个文件
    IMAGE_FILES=("$INPUT_PATH")
elif [ -d "$INPUT_PATH" ]; then
    # 文件夹 - 查找所有图片
    for f in "$INPUT_PATH"/*; do
        if [[ "$f" == *.webp ]] || [[ "$f" == *.jpg ]] || [[ "$f" == *.jpeg ]] || [[ "$f" == *.png ]]; then
            IMAGE_FILES+=("$f")
        fi
    done
else
    echo "错误: 输入路径不存在: $INPUT_PATH"
    exit 1
fi

if [ ${#IMAGE_FILES[@]} -eq 0 ]; then
    echo "错误: 未找到图片文件"
    exit 1
fi

echo "找到 ${#IMAGE_FILES[@]} 张图片，准备分析..."

# 逐张发送图片，收集结果
declare -a RESULTS
SUCCESS_COUNT=0

for img in "${IMAGE_FILES[@]}"; do
    echo "分析: $(basename "$img")"
    IMAGE_B64=$(base64 -i "$img" | tr -d '\n')

    # 检测 MIME 类型
    if [[ "$img" == *.webp ]]; then
        MIME="image/webp"
    elif [[ "$img" == *.png ]]; then
        MIME="image/png"
    else
        MIME="image/jpeg"
    fi

    RESPONSE=$(curl -s -X POST \
        "${API_URL}?key=${API_KEY}" \
        -H "Content-Type: application/json" \
        -d "{
            \"contents\": [{
                \"parts\": [
                    {\"text\": \"$PROMPT\"},
                    {\"inline_data\": {
                        \"mime_type\": \"$MIME\",
                        \"data\": \"$IMAGE_B64\"
                    }}
                ]
            }]
        }")

    RESULT=$(echo "$RESPONSE" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if 'candidates' in data:
    print(data['candidates'][0]['content']['parts'][0]['text'])
else:
    print('ERROR:', data)
" 2>/dev/null)

    if [[ "$RESULT" == ERROR:* ]]; then
        echo "  ❌ 失败: $RESULT"
    else
        RESULTS+=("$RESULT")
        ((SUCCESS_COUNT++))
        echo "  ✅ 成功"
    fi
done

echo ""
echo "分析完成: $SUCCESS_COUNT/${#IMAGE_FILES[@]} 张图片成功"

# 选择第一个成功的结果
if [ $SUCCESS_COUNT -gt 0 ]; then
    FINAL_RESULT="${RESULTS[0]}"
else
    FINAL_RESULT="所有图片分析失败"
fi

# 输出结果
if [ -n "$OUTPUT_FILE" ]; then
    echo "$FINAL_RESULT" > "$OUTPUT_FILE"
    echo "结果已保存到: $OUTPUT_FILE"
else
    echo "$FINAL_RESULT"
fi
