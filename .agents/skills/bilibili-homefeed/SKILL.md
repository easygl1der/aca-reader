# B站首页推荐爬取

## 概述

获取B站个性化首页推荐视频/热门视频/排行榜视频，支持多种分类和排序方式，返回包含完整视频链接的信息。

**区别说明**：
- **首页推荐** (`bili_homefeed`)：获取当前登录用户的个性化推荐，基于你的观看历史和兴趣
- **热门视频** (`bili_hot_videos`)：全站热门内容，所有人看到的都一样
- **排行榜** (`bili_rank`)：各分区排行榜，按播放量排序

## 触发词

### 批量推荐类
- `b站首页推荐`
- `B站推荐视频`
- `bilibili首页`
- `我的b站推荐`
- `爬取b站首页`
- `b站热门`
- `b站排行榜`
- `b站个性化推荐`
- `B站首页推荐总结`
- `批量总结B站视频`
- `获取首页视频并总结`
- `生成B站推荐报告`

### 单视频分析类
- `分析B站视频`
- `总结B站视频`
- `B站视频链接分析`
- `这个B站视频怎么样`
- `帮我看看这个视频`
- `https://www.bilibili.com/video/BVxxx`（直接输入链接）
- `https://b23.tv/xxxxxx`（短链接）

### 字幕提取类
- `提取B站字幕`
- `B站视频字幕`
- `视频文字稿`
- `提取字幕书面稿`
- `视频转文字`
- `B站转录`

## 使用方法

### 获取个性化首页推荐（推荐）

```
mcporter call bilibili-mcp bili_homefeed
```

获取当前登录用户的个性化推荐视频，与你在 B站 App/网页看到的"首页推荐"一致。

### 获取热门视频

```
mcporter call bilibili-mcp bili_hot_videos pn:=1 ps:=20
```

### 获取排行榜

```
# 全站排行榜
mcporter call bilibili-mcp bili_rank category:="all" day:=7

# 游戏区排行榜
mcporter call bilibili-mcp bili_rank category:="game" day:=3

# 知识区排行榜
mcporter call bilibili-mcp bili_rank category:="knowledge" day:=7
```

## 功能说明

1. **登录状态检查**：自动使用已登录的 MCP 凭证
2. **多种获取方式**：个性化推荐、热门视频、排行榜、分区排行
3. **返回完整信息**：标题、UP主、播放量、弹幕数、链接
4. **视频链接**：每个视频返回完整 B站链接，方便点击跳转
5. **短链接解析**：自动支持 b23.tv 短链接

## 输出格式

返回 Markdown 表格，包含以下列：
- 序号
- 标题
- UP主
- 播放
- 点赞
- 弹幕
- 分类
- 链接

## MCP 工具

### bili_homefeed - 个性化首页推荐

```bash
mcporter call bilibili-mcp bili_homefeed
```

获取当前登录用户的B站个性化首页推荐视频。

返回字段：
- `bvid`: 视频BV号
- `title`: 视频标题
- `author`: UP主名称
- `desc`: 视频简介
- `duration`: 视频时长（秒）
- `tname`: 视频分区
- `play`: 播放量
- `like`: 点赞数
- `danmaku`: 弹幕数
- `link`: 视频链接

### bili_hot_videos - 热门视频

```bash
mcporter call bilibili-mcp bili_hot_videos pn:=1 ps:=20
```

参数：
- `pn`: 页码，默认1
- `ps`: 每页数量，默认20，最大50

### bili_rank - 排行榜

```bash
mcporter call bilibili-mcp bili_rank category:="all" day:=7
```

参数：
- `category`: 分区
  - `all`=全站 `original`=原创 `rookie`=新人
  - `douga`=动画 `music`=音乐 `dance`=舞蹈 `game`=游戏
  - `knowledge`=知识 `technology`=科技 `sports`=运动 `car`=汽车
  - `life`=生活 `food`=美食 `animal`=动物 `fashion`=时尚
  - `ent`=娱乐 `cinephile`=影视
- `day`: 时间维度，`3`=三日 `7`=七日

## 输出示例

```
| 序号 | 标题 | UP主 | 播放 | 点赞 | 弹幕 | 分类 | 链接 |
|------|------|------|------|------|------|------|------|
| 1 | 视频标题 | UP主名 | 100万 | 5万 | 1000 | 知识 | [链接](https://www.bilibili.com/video/BVxxx) |
```

## 登录状态

当前已登录：
- UID: 352314171
- 用户名: yitwahyue

凭证由 MCP 自动管理，无需手动配置。

---

## 单视频分析功能

当用户提供 B站视频链接（或短链接）时，使用此功能进行单视频分析。

### 支持的链接格式

```
https://www.bilibili.com/video/BV1GoNKzTE37
https://b23.tv/l3uBHId
BV1GoNKzTE37
```

### 短链接解析

自动解析 b23.tv 短链接，获取完整的 BV号。

### 使用流程

#### Step 1: 解析链接获取 BV号

- 标准链接：直接提取 BV号
- 短链接：通过 HTTP 请求获取重定向后的 URL，提取 BV号

#### Step 2: 获取视频信息

```
mcp__bilibili-mcp__bili_video_info bvid:=xxx
```

获取：标题、UP主、播放量、点赞、收藏、弹幕、时长、简介等

#### Step 3: 获取字幕

```
mcp__bilibili-mcp__bili_subtitle bvid:=xxx
```

- 有字幕 → 使用 MiniMax API 分析
- 无字幕 → 下载视频 + Gemini 分析

#### Step 4: 生成分析报告

使用统一的分析框架（第3步的分析提示词），生成结构化总结。

#### Step 5: 输出结果

直接输出分析结果给用户，可选保存到 Obsidian。

---

## 批量总结功能

当用户请求批量获取首页推荐视频并生成结构化总结时使用此功能。

### 触发条件

用户请求批量获取首页推荐并总结时使用。

### 使用流程

#### Step 1: 获取视频列表

```
mcporter call bilibili-mcp bili_homefeed
```

获取当前登录用户的个性化首页推荐视频列表。

#### Step 2: 获取每个视频的字幕

对每个视频调用：

```
mcporter call bilibili-mcp bili_subtitle bvid:=xxx
```

**字幕检测逻辑：**
- 如果返回字幕文本（有 `subtitle` 字段）→ 走有字幕流程
- 如果返回 `{"message": "该视频没有字幕"}` → 走无字幕流程

#### Step 3a: 有字幕流程 - 生成结构化总结

使用 MiniMax API 生成总结。

**API 配置：**
- 模型: `MiniMax-M2.5`
- 端点: `https://api.minimaxi.com/anthropic/v1/chat/completions`
- 认证: Bearer Token (`ANTHROPIC_AUTH_TOKEN` 环境变量)

**系统提示词：**
```
你是一个B站视频内容分析助手。请根据以下输入，判断视频类型并执行对应的完整总结。

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
```

**用户提示词：**
```
请分析以下视频字幕，生成详细总结：

【标题】：{title}
【UP主】：{author}
【BV号】：{bvid}
【字幕/口播文本】：
{transcript_text}

请按照上述格式输出。
```

#### Step 3b: 无字幕流程 - 下载视频 + Gemini 分析

如果视频没有字幕，执行以下步骤：

**Step 3b-1: 下载视频**

```bash
# 创建临时目录
mkdir -p /tmp/bilibili/{bvid}

# 下载视频（默认 480P，可调整 height 参数）
yt-dlp -o "/tmp/bilibili/{bvid}/video.%(ext)s" \
  --no-playlist \
  --merge-output-format mp4 \
  -f "bv[height<=480][ext=mp4]/best[height<=480]" \
  "https://www.bilibili.com/video/{bvid}"
```

**画质说明：**
- 默认 **480P**（`height<=480`），文件小、下载快、适合批量处理
- 如需更高画质，告诉我：
  - 720P：`height<=720`
  - 1080P：`height<=1080`
- 480P 视频通常 20-80MB，平衡画质和 Gemini API 处理速度

**Step 3b-2: 调用 Gemini API 分析**

使用 Gemini 2.5 Flash Vision 分析视频内容。

**API 配置：**
- 模型: `gemini-2.5-flash-lite`
- 端点: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent`
- 认证: `GEMINI_API_KEY` 环境变量

**请求体：**
```python
{
  "contents": [{
    "role": "user",
    "parts": [
      {"text": PROMPT},
      {"inline_data": {"mime_type": "video/mp4", "data": base64_video}}
    ]
  }]
}
```

**提示词（使用相同的系统提示词，但添加说明）：**
```
你是一个B站视频内容分析助手。请根据以下输入，判断视频类型并执行对应的完整总结。

[注意：本视频没有字幕，以下内容是通过分析视频画面得出的总结]

请按照系统提示词中的格式要求输出。
```

**Step 3b-3: 清理视频文件**

处理完成后删除临时视频文件：
```bash
rm -rf /tmp/bilibili/{bvid}
```

#### Step 4: 写入 Markdown 文件

##### 目录格式

使用 Obsidian wikilink 格式：

```markdown
## 目录

- [[#{title}|{title}]]
- [[#{title}|{title}]]
```

##### 内容格式

每个视频追加为 h2 标题，输出格式如下：

```markdown
## {title}

### 视频信息
- **标题**: {title}
- **来源**: B站首页推荐
- **UP主**: {author}
- **BV号**: {bvid}

### 一句话总结

### 核心要点
#### [干货盘点]
- 要点1
- 要点2

#### [对比分析]
| 维度 | 内容 |
|------|------|
| 优点 | ... |
| 缺点 | ... |

### 主题提炼
- 主题1：...

### 时间线摘要
...
```

### 参数配置

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `max_videos` | 最多处理视频数 | 10 |
| `output_file` | 输出文件路径 | `/Users/yueyh/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring/Bilibili/bilibili_homefeed_summaries.md` |

### 输出文件

默认输出到 `/Users/yueyh/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring/Bilibili/bilibili_homefeed_summaries.md`，可在调用时指定其他路径。

### 完整流程示例

使用 Python 脚本自动化处理：

```bash
python3 ~/.Codex/skills/bilibili-homefeed/bilibili_summary.py
```

脚本自动完成：
1. 获取首页推荐视频
2. 检测字幕：有字幕用 MiniMax 分析，无字幕下载视频用 Gemini 分析
3. 生成结构化总结
4. 写入 Obsidian 文件

### Python 脚本

脚本路径: `~/.Codex/skills/bilibili-homefeed/bilibili_summary.py`

功能：
- 自动获取首页推荐视频
- 检测字幕：有字幕 → MiniMax 分析，无字幕 → 下载视频 + Gemini 分析
- 支持 480P 视频下载（适合 Gemini API）
- 增量写入 Obsidian，自动更新目录

参数（在脚本中修改）：
- `count`: 处理的视频数量，默认 5
- `OUTPUT_FILE`: 输出文件路径

### 注意事项

1. **字幕获取**：部分视频可能没有字幕，走无字幕流程（下载视频+Gemini分析）
2. **API 限制**：注意 MiniMax API 的调用频率限制
3. **处理进度**：批量处理时展示进度，避免长时间无反馈
4. **错误处理**：单个视频失败不影响其他视频的处理
5. **视频清理**：无字幕流程处理完成后自动清理临时视频文件

---

## 提取字幕书面稿功能

当用户需要视频的完整字幕书面稿时使用此功能。使用 AssemblyAI 转录音频 + MiniMax 整理标点，比直接用 B站字幕或 Gemini 视觉分析更准确。

### 触发条件

- `提取B站字幕`
- `B站视频字幕`
- `视频文字稿`
- `提取字幕书面稿`
- `视频转文字`
- 用户提供 B站链接并要求提取字幕

### 使用流程

#### Step 1: 下载视频并提取音频

```bash
# 创建临时目录
mkdir -p /tmp/bilibili/{bvid}

# 下载视频（480P 足够）
yt-dlp -o "/tmp/bilibili/{bvid}/video.%(ext)s" \
  --no-playlist \
  --merge-output-format mp4 \
  -f "bv[height<=480][ext=mp4]/best[height<=480]" \
  "https://www.bilibili.com/video/{bvid}"

# 提取音频（mp3 格式）
ffmpeg -i /tmp/bilibili/{bvid}/video.mp4 \
  -vn -acodec libmp3lame -q:a 2 \
  /tmp/bilibili/{bvid}/audio.mp3
```

#### Step 2: AssemblyAI 转录

```python
import requests
import os

# 读取音频
with open("/tmp/bilibili/{bvid}/audio.mp3", 'rb') as f:
    audio_data = f.read()

api_key = os.environ.get("ASSEMBLYAI_API_KEY")

# 1. 上传音频
upload_resp = requests.post(
    "https://api.assemblyai.com/v2/upload",
    headers={"authorization": api_key},
    data=audio_data
)
audio_url = upload_resp.json()["upload_url"]

# 2. 请求转录
transcript_resp = requests.post(
    "https://api.assemblyai.com/v2/transcript",
    headers={
        "authorization": api_key,
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
transcript_id = transcript_resp.json()["id"]

# 3. 轮询等待结果
import time
while True:
    result = requests.get(
        f"https://api.assemblyai.com/v2/transcript/{transcript_id}",
        headers={"authorization": api_key}
    ).json()
    if result["status"] == "completed":
        raw_text = result["text"]
        break
    time.sleep(3)
```

**API 配置：**
- 模型: `universal-2`
- 端点: `https://api.assemblyai.com/v2/`
- 认证: `ASSEMBLYAI_API_KEY` 环境变量
- 语言: `zh` (中文)

#### Step 3: MiniMax 整理标点

```python
import requests
import os

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
        "model": "MiniMax-M2.5",
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

formatted_text = resp.json()["content"][0]["text"]
```

#### Step 4: 输出结果

直接输出文字稿给用户，可选保存到 Obsidian。

### 输出格式

```markdown
## {title} - 字幕书面稿

### 视频信息
- **标题**: {title}
- **UP主**: {author}
- **BV号**: {bvid}
- **链接**: https://www.bilibili.com/video/{bvid}

---

### 字幕书面稿

{formatted_text}

---

*转录方式：AssemblyAI (audio) + MiniMax (整理)*
```

### 单独提取字幕书面稿

如果用户只需要字幕书面稿（不需要分析总结），可以直接调用：

```bash
# 1. 下载视频
# 2. 提取音频
# 3. AssemblyAI 转录
# 4. MiniMax 整理
# 5. 输出到 Obsidian
```

输出文件：
- 单独字幕文件：`/Users/yueyh/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring/Bilibili/bilibili_transcripts.md`
- 与总结合并：`bilibili_homefeed_summaries.md`（在总结后面附加字幕书面稿）

### 注意事项

1. **AssemblyAI 优势**：比 B站原生字幕更准确，尤其适合口播类视频
2. **时长限制**：免费版有 10 分钟限制，超长视频需要分段处理
3. **纯音乐/无人声**：如果视频是纯配乐无口播，转录结果会很短
4. **清理文件**：处理完成后自动删除临时音视频文件
