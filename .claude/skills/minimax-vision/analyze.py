#!/usr/bin/env python3
"""
MiniMax Vision - 图像理解分析工具
调用 MiniMax abab6.5s-chat 模型分析图片
支持本地文件、网络URL
"""

import base64
import json
import os
import sys
import tempfile
import requests
from urllib.parse import urlparse

# MiniMax API 配置
API_KEY = "sk-cp-nJf8IXFX97qoThaDvx_ctJJ0RDqCoOEXsCp3YjVPRRsDfSgoEDsfkUADKgc1FseXHTeyOBJz6noHdJGGDpwCHlwNeh2wQuyu7A2AUFa6ccIlje1Jif1k69Y"
API_URL = "https://api.minimaxi.com/v1/chat/completions"
MODEL = "abab6.5s-chat"


def is_url(path: str) -> bool:
    """判断是否是 URL"""
    return path.startswith("http://") or path.startswith("https://")


def download_image(url: str) -> str:
    """下载网络图片到临时文件"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # 获取文件扩展名
        content_type = response.headers.get("Content-Type", "")
        ext_map = {
            "image/png": ".png",
            "image/jpeg": ".jpg",
            "image/gif": ".gif",
            "image/webp": ".webp"
        }
        ext = ext_map.get(content_type, ".png")

        # 创建临时文件
        fd, temp_path = tempfile.mkstemp(suffix=ext, prefix="minimax_vision_")
        os.write(fd, response.content)
        os.close(fd)

        return temp_path
    except Exception as e:
        raise Exception(f"下载图片失败: {e}")


def encode_image(image_path: str) -> str:
    """将图片转换为 base64 编码"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_image(image_path: str, question: str = "请详细描述这张图片的内容") -> tuple:
    """
    调用 MiniMax API 分析图片

    Args:
        image_path: 图片路径或 URL
        question: 要问的问题

    Returns:
        (内容, 使用量) 元组
    """
    temp_file = None

    try:
        # 判断图片来源
        if is_url(image_path):
            print(f"🌐 检测到网络图片，正在下载...")
            temp_file = download_image(image_path)
            image_path = temp_file

        # 检查文件是否存在
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图片文件不存在: {image_path}")

        # 获取图片扩展名
        ext = os.path.splitext(image_path)[1].lower()
        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".webp": "image/webp",
            ".svg": "image/svg+xml"
        }
        mime_type = mime_types.get(ext, "image/png")

        # 转换为 base64
        image_base64 = encode_image(image_path)
        data_url = f"data:{mime_type};base64,{image_base64}"

        # 构建请求
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {"type": "image_url", "image_url": {"url": data_url}}
                ]
            }
        ]

        payload = {
            "model": MODEL,
            "messages": messages,
            "max_tokens": 2000
        }

        # 发送请求
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=120
        )

        if response.status_code != 200:
            error = response.json().get("error", {})
            raise Exception(f"API 错误: {error.get('message', '未知错误')}")

        result = response.json()
        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        # 返回使用量和内容
        usage = result.get("usage", {})
        return content, usage

    finally:
        # 清理临时文件
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)


def main():
    if len(sys.argv) < 2:
        print("用法: python3 analyze.py <图片路径或URL> [问题]")
        print()
        print("示例:")
        print("  python3 analyze.py /path/to/image.png")
        print("  python3 analyze.py /path/to/image.png '这张图片有什么特别之处？'")
        print("  python3 analyze.py 'https://example.com/image.png'")
        sys.exit(1)

    image_path = sys.argv[1]
    question = sys.argv[2] if len(sys.argv) > 2 else "请详细描述这张图片的内容"

    print(f"📷 图片: {image_path}")
    print(f"❓ 问题: {question}")
    print("⏳ 正在调用 MiniMax abab6.5s-chat 模型分析...\n")

    try:
        content, usage = analyze_image(image_path, question)

        print("=" * 50)
        print("📝 分析结果:")
        print("=" * 50)
        print(content)
        print()
        print("=" * 50)
        print(f"📊 Token 使用情况:")
        print(f"   输入: {usage.get('prompt_tokens', 'N/A')}")
        print(f"   输出: {usage.get('completion_tokens', 'N/A')}")
        print(f"   总计: {usage.get('total_tokens', 'N/A')}")

    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
