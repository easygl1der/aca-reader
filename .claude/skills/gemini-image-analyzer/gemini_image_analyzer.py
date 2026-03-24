#!/usr/bin/env python3
"""
Gemini Image Analyzer - 用 Gemini Vision 分析图片
用法: python3 gemini_image_analyzer.py <图片路径或URL> [问题]
"""

import os
import sys
import subprocess
import tempfile
import urllib.parse

def download_image(url, output_path):
    """下载图片到本地"""
    cmd = ['curl', '-L', '-o', output_path, url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"下载失败: {result.stderr}")
    return output_path

def is_url(path):
    """判断是否为 URL"""
    return path.startswith('http://') or path.startswith('https://')

def analyze_with_gemini(image_path, question="请详细描述这张图片的所有内容"):
    """用 Gemini CLI 分析图片"""
    cmd = f'echo "{question}" | gemini "{image_path}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # 过滤掉调试信息和内部消息
    output = result.stdout + result.stderr

    # 提取实际的分析结果
    lines = output.split('\n')
    useful_lines = []
    skip = False

    skip_patterns = [
        "CRITICAL INSTRUCTION", "I will now read", "I will take a look",
        "No more thoughts", "Done.", "End of thought", "Thought process:",
        "I'll output", "I'm ready", "Go ahead"
    ]

    for line in lines:
        # 跳过一些调试信息
        if any(pattern in line for pattern in skip_patterns):
            continue
        if line.strip() == "" and len(useful_lines) > 5:
            continue
        useful_lines.append(line)

    # 重新组合输出
    clean_output = '\n'.join(useful_lines).strip()

    # 如果输出太短，可能是错误
    if len(clean_output) < 50:
        return output

    return clean_output

def main():
    if len(sys.argv) < 2:
        print("用法: python3 gemini_image_analyzer.py <图片路径或URL> [问题]")
        print("示例: python3 gemini_image_analyzer.py /path/to/image.png")
        print("示例: python3 gemini_image_analyzer.py https://example.com/image.png")
        print("示例: python3 gemini_image_analyzer.py /path/to/image.png '这张图片讲了什么？'")
        sys.exit(1)

    image_input = sys.argv[1]
    question = sys.argv[2] if len(sys.argv) > 2 else "请详细描述这张图片的所有内容"

    print(f"📷 正在分析图片...")
    print(f"📝 问题: {question}")
    print()

    try:
        # 如果是 URL，先下载
        if is_url(image_input):
            # 生成临时文件名
            parsed = urllib.parse.urlparse(image_input)
            filename = os.path.basename(parsed.path)
            if not filename or '.' not in filename:
                filename = "temp_image.png"

            temp_dir = "/Users/yueyh/.openclaw/workspace"
            image_path = os.path.join(temp_dir, filename)
            print(f"⬇️  下载图片: {image_input}")
            download_image(image_input, image_path)
        else:
            image_path = image_input
            if not os.path.exists(image_path):
                print(f"❌ 文件不存在: {image_path}")
                sys.exit(1)

        # 分析图片
        result = analyze_with_gemini(image_path, question)
        print(result)

    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
