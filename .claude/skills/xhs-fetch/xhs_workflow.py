#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书内容采集分析自动化流程
1. 调用 download_xhs.py 下载内容到文件夹
2. 对每个文件夹调用 analyze_folder.py 分析
3. 对每个文件夹生成书面稿 (generate_script.py)
4. 增量同步到 Obsidian
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

# ========== 配置 ==========
SCRIPT_DIR = Path(__file__).parent
DOWNLOAD_SCRIPT = SCRIPT_DIR / "download_xhs.py"
ANALYZE_SCRIPT = SCRIPT_DIR / "analyze_folder.py"
GENERATE_SCRIPT = SCRIPT_DIR / "generate_script.py"

XHS_DIR = Path.home() / "tmp" / "xhs"
OBSIDIAN_VAULT = Path.home() / "Library" / "Mobile Documents" / "iCloud~md~obsidian" / "Documents" / "2026-spring" / "xhs"

# 确保输出目录存在
OBSIDIAN_VAULT.mkdir(parents=True, exist_ok=True)

# Obsidian 输出文件
OUTPUT_MD = OBSIDIAN_VAULT / "小红书首页推荐.md"


def run_download(count: int = 5, url: str = None):
    """调用 download_xhs.py 下载内容"""
    if url:
        print(f"\n[1/3] 下载单条链接...")
        print(f"    URL: {url}")
        result = subprocess.run(
            ["python3", str(DOWNLOAD_SCRIPT), "-u", url],
            capture_output=True, text=True
        )
    else:
        print(f"\n[1/3] 下载内容 (下载 {count} 条)...")
        result = subprocess.run(
            ["python3", str(DOWNLOAD_SCRIPT), "-n", str(count)],
            capture_output=True, text=True
        )

    if result.returncode != 0:
        print(f"    ❌ 下载失败: {result.stderr}")
        return []
    print(f"    ✓ 下载完成")
    return []


def get_downloaded_folders() -> list:
    """获取已下载的文件夹列表"""
    folders = []
    if not XHS_DIR.exists():
        return folders

    for item in sorted(XHS_DIR.iterdir()):
        if item.is_dir() and item.name[0].isdigit():
            folders.append(item)
    return folders


def analyze_folder(folder: Path, mode: str) -> str:
    """调用 analyze_folder.py 分析单个文件夹"""
    print(f"    分析: {folder.name}")
    result = subprocess.run(
        ["python3", str(ANALYZE_SCRIPT), str(folder), "-m", mode],
        capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        return f"❌ 分析失败: {result.stderr}"

    output = result.stdout

    # 方案1: 找 "📊 分析结果" 或 "===" 后的内容
    lines = output.split('\n')
    analysis_lines = []
    capture = False

    for i, line in enumerate(lines):
        # 开始捕获：找到分析结果标记
        if '📊' in line and '分析' in line:
            capture = True
            continue
        # 跳过分隔线
        if capture and line.strip().startswith('=='):
            continue
        # 遇到下一个非空非分隔线时开始记录
        if capture and line.strip():
            # 如果是新的笔记标题（数字开头），停止
            if i > 0 and lines[i-1].strip() == '' and lines[i-2].strip() == '---':
                break
            analysis_lines.append(line)

    if analysis_lines:
        return '\n'.join(analysis_lines).strip()

    # 方案2: 直接返回包含 "===【" 的内容块
    if "===【" in output:
        start = output.find("===【")
        return output[start:].strip()

    # 方案3: 返回原输出（如果有错误信息）
    if "错误" in output or "❌" in output:
        return output

    # 兜底：返回最后50行
    return '\n'.join(lines[-50:]).strip()

    return '\n'.join(analysis_lines) if analysis_lines else output


def extract_toc_entries(content: str) -> list:
    """从现有内容中提取目录条目（只提取笔记标题，跳过分析结果中的小标题）"""
    import re
    entries = []
    pattern = r'^### (.+)$'
    matches = re.findall(pattern, content, re.MULTILINE)

    for title in matches:
        anchor = title.strip()
        # 跳过分析结果中的小标题（包含 【】 或 **）
        if anchor and '【' not in anchor and not anchor.startswith('**'):
            entries.append(anchor)

    return entries


def generate_toc(entries: list) -> str:
    """生成目录"""
    if not entries:
        return ""

    lines = ["## 目录\n"]
    for i, title in enumerate(entries, 1):
        clean_title = title.replace('|', '-').replace('#', '')
        lines.append(f"{i}. [[#{clean_title}|{title}]]\n")

    return ''.join(lines)


def clean_old_toc(content: str) -> str:
    """删除所有旧的目录，保留内容部分"""
    import re

    lines = content.split('\n')
    result_lines = []
    skip_mode = False

    for line in lines:
        if line.strip() == '## 目录':
            skip_mode = True
            continue

        if skip_mode and re.match(r'^## \d{4}-\d{2}-\d{2}', line):
            skip_mode = False
            result_lines.append(line)
        elif not skip_mode:
            result_lines.append(line)

    result = '\n'.join(result_lines)
    if not result.endswith('\n'):
        result += '\n'

    return result


def append_to_obsidian(results: list):
    """增量写入 Obsidian"""
    print(f"\n[4/4] 同步到 Obsidian...")

    # 读取现有内容
    existing = ""
    if OUTPUT_MD.exists():
        existing = OUTPUT_MD.read_text(encoding='utf-8')

    # 生成新内容
    new_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    new_lines = [f"\n## {new_timestamp}\n"]

    for r in results:
        title = r.get('title', '未知')
        analysis = r.get('analysis', '')
        script = r.get('script', '')
        link = r.get('link', '')
        note_type = r.get('type', '图文')

        new_lines.append(f"### {title}\n")
        new_lines.append(f"- 类型: {note_type}\n")
        # 使用可点击的 Markdown 链接格式
        new_lines.append(f"- 链接: [查看原文 →]({link})\n\n")

        # 添加书面稿（如果有）
        if script:
            new_lines.append("## 书面稿\n")
            new_lines.append(script)
            new_lines.append("\n\n---\n\n")

        # 添加分析
        new_lines.append(analysis)
        new_lines.append("\n\n---\n")

    new_content = ''.join(new_lines)

    # 合并内容
    if existing:
        content = clean_old_toc(existing)
        content = content + new_content
    else:
        content = f"""# 小红书首页推荐

采集时间: {new_timestamp}
数据来源: 首页推荐

""" + new_content

    # 重新生成目录
    all_entries = extract_toc_entries(content)
    toc = generate_toc(all_entries)

    marker = "数据来源: 首页推荐"
    marker_pos = content.find(marker)
    if marker_pos > 0:
        header_end = content.find("\n", marker_pos)
        if header_end > 0:
            content = content[:header_end+1] + "\n" + toc + content[header_end+1:]

    OUTPUT_MD.write_text(content, encoding='utf-8')
    print(f"    ✓ 已同步到: {OUTPUT_MD}")
    print(f"    ✓ 目录已更新 ({len(all_entries)} 条)")


def generate_script_for_folder(folder: Path) -> str:
    """调用 generate_script.py 为文件夹生成书面稿"""
    print(f"    📝 生成书面稿: {folder.name}")
    result = subprocess.run(
        ["python3", str(GENERATE_SCRIPT), str(folder)],
        capture_output=True, text=True, timeout=600  # 10分钟超时，视频转录较慢
    )
    if result.returncode != 0:
        print(f"    ⚠️ 书面稿生成失败: {result.stderr[:100] if result.stderr else 'unknown'}")
        return ""

    # 读取生成的 script.txt
    script_path = folder / "script.txt"
    if script_path.exists():
        script_content = script_path.read_text(encoding='utf-8')
        print(f"    ✓ 书面稿已生成")
        return script_content
    else:
        print(f"    ⚠️ 未找到书面稿文件")
        return ""


def read_metadata() -> list:
    """读取下载的元数据"""
    metadata_path = XHS_DIR / "metadata.json"
    if not metadata_path.exists():
        return []

    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('feeds', [])
    except:
        return []


def main(count: int = 5, mode: str = "default", url: str = None):
    """主流程"""
    print("=" * 60)
    print("小红书内容采集分析自动化流程")
    if url:
        print(f"输入: 单链接")
    else:
        print(f"数量: {count} 条")
    print(f"模式: {mode}")
    print("=" * 60)

    # 1. 下载内容
    run_download(count, url)

    # 2. 读取元数据获取文件夹信息
    feeds = read_metadata()
    if not feeds:
        print("    ⚠️ 未找到下载记录")
        return

    # 如果是单链接模式，只分析1条；否则分析前 N 条
    if url:
        feeds = feeds[:1]
    else:
        feeds = feeds[:count]
    print(f"    共 {len(feeds)} 条待分析")

    # 3. 分析每个文件夹
    print(f"\n[2/4] 生成书面稿 + [3/4] 分析内容 (模式: {mode})...")
    results = []

    for feed in feeds:
        folder_path = feed.get('folder', '')
        if not folder_path:
            continue

        folder = Path(folder_path)
        if not folder.exists():
            continue

        # 分析
        analysis = analyze_folder(folder, mode)

        # 保存分析结果到文件夹
        (folder / "analysis.txt").write_text(analysis, encoding='utf-8')

        # 生成书面稿
        script = generate_script_for_folder(folder)

        # 构建结果
        note_type = feed.get('type', 'normal')
        note_id = feed.get('note_id', '')
        xsec_token = feed.get('xsec_token', '')

        result = {
            'title': feed.get('title', '未知'),
            'type': '视频' if note_type == 'video' else '图文',
            'analysis': analysis,
            'script': script,
            'link': f"https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}&xsec_source=pc_feed"
        }
        results.append(result)

    # 4. 同步到 Obsidian
    if results:
        append_to_obsidian(results)
    else:
        print("    ⚠️ 无分析结果可同步")

    print(f"\n✅ 完成！共处理 {len(results)} 条内容")


def parse_args():
    """解析命令行参数"""
    import argparse
    parser = argparse.ArgumentParser(description='小红书内容采集分析自动化流程')
    parser.add_argument('-n', '--count', type=int, default=5,
                        help='采集数量，默认5条')
    parser.add_argument('-m', '--mode', default='default',
                        choices=['default', 'summary', 'visual', 'monetize'],
                        help='分析模式: default(智能类型判断), summary(内容总结), visual(视觉策划), monetize(变现分析)')
    parser.add_argument('-u', '--url', type=str, default=None,
                        help='小红书帖子链接，支持单条下载分析')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.count, args.mode, args.url)
