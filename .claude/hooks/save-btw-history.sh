#!/bin/bash
# Save /btw history to JSON at session end

INPUT=$(cat)
HOOK_EVENT=$(echo "$INPUT" | jq -r '.hook_event_name // empty')

if [[ "$HOOK_EVENT" != "Stop" ]]; then
  exit 0
fi

SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')
if [[ -z "$SESSION_ID" || "$SESSION_ID" == "null" ]]; then
  exit 0
fi

JSONL_PATH="$HOME/.claude/projects/-home-easyglider-aca-reader/${SESSION_ID}.jsonl"
BTW_HISTORY_DIR="/home/easyglider/aca-reader/.claude/btw-history"

mkdir -p "$BTW_HISTORY_DIR"

OUTPUT_FILE="$BTW_HISTORY_DIR/${SESSION_ID}.json"

# Extract /btw entries from JSONL and parse XML
jq -r 'select(.type == "system" and .subtype == "local_command") |
       select(.content | contains("/btw")) |
       {
         timestamp: .timestamp,
         raw_content: .content,
         session_id: .sessionId
       }' "$JSONL_PATH" 2>/dev/null | \
  jq -r 'select(.raw_content != null) |
         .btw_message = (.raw_content | capture("(?s)<command-message>(?<msg>[^<]*)</command-message>") | .msg) |
         del(.raw_content)' > "$OUTPUT_FILE.tmp" 2>/dev/null

# Wrap in array and format
if [[ -s "$OUTPUT_FILE.tmp" ]]; then
  jq -s '.' "$OUTPUT_FILE.tmp" > "$OUTPUT_FILE"
  rm "$OUTPUT_FILE.tmp"
else
  echo "[]" > "$OUTPUT_FILE"
  rm -f "$OUTPUT_FILE.tmp"
fi

exit 0
