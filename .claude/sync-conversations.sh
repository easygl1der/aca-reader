#!/bin/bash
# 会话历史同步脚本
# 将对话历史复制到项目 .claude 文件夹，方便 git 迁移

PROJECT_DIR="/Users/yueyh/Projects/aca-workflow"
MEMORY_DIR="$PROJECT_DIR/.claude/conversations"

# 创建目录
mkdir -p "$MEMORY_DIR"

# 复制对话历史（排除最新的活跃会话）
# 最新的会话通常最大，我们可能不想复制它
cd ~/.claude/projects/-Users-yueyh-Projects-aca-workflow

# 获取当前会话ID（排除当前活跃的）
CURRENT_SESSION=$(ls -t *.jsonl | head -1)

# 复制所有会话文件
for file in *.jsonl; do
  if [ -f "$file" ]; then
    # 复制文件
    cp "$file" "$MEMORY_DIR/"
    echo "已复制: $file"
  fi
done

echo "同步完成！文件保存在: $MEMORY_DIR"
