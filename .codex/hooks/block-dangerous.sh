#!/bin/bash
# Block dangerous commands: rm -rf, git reset --hard, git clean -fd

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if echo "$COMMAND" | grep -qE 'rm\s+-rf\s+/|git\s+reset\s+--hard|git\s+clean\s+-fd|--no-verify'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Destructive command blocked. Use git worktree for risky operations."
    }
  }'
  exit 2
fi

exit 0
