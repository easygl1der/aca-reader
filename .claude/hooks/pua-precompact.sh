#!/bin/bash
# pua-precompact.sh - PreCompact hook to save PUA failure count
# 在 context compaction 前保存失败次数到 ~/.pua/builder-journal.md

INPUT=$(cat)
HOOK_EVENT=$(echo "$INPUT" | jq -r '.hook_event_name // empty')

if [[ "$HOOK_EVENT" != "PreCompact" ]]; then
  echo "$INPUT"
  exit 0
fi

PUA_DIR="$HOME/.pua"
BUILDER_JOURNAL="$PUA_DIR/builder-journal.md"

mkdir -p "$PUA_DIR"

# 从 INPUT 提取失败次数（如果有）
FAILURE_COUNT=$(echo "$INPUT" | jq -r '.failure_count // 0' 2>/dev/null || echo 0)

# 追加到 journal
TIMESTAMP=$(date +%Y-%m-%dT%H:%M:%S)
echo "[$TIMESTAMP] PreCompact: failure_count=$FAILURE_COUNT" >> "$BUILDER_JOURNAL"

# 保留最近 100 条
if [[ -f "$BUILDER_JOURNAL" ]]; then
  tail -100 "$BUILDER_JOURNAL" > "$BUILDER_JOURNAL.tmp"
  mv "$BUILDER_JOURNAL.tmp" "$BUILDER_JOURNAL"
fi

echo "$INPUT"
exit 0
