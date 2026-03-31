# Hooks 与 Subagent 自动化

## 当前已配置的 Hooks

| Hook 事件 | 触发条件 | 执行操作 |
|-----------|----------|----------|
| `PostToolUse:Edit` | 编辑 .tex 文件 | auto-compile-latex.sh + auto-commit-push.sh |
| `PostToolUse:Bash` | 运行 compile.sh | auto-commit-push.sh |
| `Stop` | 会话停止 | compact-reload.sh（检测上下文压缩并提醒 CLAUDE.md 关键规则） |

**Hook 脚本位置**: `.claude/hooks/`

**Hook 脚本位置**: `.claude/hooks/`

## Subagent 适用场景

**适合用 Subagent 的场景**：
- 并行处理多个独立任务（如同时写多章笔记）
- 需要专门领域知识的复杂任务
- 需要多轮迭代的工作流（如三角协作）
- 长时间运行的搜索/研究任务

**不适合用 Subagent 的场景**：
- 简单的一次性操作（直接执行即可）
- 顺序依赖的任务（用 hook 触发更简单）
- 需要读取大量上下文的任务（消耗 token）

## 常用 Subagent 类型

| Agent | 使用场景 | 触发关键词 |
|-------|----------|-----------|
| `code-expert` | 代码审查、Bug 检测 | "review", "audit", "check quality" |
| `qa-test-specialist` | 生成测试用例 | "test", "coverage", "edge case" |
| `paper-reviewer` | 论文评审 | "review paper", "referee report" |
| `web-researcher` | 网络搜索研究 | "research", "fact-check" |
| `quant-analyst` | 量化金融分析 | "backtest", "strategy", "VaR" |
| `sentiment-analyst` | 市场情绪分析 | "sentiment", "market" |

## Spawn Subagent 标准模板

```bash
Agent(
  subagent_type="<agent-type>",
  prompt="""<任务描述>

开工前用 Read 工具读取以下文件，按其中的行为协议执行：
- 核心行为：找到 pua 插件目录下的 skills/pua/SKILL.md（用 Glob 搜索 **/pua/skills/pua/SKILL.md）
- 如果是 P7 模式：同目录下的 references/p7-protocol.md
""",
  description="<简短描述>",
  run_in_background=true  # 独立任务用 true
)
```

## Hook → Subagent 协作模式

```
用户编辑 .tex
    ↓
Hook 触发
    ↓
auto-compile-latex.sh → 编译 PDF
auto-commit-push.sh → 推送到远程
    ↓
如果需要更复杂的处理（如验证内容），
则 Spawn 专门的 subagent 处理
```

## 自动化学以致用

1. **编辑触发编译**：Hook 自动处理，无需手动编译
2. **编译触发提交**：代码级备份，不丢进度
3. **复杂检查用 Agent**：内容核实、幻觉检测等用 latex-checker agent
4. **并行加速**：多章节同时写时 spawn 多个 domain-expert
