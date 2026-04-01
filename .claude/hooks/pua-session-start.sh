#!/bin/bash
# pua-session-start.sh - SessionStart hook to inject PUA flavor
# 加载 ~/.pua/config.json 并输出 flavor 提示

PUA_CONFIG="$HOME/.pua/config.json"
FLAVOR="alibaba"  # 默认阿里味

if [[ -f "$PUA_CONFIG" ]]; then
  FLAVOR=$(jq -r '.flavor // "alibaba"' "$PUA_CONFIG" 2>/dev/null || echo "alibaba")
fi

echo ""
echo "[PUA Always-On] Session started with 🟠 阿里味 (flavor: $FLAVOR)"
echo "PUA skill loaded: .claude/skills/pua/SKILL.md"
echo ""
