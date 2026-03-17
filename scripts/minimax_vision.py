#!/usr/bin/env python3
"""
MiniMax Vision (abab6.5s-chat) 图像理解测试脚本
"""

import base64
import requests
import json
import os
import sys

# 配置
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY", "sk-cp-nJf8IXFX97qoThaDvx_ctJJ0RDqCoOEXsCp3YjVPRRsDfSgoEDsfkUADKgc1FseXHTeyOBJz6noHdJGGDpwCHlwNeh2wQuyu7A2AUFa6ccIlje1Jif1k69Y")
MINIMAX_GROUP_ID = "2027069428285313025"

def encode_image_to_base64(image_path):
    """将图片转换为base64编码"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def call_minimax_vision(image_path, prompt="请描述这张图片的内容"):
    """调用 MiniMax abab6.5s-chat vision 模型"""
    url = f"https://api.minimax.chat/v1/text/chatcompletion_v2?GroupId={MINIMAX_GROUP_ID}"

    # 编码图片
    image_base64 = encode_image_to_base64(image_path)

    headers = {
        "Authorization": f"Bearer {MINIMAX_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "abab6.5s-chat",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def main():
    if len(sys.argv) < 2:
        print("用法: python minimax_vision.py <图片路径> [问题]")
        print("示例: python minimax_vision.py test.png '这张图片里有什么？'")
        sys.exit(1)

    image_path = sys.argv[1]
    prompt = sys.argv[2] if len(sys.argv) > 2 else "请详细描述这张图片的内容"

    if not os.path.exists(image_path):
        print(f"错误: 图片文件不存在: {image_path}")
        sys.exit(1)

    print(f"正在分析图片: {image_path}")
    print(f"问题: {prompt}")
    print("-" * 50)

    try:
        result = call_minimax_vision(image_path, prompt)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"调用失败: {e}")

if __name__ == "__main__":
    main()
