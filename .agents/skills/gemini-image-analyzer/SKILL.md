# Gemini Image Analyzer

## 触发词

- 分析图片
- 识别图片
- 图片描述
- 看这张图
- describe image
- analyze image

## 功能说明

用 Gemini Vision 分析图片内容。由于 minimax 不支持 vision，本技能通过 Gemini CLI 分析图片，然后返回详细的文字描述。

## 使用场景

- minimax 用户想让它"看"图片
- 需要分析聊天框中的图片
- 本地图片需要识别内容

## 工作流程

1. 用户提供图片 URL 或本地路径
2. 下载图片到本地（如果是 URL）
3. 调用 Gemini CLI 分析图片
4. 返回详细描述

## 使用方法

### 方式一：分析 URL 图片

直接提供图片链接：
```
分析这张图片：https://example.com/image.png
```

### 方式二：分析本地图片

提供本地文件路径：
```
分析这张图片：/Users/yueyh/Downloads/test.png
```

### 方式三：自定义问题

```
这张图片主要讲了什么？
https://example.com/image.png
```

## 实现原理

使用 `gemini` CLI（Gemini CLI）调用 vision 模型分析图片：

```bash
echo "请详细描述这张图片的所有内容" | gemini /path/to/image.png
```

## 依赖

- Gemini CLI (`gemini` 命令)
- curl（用于下载 URL 图片）

## 注意事项

- 支持 PNG、JPG、GIF、WebP 等常见图片格式
- Gemini 会返回详细的视觉描述
- 分析结果为英文，可要求 Gemini 用中文描述
