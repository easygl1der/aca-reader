# Gemini Expert 教训记忆

**适用对象**: gemini-expert
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| G001 | 用英文提问获得更好效果 | 1 |

---

## G001: 用英文提问获得更好效果

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**经验描述**:
向 Gemini 提问时，用英文可以获得更好的回答效果。

**正确做法**:
- 将用户的中文问题翻译成英文后再向 Gemini 提问
- 或者在问题前加上 "Please answer in Chinese:"

**防止措施**:
- 收到中文问题时先翻译成英文
- 再向 Gemini 提问

---

## PUA 自注入行为声明

**gemini-expert 必须执行**：

1. **开工前**：读取以下文件
   - 通用教训：`/Users/yueyh/Projects/aca-workflow/docs/lessons/agents/ALL-agents-memory.md`
   - 本文件：`/Users/yueyh/Projects/aca-workflow/docs/lessons/agents/gemini-expert-memory.md`

2. **收到纠正后**：
   - 分析错误类型
   - 更新对应的 memory 文件
   - 在回复中引用更新后的教训作为确认

3. **Skill 使用**：
   - 使用 `gemini-browser-chat` skill 进行浏览器对话
   - 参考 `/Users/yueyh/.claude/skills/gemini-browser-chat/SKILL.md`

---

## G002: agent-browser + Gemini 问答流程

**日期**: 2026-04-03
**经历次数**: 1 次 (累计)

**经验描述**:
使用 agent-browser 连接本地 Chrome，打开 Gemini 网页进行问答。

**正确做法 - agent-browser + Gemini 完整流程**:

```
前置条件（只需做一次）：
1. 启动 Chrome 调试模式：
   完全退出当前 Chrome 后运行
   open -a "Google Chrome" --args --remote-debugging-port=9222
2. 在那个 Chrome 里登录 Google 账号（只需做一次）
```

**日常使用流程（每次新建对话）**：

```bash
# Step 1: 连接 Chrome，打开 Gemini
agent-browser --auto-connect open https://gemini.google.com

# Step 2: 等待页面加载完成
agent-browser wait --load networkidle

# Step 3: 获取页面元素
agent-browser snapshot -i
# 输出: textbox "Enter a prompt for Gemini" [ref=e30], ...

# Step 4: 填写问题并发送
agent-browser fill @e30 "你的问题"
agent-browser press Enter

# Step 5: 等待回答
agent-browser wait --load networkidle
agent-browser wait 5000

# Step 6: 截图查看结果
agent-browser screenshot /tmp/result.png
```

**关键命令速查**：

| 操作 | 命令 |
|------|------|
| 打开网页 | agent-browser --auto-connect open <URL> |
| 等待加载 | agent-browser wait --load networkidle |
| 获取元素 | agent-browser snapshot -i |
| 填文字 | agent-browser fill @e30 "问题" |
| 回车发送 | agent-browser press Enter |
| 截图 | agent-browser screenshot /tmp/output.png |
| 关闭 | agent-browser close |

**防止措施**:
- 每次问答前确保 Chrome 调试模式已启动
- 检查 agent-browser 连接状态
