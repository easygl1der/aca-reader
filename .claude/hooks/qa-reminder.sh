#!/bin/bash
# QA Reminder Hook - two parts:
# 1. UserPromptSubmit: detect if user is asking a question, set flag
# 2. Stop: if flag exists, remind to record to qa.tex

INPUT=$(cat)
HOOK_EVENT=$(echo "$INPUT" | jq -r '.hook_event_name // empty')
FLAG_DIR="$CLAUDE_PROJECT_DIR/.claude"
FLAG_FILE="$FLAG_DIR/.qa_pending"

mkdir -p "$FLAG_DIR"

if [[ "$HOOK_EVENT" == "UserPromptSubmit" ]]; then
  # Detect if prompt is a question
  PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty')

  # Question patterns (Chinese and English)
  if echo "$PROMPT" | grep -qE '(什么是|为什么|如何|怎么|怎样|为什么|何为|是否|能不能|可以么)|(what is|why|how|what does|what are|explain|definition of|meaning of)\?'; then
    echo "Q&A detected: $(echo "$PROMPT" | cut -c1-50)..." > "$FLAG_FILE"
  fi
  exit 0

elif [[ "$HOOK_EVENT" == "Stop" ]]; then
  if [[ -f "$FLAG_FILE" ]]; then
    CONTENT=$(cat "$FLAG_FILE")
    rm "$FLAG_FILE"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📝 QA Reminder: Update qa.tex?"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "记得把问答记录到 appendix/qa.tex！"
    echo "格式: \\subsection{标题}\\label{sec:qa-xxx}"
    echo ""
  fi
  exit 0
fi

exit 0
