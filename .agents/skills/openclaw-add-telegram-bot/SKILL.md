# 配置新 Telegram Bot (openclaw-add-telegram-bot)

## 概述

在 OpenClaw 中添加新的 Telegram Bot，每个 Bot 对应一个独立的 Agent，实现消息隔离和负载分散。

## 前置条件

1. **已有 Telegram Bot Token**：从 @BotFather 获取
2. **OpenClaw 已安装并正常运行**
3. **配置文件**：`~/.openclaw/openclaw.json`

## 触发词

- `配置新 telegram bot`
- `添加 telegram bot`
- `openclaw 新 bot`
- `配置多个 telegram bot`

## 配置步骤

### 步骤 1：准备信息

| 项目 | 说明 |
|------|------|
| Bot Token | 从 @BotFather 获取 |
| Agent ID | 英文 ID，如 `bot3` |
| Agent Name | 显示名称，如 `Bot Three` |
| Workspace | 独立工作目录，如 `~/.openclaw/workspace-bot3` |

### 步骤 2：读取当前配置

```bash
cat ~/.openclaw/openclaw.json
```

### 步骤 3：修改配置文件

在 `~/.openclaw/openclaw.json` 中添加：

#### 3.1 在 `channels.telegram.accounts` 添加新账号

```json
"channels": {
  "telegram": {
    "enabled": true,
    "accounts": {
      "default": { ... },
      "bot2": { ... },
      "bot3": {  // ← 新增
        "botToken": "YOUR_NEW_BOT_TOKEN",
        "dmPolicy": "pairing",
        "groupPolicy": "allowlist",
        "allowFrom": ["8021896102"],
        "streaming": "off"
      }
    }
  }
}
```

#### 3.2 在 `agents.list` 添加新 Agent

```json
"agents": {
  "defaults": { ... },
  "list": [
    { "id": "main", ... },
    { "id": "bot2", ... },
    {                          // ← 新增
      "id": "bot3",
      "name": "Bot Three",
      "workspace": "/Users/yueyh/.openclaw/workspace-bot3"
    }
  ]
}
```

#### 3.3 在 `bindings` 添加新绑定

```json
"bindings": [
  { "agentId": "main", "match": { "channel": "telegram", "accountId": "default" } },
  { "agentId": "bot2", "match": { "channel": "telegram", "accountId": "bot2" } },
  {                                   // ← 新增
    "agentId": "bot3",
    "match": {
      "channel": "telegram",
      "accountId": "bot3"
    }
  }
]
```

### 步骤 4：创建 Workspace 目录

```bash
mkdir -p ~/.openclaw/workspace-bot3
```

### 步骤 5：重启 Gateway

```bash
openclaw gateway restart
```

### 步骤 6：验证配置

```bash
# 查看 agents 和 bindings
openclaw agents list --bindings

# 检查 channel 状态
openclaw channels status --probe
```

## 完整示例（第 N 个 Bot）

假设要添加第 3 个 Bot：

```json
// channels.telegram.accounts
"bot3": {
  "botToken": "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz",
  "dmPolicy": "pairing",
  "groupPolicy": "allowlist",
  "allowFrom": ["8021896102"],
  "streaming": "off"
}

// agents.list
{
  "id": "bot3",
  "name": "Bot Three",
  "workspace": "/Users/yueyh/.openclaw/workspace-bot3"
}

// bindings
{
  "agentId": "bot3",
  "match": {
    "channel": "telegram",
    "accountId": "bot3"
  }
}
```

## 注意事项

1. **不要复用 workspace**：会导致会话/认证冲突
2. **每个 Bot 独立运行**：不同 Bot 的消息互不影响，降低锁冲突概率
3. **路由优先级**：`peer` > `accountId` > channel-level > default agent
4. **allowFrom**：添加允许发送消息的用户 ID，否则消息会被丢弃

## 验证成功标志

```
- Telegram bot3: enabled, configured, running, mode:polling, bot:@xxx_bot, works
```
