#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B站首页推荐视频批量总结
- 获取首页推荐视频
- 检测字幕：有字幕用 MiniMax 分析，无字幕下载视频用 Gemini 分析
- 提取字幕书面稿：AssemblyAI 转录 + MiniMax 整理标点
- 输出到 Obsidian
"""

import os
import json
import subprocess
import base64
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

BILIBILI_DIR = Path("/tmp/bilibili")
OBSIDIAN_DIR = Path.home() / "Library" / "Mobile Documents" / "iCloud~md~obsidian" / "Documents" / "2026-spring" / "Bilibili"
OUTPUT_FILE = OBSIDIAN_DIR / "bilibili_homefeed_summaries.md"
TRANSCRIPT_FILE = OBSIDIAN_DIR / "bilibili_transcripts.md"

# 确保目录存在
OBSIDIAN_DIR.mkdir(parents=True, exist_ok=True)
BILIBILI_DIR.mkdir(parents=True, exist_ok=True)

# 提示词 - 智能类型判断 + 按类型深度总结
PROMPT_ANALYSIS = """你是一个B站视频内容分析助手。请根据以下输入，判断视频类型并执行对应的完整总结。

===【第一步：判断视频类型】===
请先判断属于以下哪种主类型：
- A. 知识科普类（财经/历史/科学/社会解读，10分钟以上）
- B. 技术教程类（编程/设计/工具使用，常为多P长视频）
- C. 观点评论类（时事/影评/测评，表达个人立场）
- D. Vlog/生活记录类（旅行/日常/美食探店）
- E. 技能干货类（健身/学习方法/职场，短小精悍）
- F. 番剧/纪录片类（剧情向，按集播放）
- G. 娱乐/鬼畜/搞笑类（纯娱乐向）

===【第二步：提取基础信息（所有类型通用）】===

**1. 核心速览**
- 视频类型：
- 核心主题（一句话）：
- UP主背景/定位：
- 视频时长 & 信息密度：（轻松/中等/高密度）

**2. 数据表现**
- 播放量 / 点赞率（点赞÷播放）/ 收藏率（收藏÷播放）
- 高收藏率（>2%）说明内容有较高"留存价值"，请特别标注

===【第三步：按类型执行深度总结】===

▶ 如果是 A 类（知识科普）：
1. 【核心论点】视频想回答的核心问题是什么？结论是什么？
2. 【完整知识框架】按视频叙述逻辑逐层展开所有论点和论据，不遗漏关键数据、案例，时间节点
3. 【关键数据/案例】单独列出视频中引用的重要数字、历史事件、人物案例
4. 【UP主立场/倾向】是否有明显的价值观立场或情感倾向？
5. 【评论区补充与争议】
   - 观众认同的核心观点
   - 有价值的补充信息或不同视角
   - 争议点或被质疑的地方
6. 【可延伸阅读/关联话题】评论区或简介提到的相关内容推荐

▶ 如果是 B 类（技术教程 / 多P长视频）：
1. 【课程定位】面向什么水平的学习者？需要什么前置知识？
2. 【完整目录梳理】按分P或时间轴章节，逐节列出每部分的核心内容和关键知识点
3. 【核心技术要点】提炼全程最重要的方法论、命令、配置、原理
4. 【重要注意事项 & 常见坑】教程中特别强调的错误做法或易踩的坑
5. 【学完能做什么】完成学习后可以实现的具体能力或项目
6. 【评论区精华】
   - 观众反馈的补充技巧或更优方案
   - 提问高频的难点（说明这些地方需要重点注意）
   - 版本更新/过时内容提示

▶ 如果是 C 类（观点评论 / 时事）：
1. 【事件/话题背景】用2-3句话交代来龙去脉
2. 【UP主核心观点】完整还原其论证逻辑：前提→论据→结论
3. 【支持论据清单】所有用于支撑观点的事实，数据、类比
4. 【反驳/局限性】视频中是否自我反驳或留有盲点？
5. 【评论区观点图谱】
   - 支持方主要理由
   - 反对方主要理由
   - 补充信息（评论中提到视频未涉及的重要内容）
6. 【综合判断】结合正文+评论，这个观点的可信度和完整度如何？

▶ 如果是 D 类（Vlog / 生活记录）：
1. 【内容概述】去了哪/做了什么/经历了什么
2. 【有参考价值的具体信息】地点名称、店铺、交通方式、费用，时间安排等
3. 【UP主的感受与建议】主观评价和推荐/避坑建议
4. 【弹幕/评论中的实用补充】其他人提供的补充信息或纠正

▶ 如果是 E 类（技能干货 / 方法论）：
1. 【核心方法】完整列出所有步骤/技巧/原则，不遗漏
2. 【背后的底层逻辑】为什么这个方法有效？原理是什么？
3. 【适用场景与限制】什么情况下适用？有哪些前提条件？
4. 【评论区实践反馈】有人亲测有效吗？有改进建议吗？

▶ 如果是 F 类（番剧/纪录片）：
1. 【本集/本视频内容梗概】
2. 【关键剧情点 / 信息点】
3. 【评论区解析与讨论亮点】

===【第四步：弹幕信号分析（适用于所有类型）】===
弹幕密度高的时间节点往往是视频的精华/爆点/争议点，请提取：
- 弹幕爆发的时间段 → 对应视频内容是什么
- 高频重复出现的词或句子 → 说明什么

===【第五步：综合评价与行动建议】===
1. 【值得关注的核心收获】：看完这个视频最重要的1-3个takeaway
2. 【局限性提示】：视频内容有哪些可能的偏差、过时信息或遗漏视角
3. 【适合谁看】：这个视频最值得推荐给什么类型的观众
4. 【下一步行动】：看完后可以做什么、看什么、搜什么

===【输出格式要求】===
- 使用清晰的层级标题
- 关键数据、结论加粗
- 列表项简洁，保留专业术语
- 最后附：【标签】{{原始标签}} | 【合集】{{合集名（如有）}}

===【输入内容】===
视频标题：{title}
UP主：{author}
BV号：{bvid}

字幕/口播文本：
{transcript}

请按照上述格式输出。"""

PROMPT_GEMINI = """你是一个B站视频内容分析助手。请根据以下输入，判断视频类型并执行对应的完整总结。

[注意：本视频没有字幕，以下内容是通过分析视频画面得出的总结]

===【第一步：判断视频类型】===
请先判断属于以下哪种主类型：
- A. 知识科普类（财经/历史/科学/社会解读，10分钟以上）
- B. 技术教程类（编程/设计/工具使用，常为多P长视频）
- C. 观点评论类（时事/影评/测评，表达个人立场）
- D. Vlog/生活记录类（旅行/日常/美食探店）
- E. 技能干货类（健身/学习方法/职场，短小精悍）
- F. 番剧/纪录片类（剧情向，按集播放）
- G. 娱乐/鬼畜/搞笑类（纯娱乐向）

===【第二步：提取基础信息（所有类型通用）】===

**1. 核心速览**
- 视频类型：
- 核心主题（一句话）：
- UP主背景/定位：
- 视频时长 & 信息密度：（轻松/中等/高密度）

**2. 数据表现**
- 根据画面内容推断视频定位和目标受众

===【第三步：按类型执行深度总结】===

▶ 如果是 A 类（知识科普）：
1. 【核心论点】视频想回答的核心问题是什么？结论是什么？
2. 【完整知识框架】按视频叙述逻辑逐层展开所有论点和论据
3. 【关键数据/案例】单独列出重要数字、历史事件、人物案例
4. 【UP主立场/倾向】是否有明显的价值观立场或情感倾向？

▶ 如果是 B 类（技术教程 / 多P长视频）：
1. 【课程定位】面向什么水平的学习者？需要什么前置知识？
2. 【完整目录梳理】按时间轴章节，逐节列出核心内容和关键知识点
3. 【核心技术要点】提炼最重要的方法论、命令、配置、原理
4. 【重要注意事项 & 常见坑】特别强调的错误做法或易踩的坑
5. 【学完能做什么】完成后可以实现的具体能力或项目

▶ 如果是 C 类（观点评论 / 时事）：
1. 【事件/话题背景】用2-3句话交代来龙去脉
2. 【UP主核心观点】完整还原其论证逻辑：前提→论据→结论
3. 【支持论据清单】所有用于支撑观点的事实、数据、类比
4. 【反驳/局限性】视频中是否自我反驳或留有盲点？

▶ 如果是 D 类（Vlog / 生活记录）：
1. 【内容概述】去了哪/做了什么/经历了什么
2. 【有参考价值的具体信息】地点名称、店铺、交通方式、费用等
3. 【UP主的感受与建议】主观评价和推荐/避坑建议

▶ 如果是 E 类（技能干货 / 方法论）：
1. 【核心方法】完整列出所有步骤/技巧/原则，不遗漏
2. 【背后的底层逻辑】为什么这个方法有效？原理是什么？
3. 【适用场景与限制】什么情况下适用？有哪些前提条件？

▶ 如果是 F 类（番剧/纪录片）：
1. 【本集/本视频内容梗概】
2. 【关键剧情点 / 信息点】

===【第四步：综合评价与行动建议】===
1. 【值得关注的核心收获】：看完这个视频最重要的1-3个takeaway
2. 【局限性提示】：视频内容有哪些可能的偏差或遗漏视角
3. 【适合谁看】：这个视频最值得推荐给什么类型的观众
4. 【下一步行动】：看完后可以做什么、看什么、搜什么

===【输出格式要求】===
- 使用清晰的层级标题
- 关键数据、结论加粗
- 列表项简洁，保留专业术语
- 最后附：【标签】{{原始标签}}

===【输入内容】===
视频标题：{title}
UP主：{author}
BV号：{bvid}

视频内容：
{transcript}

请按照上述格式输出。"""


def run_mcp(cmd: list) -> dict:
    """运行 MCP 命令"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    text = result.stdout
    start = text.find('{')
    if start >= 0:
        try:
            return json.loads(text[start:])
        except:
            return {}
    return {}


def get_homefeed(count: int = 5) -> list:
    """获取首页推荐"""
    print(f"\n[1/5] 获取首页推荐...")
    data = run_mcp(["mcporter", "call", "bilibili-mcp", "bili_homefeed"])
    videos = data.get('videos', [])[:count]
    print(f"    获取到 {len(videos)} 个视频")
    return videos


def get_subtitle(bvid: str) -> dict:
    """获取视频字幕"""
    return run_mcp(["mcporter", "call", "bilibili-mcp", "bili_subtitle", f"bvid={bvid}"])


def call_minimax_with_retry(transcript: str, title: str, bvid: str, author: str, max_retries: int = 3) -> str:
    """调用 MiniMax API 分析字幕（带重试）- 使用兼容 Anthropic API 格式"""
    import os
    for attempt in range(max_retries):
        try:
            print(f"    调用 MiniMax API (尝试 {attempt + 1}/{max_retries})...")

            # 使用兼容 Anthropic 的 API
            base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.minimaxi.com/anthropic")
            api_url = f"{base_url}/v1/messages"
            token = os.environ.get("ANTHROPIC_AUTH_TOKEN")

            user_prompt = PROMPT_ANALYSIS.format(
                title=title,
                author=author,
                bvid=bvid,
                transcript=transcript
            )

            resp = requests.post(
                api_url,
                json={
                    "model": "MiniMax-M2.7",
                    "max_tokens": 8192,
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
                if 'content' in data:
                    content = data['content']
                    if isinstance(content, list) and content:
                        # 兼容两种格式：text 或 thinking
                        result = content[0].get('text', '') or content[0].get('thinking', '') or content[0].get('content', '')
                    elif isinstance(content, str):
                        result = content
                    else:
                        result = ''
                    if result and len(result) > 50:
                        return result
                print(f"    ⚠ 返回内容为空，重试...")
        except Exception as e:
            print(f"    ⚠ 异常: {e}，重试...")

        if attempt < max_retries - 1:
            import time
            time.sleep(2)

    return "❌ 分析失败（已重试多次）"


def download_video(bvid: str) -> str:
    """下载视频 (480P)"""
    print(f"    下载视频 (480P)...")

    video_dir = BILIBILI_DIR / bvid
    video_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "yt-dlp", "-o", str(video_dir / "video.%(ext)s"),
        "--no-playlist", "--merge-output-format", "mp4",
        "-f", "bv[height<=480][ext=mp4]/best[height<=480]",
        f"https://www.bilibili.com/video/{bvid}"
    ]

    try:
        subprocess.run(cmd, capture_output=True, timeout=300)
        # 找视频文件
        for f in video_dir.iterdir():
            if f.suffix in ['.mp4', '.mkv'] and f.stat().st_size > 1000000:
                print(f"    视频下载完成: {f.stat().st_size / 1024 / 1024:.1f} MB")
                return str(f)
    except Exception as e:
        print(f"    下载失败: {e}")
    return None


def call_gemini_video_with_retry(video_path: str, title: str, bvid: str, author: str, max_retries: int = 3) -> str:
    """调用 Gemini API 分析视频（带重试）"""
    for attempt in range(max_retries):
        try:
            print(f"    调用 Gemini API (尝试 {attempt + 1}/{max_retries})...")

            with open(video_path, 'rb') as f:
                video_b64 = base64.b64encode(f.read()).decode('utf-8')

            resp = requests.post(
                f"{GEMINI_API_URL}?key={API_KEY}",
                json={
                    "contents": [{
                        "role": "user",
                        "parts": [
                            {"text": f"{PROMPT_GEMINI}\n\n视频标题：{title}\nBV号：{bvid}\nUP主：{author}"},
                            {"inline_data": {"mime_type": "video/mp4", "data": video_b64}}
                        ]
                    }]
                },
                headers={"Content-Type": "application/json"},
                timeout=300
            )

            if resp.status_code == 200:
                data = resp.json()
                if 'candidates' in data and data['candidates']:
                    result = data['candidates'][0]['content']['parts'][0]['text']
                    if result and len(result) > 50:
                        return result
                    else:
                        print(f"    ⚠ 返回内容过短，重试...")
            else:
                print(f"    ⚠ API 错误 {resp.status_code}，重试...")
        except Exception as e:
            print(f"    ⚠ 异常: {e}，重试...")

        if attempt < max_retries - 1:
            import time
            time.sleep(2)

    return "❌ 分析失败（已重试多次）"


def call_gemini_video(video_path: str, title: str, bvid: str, author: str) -> str:
    """调用 Gemini API 分析视频"""
    print(f"    调用 Gemini API 分析视频...")

    try:
        with open(video_path, 'rb') as f:
            video_b64 = base64.b64encode(f.read()).decode('utf-8')

        resp = requests.post(
            f"{GEMINI_API_URL}?key={API_KEY}",
            json={
                "contents": [{
                    "role": "user",
                    "parts": [
                        {"text": f"{PROMPT_GEMINI}\n\n视频标题：{title}\nBV号：{bvid}\nUP主：{author}"},
                        {"inline_data": {"mime_type": "video/mp4", "data": video_b64}}
                    ]
                }]
            },
            headers={"Content-Type": "application/json"},
            timeout=300
        )

        if resp.status_code == 200:
            data = resp.json()
            if 'candidates' in data and data['candidates']:
                return data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ 错误: {e}"
    return "❌ 分析失败"


def clean_video(bvid: str):
    """清理视频文件"""
    video_dir = BILIBILI_DIR / bvid
    if video_dir.exists():
        shutil.rmtree(video_dir)
        print(f"    已清理临时文件: {bvid}")


# ========== AssemblyAI + MiniMax 字幕提取功能 ==========

def extract_audio(video_path: str, bvid: str) -> str:
    """从视频提取音频，优先用 ffmpeg，失败则用 yt-dlp"""
    print(f"    提取音频...")
    audio_dir = BILIBILI_DIR / bvid
    audio_dir.mkdir(parents=True, exist_ok=True)
    audio_path = audio_dir / "audio.mp3"

    # 先尝试 ffmpeg
    cmd = [
        "ffmpeg", "-i", video_path,
        "-vn", "-acodec", "libmp3lame", "-q:a", "2",
        str(audio_path)
    ]

    try:
        subprocess.run(cmd, capture_output=True, timeout=60)
        if audio_path.exists() and audio_path.stat().st_size > 1000:
            size_mb = audio_path.stat().st_size / 1024 / 1024
            print(f"    音频提取完成 (ffmpeg): {size_mb:.1f} MB")
            return str(audio_path)
    except Exception as e:
        print(f"    ffmpeg 失败: {e}")

    # ffmpeg 失败，用 yt-dlp 直接下载音频
    print(f"    使用 yt-dlp 提取音频...")
    try:
        subprocess.run([
            "yt-dlp", "-x", "--audio-format", "mp3",
            "-o", str(audio_dir / "audio.%(ext)s"),
            "--no-playlist",
            f"https://www.bilibili.com/video/{bvid}"
        ], capture_output=True, timeout=300)

        # 找 mp3 文件
        for f in audio_dir.iterdir():
            if f.suffix == '.mp3' and f.stat().st_size > 1000:
                size_mb = f.stat().st_size / 1024 / 1024
                print(f"    音频提取完成 (yt-dlp): {size_mb:.1f} MB")
                return str(f)
    except Exception as e:
        print(f"    yt-dlp 失败: {e}")

    return None


def assemblyai_transcribe(audio_path: str) -> str:
    """使用 AssemblyAI 转录音频"""
    print(f"    AssemblyAI 转录中...")

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
            "language_code": "zh",
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
        else:
            time.sleep(3)


def minimax_format_transcript(raw_text: str) -> str:
    """使用 MiniMax 整理转录文本"""
    print(f"    MiniMax 整理标点...")

    base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.minimaxi.com/anthropic")
    api_url = f"{base_url}/v1/messages"
    token = os.environ.get("ANTHROPIC_AUTH_TOKEN")

    system_prompt = """你是一个专业的文字整理专家。请将以下语音转录文本整理成带标点符号、分段清晰的书面文字稿。

要求：
1. 添加合适的标点符号（逗号、句号、顿号、引号等）
2. 根据语义合理分段
3. 保持原文意思不变
4. 适当补充人名、地名等专有名词的正确写法
5. 输出格式：只有整理后的文字稿，不要有其他说明"""

    resp = requests.post(
        api_url,
        json={
            "model": "MiniMax-M2.7",
            "max_tokens": 4096,
            "system": system_prompt,
            "messages": [
                {"role": "user", "content": f"请整理以下转录文本：\n\n{raw_text}"}
            ]
        },
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        timeout=120
    )

    if resp.status_code == 200:
        data = resp.json()
        contents = data.get('content', [])
        for c in contents:
            if c.get('type') == 'text':
                return c.get('text', '')
    return raw_text  # 如果失败返回原始文本


def extract_transcript(bvid: str, title: str = "", author: str = "") -> str:
    """
    提取视频字幕书面稿
    返回：整理后的文字稿，失败返回 None
    """
    print(f"\n[字幕提取] {title[:30]}...")

    # 1. 下载视频
    video_path = download_video(bvid)
    if not video_path:
        print(f"    ⚠ 视频下载失败")
        return None

    # 2. 提取音频
    audio_path = extract_audio(video_path, bvid)
    if not audio_path:
        clean_video(bvid)
        return None

    # 3. AssemblyAI 转录
    raw_text = assemblyai_transcribe(audio_path)
    if not raw_text or len(raw_text) < 50:
        print(f"    ⚠ 转录结果太短")
        clean_video(bvid)
        return None

    # 4. MiniMax 整理
    formatted_text = minimax_format_transcript(raw_text)

    # 5. 清理临时文件
    clean_video(bvid)

    print(f"    ✓ 字幕提取完成")
    return formatted_text


def write_transcripts_to_obsidian(transcripts: list):
    """将字幕书面稿写入 Obsidian"""
    if not transcripts:
        return

    print(f"\n[字幕] 写入 Obsidian...")

    # 读取现有内容
    existing = ""
    if TRANSCRIPT_FILE.exists():
        existing = TRANSCRIPT_FILE.read_text(encoding='utf-8')

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    new_lines = [f"\n## {timestamp}\n\n"]

    for t in transcripts:
        title = t.get('title', '未知')
        bvid = t.get('bvid', '')
        author = t.get('author', '未知')
        transcript = t.get('transcript', '')

        new_lines.append(f"""## {title}

### 视频信息
- **标题**: {title}
- **UP主**: {author}
- **BV号**: {bvid}
- **链接**: https://www.bilibili.com/video/{bvid}

---

### 字幕书面稿

{transcript}

---

""")

    new_content = ''.join(new_lines)

    # 合并
    if existing:
        last_divider = existing.rfind('---')
        if last_divider > 0:
            content = existing[:last_divider + 3] + new_content
        else:
            content = existing + new_content
    else:
        content = f"""# B站视频字幕书面稿

采集时间: {timestamp}

---""" + new_content

    TRANSCRIPT_FILE.write_text(content, encoding='utf-8')
    print(f"    ✓ 已写入: {TRANSCRIPT_FILE}")


def sanitize_filename(name: str) -> str:
    """清理文件名"""
    invalid = '<>:"/\\|?*'
    for c in invalid:
        name = name.replace(c, '_')
    return name[:50] if len(name) > 50 else name


def format_summary(analysis: str, video: dict, has_subtitle: bool, transcript: str = None, transcript_method: str = None) -> str:
    """格式化总结

    transcript_method:
    - "bili": B站原生字幕 -> MiniMax 整理
    - "assemblyai": AssemblyAI 转录 -> MiniMax 整理
    - None: 无字幕书面稿
    """
    title = video.get('title', '未知')
    bvid = video.get('bvid', '')
    author = video.get('author', '未知')
    source = "B站首页推荐 (有字幕)" if has_subtitle else "B站首页推荐 (无字幕/Gemini分析)"

    content = f"""## {title}

### 视频信息
- **标题**: {title}
- **来源**: {source}
- **UP主**: {author}
- **BV号**: {bvid}
- **链接**: https://www.bilibili.com/video/{bvid}

{analysis}
"""

    # 如果有字幕书面稿，添加到总结后面
    if transcript:
        if transcript_method == "assemblyai":
            method_note = "*转录方式：AssemblyAI (视频转录) → MiniMax (整理标点)*"
        else:
            method_note = "*转录方式：B站字幕 → MiniMax (整理标点)*"

        content += f"""

---

### 字幕书面稿

{transcript}

{method_note}
"""

    content += "\n\n---\n"
    return content


def extract_titles(content: str) -> list:
    """从内容中提取标题和BV号

    处理三种格式:
    1. ## BV号 (旧格式) + **标题**: xxx + **BV号**: BVxxx
    2. ## 视频标题 (新格式) + **BV号**: BVxxx
    3. ## 普通标题 (最新格式) + **BV号**: BVxxx
    """
    import re
    # 使用字典来自动去重，key是BV号
    results = {}  # {bvid: title}

    # 模式1: ## BV号 后面跟着 **标题**: xxx (旧格式)
    # 优先使用这个模式，因为它能提取真实标题
    pattern1 = r'^## ([A-Za-z0-9]+)$[\s\S]*?\*\*标题\*\*: (.+?)\n'
    matches1 = re.findall(pattern1, content, re.MULTILINE)
    for bvid, title in matches1:
        # 排除非视频标题（如"总结"、"目录"等）和日期格式
        if title.strip() not in ['目录', '总结'] and not title.strip().startswith('20'):
            results[bvid.strip()] = title.strip()

    # 模式2: ## 普通标题 (非BV号开头) + **BV号**: BVxxx (最新格式)
    # 查找 "## 标题" 后面300字符内有 "**BV号**: BVxxx" 的情况
    pattern2 = r'^## ([^#\n][^\n]+)$[\s\S]{0,300}\*\*BV号\*\*: ([A-Za-z0-9]+)'
    matches2 = re.findall(pattern2, content, re.MULTILINE)
    for title, bvid in matches2:
        bvid = bvid.strip()
        title = title.strip()
        # 排除非视频标题
        if title in ['目录', '总结'] or title.startswith('20'):
            continue
        # 只添加：如果还没有这个BV号，或者新标题更好（不是纯BV号）
        if bvid not in results:
            results[bvid] = title
        elif not title.startswith('BV'):
            # 更新为更好的标题
            results[bvid] = title

    # 转换为列表
    return [(bvid, title) for bvid, title in results.items()]


def generate_toc(titles: list) -> str:
    """生成目录 (BV号, 标题)"""
    if not titles:
        return ""
    lines = ["## 目录\n"]
    for bvid, title in titles:
        lines.append(f"- [[#{bvid}|{title}]]\n")
    return ''.join(lines)


def write_obsidian(results: list):
    """写入 Obsidian"""
    print(f"\n[5/5] 写入 Obsidian...")

    # 读取现有内容
    existing = ""
    if OUTPUT_FILE.exists():
        existing = OUTPUT_FILE.read_text(encoding='utf-8')

    # 生成新内容
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    new_lines = [f"\n## {timestamp}\n\n"]

    for r in results:
        new_lines.append(format_summary(r['analysis'], r['video'], r['has_subtitle'], r.get('transcript'), r.get('transcript_method')))

    new_content = ''.join(new_lines)

    # 合并
    if existing:
        # 找到最后一个 --- 的位置
        last_divider = existing.rfind('---')
        if last_divider > 0:
            content = existing[:last_divider + 3] + new_content
        else:
            content = existing + new_content
    else:
        content = f"""# B站首页推荐总结

采集时间: {timestamp}
数据来源: 首页推荐

---""" + new_content

    # 更新目录
    all_titles = extract_titles(content)
    toc = generate_toc(all_titles)

    # 删除旧的目录 (从 "## 目录" 到下一个 "---" 之前)
    import re
    # 匹配 ## 目录\n...\n--- (之间所有内容)
    old_toc_pattern = r'## 目录\n[\s\S]*?\n---\n'
    content = re.sub(old_toc_pattern, '## 目录\n\n', content)

    # 插入新目录 - 兼容旧格式和新格式
    marker = None
    if "数据来源:" in content:
        marker = "数据来源: 首页推荐"
    elif "来源：" in content:
        marker = "来源：个性化首页推荐"

    if marker:
        pos = content.find(marker)
        if pos > 0:
            end = content.find('\n', pos)
            if end > 0:
                content = content[:end + 1] + "\n" + toc + content[end + 1:]

    OUTPUT_FILE.write_text(content, encoding='utf-8')
    print(f"    ✓ 已写入: {OUTPUT_FILE}")
    print(f"    ✓ 目录已更新 ({len(all_titles)} 条)")


def extract_bvid(url: str) -> str:
    """从 URL 提取 BV号"""
    import re
    bv_match = re.search(r"(BV[0-9A-Za-z]{10})", url)
    if bv_match:
        return bv_match.group(1)
    return url.strip()


def get_video_info_from_mcp(bvid: str) -> dict:
    """通过 MCP 获取单个视频信息"""
    print(f"获取视频信息...")
    result = run_mcp(["mcporter", "call", "bilibili-mcp", "bili_video_info", f"bvid={bvid}"])
    if result:
        return {
            'bvid': result.get('bvid', bvid),
            'title': result.get('title', '未知'),
            'author': result.get('author', '未知'),
            'desc': result.get('description', ''),
            'duration': result.get('duration', 0),
        }
    return {'bvid': bvid, 'title': '未知', 'author': '未知'}


def process_single_video(bvid: str, transcript_only: bool = False) -> tuple:
    """处理单个视频，返回 (results, transcripts)"""
    video = get_video_info_from_mcp(bvid)
    title = video.get('title', '未知')[:30]
    author = video.get('author', '未知')

    print(f"\n[处理] {bvid}: {title}...")

    # 获取字幕
    subtitle_data = get_subtitle(bvid)
    subtitle_text = subtitle_data.get('text', '')
    no_subtitle_msg = subtitle_data.get('message', '')

    transcript_for_summary = None
    transcript_method = None
    analysis = None
    has_subtitle = False
    transcripts = []

    if subtitle_text and len(subtitle_text) > 50:
        # 有原生字幕
        print(f"    检测到字幕 ({len(subtitle_text)} 字符)")
        transcript_for_summary = minimax_format_transcript(subtitle_text)
        transcript_method = "bili"
        has_subtitle = True

        if not transcript_only:
            analysis = call_minimax_with_retry(subtitle_text, video.get('title', ''), bvid, author)
            if "分析失败" not in analysis:
                print(f"    ✓ 有字幕，MiniMax 分析成功")
    elif "没有字幕" in no_subtitle_msg:
        print(f"    检测到无字幕，使用 AssemblyAI 转录...")
        transcript_for_summary = extract_transcript(bvid, video.get('title', ''), author)
        transcript_method = "assemblyai"
        has_subtitle = False

        if transcript_for_summary:
            if not transcript_only:
                analysis = call_minimax_with_retry(transcript_for_summary, video.get('title', ''), bvid, author)
                if "分析失败" not in analysis:
                    print(f"    ✓ AssemblyAI 转录 + MiniMax 分析成功")
            transcripts.append({
                'title': video.get('title', ''),
                'bvid': bvid,
                'author': author,
                'transcript': transcript_for_summary
            })
    else:
        print(f"    ⚠ 字幕无效")
        analysis = "⚠️ 字幕无效"
        has_subtitle = True

    results = [{
        'video': video,
        'analysis': analysis,
        'has_subtitle': has_subtitle,
        'transcript': transcript_for_summary,
        'transcript_method': transcript_method
    }]

    return results, transcripts


def main():
    import argparse
    parser = argparse.ArgumentParser(description="B站首页推荐视频批量总结")
    parser.add_argument("--count", "-c", type=int, default=5, help="处理的视频数量")
    parser.add_argument("--transcript", "-t", action="store_true", help="同时提取字幕书面稿 (AssemblyAI + MiniMax)")
    parser.add_argument("--transcript-only", action="store_true", help="仅提取字幕书面稿，不生成总结")
    parser.add_argument("--url", "-u", type=str, default=None, help="单视频模式：直接处理指定BV号或URL")
    args = parser.parse_args()

    print("=" * 60)
    print("B站视频批量总结")
    print("=" * 60)

    # 单链接模式
    if args.url:
        bvid = extract_bvid(args.url)
        print(f"单视频模式: {bvid}")

        results, transcripts = process_single_video(bvid, args.transcript_only)

        # 写入 Obsidian
        if not args.transcript_only:
            write_obsidian(results)

        if transcripts:
            write_transcripts_to_obsidian(transcripts)

        print(f"\n✅ 完成！")
        return

    # 批量模式 - 获取首页推荐
    videos = get_homefeed(args.count)

    # 2-4. 处理每个视频
    results = []
    transcripts = []

    for i, video in enumerate(videos, 1):
        bvid = video.get('bvid', '')
        title = video.get('title', '未知')[:30]
        author = video.get('author', '未知')

        print(f"\n[处理] {i}/{len(videos)}: {title}...")

        # 提取字幕书面稿 (如果需要)
        transcript_text = None
        if args.transcript or args.transcript_only:
            full_title = video.get('title', '')
            full_author = video.get('author', '')
            transcript_text = extract_transcript(bvid, full_title, full_author)

            if transcript_text:
                transcripts.append({
                    'title': full_title,
                    'bvid': bvid,
                    'author': full_author,
                    'transcript': transcript_text
                })

        # 如果只提取字幕，跳过总结
        if args.transcript_only:
            continue

        # 获取字幕进行总结
        subtitle_data = get_subtitle(bvid)
        print(f"    字幕数据: {list(subtitle_data.keys())}")

        subtitle_text = subtitle_data.get('text', '')
        no_subtitle_msg = subtitle_data.get('message', '')

        # 初始化 transcript 变量
        transcript_for_summary = None
        transcript_method = None  # "bili" 或 "assemblyai"

        if subtitle_text and len(subtitle_text) > 50:
            # 有原生字幕：生成书面稿格式 + 分析
            transcript = subtitle_text
            print(f"    检测到字幕 ({len(transcript)} 字符)")

            # 用 MiniMax 整理成书面稿格式
            transcript_for_summary = minimax_format_transcript(transcript)
            transcript_method = "bili"
            print(f"    已生成书面稿格式 ({len(transcript_for_summary)} 字符)")

            analysis = call_minimax_with_retry(transcript, video.get('title', ''), bvid, author)
            has_subtitle = True
            if "分析失败" not in analysis:
                print(f"    ✓ 有字幕，MiniMax 分析成功")
            else:
                print(f"    ⚠ MiniMax 分析失败")
        elif "没有字幕" in no_subtitle_msg:
            print(f"    检测到无字幕消息: {no_subtitle_msg}")
            # 如果指定了 --transcript 参数，用 AssemblyAI 转录
            transcript_for_summary = None
            if args.transcript or args.transcript_only:
                transcript_for_summary = extract_transcript(bvid, video.get('title', ''), author)
                transcript_method = "assemblyai"
            else:
                # 使用 AssemblyAI 转录 + MiniMax 分析（不再使用 Gemini）
                transcript_for_summary = extract_transcript(bvid, video.get('title', ''), author)
                transcript_method = "assemblyai"
                if transcript_for_summary:
                    analysis = call_minimax_with_retry(transcript_for_summary, video.get('title', ''), bvid, author)
                    has_subtitle = False
                    if "分析失败" not in analysis:
                        print(f"    ✓ 无字幕，AssemblyAI 转录 + MiniMax 分析成功")
                    else:
                        print(f"    ⚠ MiniMax 分析失败")
                else:
                    analysis = "❌ AssemblyAI 转录失败"
                    has_subtitle = False
        else:
            print(f"    ⚠ 字幕无效或太短")
            analysis = "⚠️ 字幕无效，跳过分析"
            has_subtitle = True

        results.append({
            'video': video,
            'analysis': analysis,
            'has_subtitle': has_subtitle,
            'transcript': transcript_for_summary,  # 书面稿格式的字幕
            'transcript_method': transcript_method  # 转录方式
        })

    # 5. 写入 Obsidian
    if not args.transcript_only:
        write_obsidian(results)

    # 写入字幕书面稿
    if transcripts:
        write_transcripts_to_obsidian(transcripts)

    print(f"\n✅ 完成！")
    if results:
        print(f"📝 总结: {len(results)} 个视频 -> {OUTPUT_FILE}")
    if transcripts:
        print(f"📄 字幕: {len(transcripts)} 个视频 -> {TRANSCRIPT_FILE}")


if __name__ == "__main__":
    main()
