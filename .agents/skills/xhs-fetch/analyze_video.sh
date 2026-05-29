#!/bin/bash
# 分析小红书视频内容 - 使用 Gemini 2.5 Flash API
# 用法: ./analyze_video.sh <视频路径> <文案文件路径> [输出文件路径]

set -e

VIDEO_PATH="$1"
TEXT_FILE="$2"
OUTPUT_FILE="$3"

if [ -z "$VIDEO_PATH" ] || [ -z "$TEXT_FILE" ]; then
    echo "用法: $0 <视频路径> <文案文件路径> [输出文件路径]"
    exit 1
fi

if [ ! -f "$VIDEO_PATH" ]; then
    echo "错误: 视频文件不存在: $VIDEO_PATH"
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

# 获取视频大小
VIDEO_SIZE=$(stat -f%z "$VIDEO_PATH" 2>/dev/null || stat -c%s "$VIDEO_PATH" 2>/dev/null)
VIDEO_SIZE_MB=$((VIDEO_SIZE / 1024 / 1024))

echo "视频大小: ${VIDEO_SIZE_MB}MB"

# 如果视频太大 (>20MB)，提取第一帧
if [ "$VIDEO_SIZE_MB" -gt 20 ]; then
    echo "视频较大，提取第一帧..."
    FRAME_PATH="/tmp/video_frame_$$.jpg"
    ffmpeg -i "$VIDEO_PATH" -vframes 1 -q:v 2 "$FRAME_PATH" -y 2>/dev/null
    if [ -f "$FRAME_PATH" ]; then
        VIDEO_B64=$(base64 -i "$FRAME_PATH" | tr -d '\n')
        MIME_TYPE="image/jpeg"
        rm -f "$FRAME_PATH"
    else
        echo "提取帧失败，尝试发送原视频..."
        VIDEO_B64=$(base64 -i "$VIDEO_PATH" | tr -d '\n')
        MIME_TYPE="video/mp4"
    fi
else
    VIDEO_B64=$(base64 -i "$VIDEO_PATH" | tr -d '\n')
    MIME_TYPE="video/mp4"
fi

# 调用 API
RESPONSE=$(curl -s -X POST \
    "${API_URL}?key=${API_KEY}" \
    -H "Content-Type: application/json" \
    -d "{
        \"contents\": [{
            \"parts\": [
                {\"text\": \"$PROMPT\"},
                {\"inline_data\": {
                    \"mime_type\": \"$MIME_TYPE\",
                    \"data\": \"$VIDEO_B64\"
                }}
            ]
        }]
    }")

# 解析结果
RESULT=$(echo "$RESPONSE" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if 'candidates' in data:
    print(data['candidates'][0]['content']['parts'][0]['text'])
else:
    print('错误:', data)
")

# 输出结果
if [ -n "$OUTPUT_FILE" ]; then
    echo "$RESULT" > "$OUTPUT_FILE"
    echo "结果已保存到: $OUTPUT_FILE"
else
    echo "$RESULT"
fi
