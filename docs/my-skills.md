# Claude Code Skills 使用指南

本文档介绍本项目可用的所有 skills。

---

## 笔记与学习

| Skill | 功能 | 介绍 |
|-------|------|------|
| `latex-notes` | 生成 LaTeX 讲义 | 生成 LaTeX 格式的学习讲义，包含用户注解、问题、Stein 风格的 motivation 写作 |
| `obsidian-cli` | Obsidian 命令行 | 通过 CLI 与 Obsidian 交互，读取、创建、搜索笔记，管理任务和属性 |
| `obsidian-markdown` | Obsidian 格式 | 创建/编辑 Obsidian Flavored Markdown，支持 wikilinks、embeds、callouts、properties |
| `reading-progress` | 阅读进度 | 管理阅读进度，包括当前阅读位置、历史提问、章节状态 |
| `reading-workflow` | 主工作流 | 协调扫描阶段、逐章阅读、问答、讲义生成的完整流程 |
| `interactive-qa` | 交互问答 | 理解当前阅读位置，实时回答问题并同步更新讲义 |
| `skim-jump` | PDF 跳转 | 使用 Skim PDF 阅读器的 displayline 功能跳转到笔记 TeX 文件的特定行号 |

---

## 文献处理

| Skill | 功能 | 介绍 |
|-------|------|------|
| `paper-references-generator` | 生成 BibTeX | 从论文 md 转录文件提取参考文献列表，使用 CrossRef API 搜索获取 DOI 并生成 BibTeX |
| `citation-bibliography-generator` | 格式化引用 | 格式化引用为 APA/MLA/Chicago/IEEE/Harvard 等格式，支持 DOI/ISBN 查询 |
| `literature-reference-manager` | 文献管理 | 扫描文献库，提取参考文献，从 CrossRef/Google Scholar 获取标准 BibTeX |
| `gs-search` | Google Scholar | 搜索学术论文，返回标题、作者、期刊、年份、引用数和全文链接 |
| `literature-notes-template` | 文献笔记模板 | 标准化文献笔记格式 |

---

## PDF 处理

| Skill | 功能 | 介绍 |
|-------|------|------|
| `pdf-figure-extractor` | 提取插图 | 从教材 PDF 或图片中自动提取数学插图，600 DPI 高清渲染，Gemini Vision 识别裁剪 |
| `pdf-reader` | 解析 PDF | 解析 PDF 文献，提取章节结构，理解内容框架 |
| `pdf-merger` | 合并 PDF | 合并多个 PDF 文件（简历、自我陈述、商业计划书等） |
| `figure-extractor` | 提取图片 | 从文档中提取 figure 图片 |

---

## 演示与文档

| Skill | 功能 | 介绍 |
|-------|------|------|
| `frontend-slides` | HTML 演示 | 创建精美的动画 HTML 演示文稿，或转换 PPT/PPTX |
| `beamer-chinese-presentation` | Beamer 演示 | 使用 LaTeX Beamer 创建中文演示，支持 SYPSTLE/CambridgeUS 主题 |
| `pptx` | PPT 处理 | 创建、编辑、解析 PowerPoint 文件 |
| `docx` | Word 处理 | 创建、编辑 Word 文档 |

---

## AI 工具

| Skill | 功能 | 介绍 |
|-------|------|------|
| `gemini-browser-chat` | Gemini 对话 | 通过 Playwright 浏览器与 Gemini 对话，适合数学问题、复杂推理（必须用 Pro 模式） |
| `gemini-image-generation` | 图片生成 | 使用 Google Gemini API 生成图片 |
| `gemini-video-understanding` | 视频理解 | 分析视频内容，描述、转录、剪辑 |
| `ai-image-generation` | AI 画图 | FLUX/Grok/Seedream 等 50+ 模型生成图片 |
| `minimax-vision` | 视觉分析 | Minmax 视觉模型分析 |

---

## 代码与开发

| Skill | 功能 | 介绍 |
|-------|------|------|
| `auto-commit-push` | 自动提交 | 自动 git add/commit/push，大文件自动检查，规范提交信息 |
| `latex-debug` | LaTeX 调试 | 检测并修复 LaTeX 编译错误，修复后自动提交 |
| `latex-label-ref-verifier` | 标签验证 | 验证 LaTeX 文档中的 label 和引用 |
| `note-content-verifier` | 内容验证 | 验证笔记内容完整性 |
| `chapter0-template` | 章节模板 | 生成章节模板 |
| `mcp-builder` | MCP 服务器 | 构建 MCP 服务器使 LLM 与外部服务交互 |
| `skill-creator` | 创建 Skill | 从零创建新 skill，修改优化现有 skill |

---

## 视频平台

| Skill | 功能 | 介绍 |
|-------|------|------|
| `bilibili-subtitle` | B站字幕 | 从 Bilibili 视频提取字幕，转录无字幕视频，生成结构化摘要 |
| `youtube-transcript` | YouTube 字幕 | 下载 YouTube 视频字幕 |
| `video-summary` | 视频笔记 | 从字幕生成结构化视频笔记 |
| `youtube-data` | YouTube 数据 | 搜索视频、获取详情、评论、热榜 |

---

## 数据分析

| Skill | 功能 | 介绍 |
|-------|------|------|
| `r-expert` | R 专家 | 高级 R 统计分析、数据分析、可视化 |
| `weather-collector` | 气温采集 | 采集城市气温预报数据（24小时），保存到 Obsidian |
| `polymarket-data-collector` | 预测市场 | 采集 Polymarket 气温预测数据，生成报告 |

---

## 工作流

| Skill | 功能 | 介绍 |
|-------|------|------|
| `homework-workflow` | 作业流程 | 管理作业提交的工作流 |
| `interactive-qa-schubert` | Schubert 问答 | Schubert 多项式专题的交互问答 |

---

## 其他工具

| Skill | 功能 | 介绍 |
|-------|------|------|
| `json-canvas` | Canvas 文件 | 创建/编辑 JSON Canvas 文件（节点、边、分组连接） |
| `defuddle` | 网页提取 | 提取网页干净内容，移除广告导航 |
| `find-skills` | 查找 Skill | 查找和安装新 skills |
| `document-skills:canvas-design` | 画布设计 | 创建 PNG/PDF 视觉艺术 |
| `document-skills:algorithmic-art` | 算法艺术 | 用 p5.js 创建算法艺术 |
| `playground` | 交互 playground | 创建交互式 HTML 探索器 |

---

## Claude Code 超级能力

| Skill | 功能 | 介绍 |
|-------|------|------|
| `superpowers:brainstorming` | 头脑风暴 | 创造性工作前必须使用，探索意图和需求 |
| `superpowers:systematic-debugging` | 系统调试 | 遇到 bug、测试失败时使用 |
| `superpowers:test-driven-development` | TDD | 实现功能/修复前编写测试 |
| `superpowers:writing-plans` | 写作计划 | 多步骤任务前编写实施计划 |
| `superpowers:executing-plans` | 执行计划 | 在单独会话中执行计划 |
| `superpowers:verification-before-completion` | 验证完成 | 声称完成前运行验证 |
| `superpowers:requesting-code-review` | 代码审查 | 完成任务后请求审查 |
| `superpowers:finishing-a-development-branch` | 完成分支 | 开发分支完成后的整合选项 |
| `superpowers:dispatching-parallel-agents` | 并行代理 | 2+ 独立任务并行处理 |
| `superpowers:subagent-driven-development` | 子代理开发 | 使用子代理执行计划 |
| `superpowers:receiving-code-review` | 接收审查 | 收到审查反馈时使用 |
| `superpowers:writing-skills` | 编写 Skills | 创建或编辑 skills |
| `superpowers:using-git-worktrees` | Git Worktree | 需要隔离时创建 git worktree |

---

## 使用方式

在 Claude Code 中，使用 `/skill-name` 调用。例如：

```bash
/gs-search 关键词
/latex-notes
/pdf-figure-extractor
```
