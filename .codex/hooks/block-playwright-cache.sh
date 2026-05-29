#!/bin/bash
# Block rm -rf commands targeting Playwright browser cache

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Check if command contains rm -rf AND (ms-playwright or playwright)
if echo "$COMMAND" | grep -qE 'rm\s+-rf.*ms-playwright|rm\s+-rf.*playwright'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Blocking deletion of Playwright browser cache. This cache is required for browser automation and should not be deleted."
    }
  }'
  exit 2
fi

exit 0
