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
