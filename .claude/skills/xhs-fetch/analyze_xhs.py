#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书内容分析器 - 使用 Gemini 2.5 Flash Lite
分析每个文件夹的内容：文案、评论、视频/图片信息
"""

import os
import json
from pathlib import Path
from google import genai

# 配置 API
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

XHS_DIR = Path.home() / "tmp" / "xhs"
ANALYSIS_PROMPT = """你是一个社交媒体内容分析师。请分析以下小红书内容并给出深度分析：

## 分析要求：
1. **内容总结** - 用100字以内总结内容主旨
2. **情感分析** - 分析评论区的整体情绪倾向（正面/负面/中性）
3. **热门观点** - 提取评论区最有价值的3条观点
4. **话题标签** - 生成3-5个标签
5. **亮点评论** - 找出点赞最高的3条评论

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

【高赞评论】
1. xxx (xxx赞)
2. xxx (xxx赞)
3. xxx (xxx赞)
===

## 内容如下：
"""


def analyze_content(folder_path: Path) -> str:
    """分析单个文件夹的内容"""
    info_file = folder_path / "info.txt"

    if not info_file.exists():
        return "❌ 找不到 info.txt"

    # 读取内容
    content = info_file.read_text(encoding="utf-8")

    # 调用 Gemini 分析
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=ANALYSIS_PROMPT + content
        )
        return response.text
    except Exception as e:
        return f"❌ 分析失败: {e}"


def main():
    print("=" * 50)
    print("小红书内容分析器 - Gemini 2.5 Flash Lite")
    print("=" * 50)

    # 获取所有文件夹
    folders = sorted([f for f in XHS_DIR.iterdir() if f.is_dir()])

    print(f"\n找到 {len(folders)} 个文件夹，开始分析...\n")

    results = []

    for i, folder in enumerate(folders, 1):
        print(f"[{i}/{len(folders)}] 分析: {folder.name[:30]}...")

        analysis = analyze_content(folder)
        results.append({
            "folder": folder.name,
            "analysis": analysis
        })

        # 保存分析结果到文件夹
        analysis_file = folder / "analysis.txt"
        analysis_file.write_text(analysis, encoding="utf-8")
        print(f"  ✓ 已保存: analysis.txt")

    # 保存汇总报告
    summary_file = XHS_DIR / "analysis_summary.txt"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("小红书内容分析汇总\n")
        f.write("=" * 60 + "\n\n")

        for result in results:
            f.write(f"【{result['folder']}】\n")
            f.write(result['analysis'])
            f.write("\n" + "-" * 40 + "\n\n")

    print(f"\n✓ 汇总报告已保存: {summary_file}")
    print(f"✓ 共分析 {len(folders)} 个内容")


if __name__ == "__main__":
    main()
