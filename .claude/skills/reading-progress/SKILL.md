---
name: reading-progress
description: 管理阅读进度，包括当前阅读位置、历史提问、章节状态
user-invocable: true
---

# 阅读进度管理 Skill

## 功能

1. 记录当前阅读位置（第几章、哪一节）
2. 追踪每个章节的阅读状态（未读/在读/已读/有疑问）
3. 记录用户的提问历史
4. 展示阅读仪表盘

## 使用方式

- "我现在在读第3章第2节"
- "我不懂这个定理" - 自动记录问题位置
- "我的阅读进度怎么样了"
- "这一章我觉得很难"

## 数据存储

进度存储在 `reading-progress/progress.json` 和 `progress.md`

## 输出格式

生成进度仪表盘：
- JSON：机器可读
- Markdown：人类可读，可包含 Mermaid 图
