# Smart Figure Extractor - 智能图表提取器

## 完整工作流

### 第一步：提取候选图
```bash
python3 figure_extractor.py <图片路径> -o <输出目录>
```

### 第二步：Gemini 二次验证
提取后，必须用 Gemini 逐一验证每个图是否有 Figure caption：

```
Check if this image has a 'Figure X-XX' caption at the bottom.
- HAS_FIGURE: Figure X-XX. [caption] → 重命名为 fig_X-XX.png
- NOT_FIGURE → 删除
- INCOMPLETE: missing caption → 报错，需要调整参数重新提取
```

### 完整流程示例

```bash
# 1. 提取候选
python3 figure_extractor.py page.png -o ./

# 2. 逐一用 Gemini 验证（必须执行！）
for f in *_figure_*.png; do
    result=$(python3 gemini_image_analyzer.py "$f" "Check caption. Reply: HAS_FIGURE, NOT_FIGURE, or INCOMPLETE")
    echo "$f: $result"
done
```

## Python 代码 (figure_extractor.py)

见 `figure_extractor.py` 文件，包含：
- Phase 1: 复合图识别（caption anchor）
- Phase 2: 正常分割
- 内置 figure 过滤器

## 依赖
- opencv-python-headless
- numpy
- Pillow
- gemini-image-analyzer
