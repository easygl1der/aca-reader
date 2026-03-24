#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书内容下载器 - 完整版
下载首页推荐的笔记所有内容：
- 图文：所有图片 + 文案 + 评论
- 视频：视频文件 + 文案 + 评论 + 视频信息
"""

import json
import os
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

DOWNLOAD_DIR = Path.home() / "tmp" / "xhs"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

def sanitize_filename(name: str) -> str:
    """清理文件名，去除非法_chars = '<>字符"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name[:50] if len(name) > 50 else name

def download_video(url: str, folder_path: Path) -> str:
    """使用 yt-dlp 下载视频，支持重试"""
    retry_delays = [5, 10, 15]  # 重试间隔：5秒、10秒、15秒

    for attempt in range(3):
        try:
            print(f"  尝试 {attempt + 1}/3 ...")
            # 使用 yt-dlp 下载视频到指定文件夹
            result = subprocess.run(
                ['yt-dlp', '-o', str(folder_path / 'video.%(ext)s'),
                 '--no-playlist', '--merge-output-format', 'mp4',
                 url],
                capture_output=True, text=True, timeout=300
            )
            if result.returncode == 0:
                # 找到下载的文件
                for f in folder_path.iterdir():
                    if f.name.startswith('video.'):
                        return str(f)

            # 下载失败，记录错误并重试
            error_msg = result.stderr[:100] if result.stderr else 'unknown error'
            print(f"  ✗ 尝试 {attempt + 1} 失败: {error_msg}")

            # 如果还有重试次数，等待后重试
            if attempt < 2:
                wait_time = retry_delays[attempt]
                print(f"  ⏳ 等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
        except Exception as e:
            print(f"  ✗ 尝试 {attempt + 1} 异常: {e}")
            if attempt < 2:
                wait_time = retry_delays[attempt]
                print(f"  ⏳ 等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)

    # 3次都失败
    print(f"  ✗ 视频下载失败：3次尝试均未成功")
    return ''

def download_file(url: str, filepath: Path, is_video: bool = False) -> bool:
    """下载文件（图片或视频）"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        timeout = 300 if is_video else 30  # 视频下载时间更长
        with urllib.request.urlopen(req, timeout=timeout) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"  ✗ 下载失败: {url[:50]}... - {e}")
        return False

def get_feed_detail(feed_id: str, xsec_token: str, click_more_replies: bool = True, load_all_comments: bool = True, limit: int = 20) -> dict:
    """调用 MCP 获取笔记详情"""
    result = subprocess.run(
        ["mcporter", "call", "xiaohongshu-mcp", "get_feed_detail",
         f"click_more_replies={str(click_more_replies).lower()}",
         f"load_all_comments={str(load_all_comments).lower()}",
         f"limit={limit}",
         f"xsec_token={xsec_token}",
         f"feed_id={feed_id}"],
        capture_output=True, text=True, timeout=60
    )
    text = result.stdout

    # 解析外层 JSON
    start = text.find('{')
    if start < 0:
        print(f"    警告: 无法解析返回数据")
        return {}

    # 找到对应的闭合括号
    # 简单方法：找到第一个 { 开始的完整 JSON
    try:
        # 使用 JSONDecoder 的 raw_decode 来解析
        decoder = json.JSONDecoder()
        outer, idx = decoder.raw_decode(text[start:])
        # 返回的 data 字段可能是 JSON 字符串，也可能是字典
        data = outer.get('data', {})
        if isinstance(data, str):
            return json.loads(data)
        return data  # 直接返回 data 部分
    except Exception as e:
        print(f"    警告: 解析失败 - {e}")
        return {}

def process_feed(feed: dict, index: int) -> dict:
    """处理单条feed，下载完整内容"""
    note = feed.get('noteCard', {})
    title = note.get('displayTitle', f'无标题_{index}')
    title = sanitize_filename(title)
    note_type = note.get('type', 'normal')  # video 或 normal

    note_id = feed.get('id', '')
    xsec_token = feed.get('xsecToken', '')

    # 创建文件夹
    folder_name = f"{index:02d}_{title}"
    folder_path = DOWNLOAD_DIR / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    result = {
        'index': index,
        'title': title,
        'note_id': note_id,
        'type': note_type,
        'folder': str(folder_path),
        'xsec_token': xsec_token,
        'images': [],
        'videos': [],
        'cover': ''
    }

    # 获取笔记详情
    print(f"  获取笔记详情: {note_id}")
    detail = get_feed_detail(note_id, xsec_token)

    # 解析详情数据
    note_detail = detail.get('note', {})

    # ===== 下载图片 =====
    image_urls = []

    # 从详情中获取所有图片 (note.imageList)
    image_list = note_detail.get('imageList', [])
    for img in image_list:
        if isinstance(img, dict):
            url = img.get('urlDefault', '') or img.get('url', '')
            if url:
                image_urls.append(url)
        elif isinstance(img, str):
            image_urls.append(img)

    # 如果没有图片，尝试从封面获取
    if not image_urls:
        cover = note.get('cover', {})
        cover_url = cover.get('urlDefault', '')
        if cover_url:
            image_urls.append(cover_url)

    # 下载所有图片
    for i, img_url in enumerate(image_urls):
        ext = '.jpg'
        if 'webp' in img_url.lower():
            ext = '.webp'
        elif 'png' in img_url.lower():
            ext = '.png'

        img_path = folder_path / f"image_{i+1:02d}{ext}"
        print(f"  下载图片 {i+1}/{len(image_urls)}: {img_path.name}")
        if download_file(img_url, img_path):
            result['images'].append(str(img_path))

    # ===== 下载视频 =====
    # 注意：小红书 MCP 的 get_feed_detail 不返回视频 URL，只从 feed 获取视频信息
    if note_type == 'video':
        # 构建小红书链接
        xsec_token = feed.get('xsecToken', '')
        note_id = feed.get('id', '')
        xhs_url = f"https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}&xsec_source=pc_feed"

        # 使用 yt-dlp 下载视频
        print(f"  使用 yt-dlp 下载视频...")
        video_path = download_video(xhs_url, folder_path)
        if video_path:
            result['videos'].append(video_path)
            print(f"  ✓ 视频下载成功: {Path(video_path).name}")

    # ===== 提取文案/标题 =====
    # 尝试多种字段获取文案
    content = note_detail.get('desc', '') or note_detail.get('content', '')

    # ===== 提取评论 =====
    comments = []
    # 评论在 comments.list 里面
    comments_data = detail.get('comments', {})
    comment_list = comments_data.get('list', []) if isinstance(comments_data, dict) else []

    # 按赞数降序排序
    def get_like_count(c):
        lc = c.get('likeCount', '0')
        try:
            return int(lc) if lc else 0
        except:
            return 0

    # 时间戳转换函数
    def format_time(ts):
        if not ts:
            return ''
        try:
            # 毫秒转秒
            ts = int(ts)
            if ts > 1e12:  # 毫秒
                ts = ts // 1000
            import datetime
            dt = datetime.datetime.fromtimestamp(ts)
            now = datetime.datetime.now()
            diff = now - dt
            if diff.days > 365:
                return f"{diff.days // 365}年前"
            elif diff.days > 30:
                return f"{diff.days // 30}个月前"
            elif diff.days > 0:
                return f"{diff.days}天前"
            elif diff.seconds > 3600:
                return f"{diff.seconds // 3600}小时前"
            elif diff.seconds > 60:
                return f"{diff.seconds // 60}分钟前"
            else:
                return "刚刚"
        except:
            return ''

    comment_list.sort(key=get_like_count, reverse=True)

    comment_count = len(comment_list)  # 正确的评论数量
    for comment in comment_list:  # 获取所有评论
        user_info = comment.get('userInfo', {})
        nickname = user_info.get('nickname', '未知用户')
        text = comment.get('content', '')
        like_count = comment.get('likeCount', '0')  # 点赞数
        ip_location = comment.get('ipLocation', '')  # IP归属地
        sub_comment_count = comment.get('subCommentCount', '')  # 子评论数量
        create_time = comment.get('createTime', '')  # 发布时间
        time_str = format_time(create_time) if create_time else ''
        if text:
            # 构建评论信息，包含点赞数、归属地、子评论数和发布时间
            comment_info = f"用户: {nickname}"
            if like_count and like_count != '0':
                comment_info += f" ❤️{like_count}"
            if ip_location:
                comment_info += f" 📍{ip_location}"
            if sub_comment_count and sub_comment_count != '0':
                comment_info += f" 💬{sub_comment_count}"
            if time_str:
                comment_info += f" ⏰{time_str}"
            comment_info += f"\n评论: {text}"
            comments.append(comment_info)

            # 提取回复 - 只输出非0赞的回复
            sub_comments = comment.get('subComments', [])
            if sub_comments:
                # 按赞数排序
                sub_comments.sort(key=get_like_count, reverse=True)
                for sub in sub_comments:
                    sub_user = sub.get('userInfo', {})
                    sub_nickname = sub_user.get('nickname', '未知用户')
                    sub_text = sub.get('content', '')
                    sub_like = sub.get('likeCount', '0')  # 回复点赞数
                    sub_time = sub.get('createTime', '')
                    sub_time_str = format_time(sub_time) if sub_time else ''
                    # 只输出非0赞的回复
                    if sub_text and sub_like and sub_like != '0':
                        reply_info = f"  └ 回复: {sub_nickname} ❤️{sub_like}"
                        if sub_time_str:
                            reply_info += f" ⏰{sub_time_str}"
                        reply_info += f": {sub_text}"
                        comments.append(reply_info)
            comments.append("")

    # ===== 提取视频信息 =====
    video_info = {}
    if note_type == 'video':
        # 尝试从 feed 的 noteCard 获取视频信息
        video = note.get('video', {})
        capa = video.get('capa', {})
        duration = capa.get('duration', 0)
        video_info = {
            'duration': duration,  # 秒数
            'width': video.get('width', 0),
            'height': video.get('height', 0),
            'hasAudio': video.get('hasAudio', True),
            'bitrate': video.get('bitrate', 0),
        }

    # ===== 保存文本信息 =====
    txt_lines = []

    # 标题
    txt_lines.append(f"标题: {title}")
    txt_lines.append(f"笔记ID: {note_id}")
    txt_lines.append(f"类型: {'视频' if note_type == 'video' else '图文'}")
    txt_lines.append("")

    # 链接
    xsec_token = feed.get('xsecToken', '')
    link = f"https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}&xsec_source=pc_feed"
    txt_lines.append(f"链接: {link}")
    txt_lines.append("")

    # 文案/内容
    if content:
        txt_lines.append("=" * 40)
        txt_lines.append("文案内容:")
        txt_lines.append("=" * 40)
        txt_lines.append(content)
        txt_lines.append("")

    # 视频信息
    if note_type == 'video' and video_info:
        txt_lines.append("=" * 40)
        txt_lines.append("视频信息:")
        txt_lines.append("=" * 40)
        duration = video_info.get('duration', 0)
        minutes = duration // 60
        seconds = duration % 60
        txt_lines.append(f"时长: {minutes}分{seconds}秒")
        if result['videos']:
            txt_lines.append(f"视频文件: video.mp4")
        else:
            txt_lines.append(f"提示: 视频文件下载失败，请通过链接手动下载")
            txt_lines.append(f"链接: {link}")
        txt_lines.append("")

    # 评论
    if comments:
        txt_lines.append("=" * 40)
        txt_lines.append(f"评论 (共{comment_count}条):")
        txt_lines.append("=" * 40)
        txt_lines.extend(comments)
    else:
        txt_lines.append("=" * 40)
        txt_lines.append("评论: 无")
        txt_lines.append("")

    # 写入txt文件
    txt_path = folder_path / "info.txt"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(txt_lines))

    print(f"  ✓ 已保存: info.txt")
    result['cover'] = result['images'][0] if result['images'] else ''

    return result

def parse_url(url: str) -> tuple:
    """解析小红书链接，提取 note_id 和 xsec_token"""
    from urllib.parse import urlparse, parse_qs

    # 处理短链接 (xhslink.com)
    if 'xhslink.com' in url:
        import subprocess
        result = subprocess.run(
            ['curl', '-sL', url, '-w', '%{url_effective}', '-o', '/dev/null'],
            capture_output=True, text=True, timeout=10
        )
        final_url = result.stdout.strip()
        if final_url and 'xiaohongshu.com' in final_url:
            url = final_url

    # 提取 note_id
    note_id = ''
    if '/explore/' in url:
        # https://www.xiaohongshu.com/explore/xxx?xsec_token=...
        parts = url.split('/explore/')
        if len(parts) > 1:
            id_part = parts[1].split('?')[0]
            note_id = id_part
    elif '/discovery/item/' in url:
        # https://www.xiaohongshu.com/discovery/item/xxx?...
        parts = url.split('/discovery/item/')
        if len(parts) > 1:
            id_part = parts[1].split('?')[0]
            note_id = id_part

    # 提取 xsec_token
    xsec_token = ''
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if 'xsec_token' in query:
        xsec_token = query['xsec_token'][0]

    return note_id, xsec_token


def process_single_url(url: str) -> dict:
    """处理单个小红书链接，下载完整内容"""
    note_id, xsec_token = parse_url(url)

    if not note_id:
        print(f"  ✗ 无法从链接中提取笔记ID: {url}")
        return None

    print(f"  note_id: {note_id}")
    print(f"  xsec_token: {xsec_token}")

    # 调用 MCP 获取笔记详情
    print(f"  获取笔记详情...")
    detail = get_feed_detail(note_id, xsec_token)

    if not detail:
        print(f"  ✗ 获取笔记详情失败")
        return None

    # 解析详情数据
    note_detail = detail.get('note', {})

    # 获取标题
    title = note_detail.get('title', note_detail.get('desc', ''))
    if not title:
        title = note_detail.get('content', '无标题')
    title = sanitize_filename(title)
    if not title or title == '无标题':
        title = f'笔记_{note_id[:8]}'

    # 确定笔记类型
    note_type = note_detail.get('type', 'normal')
    if not note_type:
        # 尝试从 video 字段判断
        note_type = 'video' if note_detail.get('video') else 'normal'

    # 创建文件夹 (使用 99_ 前缀表示单条)
    folder_name = f"99_{title}"
    folder_path = DOWNLOAD_DIR / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    result = {
        'index': 1,
        'title': title,
        'note_id': note_id,
        'type': note_type,
        'folder': str(folder_path),
        'xsec_token': xsec_token,
        'images': [],
        'videos': [],
        'cover': ''
    }

    # ===== 下载图片 =====
    image_urls = []
    image_list = note_detail.get('imageList', [])
    for img in image_list:
        if isinstance(img, dict):
            url = img.get('urlDefault', '') or img.get('url', '')
            if url:
                image_urls.append(url)
        elif isinstance(img, str):
            image_urls.append(img)

    # 如果没有图片，尝试从封面获取
    if not image_urls:
        cover = note_detail.get('cover', {})
        cover_url = cover.get('urlDefault', '')
        if cover_url:
            image_urls.append(cover_url)

    # 下载所有图片
    for i, img_url in enumerate(image_urls):
        ext = '.jpg'
        if 'webp' in img_url.lower():
            ext = '.webp'
        elif 'png' in img_url.lower():
            ext = '.png'

        img_path = folder_path / f"image_{i+1:02d}{ext}"
        print(f"  下载图片 {i+1}/{len(image_urls)}: {img_path.name}")
        if download_file(img_url, img_path):
            result['images'].append(str(img_path))

    # ===== 下载视频 =====
    if note_type == 'video':
        # 构建小红书链接
        xhs_url = f"https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}&xsec_source=pc_feed"

        # 使用 yt-dlp 下载视频
        print(f"  使用 yt-dlp 下载视频...")
        video_path = download_video(xhs_url, folder_path)
        if video_path:
            result['videos'].append(video_path)
            print(f"  ✓ 视频下载成功: {Path(video_path).name}")

    # ===== 提取文案/标题 =====
    content = note_detail.get('desc', '') or note_detail.get('content', '')

    # ===== 提取评论 =====
    comments = []
    comments_data = detail.get('comments', {})
    comment_list = comments_data.get('list', []) if isinstance(comments_data, dict) else []

    def get_like_count(c):
        lc = c.get('likeCount', '0')
        try:
            return int(lc) if lc else 0
        except:
            return 0

    def format_time(ts):
        if not ts:
            return ''
        try:
            ts = int(ts)
            if ts > 1e12:
                ts = ts // 1000
            import datetime
            dt = datetime.datetime.fromtimestamp(ts)
            now = datetime.datetime.now()
            diff = now - dt
            if diff.days > 365:
                return f"{diff.days // 365}年前"
            elif diff.days > 30:
                return f"{diff.days // 30}个月前"
            elif diff.days > 0:
                return f"{diff.days}天前"
            elif diff.seconds > 3600:
                return f"{diff.seconds // 3600}小时前"
            elif diff.seconds > 60:
                return f"{diff.seconds // 60}分钟前"
            else:
                return "刚刚"
        except:
            return ''

    comment_list.sort(key=get_like_count, reverse=True)

    comment_count = len(comment_list)
    for comment in comment_list:
        user_info = comment.get('userInfo', {})
        nickname = user_info.get('nickname', '未知用户')
        text = comment.get('content', '')
        like_count = comment.get('likeCount', '0')
        ip_location = comment.get('ipLocation', '')
        sub_comment_count = comment.get('subCommentCount', '')
        create_time = comment.get('createTime', '')
        time_str = format_time(create_time) if create_time else ''
        if text:
            comment_info = f"用户: {nickname}"
            if like_count and like_count != '0':
                comment_info += f" ❤️{like_count}"
            if ip_location:
                comment_info += f" 📍{ip_location}"
            if sub_comment_count and sub_comment_count != '0':
                comment_info += f" 💬{sub_comment_count}"
            if time_str:
                comment_info += f" ⏰{time_str}"
            comment_info += f"\n评论: {text}"
            comments.append(comment_info)

            sub_comments = comment.get('subComments', [])
            if sub_comments:
                sub_comments.sort(key=get_like_count, reverse=True)
                for sub in sub_comments:
                    sub_user = sub.get('userInfo', {})
                    sub_nickname = sub_user.get('nickname', '未知用户')
                    sub_text = sub.get('content', '')
                    sub_like = sub.get('likeCount', '0')
                    sub_time = sub.get('createTime', '')
                    sub_time_str = format_time(sub_time) if sub_time else ''
                    if sub_text and sub_like and sub_like != '0':
                        reply_info = f"  └ 回复: {sub_nickname} ❤️{sub_like}"
                        if sub_time_str:
                            reply_info += f" ⏰{sub_time_str}"
                        reply_info += f": {sub_text}"
                        comments.append(reply_info)
            comments.append("")

    # ===== 提取视频信息 =====
    video_info = {}
    if note_type == 'video':
        video = note_detail.get('video', {})
        capa = video.get('capa', {})
        duration = capa.get('duration', 0)
        video_info = {
            'duration': duration,
            'width': video.get('width', 0),
            'height': video.get('height', 0),
            'hasAudio': video.get('hasAudio', True),
            'bitrate': video.get('bitrate', 0),
        }

    # ===== 保存文本信息 =====
    txt_lines = []
    txt_lines.append(f"标题: {title}")
    txt_lines.append(f"笔记ID: {note_id}")
    txt_lines.append(f"类型: {'视频' if note_type == 'video' else '图文'}")
    txt_lines.append("")

    link = f"https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}&xsec_source=pc_feed"
    txt_lines.append(f"链接: {link}")
    txt_lines.append("")

    if content:
        txt_lines.append("=" * 40)
        txt_lines.append("文案内容:")
        txt_lines.append("=" * 40)
        txt_lines.append(content)
        txt_lines.append("")

    if note_type == 'video' and video_info:
        txt_lines.append("=" * 40)
        txt_lines.append("视频信息:")
        txt_lines.append("=" * 40)
        duration = video_info.get('duration', 0)
        minutes = duration // 60
        seconds = duration % 60
        txt_lines.append(f"时长: {minutes}分{seconds}秒")
        if result['videos']:
            txt_lines.append(f"视频文件: video.mp4")
        else:
            txt_lines.append(f"提示: 视频文件下载失败，请通过链接手动下载")
            txt_lines.append(f"链接: {link}")
        txt_lines.append("")

    if comments:
        txt_lines.append("=" * 40)
        txt_lines.append(f"评论 (共{comment_count}条):")
        txt_lines.append("=" * 40)
        txt_lines.extend(comments)
    else:
        txt_lines.append("=" * 40)
        txt_lines.append("评论: 无")
        txt_lines.append("")

    txt_path = folder_path / "info.txt"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(txt_lines))

    print(f"  ✓ 已保存: info.txt")
    result['cover'] = result['images'][0] if result['images'] else ''

    return result


def main(count: int = 5, url: str = None):
    print("=" * 50)
    print("小红书内容下载器 - 完整版")
    print("=" * 50)

    # 如果提供了单链接模式
    if url:
        print(f"\n[1/2] 处理单条链接...")
        print(f"  URL: {url}")

        result = process_single_url(url)

        if result:
            # 保存元数据
            print(f"\n[2/2] 保存元数据...")
            metadata = {
                'total': 1,
                'feeds': [result]
            }
            metadata_path = DOWNLOAD_DIR / "metadata.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)

            print(f"\n✓ 完成！内容已保存到: {result['folder']}")
            print(f"  文件夹: {result['folder']}")

            # 列出文件夹内容
            print("\n文件夹内容:")
            for f in Path(result['folder']).iterdir():
                print(f"  - {f.name}")

            return [result]
        else:
            print("\n✗ 处理失败")
            return []

    # 1. 获取首页 feeds
    print("\n[1/3] 获取首页推荐...")
    result = subprocess.run(
        ["mcporter", "call", "xiaohongshu-mcp", "list_feeds"],
        capture_output=True, text=True
    )

    text = result.stdout
    start = text.find('{')
    if start < 0:
        print("获取数据失败")
        return

    data = json.loads(text[start:])
    feeds = data.get('feeds', [])
    print(f"获取到 {len(feeds)} 条笔记")

    # 2. 下载前 N 条内容
    print(f"\n[2/3] 下载内容到 {DOWNLOAD_DIR}...")
    results = []
    for i, feed in enumerate(feeds[:count]):
        print(f"\n处理 {i+1}/{count}: {feed.get('noteCard', {}).get('displayTitle', '无标题')[:30]}...")
        try:
            r = process_feed(feed, i+1)
            results.append(r)
        except Exception as e:
            print(f"  ✗ 处理失败: {e}")

    # 3. 保存元数据
    print(f"\n[3/3] 保存元数据...")
    metadata = {
        'total': len(results),
        'feeds': results
    }
    metadata_path = DOWNLOAD_DIR / "metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"\n完成！内容已保存到: {DOWNLOAD_DIR}")
    print(f"共处理 {len(results)} 条内容")

    # 列出文件夹
    print("\n文件夹列表:")
    for item in sorted(DOWNLOAD_DIR.iterdir()):
        if item.is_dir():
            files = list(item.iterdir())
            print(f"  📁 {item.name}")
            for f in files:
                print(f"      - {f.name}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='小红书内容下载器')
    parser.add_argument('-n', '--count', type=int, default=5,
                        help='下载数量，默认5条')
    parser.add_argument('-u', '--url', type=str, default=None,
                        help='小红书帖子链接，支持单条下载')
    args = parser.parse_args()
    main(args.count, args.url)
