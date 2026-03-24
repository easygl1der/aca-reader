# MiniMax Vision Skill

## 触发词
- minimax 图像分析
- minimax 图片理解
- minimax vision
- 分析这张图片

## 功能
调用 MiniMax 的 abab6.5s-chat 模型分析图片内容，支持本地文件和 URL

## 使用方法

### Claude Code 中直接使用
```
"分析这张图片" - 分析当前对话中的图片
"minimax 分析 https://example.com/image.png" - 分析 URL 图片
"minimax 分析 /path/to/image.png" - 分析本地图片
```

### 命令行
```bash
python3 ~/.claude/skills/minimax-vision/analyze.py <图片路径或URL> [问题]
```

### 示例
```bash
# 描述本地图片
python3 ~/.claude/skills/minimax-vision/analyze.py /path/to/image.png

# 分析网络图片
python3 ~/.claude/skills/minimax-vision/analyze.py "https://example.com/image.png"

# 自定义问题
python3 ~/.claude/skills/minimax-vision/analyze.py /path/to/image.png "这张图片有什么特别之处？"
```

## 支持的图片格式
- PNG
- JPEG
- GIF
- WebP
- SVG
- 不支持 PDF

## 支持的图片来源
1. **本地文件**: 直接传入文件路径
2. **网络 URL**: 自动下载后分析
3. **Claude Code 图片**: 用户在对话中发送的图片

## Token 使用量
- 输入: ~3 tokens/图片像素 (根据图片大小)
- 输出: 根据回答长度

## 配置
API Key 已配置在代码中，如需更新请编辑:
`~/.claude/skills/minimax-vision/analyze.py`

## 实现原理
- 使用 MiniMax abab6.5s-chat 多模态模型
- 将图片转为 base64 后传入 API
- 支持自定义问题进行针对性分析

## 注意事项
- 图片过大会导致输入 token 过多，建议先压缩
- 网络图片会自动下载到临时目录
- 不支持 PDF 文件
