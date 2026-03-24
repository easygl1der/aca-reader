---
name: video-summary
description: Use when user wants to summarize video content from subtitles into structured notes. Triggered by requests like "视频总结", "video notes", "根据字幕总结", or when user provides a video URL with transcript.
---

# 视频总结

将视频字幕内容结构化输出为方便理解的格式，支持多种输入来源和输出模式。

## 核心功能

1. **多来源字幕获取** - B站视频、YouTube视频、本地字幕文件
2. **结构化输出** - 主题提炼 + 要点清单 + 时间线摘要
3. **多种输出模式** - 完整模式、要点模式、时间线模式、主题模式

## 触发词

- 视频总结、视频摘要、视频笔记
- summarize video、video notes
- 根据字幕总结
- 视频结构化、提取视频要点

## 前置条件

### MCP 工具（自动调用）

| 工具 | 用途 |
|------|------|
| `bilibili-subtitle` | 获取 B站视频字幕 |
| `youtube-transcript` | 获取 YouTube 字幕 |
| 本地文件读取 | 读取 .srt/.vtt/.txt 字幕文件 |

### 本地字幕文件支持

- `.srt` 格式
- `.vtt` 格式
- `.txt` 纯文本格式

## 使用流程

### Step 1: 识别输入来源

根据用户输入自动判断：

```
B站视频 URL → bilibili-subtitle MCP
YouTube URL → youtube-transcript MCP
本地文件路径 → 读取本地文件
BV ID → bilibili-subtitle MCP
```

### Step 2: 获取字幕

**B站视频：**
```
使用 bilibili-subtitle MCP 获取字幕
```

**YouTube 视频：**
```
使用 youtube-transcript MCP 获取字幕
```

**本地文件：**
```
读取用户提供的 .srt/.vtt/.txt 文件
```

### Step 3: 分析内容结构

分析字幕内容，提取：
- 视频主题
- 关键要点
- 时间线/章节划分
- 优缺点（如果适用）

### Step 4: 输出结构化结果

根据用户选择的输出模式生成 Markdown。

## 输出模式

### 完整模式（默认）

包含所有模块：

```markdown
## 视频信息
- 标题：
- 来源：
- 时长：
- UP主/作者：

## 一句话总结

## 核心要点
### [干货盘点]
- 要点1
- 要点2

### [对比分析]
| 维度 | 内容 |
|------|------|
| 优点 | 1. ... 2. ... |
| 缺点 | 1. ... 2. ... |
| 适用场景 | ... |
| 不适用场景 | ... |

## 主题提炼
- 主题1：...
- 主题2：...

## 时间线摘要
### [时间点] 章节标题
内容摘要...
```

### 要点模式

只输出核心要点和对比分析：
- 一句话总结
- 干货盘点
- 对比分析

### 时间线模式

按时间线分段输出：
- 视频信息
- 一句话总结
- 时间线摘要（每段含时间戳和核心内容）

### 主题模式

按主题分类输出：
- 视频信息
- 一句话总结
- 主题提炼

## 输出格式

### Obsidian Callout 语法

```markdown
> [!tip] 视频信息
> - 标题：xxx
> - 来源：xxx

> [!summary] 一句话总结
> 视频核心观点...

> [!note] 核心要点
> - 要点1
> - 要点2
```

### 对比分析模板

```markdown
### [对比分析]

| 维度 | 内容 |
|------|------|
| 优点 | 1. ... 2. ... |
| 缺点 | 1. ... 2. ... |
| 适用场景 | ... |
| 不适用场景 | ... |
```

## 使用示例

### 示例1：B站视频

```
用户：总结这个视频 https://www.bilibili.com/video/BV1xx411c7mD
```

1. 识别为 B站视频 URL
2. 调用 bilibili-subtitle MCP 获取字幕
3. 分析内容，提取要点
4. 输出完整模式的 Markdown

### 示例2：YouTube视频

```
用户：提取这个视频的要点 https://youtube.com/watch?v=xxx
```

1. 识别为 YouTube URL
2. 调用 youtube-transcript MCP 获取字幕
3. 输出要点模式的 Markdown

### 示例3：本地字幕

```
用户：根据这个字幕文件总结 ~/documents/lecture.srt
```

1. 读取本地 .srt 文件
2. 分析内容
3. 输出完整模式的 Markdown

## 配置选项

用户可以通过以下方式指定输出模式：

- 直接指定：`用要点模式总结`
- 完整模式（默认）：`总结这个视频`
- 时间线模式：`按时间线输出`
- 主题模式：`提炼主题`

## 注意事项

1. **字幕质量**：依赖外部 MCP 获取的字幕质量
2. **无字幕视频**：对于无字幕的 B站/YouTube 视频，需要提示用户
3. **长视频**：对于超长视频，可以分段处理
4. **语言**：支持中英文双语处理
