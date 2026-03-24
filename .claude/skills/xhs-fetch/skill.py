#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书首页爬取 Skill

功能: 获取小红书首页推荐，返回结构化数据
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any

# 添加路径
SKILL_ROOT = Path(__file__).parent
sys.path.insert(0, str(SKILL_ROOT.parent / "xhs-homepage-analysis" / "workflows"))

from adapters.mcp_adapter import XiaohongshuMCPAdapter


async def run(args: str = "") -> Dict[str, Any]:
    """运行 Skill"""

    # 注意: 这个函数会在 Claude Code 环境中被 MCP 工具调用结果触发
    # 实际的 MCP 调用由 Claude Code 处理，这里只负责解析

    return {
        "status": "ready",
        "message": "请使用 MCP 工具获取首页数据，然后传入解析"
    }


def parse_mcp_result(mcp_data: Dict) -> Dict[str, Any]:
    """解析 MCP 返回的数据"""

    adapter = XiaohongshuMCPAdapter()
    feeds = adapter.parse_feeds_from_mcp(mcp_data)

    result = {
        "total": len(feeds),
        "feeds": []
    }

    for feed in feeds:
        result["feeds"].append({
            "title": feed.title,
            "author": feed.author,
            "type": feed.type,
            "feed_id": feed.feed_id,
            "xsec_token": feed.xsec_token,
            "url": f"https://www.xiaohongshu.com/explore/{feed.feed_id}?xsec_token={feed.xsec_token}" if feed.feed_id and feed.xsec_token else "",
            "likes": feed.likes,
            "comments": feed.comments,
            "collects": feed.collects,
            "cover_url": feed.cover_url,
            "video_url": feed.video_url,
            "image_urls": feed.image_urls
        })

    return result


def format_markdown(feeds_data: Dict) -> str:
    """格式化为 Markdown 展示"""
    lines = [f"# 小红书首页推荐\n", f"共 {feeds_data['total']} 条笔记\n"]

    for i, feed in enumerate(feeds_data["feeds"][:10], 1):
        lines.append(f"### {i}. {feed['title']}")
        lines.append(f"- 作者: {feed['author']}")
        lines.append(f"- 类型: {'视频' if feed['type'] == 'video' else '图文'}")
        lines.append(f"- 点赞: {feed['likes']} | 评论: {feed['comments']} | 收藏: {feed['collects']}")
        lines.append(f"- [查看笔记]({feed['url']})")
        lines.append("")

    return "\n".join(lines)


# CLI 入口 (用于测试)
if __name__ == "__main__":
    import asyncio

    # 模拟测试
    print("请在 Claude Code 中使用 /xhs 命令调用此 Skill")
