#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书内容分析工具
- 输入：文件夹路径
- 自动检测图片、视频、txt文件
- 发送给 Gemini 分析
- 输出：内容总结
"""

import os
import sys
import json
import base64
import requests
from pathlib import Path
from datetime import datetime

# ========== 配置 ==========
API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"

# 默认提示词 - 智能类型判断 + 按类型总结
PROMPT_DEFAULT = """你是一个小红书内容分析助手。请根据以下输入内容，判断帖子类型并执行对应总结逻辑。

===【输入内容】===
标题：{title}
正文/字幕/图片文字：{text_content}
话题标签：{media_desc}

===【第一步：判断帖子类型】===
请先判断属于以下哪种类型：
- A. 图文干货帖（知识/教程/清单，内容主要在图片文字中）
- B. 情感/观点长文帖（两性/心理/生活感悟，内容在图片文字卡片中）
- C. 视频教程帖（健身/美食/技能，内容在视频字幕或口播中）
- D. 生活记录/Vlog帖（日常/旅行/穿搭展示）
- E. 热点评论/吐槽帖（影视/社会话题）
- F. 需求求助帖（提问/选择/困惑，作者在寻求建议）

===【第二步：按类型执行对应总结】===

▶ 如果是 A/B 类（图文干货 或 情感长文）：
1. 【核心主题】一句话概括
2. 【完整要点提取】将图片中所有文字要点按原有结构逐条列出，不遗漏
3. 【作者核心观点/建议】提炼作者最想表达的立场或结论
4. 【适用人群】这篇内容对谁最有用
5. 【可行动建议】读完这篇内容，读者可以做什么

▶ 如果是 C 类（视频教程）：
1. 【视频主题】一句话概括
2. 【完整知识点/步骤列表】将视频中提到的所有动作/步骤/知识点按顺序完整列出
3. 【核心方法论】提炼博主的核心理念或原则
4. 【注意事项/禁忌】视频中提到的错误做法或需要特别注意的点
5. 【评论区有价值补充】从评论中提取专业补充、修正意见、用户实践反馈，整理成要点
6. 【综合建议】结合正文和评论，给出完整的行动建议

▶ 如果是 F 类（需求/求助帖）：
1. 【提问者的核心需求】一句话概括 TA 在寻求什么帮助
2. 【背景信息】提问者提供的关键背景条件
3. 【评论区回复汇总】按以下维度整理所有有价值的评论：
   - 主流建议（多人认同的方向）
   - 少数派/反对观点
   - 有经验的亲测分享
   - 需要注意的风险提示
4. 【综合建议】综合评论区内容，给出一个平衡的实操建议

▶ 如果是 D/E 类（生活记录 或 热点评论）：
1. 【内容概述】简洁描述这篇帖子讲了什么
2. 【核心信息/有用细节】提取其中具有参考价值的信息（地点/产品/观点/数据）
3. 【情绪基调】正能量/吐槽/搞笑/感动等
4. 【评论区亮点】有趣或有价值的评论观点

===【输出格式要求】===
- 用清晰的标题分层，重点内容加粗
- 要点用数字或符号列出，层次分明
- 保留专业术语，不过度简化
"""

# 分析提示词 - 使用 xhs-summary 风格
PROMPT_CONTENT_SUMMARY = """你是一名严谨的内容编辑，擅长把口语化视频整理成结构清晰，可复用的笔记与教程。
你的任务是：在不丢失信息的前提下，把视频内容和评论区信息，整理成对创作者有用的结构化分析。

## 分析要求：
1. 视频核心信息总结（限制在 200 字内，偏客观）
2. 内容结构拆解：开头钩子，信息块/章节、结尾设计
3. 评论区洞察：高频观点、典型支持/质疑点
4. 给创作者的优化建议

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
{text_content}

## 媒体文件：
{media_desc}
"""


PROMPT_VISUAL = """你是一位专业的小红书视觉内容策划师，擅长为视频内容设计封面图和信息卡片，让用户在 3 秒内明确主题并愿意点开/看完。

## 分析要求：
1. 封面图方案：标题文案、辅助文案、主视觉元素、配色建议
2. 视频中间信息卡片：每张卡片只承载 1 个观点，文字+简单视觉说明
3. 时间轴标注：第 X 秒~第 Y 秒适合插入信息卡片

## 输出格式：
===
【封面设计方案】
- 主标题：xxx
- 副标题：xxx
- 视觉元素：xxx
- 配色建议：xxx

【信息卡片脚本】
1. [时间] 核心观点：xxx
2. [时间] 核心观点：xxx

【视觉风格建议】
xxx
===

## 内容如下：
{text_content}

## 媒体文件：
{media_desc}
"""


PROMPT_MONETIZE = """你是一名小红书变现与转化专家，熟悉从曝光 → 互动 → 私域/成交的完整路径。你的任务是评估这条视频内容的变现潜力，并给出可执行的优化方案。

## 分析要求：
1. 目标用户画像：谁在看，内容是否击中目标人群痛点
2. 信任构建分析：专业度、背书、案例，数据
3. 种草链路分析：从"种草点"到"点击/私信/下单"的引导
4. 评论区需求转化：潜在需求问题可转化成后续选题/产品

## 输出格式：
===
【目标用户画像与痛点分析】
xxx

【信任构建评估】
xxx

【种草链路优化建议】
xxx

【评论区变现机会】
xxx

【可执行的变现优化方案】
xxx
===

## 内容如下：
{text_content}

## 媒体文件：
{media_desc}
"""


def encode_media(file_path: Path) -> dict:
    """将文件转为 base64"""
    with open(file_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')

    suffix = file_path.suffix.lower()
    if suffix == '.webp':
        mime = 'image/webp'
    elif suffix == '.png':
        mime = 'image/png'
    elif suffix == '.jpg' or suffix == '.jpeg':
        mime = 'image/jpeg'
    elif suffix == '.mp4':
        mime = 'video/mp4'
    elif suffix == '.mov':
        mime = 'video/quicktime'
    else:
        mime = 'application/octet-stream'

    return {"inline_data": {"mime_type": mime, "data": b64}}


def analyze_folder(folder_path: str, mode: str = "summary"):
    """分析文件夹中的内容
    mode: default(智能类型判断), summary(内容总结), visual(视觉策划), monetize(变现分析)
    """
    # 选择提示词模板
    prompt_templates = {
        "default": PROMPT_DEFAULT,
        "summary": PROMPT_CONTENT_SUMMARY,
        "visual": PROMPT_VISUAL,
        "monetize": PROMPT_MONETIZE,
    }
    selected_prompt = prompt_templates.get(mode, PROMPT_DEFAULT)

    folder = Path(folder_path)

    if not folder.exists():
        print(f"错误: 文件夹不存在: {folder_path}")
        return

    # 查找所有图片
    images = []
    for ext in ['*.webp', '*.jpg', '*.jpeg', '*.png', '*.gif']:
        images.extend(sorted(folder.glob(ext)))

    # 查找视频
    videos = []
    for ext in ['*.mp4', '*.mov', '*.avi']:
        videos.extend(sorted(folder.glob(ext)))

    # 查找 txt 文件
    txt_files = list(folder.glob('*.txt'))

    if not images and not videos:
        print("错误: 未找到图片或视频文件")
        return

    # 简洁输出帖子信息
    is_video = bool(videos)
    post_type = "视频" if is_video else "图文"
    img_count = len(images)

    if is_video:
        print(f"📌 {post_type}帖子 (1张封面 + 1个视频)")
    else:
        print(f"📌 {post_type}帖子 ({img_count}张图片)")

    # 读取文案
    text_content = ""
    title = "未知标题"
    for txt in txt_files:
        full_text = txt.read_text(encoding='utf-8')
        text_content += full_text + "\n"
        # 提取标题（从第一行 "标题: xxx" 中提取）
        for line in full_text.split('\n'):
            if line.startswith('标题:'):
                title = line[3:].strip()
                break

    if not text_content.strip():
        text_content = "无文案内容"

    # 构建媒体描述
    media_parts = []
    if images:
        media_parts.append(f"共 {len(images)} 张图片")
    if videos:
        media_parts.append(f"共 {len(videos)} 个视频")

    media_desc = "，".join(media_parts)

    # 构建 prompt（根据模式选择不同的参数）
    if mode == "default":
        prompt = selected_prompt.format(
            title=title,
            text_content=text_content,
            media_desc=media_desc
        )
    else:
        prompt = selected_prompt.format(
            text_content=text_content,
            media_desc=media_desc
        )

    # 构建请求内容
    parts = [{"text": prompt}]

    # 添加所有图片（静默处理）
    for img in images:
        parts.append(encode_media(img))

    # 添加视频（如果有）
    for vid in videos:
        parts.append(encode_media(vid))

    # 调用 API
    try:
        resp = requests.post(
            f"{GEMINI_API_URL}?key={API_KEY}",
            json={"contents": [{"role": "user", "parts": parts}]},
            headers={"Content-Type": "application/json"},
            timeout=300
        )

        if resp.status_code == 200:
            data = resp.json()
            if 'candidates' in data:
                result = data['candidates'][0]['content']['parts'][0]['text']
                print("\n" + "=" * 50)
                print("📊 分析结果")
                print("=" * 50)
                print(result)
                return result
            else:
                print(f"错误: {data}")
        else:
            print(f"API 错误: {resp.status_code}")
            print(resp.text)

    except Exception as e:
        print(f"错误: {e}")

    return None


def main():
    import argparse

    parser = argparse.ArgumentParser(description='小红书内容分析工具')
    parser.add_argument('folder', help='文件夹路径')
    parser.add_argument('-m', '--mode', default='default',
                        choices=['default', 'summary', 'visual', 'monetize'],
                        help='分析模式: default(智能类型判断), summary(内容总结), visual(视觉策划), monetize(变现分析)')
    args = parser.parse_args()

    folder_path = args.folder
    # 处理 ~ 路径
    if folder_path.startswith('~'):
        folder_path = os.path.expanduser(folder_path)

    # 显示模式
    mode_names = {
        'default': '智能类型判断',
        'summary': '内容总结',
        'visual': '视觉策划',
        'monetize': '变现分析'
    }
    print(f"\n📊 分析模式: {mode_names[args.mode]}")

    analyze_folder(folder_path, mode=args.mode)


if __name__ == "__main__":
    main()
