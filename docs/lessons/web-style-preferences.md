# 网页设计偏好记录

**适用对象**: 全局风格学习 agent、所有前端开发任务
**最后更新**: 2026-03-30
**版本**: v1

---

## 用户偏好概览

### 整体风格定位
- [x] 高端艺术展风格
- [x] 极简奢华
- [x] 科技感与艺术感融合
- [ ] 简洁信息流（daheiai 偏向这个）

### 色彩偏好矩阵

| 类型 | 偏好色彩 | 示例网站 |
|------|----------|----------|
| 主色 | 黑色系 `#000`, `#111` | 流光螺旋 |
| 辅助 | 深灰 `#1a1a1a`, `#222` | 流光螺旋 |
| 强调 | 金色 `#d4af37` | 流光螺旋 |
| 渐变 | 紫-蓝 `#667eea → #764ba2` | daheiai |
| 背景 | 纯白 `#fff`, 浅灰 `#fafafa` | daheiai |

### 字体偏好

| 用途 | 字体 | 说明 |
|------|------|------|
| 标题 | Noto Serif SC | 中文衬线体，优雅，有文化感 |
| 正文 | Noto Sans SC | 中文无衬线，清晰可读 |
| 数字 | 无衬线 + 金色 | 大号数字作为视觉锚点 |

### 布局偏好

- [x] 大留白、充足呼吸感
- [x] 卡片式布局
- [x] 文字与图片交替排列（alternating layout）
- [x] 固定顶部导航（待确认）
- [ ] 网格图库（daheiai 的 3 列网格）

### 动效偏好

- [x] 淡入动画（fade-in）
- [x] hover 金色边框效果
- [x] hover 卡片上浮 + 阴影
- [x] 文字间距艺术（标题字间空格）
- [x] 平滑过渡，非夸张动效
- [x] 图标光晕效果（icon-glow）

---

## 已分析网站案例库

### 案例 1：流光螺旋

**URL**: https://fashion-spiral-lorry.netlify.app/
**日期**: 2026-03-30
**风格标签**: 高端时尚、艺术展、科技融合、极简奢华

**设计要素提取**：

#### 色彩系统

```css
--primary: #000000;        /* 纯黑主色 */
--secondary: #111111;      /* 深灰辅助 */
--accent: #d4af37;         /* 金色强调 */
--text-light: #ffffff;     /* 白色文字 */
--text-muted: #a0a0a0;     /* 灰色次要文字 */
--gradient-start: #8b5cf6; /* 紫色渐变起点 */
--gradient-end: #3b82f6;   /* 蓝色渐变终点 */
```

#### 排版系统

```
标题字体: Noto Serif SC, 700 weight, letter-spacing: 0.2em
正文字体: Noto Sans SC, 400 weight
大号数字: 80-120px, 金色, 无衬线
```

#### 布局特点

1. **Hero区**：全屏高度，大标题"流 光 螺 旋"（字间空格）
2. **统计数字**：金色大号数字 + 小字说明（"4" + "套系列作品"）
3. **卡片hover**：边框从灰色变为金色 + 上浮
4. **图片文字交替**：左图右文 / 右图左文
5. **图库布局**：2-3 列网格，hover 显示边框

#### 动效技巧

```css
/* 文字间距艺术 - 高端感 */
.title-spacing {
  letter-spacing: 0.2em;
}

/* hover 金色边框 */
.card:hover {
  border-color: #d4af37;
  transition: border-color 0.3s ease, transform 0.3s ease;
}

/* 卡片上浮效果 */
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -8px rgba(0, 0, 0, 0.15);
}

/* 淡入动画 */
.fade-in {
  animation: fadeInUp 0.6s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

#### 组件模式

| 组件 | 特征 |
|------|------|
| Hero 标题 | 衬线字体、超大字号、字间空格 |
| 统计数字 | 金色、超大、无衬线 + 小号说明文字 |
| 图片卡片 | 深色边框、hover 变金色、hover 上浮 |
| 导航链接 | 白色文字、hover 金色下划线 |

---

### 案例 2：大黑AI速报

**URL**: `webpage/daheiai-clone/` (本地克隆)
**日期**: 2026-03-30
**风格标签**: 简洁信息流、工具型、数据可视化

**设计要素提取**：

#### 色彩系统

```css
--primary: #667eea;        /* 紫蓝色主调 */
--secondary: #764ba2;      /* 深紫色 */
--accent: #10A37F;         /* OpenAI 绿 */
--background: #fafafa;      /* 浅灰背景 */
--text-dark: #1a1a1a;       /* 深色文字 */
--text-muted: #6b7280;      /* 灰色次要文字 */
--card-bg: #ffffff;         /* 白色卡片 */
--border: #e5e7eb;          /* 边框灰 */
```

#### 排版系统

```
标题字体: Noto Sans SC, 700 weight
正文字体: Noto Sans SC, 400 weight
正文字号: 14-16px
行高: 1.6-1.8 (舒适阅读)
```

#### 布局特点

1. **Header**: Logo + 统计数字（已更新期数 858、4h 更新频率、内容分类 5）
2. **按钮组**: 水平排列，灰色边框按钮
3. **卡片网格**: 3 列响应式网格（md: 2列, lg: 3列）
4. **卡片内容**: 期号 + 日期时间 + 摘要（3行截断）+ 公司图标 + 条数

#### 动效技巧

```css
/* 卡片 hover 上浮 + 阴影加深 */
.card-hover {
  transition: all 0.3s ease;
}
.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -8px rgba(0, 0, 0, 0.12);
}

/* 渐变文字 */
.gradient-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* 图标光晕 */
.icon-glow {
  filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.3));
}

/* 文字截断 */
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

#### 组件模式

| 组件 | 特征 |
|------|------|
| Logo | SVG 几何图形 + 紫色光晕 |
| 统计数字 | 36-48px 粗体 + 14px 灰色说明 |
| 操作按钮 | 灰色边框、hover 背景变化 |
| 新闻卡片 | 白色背景、圆角 12px、hover 上浮 |
| 公司图标 | 24px 圆角矩形 + 字母 |

#### 用户偏好标记

- ✅ 喜欢：渐变文字效果
- ✅ 喜欢：图标光晕
- ✅ 喜欢：hover 上浮 + 阴影
- ✅ 喜欢：3行文字截断（line-clamp）
- ❌ 不喜欢：纯灰白配色（相比流光螺旋缺少个性）

---

## 设计技巧库（可复用）

### 1. 文字间距艺术

```css
/* 中文标题字间空格 - 高端感 */
.spaced-title {
  letter-spacing: 0.15em;  /* 或 0.2em */
}
```

### 2. 金色数字锚点

```css
.stat-number {
  font-size: 5rem;           /* 80-120px */
  font-weight: 700;
  color: #d4af37;
  font-family: 'Noto Sans SC', sans-serif;
  line-height: 1;
}
.stat-label {
  font-size: 0.875rem;
  color: #a0a0a0;
  margin-top: -0.5rem;
}
```

### 3. 卡片 hover 效果

```css
/* 边框颜色变化 + 上浮 */
.card {
  border: 1px solid #333;
  transition: all 0.3s ease;
}
.card:hover {
  border-color: #d4af37;     /* 金色边框 */
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -8px rgba(0, 0, 0, 0.15);
}

/* 或浅色版本 */
.card-light {
  border: 1px solid #e5e7eb;
  transition: all 0.3s ease;
}
.card-light:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -8px rgba(0, 0, 0, 0.12);
}
```

### 4. 渐变背景与文字

```css
/* 渐变背景 */
.hero-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* 渐变文字 */
.gradient-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

### 5. 图标光晕效果

```css
.icon-glow {
  filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.3));
}
```

### 6. 文字截断

```css
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

### 7. 淡入动画

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in {
  animation: fadeInUp 0.6s ease-out;
}
```

### 8. 按钮样式

```css
/* 基础按钮 */
.btn {
  padding: 0.625rem 1.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 0.5rem;
  transition: all 0.2s ease;
}

/* 边框按钮 */
.btn-outline {
  background: white;
  color: #374151;
  border: 1px solid #e5e7eb;
}
.btn-outline:hover {
  border-color: #d1d5db;
  background: #f9fafb;
}

/* 实心按钮 */
.btn-solid {
  background: #111;
  color: white;
}
.btn-solid:hover {
  background: #000;
}
```

---

## 使用方法

### 分析新网站

1. 用户分享 URL + "分析这个网页风格"
2. Agent 使用 Playwright 截图 + 快照
3. 提取设计要素并记录到本文档
4. 与用户确认哪些元素喜欢/不喜欢
5. 更新"用户偏好标记"

### 参考风格做新网页

1. 用户说"做一个 XXX 风格的网页"
2. Agent 读取本文档
3. 参考已有的设计要素和技巧
4. 应用到新网页中

---

## 变更记录

| 日期 | 版本 | 变更内容 |
|------|------|----------|
| 2026-03-30 | v1 | 创建文档，分析流光螺旋网站 |
| 2026-03-30 | v1.1 | 添加大黑AI速报案例，分析 Tailwind 风格 |
