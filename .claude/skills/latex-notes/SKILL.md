---
name: latex-notes
description: 生成 LaTeX 格式的学习讲义，包含用户注解、问题、Stein 风格的 motivation 写作
user-invocable: true
---

# LaTeX 讲义生成 Skill

## 功能

1. 根据阅读进度生成对应章节的 .tex 文件
2. 在定义/命题/证明之间插入用户注解
3. 记录问答内容到附录
4. 生成 main.tex 整合所有章节
5. 交叉引用支持

## 使用方式

- "帮我更新第3章第2节的讲义"
- "把这个问题和解答加到讲义里"
- "生成 main.tex"

## 讲义风格

参考 Stein 的写作风格：
- 动机驱动：先解释为什么需要这个概念
- 与已有知识关联
- 清晰的叙事流程
- 不是干巴巴的定义定理证明，而是有"为什么"的解释

## 文件结构

```
main.tex
├── chapters/chapter1/
│   ├── section1.tex
│   ├── section2.tex
│   └── ...
├── chapters/chapter2/
│   └── ...
└── appendix/qa.tex
```

## 用户注解格式

在定理/定义/证明之间插入：

% === 用户注解 ===
% 问题：为什么需要引入这个概念？
% 解答：...
% 关联：与第2章的XX定理有关联
% ===
