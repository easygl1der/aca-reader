#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube 视频转录脚本
- 下载视频/字幕
- 检测字幕：有字幕直接用，无字幕用 AssemblyAI 转录
- 生成字幕书面稿 + 结构化总结
- 输出到 Obsidian
"""

import os
import re
import json
import subprocess
import requests
import shutil
import time
from pathlib import Path
from datetime import datetime

# ========== 配置 ==========
API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
MINIMAX_API_URL = "https://api.minimaxi.com/anthropic/v1/chat/completions"
MINIMAX_TOKEN = os.environ.get("ANTHROPIC_AUTH_TOKEN")
ASSEMBLYAI_TOKEN = os.environ.get("ASSEMBLYAI_API_KEY")

YOUTUBE_DIR = Path("/tmp/youtube")
OBSIDIAN_DIR = Path.home() / "Library" / "Mobile Documents" / "iCloud~md~obsidian" / "Documents" / "2026-spring" / "YouTube"
OUTPUT_SUMMARY = OBSIDIAN_DIR / "youtube_summaries.md"
OUTPUT_TRANSCRIPT = OBSIDIAN_DIR / "youtube_transcripts.md"

# 确保目录存在
OBSIDIAN_DIR.mkdir(parents=True, exist_ok=True)
YOUTUBE_DIR.mkdir(parents=True, exist_ok=True)

# 提示词
PROMPT_FORMAT_TRANSCRIPT = """你是一个专业的文字整理专家。请将以下语音转录文本整理成带标点符号、分段清晰的书面文字稿。

要求：
1. 添加合适的标点符号（逗号、句号、顿号、引号等）
2. 根据语义合理分段
3. 保持原文意思不变
4. 适当补充人名、地名等专有名词的正确写法
5. 输出格式：只有整理后的文字稿，不要有其他说明"""

PROMPT_SUMMARY = """你是一个专业的视频内容分析专家。根据提供的字幕文本，生成详细的结构化总结。

输出格式要求：
1. 视频信息：一句话总结
2. 核心要点：干货盘点 + 对比分析
3. 主题提炼
4. 时间线摘要

语言：中文
格式：Markdown"""


def run_cmd(cmd: list, timeout: int = 300, stderr_ok: bool = False) -> str:
    """运行命令"""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        output = result.stdout
        # 如果没有 stdout 但允许 stderr，则使用 stderr
        if not output.strip() and stderr_ok:
            output = result.stderr
        return output
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        return str(e)


def get_video_id(url: str) -> str:
    """提取 YouTube 视频 ID"""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
        r'([a-zA-Z0-9_-]{11})$'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_video_info(video_id: str) -> dict:
    """获取视频信息"""
    print(f"    获取视频信息...")

    # 获取标题
    title_cmd = ["yt-dlp", "--print", "%(title)s", f"https://www.youtube.com/watch?v={video_id}"]
    title = run_cmd(title_cmd).strip() or "YouTube Video"

    # 获取频道名
    channel_cmd = ["yt-dlp", "--print", "%(channel)s", f"https://www.youtube.com/watch?v={video_id}"]
    channel = run_cmd(channel_cmd).strip() or "Unknown"

    # 获取时长
    duration_cmd = ["yt-dlp", "--print", "%(duration)s", f"https://www.youtube.com/watch?v={video_id}"]
    duration_str = run_cmd(duration_cmd).strip()
    duration = int(duration_str) if duration_str.isdigit() else 0
    duration_formatted = f"{duration // 60}:{duration % 60:02d}" if duration else "N/A"

    return {
        "title": title,
        "channel": channel,
        "duration": duration_formatted,
        "video_id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}"
    }


def list_subtitles(video_id: str) -> dict:
    """列出可用字幕"""
    cmd = ["yt-dlp", "--list-subs", f"https://www.youtube.com/watch?v={video_id}"]
    output = run_cmd(cmd)

    has_manual = "Language:" in output and "subtitles" in output.lower()
    has_auto = "automatic" in output.lower()

    return {"manual": has_manual, "auto": has_auto, "raw": output}


def download_subtitle(video_id: str, output_name: str) -> str:
    """下载字幕文件路径"""
    # 先尝试人工字幕
    cmd = [
        "yt-dlp", "--write-sub", "--skip-download",
        "--output", output_name,
        f"https://www.youtube.com/watch?v={video_id}"
    ]
    run_cmd(cmd)

    # 检查是否有 vtt 文件
    vtt_files = list(Path(".").glob(f"{output_name}*.vtt"))
    if vtt_files:
        return str(vtt_files[0])

    # 尝试自动字幕
    cmd = [
        "yt-dlp", "--write-auto-sub", "--skip-download",
        "--output", output_name,
        f"https://www.youtube.com/watch?v={video_id}"
    ]
    run_cmd(cmd)

    vtt_files = list(Path(".").glob(f"{output_name}*.vtt"))
    if vtt_files:
        return str(vtt_files[0])

    return None


def parse_vtt(vtt_path: str) -> str:
    """解析 VTT 文件为纯文本"""
    try:
        with open(vtt_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        text_lines = []
        for line in lines:
            line = line.strip()
            # 跳过 VTT 标记、时间戳、空行
            if not line:
                continue
            if line.startswith("WEBVTT"):
                continue
            if "-->" in line:
                continue
            if line.startswith("Kind:") or line.startswith("Language:"):
                continue
            # 清理 HTML 标签
            line = re.sub(r'<[^>]+>', '', line)
            line = line.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
            if line:
                text_lines.append(line)

        # 去重
        seen = set()
        unique_lines = []
        for line in text_lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)

        return "\n".join(unique_lines)
    except Exception as e:
        print(f"    解析 VTT 失败: {e}")
        return None


def download_video(video_id: str) -> str:
    """下载视频并提取音频"""
    video_dir = YOUTUBE_DIR / video_id
    video_dir.mkdir(parents=True, exist_ok=True)

    video_path = video_dir / "video.mp4"

    if video_path.exists():
        print(f"    视频已存在，跳过下载")
        return str(video_path)

    print(f"    下载视频 (480P)...")

    # 下载视频
    cmd = [
        "yt-dlp",
        "-f", "bv[height<=480][ext=mp4]/best[height<=480]",
        "--merge-output-format", "mp4",
        "-o", str(video_path),
        f"https://www.youtube.com/watch?v={video_id}"
    ]

    result = run_cmd(cmd, timeout=600)

    if not video_path.exists():
        print(f"    下载失败: {result}")
        return None

    print(f"    视频下载完成")

    # 提取音频
    audio_path = video_dir / "audio.mp3"

    print(f"    提取音频...")

    cmd = [
        "ffmpeg", "-i", str(video_path),
        "-vn", "-acodec", "libmp3lame", "-q:a", "2",
        str(audio_path)
    ]

    run_cmd(cmd, timeout=120)

    if audio_path.exists():
        size_mb = audio_path.stat().st_size / 1024 / 1024
        print(f"    音频提取完成: {size_mb:.1f} MB")
        return str(audio_path)

    return None


def assemblyai_transcribe(audio_path: str, language: str = "en") -> str:
    """使用 AssemblyAI 转录音频"""
    print(f"    AssemblyAI 转录中...")

    try:
        with open(audio_path, 'rb') as f:
            audio_data = f.read()

        # 1. 上传音频
        upload_resp = requests.post(
            "https://api.assemblyai.com/v2/upload",
            headers={"authorization": ASSEMBLYAI_TOKEN},
            data=audio_data
        )

        if upload_resp.status_code != 200:
            print(f"    上传失败: {upload_resp.status_code}")
            return None

        audio_url = upload_resp.json()["upload_url"]

        # 2. 请求转录
        transcript_resp = requests.post(
            "https://api.assemblyai.com/v2/transcript",
            headers={
                "authorization": ASSEMBLYAI_TOKEN,
                "content-type": "application/json"
            },
            json={
                "audio_url": audio_url,
                "language_code": language,
                "speech_models": ["universal-2"],
                "punctuate": True,
                "format_text": True,
            }
        )

        if transcript_resp.status_code != 200:
            print(f"    请求转录失败: {transcript_resp.status_code}")
            return None

        transcript_id = transcript_resp.json()["id"]

        # 3. 轮询等待结果
        while True:
            result_resp = requests.get(
                f"https://api.assemblyai.com/v2/transcript/{transcript_id}",
                headers={"authorization": ASSEMBLYAI_TOKEN}
            )
            status = result_resp.json()["status"]

            if status == "completed":
                text = result_resp.json()["text"]
                print(f"    转录完成: {len(text)} 字符")
                return text
            elif status == "error":
                print(f"    转录错误: {result_resp.json()}")
                return None

            time.sleep(3)

    except Exception as e:
        print(f"    AssemblyAI 转录异常: {e}")
        return None


def minimax_format_transcript(raw_text: str) -> str:
    """使用 MiniMax 整理字幕格式"""
    print(f"    MiniMax 整理字幕格式...")

    try:
        base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.minimaxi.com/anthropic")
        api_url = f"{base_url}/v1/messages"
        token = os.environ.get("ANTHROPIC_AUTH_TOKEN")

        resp = requests.post(
            api_url,
            json={
                "model": "MiniMax-M2.5",
                "max_tokens": 4096,
                "system": PROMPT_FORMAT_TRANSCRIPT,
                "messages": [
                    {"role": "user", "content": f"请整理以下转录文本：\n\n{raw_text}"}
                ]
            },
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            timeout=180
        )

        if resp.status_code == 200:
            data = resp.json()
            content = data.get("content", [])
            if content and isinstance(content, list):
                # MiniMax 返回格式: [{"thinking": "...", "type": "text", "text": "..."}]
                result = ""
                for item in content:
                    if isinstance(item, dict):
                        # 优先取 text
                        text = item.get("text", "")
                        if text:
                            # 检查是否像思考过程（而非实际输出）
                            if any(phrase in text for phrase in ["让我来", "我需要", "用户要求", "这段", "这段文本"]):
                                continue
                            result = text
                            break
                        # 其次取 thinking
                        thinking = item.get("thinking", "")
                        if thinking:
                            result = thinking

                # 如果结果像思考过程，使用原始文本
                if result and any(phrase in result for phrase in ["让我来", "我需要", "用户要求", "这段文本", "这段转录"]):
                    print(f"    返回内容为思考过程，使用原始字幕")
                    return raw_text

                if result and len(result) > 50:
                    return result

        print(f"    MiniMax 整理失败或返回内容过短")
        return raw_text

    except Exception as e:
        print(f"    MiniMax 异常: {e}")
        return raw_text


def minimax_summary(transcript: str, video_info: dict) -> str:
    """使用 MiniMax 生成结构化总结"""
    print(f"    MiniMax 生成总结...")

    try:
        base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.minimaxi.com/anthropic")
        api_url = f"{base_url}/v1/messages"
        token = os.environ.get("ANTHROPIC_AUTH_TOKEN")

        user_prompt = f"""请分析以下视频字幕，生成详细总结：

视频标题：{video_info['title']}
频道：{video_info['channel']}
时长：{video_info['duration']}
YouTube：{video_info['url']}

字幕内容：
{transcript[:8000]}

请按照上述格式输出。"""

        resp = requests.post(
            api_url,
            json={
                "model": "MiniMax-M2.5",
                "max_tokens": 4096,
                "system": PROMPT_SUMMARY,
                "messages": [
                    {"role": "user", "content": user_prompt}
                ]
            },
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            timeout=180
        )

        if resp.status_code == 200:
            data = resp.json()
            content = data.get("content", [])
            if content and isinstance(content, list):
                # MiniMax 返回格式: [{"thinking": "...", "type": "text", "text": "..."}]
                result = ""
                for item in content:
                    if isinstance(item, dict):
                        text = item.get("text", "")
                        if text:
                            # 检查是否像思考过程
                            if any(phrase in text for phrase in ["让我分析", "我需要", "用户要求", "现在我需要", "按照要求"]):
                                continue
                            result = text
                            break
                        thinking = item.get("thinking", "")
                        if thinking:
                            result = thinking

                # 如果结果像思考过程，返回简短提示
                if result and any(phrase in result for phrase in ["让我分析", "我需要", "用户要求", "现在我需要", "按照要求"]):
                    print(f"    返回内容为思考过程")
                    return "（视频内容较短，请查看字幕书面稿获取完整内容）"

                if result and len(result) > 50:
                    return result

        print(f"    MiniMax 总结失败")
        return None

    except Exception as e:
        print(f"    MiniMax 异常: {e}")
        return None


def read_existing_content(file_path: Path) -> str:
    """读取现有文件内容"""
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


def extract_titles(content: str) -> list:
    """提取现有文件中的标题列表"""
    titles = []
    # 匹配 ## 标题 或 ### 标题 格式
    pattern = r'^#{1,3}\s+(.+?)(?:\n|$)'
    for match in re.finditer(pattern, content, re.MULTILINE):
        title = match.group(1).strip()
        if title and not title.startswith("目录"):
            titles.append(title)
    return titles


def update_toc(file_path: Path, new_title: str):
    """更新目录"""
    content = read_existing_content(file_path)

    # 提取现有标题
    existing_titles = extract_titles(content)

    # 如果已存在，跳过
    if new_title in existing_titles:
        return False

    # 插入目录后面或文件开头
    lines = content.split("\n")

    # 查找目录位置
    toc_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("## 目录") or line.strip().startswith("# 目录"):
            toc_idx = i
            break

    # 构建新目录项
    toc_entry = f"- [[#{new_title}|{new_title}]]"

    if toc_idx >= 0:
        # 找到目录，添加到目录后面
        insert_idx = toc_idx + 1
        while insert_idx < len(lines) and (lines[insert_idx].strip().startswith("- ") or not lines[insert_idx].strip()):
            insert_idx += 1
        lines.insert(insert_idx, toc_entry)
    else:
        # 没有目录，在文件开头添加
        lines.insert(0, "")
        lines.insert(0, "## 目录")
        lines.insert(1, toc_entry)

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))

    return True


def write_summary(video_info: dict, summary: str):
    """写入结构化总结"""
    title = video_info['title']

    # 读取现有内容
    content = read_existing_content(OUTPUT_SUMMARY)

    # 检查是否已存在
    if f"## {title}" in content or f"### {title}" in content:
        print(f"    总结已存在，跳过")
        return

    # 追加新内容
    new_content = f"""

## {title}

### 视频信息
- **来源**: YouTube
- **标题**: {title}
- **频道**: {video_info['channel']}
- **时长**: {video_info['duration']}
- **链接**: {video_info['url']}

### 一句话总结

{summary}

---

*生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""

    with open(OUTPUT_SUMMARY, 'a', encoding='utf-8') as f:
        f.write(new_content)

    # 更新目录
    update_toc(OUTPUT_SUMMARY, title)

    print(f"    已写入: {OUTPUT_SUMMARY.name}")


def write_transcript(video_info: dict, transcript: str, method: str = "YouTube"):
    """写入字幕书面稿"""
    title = video_info['title']

    # 读取现有内容
    content = read_existing_content(OUTPUT_TRANSCRIPT)

    # 检查是否已存在
    if f"## {title} - 字幕书面稿" in content:
        print(f"    字幕稿已存在，跳过")
        return

    # 追加新内容
    new_content = f"""

## {title} - 字幕书面稿

### 视频信息
- **来源**: YouTube
- **标题**: {title}
- **频道**: {video_info['channel']}
- **链接**: {video_info['url']}

---

### 字幕书面稿

{transcript}

---

*转录方式: {method} | 生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""

    with open(OUTPUT_TRANSCRIPT, 'a', encoding='utf-8') as f:
        f.write(new_content)

    # 更新目录
    update_toc(OUTPUT_TRANSCRIPT, f"{title} - 字幕书面稿")

    print(f"    已写入: {OUTPUT_TRANSCRIPT.name}")


def cleanup(video_id: str):
    """清理临时文件"""
    video_dir = YOUTUBE_DIR / video_id
    if video_dir.exists():
        shutil.rmtree(video_dir)
        print(f"    已清理临时文件")


def process_youtube_video(url: str, force_assemblyai: bool = False):
    """处理 YouTube 视频"""
    print(f"\n{'='*50}")
    print(f"处理: {url}")
    print(f"{'='*50}")

    # 1. 提取视频 ID
    video_id = get_video_id(url)
    if not video_id:
        print("    无法提取视频 ID")
        return False

    print(f"    视频 ID: {video_id}")

    # 2. 获取视频信息
    video_info = get_video_info(video_id)
    print(f"    标题: {video_info['title']}")
    print(f"    频道: {video_info['channel']}")

    # 3. 检测字幕
    print(f"\n[2/5] 检测字幕...")
    subtitles = list_subtitles(video_id)

    raw_transcript = None
    transcript_method = None

    if subtitles["manual"] or subtitles["auto"]:
        # 有字幕，下载并解析
        print(f"    检测到可用字幕，下载中...")
        output_name = f"youtube_sub_{video_id}"
        vtt_path = download_subtitle(video_id, output_name)

        if vtt_path:
            raw_transcript = parse_vtt(vtt_path)
            if raw_transcript:
                print(f"    字幕获取成功: {len(raw_transcript)} 字符")
                transcript_method = "YouTube 字幕"
            # 清理 vtt 文件
            try:
                Path(vtt_path).unlink()
            except:
                pass
    else:
        print(f"    无可用字幕")

    # 4. 如果没有字幕，使用 AssemblyAI
    if not raw_transcript or force_assemblyai:
        print(f"\n[3/5] AssemblyAI 转录...")

        # 下载视频并提取音频
        audio_path = download_video(video_id)
        if not audio_path:
            print(f"    无法下载视频")
            return False

        # AssemblyAI 转录
        raw_transcript = assemblyai_transcribe(audio_path)
        if not raw_transcript:
            print(f"    AssemblyAI 转录失败")
            cleanup(video_id)
            return False

        transcript_method = "AssemblyAI"

        # 清理临时文件
        cleanup(video_id)

    # 5. 整理字幕格式
    print(f"\n[4/5] 整理字幕格式...")
    formatted_transcript = minimax_format_transcript(raw_transcript)

    # 6. 生成结构化总结
    print(f"\n[5/5] 生成总结...")
    summary = minimax_summary(formatted_transcript, video_info)

    # 7. 写入文件
    print(f"\n[6/6] 写入 Obsidian...")

    # 写入字幕书面稿
    write_transcript(video_info, formatted_transcript, transcript_method or "YouTube")

    # 写入结构化总结
    if summary:
        write_summary(video_info, summary)

    print(f"\n    完成!")
    return True


def main():
    """主函数"""
    import sys

    if len(sys.argv) < 2:
        print("用法: python youtube_summary.py <YouTube_URL>")
        print("示例: python youtube_summary.py https://www.youtube.com/watch?v=xxx")
        sys.exit(1)

    url = sys.argv[1]

    # 支持 YouTube 链接格式
    # https://www.youtube.com/watch?v=xxx
    # https://youtu.be/xxx
    # xxx (直接给视频 ID)

    # 如果没有 scheme，添加
    if not url.startswith("http"):
        url = f"https://www.youtube.com/watch?v={url}"

    success = process_youtube_video(url)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
