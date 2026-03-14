---
name: interactive-qa
description: 交互式问答，理解用户当前阅读位置，实时回答问题并同步更新讲义
user-invocable: true
---

# 交互式问答 Skill

## 功能

1. 理解用户当前阅读位置（哪章哪节哪个定理）
2. 实时回答用户问题
3. **【自动】更新讲义和进度记录**

## 使用方式

- "我不懂这个定理"
- "这个定理是干嘛的"
- "证明我没看懂"

## 核心工作流（每次必须执行）

**【重要】用户每次提问后，必须自动执行以下全部步骤：**

### Step 1: 对话式回答
- 用口语化、让初学者能看懂的方式回答
- 可以举例说明

### Step 2: 自动更新讲义
- 在当前章节的 .tex 文件中添加用户注解块
- 使用 `\userannotation{问题}{回答}` 格式
- 内容要与 Stein 风格一致

### Step 3: 自动更新进度
- 将问题记录到 `progress.json` 的 `questions` 数组中
- 包含：日期、章节、问题、简答

### Step 4: 重新编译
- 运行 `xelatex` 编译更新后的讲义

### Step 5: 自动提交 Git
- 执行 `git add notes/ .claude/skills/reading-progress/progress.json`
- 使用 `git commit -m "QA: 第X章 - 问题简述"` 提交

## 自动更新

每次问答后（必须全部执行）：
1. ✅ 用口语化方式回答用户
2. ✅ 添加用户注解到 LaTeX 讲义（使用 \userannotation）
3. ✅ 记录问题到 progress.json
4. ✅ 重新编译 PDF
5. ✅ 自动提交到 Git

## Git 提交脚本

也可以使用脚本手动提交：
```bash
./scripts/commit_notes.sh "更新讲义"
```
