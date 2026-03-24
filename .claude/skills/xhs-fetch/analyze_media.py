#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书内容分析器 - Gemini 2.5 Flash
支持：图文发送图片+文案，视频发送视频+文案
"""

import os
import json
import base64
import subprocess
import requests
from pathlib import Path

# 配置
API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
XHS_DIR = Path.home() / "tmp" / "xhs"

PROMPT = """你是一名小红书内容分析专家。根据以下内容进行分析：

## 分析要求：
1. 内容总结（200字内）
2. 内容结构拆解：开头钩子、信息块章节、结尾设计
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
"""


def get_info_content(folder_path: Path) -> str:
    """获取 info.txt 内容"""
    info_file = folder_path / "info.txt"
    if info_file.exists():
        return info_file.read_text(encoding="utf-8")
    return ""


def extract_video_frame(video_path: Path) -> Path:
    """用 ffmpeg 提取视频第一帧"""
    frame_path = Path("/tmp/video_frame.jpg")
    subprocess.run(
        ["ffmpeg", "-i", str(video_path), "-vframes", "1", "-q:v", "2", str(frame_path), "-y"],
        capture_output=True, timeout=30
    )
    return frame_path


def call_gemini(text: str, media_path: Path = None, mime_type: str = None) -> str:
    """调用 Gemini API"""
    parts = [{"text": PROMPT + text}]

    if media_path and media_path.exists():
        # 读取媒体文件并 base64 编码
        with open(media_path, 'rb') as f:
            b64_data = base64.b64encode(f.read()).decode('utf-8')
        parts.append({
            "inline_data": {
                "mime_type": mime_type,
                "data": b64_data
            }
        })

    payload = {
        "contents": [{
            "role": "user",
            "parts": parts
        }]
    }

    response = requests.post(
        f"{GEMINI_API_URL}?key={API_KEY}",
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=120
    )

    if response.status_code != 200:
        return f"❌ API 错误: {response.text[:200]}"

    data = response.json()
    if 'candidates' in data:
        return data['candidates'][0]['content']['parts'][0]['text']
    return f"❌ 解析错误: {data}"


def analyze_image_post(folder_path: Path) -> str:
    """分析图文笔记 - 发送所有图片"""
    # 获取所有图片
    image_files = sorted(folder_path.glob("image_*.webp")) + \
                  sorted(folder_path.glob("image_*.jpg")) + \
                  sorted(folder_path.glob("image_*.png"))

    if not image_files:
        return "❌ 找不到图片文件"

    text = get_info_content(folder_path)

    # 发送所有图片（每张单独调用，然后合并结果）
    results = []
    for i, img in enumerate(image_files, 1):
        print(f"    发送图片 {i}/{len(image_files)}: {img.name}")
        result = call_gemini(text, img, "image/webp")
        results.append(result)

    # 返回第一个成功的结果
    for r in results:
        if r and not r.startswith("❌"):
            return r

    return results[0] if results else "❌ 所有图片发送失败"


def analyze_video_post(folder_path: Path) -> str:
    """分析视频笔记"""
    video_file = folder_path / "video.mp4"

    if not video_file.exists():
        return "❌ 找不到视频文件"

    # 检查视频大小
    size_mb = video_file.stat().st_size / (1024 * 1024)
    print(f"    视频大小: {size_mb:.1f} MB")

    # 尝试发送完整视频
    print(f"    发送完整视频")
    text = get_info_content(folder_path)
    result = call_gemini(text, video_file, "video/mp4")

    # 如果失败且视频太大，尝试提取第一帧
    if "error" in result.lower() and size_mb > 20:
        print("    视频发送失败，提取第一帧重试...")
        frame_file = extract_video_frame(video_file)
        if frame_file.exists():
            print(f"    发送视频第一帧")
            return call_gemini(text, frame_file, "image/jpeg")

    return result


def main():
    print("=" * 60)
    print("小红书内容分析器 - Gemini 2.5 Flash")
    print("=" * 60)

    # 测试用例
    test_cases = [
        ("图文", "01_上班ing💼都开始养小龙虾了吗"),
        ("图文", "02_DeerMeet 约饭APP，不被定义目的的社交"),
        ("视频", "01_欧洲职场的coffee chat，到底在聊什么？"),
        ("视频", "01_我妈眼中的博士后女儿与她的论文"),
    ]

    for content_type, folder_name in test_cases:
        folder_path = XHS_DIR / folder_name
        if not folder_path.exists():
            print(f"\n[{content_type}] {folder_name}: ❌ 文件夹不存在")
            continue

        print(f"\n[{content_type}] 分析: {folder_name}")

        if content_type == "图文":
            result = analyze_image_post(folder_path)
        else:
            result = analyze_video_post(folder_path)

        # 保存结果
        analysis_file = folder_path / "analysis_v2.txt"
        analysis_file.write_text(result, encoding="utf-8")
        print(f"    ✓ 已保存")
        print(f"    结果: {result[:200]}...")


if __name__ == "__main__":
    main()
