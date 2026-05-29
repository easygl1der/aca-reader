---
name: gemini-image-generation
description: 使用 Google Gemini API 生成图片。支持 gemini-2.5-flash-image, gemini-3.1-flash-image-preview, gemini-3-pro-image-preview 等模型。触发词：生成图片、AI画图、generate image、create image、画图、帮我画、text to image、t2i、ai art、画一个、生成一张图
allowed-tools: Bash(python3 *)
---

# Gemini 图片生成

使用 Google Gemini API 生成图片的 skill。

## 环境要求

- `GEMINI_API_KEY` 环境变量必须已设置
- Python 3.x

## 使用方式

### 命令行调用

```bash
# 基本用法
python3 /Users/yueyh/.Codex/skills/gemini-image-generation/generate.py "你的提示词"

# 指定模型
python3 /Users/yueyh/.Codex/skills/gemini-image-generation/generate.py "你的提示词" --model gemini-3-pro-image-preview

# 指定输出文件
python3 /Users/yueyh/.Codex/skills/gemini-image-generation/generate.py "你的提示词" -o output.png
```

### 可用模型

| 模型 | 名称 | 特点 |
|------|------|------|
| `gemini-2.5-flash-image` | Nano Banana | 快速，默认 |
| `gemini-3.1-flash-image-preview` | Nano Banana 2 | 较新 |
| `gemini-3-pro-image-preview` | Nano Banana Pro | 高质量 |

## 参数说明

| 参数 | 简写 | 默认值 | 说明 |
|------|------|--------|------|
| `prompt` | - | (必填) | 图片描述文本 |
| `--model` | `-m` | gemini-2.5-flash-image | 使用的模型 |
| `--output` | `-o` | gemini_output.png | 输出文件名 |
| `--api-key` | `-k` | $GEMINI_API_KEY | API Key |

## 示例

```bash
# 生成日落海滩
python3 /Users/yueyh/.Codex/skills/gemini-image-generation/generate.py "Generate a sunset beach landscape" -o sunset.png

# 使用高质量模型
python3 /Users/yueyh/.Codex/skills/gemini-image-generation/generate.py "A cat astronaut in space" -m gemini-3-pro-image-preview -o cat_astronaut.png
```

## API 端点

```
POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent
Headers:
  x-goog-api-key: {API_KEY}
  Content-Type: application/json
Body:
  {
    "contents": [{"parts": [{"text": "prompt"}]}],
    "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
  }
```
