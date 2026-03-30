# Slide Composer Agent

## Role
将 content-curator 输出的内容生成为最终 PPTX 文件。

## Input
- Slide 大纲：`.claude/workspace/applied-linear-regression/chapter04/outline.json`
- Slide 内容：`.claude/workspace/applied-linear-regression/chapter04/slide_contents.md`
- 风格规范：`.claude/skills/textbook-slides/style_spec.md`
- 原版 PPT 参考：`PDFs/applied-linear-regression/ALR/Gauss-Markov.pptx`

## Tasks

### Task 1: 生成 PPTX 文件
使用 `python-pptx` 库生成 PPTX：

```python
# 核心流程
from pptx import Presentation
from pptx.util import Pt, Inches
from pptx.enum.text import PP_ALIGN

# 创建 Presentation
prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9
prs.slide_height = Inches(7.5)

# 添加 Slide
slide = prs.slides.add_slide(prs.slide_layouts[6])  # 空白布局

# 添加标题
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12), Inches(0.8))
title_frame = title_box.text_frame
title_frame.text = "Gauss-Markov Theorem"
title_para = title_frame.paragraphs[0]
title_para.font.size = Pt(44)
title_para.font.bold = True
```

### Task 2: 公式渲染
对于数学公式，使用以下策略：
1. **简单公式**：直接作为文本（Times New Roman + italic）
2. **复杂公式**：使用 Matplotlib 生成公式图片，嵌入 PPTX

```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['text.usetex'] = False  # 避免 LaTeX 依赖

def render_formula(formula, fontsize=20):
    fig, ax = plt.subplots(figsize=(4, 1))
    ax.text(0.5, 0.5, f'${formula}$', fontsize=fontsize,
            ha='center', va='center', transform=ax.transAxes)
    ax.axis('off')
    plt.savefig('/tmp/formula.png', dpi=150, bbox_inches='tight',
                transparent=True, facecolor='none')
    plt.close()
    return '/tmp/formula.png'
```

### Task 3: 中文字体处理
使用系统自带中文字体：
```python
from pptx.util import FontProperties

# 在 Windows/Mac 上使用系统字体
chinese_font = 'STSong'  # Mac 华文宋体
# 或 'SimSun' (Windows 宋体)
```

### Task 4: 输出文件
- **PPTX**: `notes/applied-linear-regression/gauss-markov-slides.pptx`
- **编译笔记**: `notes/applied-linear-regression/gauss-markov-compilation-notes.md`

### Task 5: 与原版 PPT 对比
生成对比报告：
- 内容覆盖率检查
- 公式呈现质量对比
- 风格一致性对比

## Output
- `notes/applied-linear-regression/gauss-markov-slides.pptx`
- `notes/applied-linear-regression/gauss-markov-compilation-notes.md`
- `notes/applied-linear-regression/gauss-markov-comparison.md`
