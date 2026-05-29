# Textbook-to-Slides Pipeline

将教材内容转化为授课 slides 的完整工作流。

## 核心 Agent

| Agent | 职责 |
|-------|------|
| `style-analyst` | 分析老师 PPT 风格，生成 `style_spec.md` |
| `topic-mapper` | 建立 PPT topic ↔ 教材 chapter 映射 |
| `curriculum-planner` | 规划每章 slide 大纲（核心思考步骤） |
| `content-curator` | 从教材提取并改写内容 |
| `slide-composer` | 生成最终 PPTX 文件 |

## 工作流

```
用户指令 → style-analyst (一次性)
         → topic-mapper (一次性)
         → curriculum-planner (每章执行)
         → content-curator (每章执行)
         → slide-composer (每章执行)
         → 对比原版 PPT (验证)
```

## 测试用例

**目标**: Gauss-Markov (Chapter 04)
- PPT 文件: `PDFs/applied-linear-regression/ALR/Gauss-Markov.pptx`
- 教材章节: `PDFs/applied-linear-regression/chapters/chapter04_gauss.tex`
- 输出路径: `notes/applied-linear-regression/gauss-markov-slides.pptx`

## 风格规范
- 详见: `style_spec.md`

## Topic 映射
- 详见: `topic_map.md`

## Agent 文件位置
- `.Codex/agents/textbook-slides/`
