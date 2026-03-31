#!/bin/bash
# compact-reload.sh - 检测 compact 并重新加载 CLAUDE.md 关键内容
# 原理：通过启发式检测（行数减少 > 20%）判断是否发生了上下文压缩

INPUT=$(cat)
HOOK_EVENT=$(echo "$INPUT" | jq -r '.hook_event_name // empty')

if [[ "$HOOK_EVENT" != "Stop" ]]; then
  exit 0
fi

FLAG_DIR="$CLAUDE_PROJECT_DIR/.claude"
HISTORY_FILE="$FLAG_DIR/.compact_history"
CLAUDE_MD="$CLAUDE_PROJECT_DIR/CLAUDE.md"

# 读取上次消息行数
if [[ -f "$HISTORY_FILE" ]]; then
  LAST_LINES=$(cat "$HISTORY_FILE")
else
  LAST_LINES=0
fi

# 尝试从 INPUT 中提取消息统计信息
# Claude Code 的 hook 会传递丰富的事件数据
TOOL_RESULT=$(echo "$INPUT" | jq -r '.tool_results // [] | length' 2>/dev/null || echo 0)
MESSAGES=$(echo "$INPUT" | jq -r '.messages // [] | length' 2>/dev/null || echo 0)

# 启发式：综合判断
CURRENT_LINES=$((TOOL_RESULT + MESSAGES))

# 首次运行或数字异常，跳过
if [[ "$LAST_LINES" -eq 0 || "$CURRENT_LINES" -eq 0 ]]; then
  echo "$CURRENT_LINES" > "$HISTORY_FILE"
  exit 0
fi

# 检测 compact：当前行数 < 上次的 80%
THRESHOLD=$((LAST_LINES * 80 / 100))
if [[ "$CURRENT_LINES" -lt "$THRESHOLD" && "$LAST_LINES" -gt 50 ]]; then
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "📋 Context Compact Detected!"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "上次: $LAST_LINES 行 → 当前: $CURRENT_LINES 行"
  echo ""
  echo "CLAUDE.md 关键提醒:"
  echo "• QA 记录: 每次提问后记录到 appendix/qa.tex"
  echo "• 编译: 必须用 compile.sh (xelatex 3次)"
  echo "• LaTeX 红线: 禁止 Markdown 语法、\\bm、\\I"
  echo "• Skim: PDF 跳转用 displayline -r -g"
  echo "• 引用补充: 引用定理时必须给出完整内容"
  echo ""
  echo "完整内容见: $CLAUDE_MD"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
fi

# 更新历史
echo "$CURRENT_LINES" > "$HISTORY_FILE"
exit 0
