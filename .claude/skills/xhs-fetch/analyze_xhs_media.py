#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书内容分析器 - 使用 Gemini API (REST)
分析每个文件夹的内容：视频/图片 + 文案 + 评论
"""

import os
import json
import requests
from pathlib import Path

# 配置
API_KEY = os.environ.get("GEMINI_API_KEY")
XHS_DIR = Path.home() / "tmp" / "xhs"

# Gemini API 端点
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent"

ANALYSIS_PROMPT = """你是一个社交媒体内容分析师。请分析以下小红书内容并给出深度分析：

## 分析要求：
1. **内容总结** - 用100字以内总结内容主旨
2. **情感分析** - 分析评论区的整体情绪倾向（正面/负面/中性）
3. **热门观点** - 提取评论区最有价值的3条观点
4. **话题标签** - 生成3-5个标签

## 输出格式：
请用中文输出，格式如下：
===
【内容总结】
xxx

【情感分析】
整体情绪：xxx
原因：xxx

【热门观点】
1. xxx
2. xxx
3. xxx

【话题标签】
#标签1 #标签2 #标签3
===

## 内容如下：
"""


def upload_file(file_path: Path, mime_type: str) -> str:
    """上传文件到 Gemini，返回 file URI"""
    print(f"    上传: {file_path.name}")

    # 使用 files.upload API
    upload_url = "https://generativelanguage.googleapis.com/upload/v1beta/files"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    with open(file_path, 'rb') as f:
        files = {'file': (file_path.name, f, mime_type)}
        response = requests.post(upload_url, headers=headers, files=files)

    if response.status_code != 200:
        print(f"    上传失败: {response.text}")
        return None

    data = response.json()
    # 返回 file URI
    return f"files/{data['file']['uri'].split('/')[-1]}"


def analyze_with_media(text_content: str, media_uris: list, mime_type: str) -> str:
    """调用 Gemini API 分析"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 构建 content
    parts = [{"text": ANALYSIS_PROMPT + text_content[:500]}]

    for uri in media_uris:
        parts.append({
            "fileData": {
                "mimeType": mime_type,
                "uri": uri
            }
        })

    payload = {
        "contents": [{
            "role": "user",
            "parts": parts
        }]
    }

    response = requests.post(
        GEMINI_API_URL,
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return f"❌ API 错误: {response.text[:200]}"

    try:
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ 解析错误: {e}\n{response.text[:200]}"


def analyze_video(folder_path: Path) -> str:
    """分析视频内容"""
    info_file = folder_path / "info.txt"
    video_file = folder_path / "video.mp4"

    if not info_file.exists():
        return "❌ 找不到 info.txt"
    if not video_file.exists():
        return "❌ 找不到 video.mp4"

    content = info_file.read_text(encoding="utf-8")

    print(f"    上传视频文件...")
    file_uri = upload_file(video_file, "video/mp4")

    if not file_uri:
        return "❌ 视频上传失败"

    return analyze_with_media(content, [file_uri], "video/mp4")


def analyze_images(folder_path: Path) -> str:
    """分析图文内容"""
    info_file = folder_path / "info.txt"

    if not info_file.exists():
        return "❌ 找不到 info.txt"

    content = info_file.read_text(encoding="utf-8")

    # 获取所有图片
    image_files = sorted(folder_path.glob("image_*.webp")) + \
                  sorted(folder_path.glob("image_*.jpg")) + \
                  sorted(folder_path.glob("image_*.png"))

    if not image_files:
        return "❌ 找不到图片文件"

    # 上传所有图片
    print(f"    上传 {len(image_files)} 张图片...")
    uploaded_uris = []
    for img in image_files:
        uri = upload_file(img, "image/webp")
        if uri:
            uploaded_uris.append(uri)

    if not uploaded_uris:
        return "❌ 图片上传失败"

    return analyze_with_media(content, uploaded_uris, "image/webp")


def main():
    print("=" * 60)
    print("小红书内容分析器 - Gemini (视频/图片分析)")
    print("=" * 60)

    # 测试用例
    test_cases = [
        ("视频", "01_我妈眼中的博士后女儿与她的论文"),
        ("视频", "01_欧洲职场的coffee chat，到底在聊什么？"),
        ("图文", "01_上班ing💼都开始养小龙虾了吗"),
        ("图文", "02_DeerMeet 约饭APP，不被定义目的的社交"),
    ]

    for content_type, folder_name in test_cases:
        folder_path = XHS_DIR / folder_name
        if not folder_path.exists():
            print(f"\n[{content_type}] {folder_name}: ❌ 文件夹不存在")
            continue

        print(f"\n[{content_type}] 分析: {folder_name}")

        if content_type == "视频":
            analysis = analyze_video(folder_path)
        else:
            analysis = analyze_images(folder_path)

        # 保存结果
        analysis_file = folder_path / "analysis_media.txt"
        analysis_file.write_text(analysis, encoding="utf-8")
        print(f"    ✓ 已保存")
        print(f"    结果: {analysis[:150]}...")


if __name__ == "__main__":
    main()
