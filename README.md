# aca-reader

文献阅读与讲义生成工作流

## 概述

一个模拟用户阅读文献、学习知识、生成个性化 LaTeX 讲义的工作流系统。

## 功能

- PDF 文献/教材解析
- 两阶段阅读流程（扫描 + 逐章）
- 交互式问答
- LaTeX 讲义生成（Stein 风格）
- 阅读记忆系统
- 进度仪表盘

## 使用方法

1. 加载 PDF 文件
2. 进行扫描阶段
3. 逐章阅读并提问
4. 查看生成的 LaTeX 讲义
5. 导出 PDF

## 大文件规则

**超过 100MB 的文件不提交到 Git**

由于 Git 不适合存储大文件（如 PDF、视频等），本项目设置以下规则：

- 超过 100MB 的文件不会提交
- `.git/hooks/pre-commit` 已配置 pre-commit hook 检查文件大小
- 请将大文件本地保存，或使用外部存储（如 Google Drive）
- `.gitignore` 已配置忽略常见大文件类型

## 项目结构

```
├── README.md
├── CLAUDE.md              # Claude Code 工作指引
├── docs/                  # 规范文档
│   ├── latex-style.md     # LaTeX 格式规范
│   ├── label-reference.md  # Label 引用规范
│   ├── structure.md        # 目录结构规范
│   ├── lessons/            # 经验教训
│   └── plans/              # 工作流设计文档
├── notes/                 # 笔记目录
│   ├── A-First-Course-in-Causal-Inference/
│   ├── differential-geometry/
│   ├── Schubert-Polynomials/
│   ├── bayesian/
│   └── information-geometry/
├── reading-progress/       # 阅读进度记录
├── PDFs/                   # PDF 文献库
│   └── causal-inference/
│   └── differential-geometry/
└── skills/                # Claude Code skills
```

## 主题进度

| 主题 | 书籍 | 状态 |
|------|------|------|
| 因果推断 | A First Course in Causal Inference (Peng Ding) | 1-4章 ✅ |
| 微分几何 | Do Carmo - Differential Geometry | Chapter 1-2 ✅ |
| Schubert 多项式 | Schubert Positivity | 进行中 |
| 贝叶斯统计 | Bayesian Data Analysis (Gelman et al.) | 进行中 |
| 信息几何 | Information Geometry (Amari) | 进行中 |
