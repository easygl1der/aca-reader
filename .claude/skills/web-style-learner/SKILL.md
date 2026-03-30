# Web Style Learner Skill

## Purpose

当用户分享网页 URL 或说"分析这个网页风格"时，使用本 skill 分析其设计风格并积累到偏好系统。

## Trigger

- 用户分享 URL + "分析这个网页风格"
- 用户说"分析这个网站"
- 用户说"帮我看看这个网页的设计"

## Workflow

### Step 1: 截图 + 快照分析

使用 Playwright 工具：

```
1. mcp__plugin_playwright_playwright__browser_navigate - 导航到 URL
2. mcp__plugin_playwright_playwright__browser_take_screenshot - 截图保存
3. mcp__plugin_playwright_playwright__browser_snapshot - 获取页面结构
```

### Step 2: 提取设计要素

分析以下维度：

| 维度 | 提取内容 |
|------|----------|
| 色彩系统 | 主色、辅助色、强调色、渐变 |
| 字体系统 | 标题字体、正文字体、字号层级 |
| 布局模式 | 网格系统、留白、响应式策略 |
| 动效技巧 | hover 效果、过渡动画、加载动画 |
| 图标风格 | 线条/填充、尺寸、用途 |
| 组件模式 | 卡片、按钮、表单、导航 |

### Step 3: 保存截图

保存到 `webpage/style-references/<网站名>/screenshot-{n}.png`

### Step 4: 更新偏好记录

使用 Edit tool 更新 `docs/lessons/web-style-preferences.md`：

1. 在"已分析网站案例库"添加新案例
2. 更新"用户偏好概览"中的相关偏好
3. 在"设计技巧库"添加可复用技巧

### Step 5: 与用户讨论

向用户确认：
- 哪些元素喜欢？
- 哪些元素不喜欢？
- 有没有特别想借鉴的地方？

根据用户反馈更新偏好记录中的"喜欢/不喜欢"标记。

## 分析 Prompt 模板

```markdown
## 网页设计分析报告：{网站名}

**URL**: {URL}
**日期**: {日期}

### 整体风格定位
[描述整体感受：高端、简约、科技感等]

### 色彩系统
```
主色: #XXXXXX
辅助色: #XXXXXX
强调色: #XXXXXX
背景色: #XXXXXX
文字色: #XXXXXX
渐变: #XXXXXX → #XXXXXX
```

### 排版系统
```
标题字体:
正文字体:
字号层级:
字间距:
行间距:
```

### 布局特点
1. [布局特点1]
2. [布局特点2]
3. [布局特点3]

### 动效技巧
```css
[可复用的 CSS 代码]
```

### 组件模式
- 卡片:
- 按钮:
- 导航:

### 用户偏好标记
- ✅ 喜欢:
- ❌ 不喜欢:
- 💡 想借鉴:
```

## 输出位置

- 截图：`webpage/style-references/<网站名>/`
- 分析报告：追加到 `docs/lessons/web-style-preferences.md`
