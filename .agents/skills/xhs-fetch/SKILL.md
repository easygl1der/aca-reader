# 小红书内容爬取 (xhs-fetch)

## 概述

快速获取小红书首页推荐内容，支持下载笔记的完整内容（图片、视频、文案、评论）。

## 前置条件

1. **MCP 服务运行中**：
   - 进程：`/Users/yueyh/Downloads/xiaohongshu-mcp-darwin-arm64 -port :18060`
   - 地址：`http://localhost:18060`

2. **已登录账号**：使用 `check_login_status` 确认登录状态

3. **yt-dlp 已安装**（用于下载视频）：
   ```bash
   pip3 install yt-dlp
   ```

## 触发词

- `xhs`
- `小红书首页`
- `xhs fetch`
- `爬取小红书`
- `下载小红书`
- `小红书下载`
- `xhs workflow`
- `小红书分析`
- `xhs 自动分析`
- `小红书同步 obsidian`

## 功能列表

### 1. 检查登录状态
```bash
mcporter call xiaohongshu-mcp check_login_status
```

### 2. 获取首页推荐
```bash
mcporter call xiaohongshu-mcp list_feeds
```
返回首页推荐笔记列表，包含：标题、作者、笔记类型、xsec_token 等

### 3. 获取笔记详情
```bash
mcporter call xiaohongshu-mcp get_feed_detail click_more_replies=true xsec_token=xxx feed_id=xxx
```
返回笔记的详细内容（文案、评论、图片列表等）

### 4. 下载内容到本地（核心功能）

运行下载脚本，自动下载首页前5条笔记的完整内容：

```bash
python3 ~/.Codex/skills/xhs-fetch/download_xhs.py
```

## 下载功能

| 类型 | 下载内容 |
|------|----------|
| **图文笔记** | 所有图片 (image_01.webp, image_02.webp...) + 文案 + 评论（含回复） |
| **视频笔记** | 视频文件 (video.mp4) + 文案 + 评论（含回复） |

## 输出目录结构

```
~/tmp/xhs/
├── 01_笔记标题/
│   ├── image_01.webp      # 图文笔记的图片
│   ├── image_02.webp
│   ├── video.mp4           # 视频笔记的视频文件
│   └── info.txt            # 文案 + 评论 + 视频信息
├── 02_另一个笔记/
│   └── ...
├── 03_...
├── 04_...
├── 05_...
└── metadata.json           # 所有笔记的元数据
```

## info.txt 内容格式

```
标题: xxx
笔记ID: xxx
类型: 视频/图文

链接: https://www.xiaohongshu.com/explore/xxx?xsec_token=xxx

========================================
文案内容:
========================================
笔记正文内容...

========================================
视频信息: (仅视频笔记)
========================================
时长: 2分56秒
视频文件: video.mp4

========================================
评论 (共22条):
========================================
用户: xxx
评论: xxx
  └ 回复: xxx: xxx

用户: xxx
评论: xxx
```

## 链接格式

小红书笔记链接必须包含 `xsec_token` 参数：
```
https://www.xiaohongshu.com/explore/{note_id}?xsec_token={token}&xsec_source=pc_feed
```

xsec_token 从 list_feeds 返回数据的 `xsecToken` 字段获取。

## 注意事项

1. **视频下载**：使用 yt-dlp 从小红书网页提取视频 URL 并下载
2. **图片下载**：从 MCP 返回的 imageList 中提取所有图片 URL
3. **评论获取**：调用 get_feed_detail 获取评论列表，包含子回复
4. **下载数量**：默认下载首页前 5 条笔记，可在脚本中修改 `feeds[:5]` 参数

---

## 完整工作流：爬取 + 分析 + 同步 Obsidian

### 功能说明

一键完成以下全部流程：
1. 调用 download_xhs.py 下载首页推荐内容到 `~/tmp/xhs/` 文件夹
2. 对每个文件夹调用 analyze_folder.py 进行智能分析
3. 增量同步到 Obsidian (`~/Documents/2026-spring/xhs/小红书首页推荐.md`)

### 运行命令

```bash
# 默认模式（智能类型判断）- 采集首页5条
python3 ~/.Codex/skills/xhs-fetch/xhs_workflow.py -n 5

# 指定分析模式
python3 ~/.Codex/skills/xhs-fetch/xhs_workflow.py -n 5 -m summary      # 内容总结
python3 ~/.Codex/skills/xhs-fetch/xhs_workflow.py -n 5 -m visual      # 视觉策划
python3 ~/.Codex/skills/xhs-fetch/xhs_workflow.py -n 5 -m monetize    # 变现分析

# 单链接模式 - 直接分析你发送的小红书链接
python3 ~/.Codex/skills/xhs-fetch/xhs_workflow.py -u "https://www.xiaohongshu.com/explore/xxx?xsec_token=xxx"
python3 ~/.Codex/skills/xhs-fetch/xhs_workflow.py -u "链接" -m summary   # 单链接 + 指定模式
```

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-n, --count` | 采集数量（首页模式） | 5 |
| `-m, --mode` | 分析模式 | default |
| `-u, --url` | 小红书帖子链接（单链接模式） | 无 |

### 分析模式

| 模式 | 说明 |
|------|------|
| `default` | 智能类型判断，根据内容类型自动选择分析角度 |
| `summary` | 内容总结：核心要点、适用人群、行动建议 |
| `visual` | 视觉策划：封面设计、信息卡片、时间轴 |
| `monetize` | 变现分析：用户画像、信任构建、种草链路 |

### 输出示例

运行后会：
- 在 `~/tmp/xhs/` 创建文件夹，每条笔记一个文件夹
- 每个文件夹包含：`info.txt`（文案+评论）、`analysis.txt`（分析结果）、媒体文件
- 在 Obsidian 生成 `小红书首页推荐.md`，包含所有分析

### 增量同步

每次运行都会**追加**新内容到 Obsidian 文件，不会覆盖之前的记录。

### 严格空行规范

Obsidian Markdown 格式要求：
- 标题与内容之间必须有**空行**
- 列表项与段落之间必须有**空行**
- 有序/无序列表和纯文本之间必须有**空行**
- 不同区块之间必须有**空行**分隔

示例（正确格式）：
```markdown
## 2026-03-14 10:30

### 笔记标题
- 类型: 图文
- 链接: [xxx](url)

内容总结...

---

### 另一个笔记
- 要点1
- 要点2

下一段内容...
```

### 目录功能

Obsidian 文件中会自动生成目录，包含所有笔记标题的链接，点击可跳转到对应内容。每次运行后目录会自动更新。

---

## 独立脚本

### analyze_folder.py - 分析文件夹

分析已下载的小红书内容文件夹：

```bash
# 默认模式
python3 ~/.Codex/skills/xhs-fetch/analyze_folder.py ~/tmp/xhs/01_笔记标题 -m default

# 指定模式
python3 ~/.Codex/skills/xhs-fetch/analyze_folder.py ~/tmp/xhs/01_笔记标题 -m summary
python3 ~/.Codex/skills/xhs-fetch/analyze_folder.py ~/tmp/xhs/01_笔记标题 -m visual
python3 ~/.Codex/skills/xhs-fetch/analyze_folder.py ~/tmp/xhs/01_笔记标题 -m monetize
```

### download_xhs.py - 单独下载

只下载内容，不进行分析：

```bash
python3 ~/.Codex/skills/xhs-fetch/download_xhs.py
```

### 视频画质选项

在 `download_xhs.py` 中修改视频下载参数：

| 分辨率 | 参数值 | 预计大小 |
|--------|--------|----------|
| 480P | `best[height<=480]` | 5-15MB |
| 720P | `best[height<=720]` | 15-40MB |
| 1080P | `best` | 50-150MB |

默认：**最佳画质**

---

## 5. 书面稿生成器 (generate_script.py)

为下载的内容生成书面稿：
- **视频笔记**：使用 AssemblyAI 转录音频 → MiniMax 整理标点 → 书面稿
- **图文笔记**：整理文案为流畅的书面叙述

### 使用方法

```bash
# 为最新下载的文件夹生成书面稿
python3 ~/.Codex/skills/xhs-fetch/generate_script.py

# 为指定文件夹生成书面稿
python3 ~/.Codex/skills/xhs-fetch/generate_script.py ~/tmp/xhs/01_笔记标题
```

### 前置条件

1. **AssemblyAI API Key**（用于转录）：
   - 设置环境变量：`export ASSEMBLYAI_API_KEY="你的API Key"`
   - 免费版有 10 分钟转录时长限制

2. **MiniMax API**（用于整理标点，可选）：
   - 使用环境变量 `ANTHROPIC_AUTH_TOKEN`
   - 如果未设置，将使用原始转录文本（已带基本标点）

### 工作流程

```
视频 → ffmpeg 提取音频(mp3) → AssemblyAI 转录 → MiniMax 整理 → 书面稿
```

### 输出文件

在每个笔记文件夹中生成 `script.txt`，包含：
- 标题、类型
- 字幕书面稿（视频笔记）
- 文案书面稿（图文笔记）
