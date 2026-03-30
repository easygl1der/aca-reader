# Knowledge Profile System

> 用户知识画像系统 — 根据用户已有知识水平调整回答深度

---

## 1. 设计目标

CodeEx（agent）在回答科研问题时，应根据用户已有的知识水平决定语言层次和叙述方式：
- 避免过于基础 → 浪费用户时间
- 避免过于高级 → 导致困惑

---

## 2. 核心概念

### 2.1 领域（Domain）

与文献库对应的知识领域：
- `causal-inference` — 因果推断（Peng Ding）
- `differential-geometry` — 微分几何（Do Carmo）
- `schubert-calculus` — Schubert 演算
- `bayesian` — 贝叶斯统计（BDA）
- `information-geometry` — 信息几何（Amari）

### 2.2 知识等级（Level）

| Level | 名称 | 描述 | 回答风格 |
|-------|------|------|----------|
| 1 | `beginner` | 初学者 | 多用类比、动机解释、定义所有术语 |
| 2 | `acquainted` | 了解者 | 简要回顾、逐步引入严格性 |
| 3 | `familiar` | 熟悉者 | 标准技术陈述 |
| 4 | `proficient` | 熟练者 | 可深入细节、处理复杂证明 |
| 5 | `mastered` | 精通者 | 前沿讨论、批判性分析 |

### 2.3 概念追踪（Concept Tracking）

可选功能：追踪用户对特定概念的理解水平。

```json
"concepts": {
  "potential-outcomes": {
    "level": "understanding",
    "evidence": ["completed Chapter 3", "asked about SUTVA"],
    "last_observed": "2026-03-29"
  }
}
```

---

## 3. 文件结构

### 3.1 主配置文件

**位置**: `config/knowledge-profile.json`

**结构**:
```json
{
  "domains": {
    "<domain-name>": {
      "level": "familiar",
      "concepts": {
        "<concept-name>": {
          "level": "understanding",
          "evidence": ["evidence1", "evidence2"],
          "last_observed": "2026-03-29"
        }
      },
      "prerequisites": ["mathematical-statistics"],
      "reading_progress": {
        "current_chapter": 11,
        "total_chapters": 18
      },
      "assessment_history": [],
      "notes": "strong math background, prefers proofs over intuition"
    }
  },
  "last_updated": "2026-03-30",
  "settings": {
    "inquiry_strategy": "lazy",
    "min_confidence_threshold": 0.7,
    "auto_update": true
  }
}
```

### 3.2 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `domains` | object | 各领域知识画像 |
| `domains.<domain>.level` | string | 总体等级 (beginner/acquainted/familiar/proficient/mastered) |
| `domains.<domain>.concepts` | object | 具体概念的理解水平 |
| `domains.<domain>.concepts.<concept>.level` | string | 概念等级 |
| `domains.<domain>.concepts.<concept>.evidence` | array | 证据（如"完成第3章"、"问过SUTVA问题"） |
| `domains.<domain>.reading_progress` | object | 阅读进度（可选） |
| `domains.<domain>.assessment_history` | array | 评估历史记录 |
| `domains.<domain>.notes` | string | 用户偏好备注 |
| `settings.inquiry_strategy` | string | 询问策略 (lazy/eager/consent_first) |
| `settings.auto_update` | boolean | 是否自动更新证据 |

---

## 4. Agent 行为流程

### 4.1 开工检查流程

```
[Agent 收到问题 in domain X]
            │
            ▼
    读取 config/knowledge-profile.json
            │
     ┌──────┴──────┐
     │  领域存在？  │
     └──────┬──────┘
        Yes │  No
     ┌──────┴──────────────────┐
     ▼                          ▼
  使用已记录水平            inquiry_strategy 决定
     │                    • lazy → 直接用默认水平（beginner）
     │                    • eager → 问 1-3 个诊断问题
     │                    • consent_first → 等用户同意才问
     ▼
  根据 level 调整回答深度
     │
     ▼
  交互后自动更新 evidence（如果 auto_update=true）
```

### 4.2 询问策略

| 策略 | 行为 | 适用场景 |
|------|------|----------|
| `lazy` | 有记录就用，无记录用默认（beginner） | 最小打扰，适合主动用户 |
| `eager` | 无记录时主动问 1-3 个诊断问题 | 适合新用户引导 |
| `consent_first` | 询问前先请求用户同意 | 适合需要透明度的场景 |

### 4.3 诊断问题示例（eager 模式）

```
"你之前是否学习过因果推断？"
"你对潜在结果框架（potential outcomes）了解多少？"
"是否接触过 Rubin causal model？"
```

---

## 5. Level 对应回答风格

### 5.1 beginner

```
"让我从基础讲起..."
- 使用生活类比
- 解释每个专业术语
- 强调动机和直观理解
- 避免跳步
```

### 5.2 acquainted

```
"你可能记得..."
- 简要回顾必要基础
- 逐步引入严格定义
- 在直觉和形式化之间平衡
```

### 5.3 familiar

```
标准技术陈述
- 直接给出定义和定理
- 正常的数学写作风格
- 适当的符号和推导
```

### 5.4 proficient

```
"如你所知..."
- 可深入技术细节
- 处理复杂证明
- 讨论微妙之处和常见误区
```

### 5.5 mastered

```
"从前沿角度看..."
- 深入讨论最新研究
- 批判性分析方法和局限
- 比较不同流派观点
```

---

## 6. 自动更新机制

当 `settings.auto_update=true` 时，Agent 在交互后自动更新 evidence：

```json
{
  "evidence": [
    "completed Chapter 3",        // 原有
    "asked about SUTVA"          // 新增
  ]
}
```

**更新时机**：
- 用户明确表示理解/不理解某概念
- 用户提问显示对某领域的了解程度
- 用户纠正 Agent 的错误

---

## 7. 使用示例

### 7.1 读取知识画像

```javascript
// Agent 开工时执行
const profile = JSON.parse(readFile('config/knowledge-profile.json'));
const domainLevel = profile.domains['causal-inference']?.level || 'beginner';
```

### 7.2 更新证据

```javascript
// 交互后自动执行
profile.domains['causal-inference'].assessment_history.push({
  timestamp: '2026-03-30',
  action: 'asked about SUTVA',
  new_evidence: ['asked about SUTVA']
});
profile.last_updated = '2026-03-30';
```

---

## 8. 与其他系统的集成

### 8.1 与 QA 记录系统

每次问答后，如果用户展示了新的知识水平信号，可以更新 profile：

```latex
% 问答记录
\subsection{用户对 SUTVA 的理解}\label{sec:qa-sutva}
用户问："SUTVA 假设在实际中可能违反吗？"
→ 这表明用户处于 acquainted ~ familiar 水平
```

### 8.2 与进度追踪

reading_progress 可用于推断水平：
- Chapter 1-3 → beginner ~ acquainted
- Chapter 4-8 → acquainted ~ familiar
- Chapter 9+ → familiar ~ proficient

---

## 9. 配置文件位置

**主文件**: `config/knowledge-profile.json`

同一目录还有：
- `config/user-preferences.json` — 用户偏好设置

---

## 10. 未来扩展

- [ ] 添加概念级（concept-level）追踪作为可选功能
- [ ] 支持导入导出知识画像
- [ ] 与 Obsidian 笔记系统集成
- [ ] 添加知识水平可视化面板
