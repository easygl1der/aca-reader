#!/bin/bash
# Expert Dispatcher Hook - detects keywords and queues tasks for team-lead
# Triggered on: UserPromptSubmit

INPUT=$(cat)
HOOK_EVENT=$(echo "$INPUT" | jq -r '.hook_event_name // empty')

if [[ "$HOOK_EVENT" != "UserPromptSubmit" ]]; then
  exit 0
fi

FLAG_DIR="$CLAUDE_PROJECT_DIR/.claude"
TASK_FILE="$FLAG_DIR/expert-tasks.json"

mkdir -p "$FLAG_DIR"

PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty')

# Expert keyword mappings
declare -A EXPERT_KEYWORDS=(
  ["因果推断,潜在结果,Neyman-Rubin,反事实"]="causal-expert"
  ["因果,causal,inference,rubin,potential outcome"]="causal-expert"
  ["微分几何,do carmo,曲线,曲面,黎曼"]="geometry-expert"
  ["贝叶斯,Bayes,BDA,Gelman,层次模型"]="bayesian-expert"
  ["信息几何,Amari,指数族,KL散度"]="info-geo-expert"
  ["Schubert,多项式,旗流形,除差算子"]="schubert-expert"
  ["写作,学术写作,Stein风格"]="writing-expert"
  ["习题,exercise,练习题"]="exercise-expert"
  ["LaTeX,格式,符号,规范"]="latex-checker"
  ["qa,问答,记录"]="qa-specialist"
)

# Check for matches
MATCHED=""
for keywords in "${!EXPERT_KEYWORDS[@]}"; do
  expert="${EXPERT_KEYWORDS[$keywords]}"
  if echo "$PROMPT" | grep -qiE "$keywords"; then
    MATCHED="$expert"
    break
  fi
done

if [[ -n "$MATCHED" ]]; then
  TIMESTAMP=$(date +%s)
  TASK_ID="task-${TIMESTAMP}"

  # Read existing tasks or create empty array
  if [[ -f "$TASK_FILE" ]]; then
    TASKS=$(cat "$TASK_FILE")
  else
    TASKS="[]"
  fi

  # Add new task
  TASK=$(jq -n \
    --arg id "$TASK_ID" \
    --arg expert "$MATCHED" \
    --arg prompt "$PROMPT" \
    '{
      id: $id,
      expert: $expert,
      prompt: $prompt,
      status: "pending",
      created_at: now | todate
    }')

  # Append to tasks array
  TASKS=$(echo "$TASKS" | jq ". + [$TASK]")

  echo "$TASKS" > "$TASK_FILE"

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "📋 Expert Task Queued: $MATCHED"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Prompt: $(echo "$PROMPT" | cut -c1-80)..."
  echo "Task ID: $TASK_ID"
  echo ""
fi

exit 0
