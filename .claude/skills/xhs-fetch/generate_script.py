#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书内容 - 书面稿生成器
使用 AssemblyAI 转录 + MiniMax 整理（与 bilibili-homefeed 一致）
功能：
- 视频笔记：提取音频 → AssemblyAI 转录 → MiniMax 整理 → 书面稿
- 图文笔记：整理文案生成书面叙述
"""

import os
import sys
import subprocess
import time
import requests
from pathlib import Path
from pathlib import Path

# 配置
XHS_DIR = Path.home() / "tmp" / "xhs"
ASSEMBLYAI_TOKEN = os.environ.get("ASSEMBLYAI_API_KEY")
MINIMAX_TOKEN = os.environ.get("MINIMAX_API_KEY")  # MiniMax 专用 API Key
MINIMAX_API_URL = "https://api.minimax.chat/v1/text/chatcompletion_v2"

# MiniMax 提示词
PROMPT_MINIMAX = """你是一个专业的文字整理专家。根据提供的视频转录文本，添加合适的标点符号，并整理成阅读流畅的书面稿格式。

要求：
1. 添加合适的标点符号（，。、！？：；""）使语句完整
2. 适当分段，使内容层次清晰
3. 保留口语化表达的真实感
4. 不要添加原文没有的内容
5. 不要改变原意

直接输出整理后的文本，不要添加任何解释或前缀。"""


def extract_audio(video_path: str, output_dir: Path) -> str:
    """从视频提取音频 (mp3)"""
    audio_path = output_dir / "audio.mp3"

    # 使用 ffmpeg 提取音频
    result = subprocess.run(
        ["ffmpeg", "-i", video_path,
         "-vn", "-acodec", "libmp3lame", "-q:a", "2",
         "-y", str(audio_path)],
        capture_output=True, text=True, timeout=120
    )

    if result.returncode == 0 and audio_path.exists():
        return str(audio_path)
    else:
        print(f"  ✗ 音频提取失败: {result.stderr[:200] if result.stderr else 'unknown'}")
        return None


def assemblyai_transcribe(audio_path: str) -> str:
    """使用 AssemblyAI 转录音频"""
    if not ASSEMBLYAI_TOKEN:
        print("  ✗ 未设置 ASSEMBLYAI_API_KEY 环境变量")
        return None

    print(f"  🎙️ AssemblyAI 转录中...")

    try:
        # 1. 上传音频
        with open(audio_path, 'rb') as f:
            audio_data = f.read()

        upload_resp = requests.post(
            "https://api.assemblyai.com/v2/upload",
            headers={"authorization": ASSEMBLYAI_TOKEN},
            data=audio_data,
            timeout=60
        )

        if upload_resp.status_code != 200:
            print(f"  ✗ 音频上传失败: {upload_resp.text[:100]}")
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
                "punctuate": True,
                "speech_models": ["universal-3-pro", "universal-2"],
            },
            timeout=30
        )

        if transcript_resp.status_code != 200:
            print(f"  ✗ 转录请求失败: {transcript_resp.text[:100]}")
            return None

        transcript_id = transcript_resp.json()["id"]

        # 3. 轮询等待结果
        print(f"  ⏳ 等待转录完成...")
        max_wait = 300  # 5分钟超时
        start_time = time.time()

        while time.time() - start_time < max_wait:
            result_resp = requests.get(
                f"https://api.assemblyai.com/v2/transcript/{transcript_id}",
                headers={"authorization": ASSEMBLYAI_TOKEN}
            )

            status = result_resp.json()["status"]

            if status == "completed":
                text = result_resp.json()["text"]
                print(f"  ✓ 转录完成 ({len(text)} 字符)")
                return text
            elif status == "error":
                print(f"  ✗ 转录失败: {result_resp.json().get('error', 'unknown')}")
                return None
            else:
                time.sleep(3)

        print(f"  ✗ 转录超时")
        return None

    except Exception as e:
        print(f"  ✗ 转录异常: {e}")
        return None


def minimax_format(text: str) -> str:
    """使用 MiniMax 整理文本标点"""
    if not MINIMAX_TOKEN:
        print("  ⚠ 未设置 MINIMAX_API_KEY，使用原始转录文本")
        return text

    print(f"  ✨ MiniMax 整理标点 (M2.7)...")

    try:
        response = requests.post(
            MINIMAX_API_URL,
            headers={
                "Authorization": f"Bearer {MINIMAX_TOKEN}",
                "Content-Type": "application/json"
            },
            json={
                "model": "MiniMax-M2.7",
                "max_tokens": 4096,
                "temperature": 0.3,
                "messages": [
                    {"role": "system", "content": PROMPT_MINIMAX},
                    {"role": "user", "content": f"请整理以下转录文本：\n\n{text}"}
                ]
            },
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            # MiniMax 返回格式: result.choices[0].message.content
            formatted = result.get('choices', [{}])[0].get('message', {}).get('content', '')
            if formatted:
                print(f"  ✓ MiniMax 整理完成")
                return formatted
            else:
                print(f"  ⚠ MiniMax 返回为空: {result}")
        else:
            print(f"  ⚠ MiniMax API 错误: {response.status_code} - {response.text[:200]}")

        return text

    except Exception as e:
        print(f"  ⚠ MiniMax 异常: {e}，使用原始文本")
        return text


def transcribe_video(video_path: str) -> str:
    """完整转录流程：提取音频 → AssemblyAI 转录 → MiniMax 整理"""
    video_dir = Path(video_path).parent

    # Step 1: 提取音频
    print(f"  🎵 提取音频...")
    audio_path = extract_audio(video_path, video_dir)

    if not audio_path:
        return None

    # Step 2: AssemblyAI 转录
    raw_text = assemblyai_transcribe(audio_path)

    # 清理音频文件
    try:
        os.remove(audio_path)
    except:
        pass

    if not raw_text or len(raw_text) < 10:
        return None

    # Step 3: MiniMax 整理
    formatted_text = minimax_format(raw_text)

    return formatted_text


def generate_script_for_folder(folder_path: str) -> bool:
    """为文件夹生成书面稿"""
    folder = Path(folder_path)

    if not folder.exists():
        print(f"  ✗ 文件夹不存在: {folder_path}")
        return False

    # 检查是否有视频文件
    video_files = list(folder.glob("*.mp4")) + list(folder.glob("*.webm"))
    info_txt = folder / "info.txt"

    script_content = []
    has_content = False

    # 读取 info.txt 获取基本信息
    note_type = "图文"
    title = folder.name

    if info_txt.exists():
        with open(info_txt, 'r', encoding='utf-8') as f:
            info_content = f.read()

        # 提取笔记类型
        if "类型: 视频" in info_content:
            note_type = "视频"

        # 提取标题
        for line in info_content.split('\n'):
            if line.startswith("标题:"):
                title = line.replace("标题:", "").strip()
                break

    script_content.append(f"标题: {title}")
    script_content.append(f"类型: {note_type}")
    script_content.append("")

    # 生成书面稿
    if video_files:
        # 视频笔记：转录
        print(f"  📹 检测到视频文件: {video_files[0].name}")
        transcript = transcribe_video(str(video_files[0]))

        if transcript:
            script_content.append("=" * 40)
            script_content.append("字幕书面稿:")
            script_content.append("=" * 40)
            script_content.append("")
            script_content.append(transcript)
            has_content = True
        else:
            script_content.append("=" * 40)
            script_content.append("字幕:")
            script_content.append("=" * 40)
            script_content.append("（转录失败，请手动查看视频）")
            has_content = True
    else:
        # 图文笔记：整理文案
        print(f"  📝 检测到图文笔记，生成书面叙述...")

        if info_txt.exists():
            with open(info_txt, 'r', encoding='utf-8') as f:
                info_content = f.read()

            # 提取文案内容
            desc = ""
            in_desc = False
            skip_next_line = False  # 跳过"文案内容:"后面的分隔线
            for line in info_content.split('\n'):
                # 跳过"文案内容:"这一行
                if "文案内容:" in line:
                    in_desc = True
                    skip_next_line = True
                    continue
                # 跳过紧跟着的分隔线
                if skip_next_line and line.startswith("=="):
                    skip_next_line = False
                    continue
                # 遇到评论部分停止
                if in_desc and line.startswith("评论"):
                    break
                if in_desc and line.strip():
                    desc += line.strip() + "\n"

            if desc.strip():
                script_content.append("=" * 40)
                script_content.append("文案书面稿:")
                script_content.append("=" * 40)
                script_content.append("")
                script_content.append(desc.strip())
                has_content = True
            else:
                script_content.append("（未找到文案内容）")

    # 保存书面稿
    if has_content:
        script_path = folder / "script.txt"
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(script_content))
        print(f"  ✓ 已生成书面稿: script.txt")
        return True
    else:
        print(f"  ✗ 无法生成书面稿")
        return False


def main():
    """主函数"""
    if len(sys.argv) < 2:
        # 默认处理最新的下载文件夹
        download_dir = Path.home() / "tmp" / "xhs"

        # 找到最新的文件夹
        folders = [f for f in download_dir.iterdir() if f.is_dir()]
        if not folders:
            print("未找到下载的文件夹")
            return

        # 按修改时间排序
        folders.sort(key=lambda x: x.stat().st_mtime, reverse=True)

        print(f"处理最新文件夹: {folders[0].name}")
        generate_script_for_folder(str(folders[0]))
    else:
        # 处理指定文件夹
        folder_path = sys.argv[1]
        generate_script_for_folder(folder_path)


if __name__ == "__main__":
    main()
