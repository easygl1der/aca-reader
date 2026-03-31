# SciSpace Clone - SPEC.md

**项目状态**: P0 实现中
**技术栈**: Next.js 15 + TypeScript + Tailwind CSS + shadcn/ui + Zustand

---

## 🗺️ 功能规划

### P0 - 核心功能（首先实现）

| 功能 | 页面路径 | 优先级 | 状态 |
|------|----------|--------|------|
| 侧边栏导航 | Layout 组件 | P0 | ⭕ |
| 首页 | `/` | P0 | ⭕ |
| Chat with PDF | `/chat-pdf` | P0 | ⭕ |
| 论文搜索 | `/search` | P0 | ⭕ |

### P1 - 重要功能（第二阶段）

| 功能 | 页面路径 | 优先级 |
|------|----------|--------|
| Literature Review | `/literature-review` | P1 |
| AI Writer | `/ai-writer` | P1 |
| Agent Gallery | `/agents` | P1 |
| Find Topics | `/concepts` | P1 |

### P2 - 增值功能（未来）

| 功能 | 页面路径 | 优先级 |
|------|----------|--------|
| Extract Data | `/extract-data` | P2 |
| Citation Generator | `/citation-generator` | P2 |
| Paraphraser | `/paraphraser` | P2 |
| AI Detector | `/ai-detector` | P2 |

---

## 🎨 设计规范

### 色彩系统
```css
--bg-primary: #0a0a0a;        /* 深色背景 */
--bg-secondary: #171717;       /* 卡片/面板 */
--bg-tertiary: #262626;        /* 悬停/激活 */
--border: #333333;              /* 边框 */
--text-primary: #ffffff;        /* 主文字 */
--text-secondary: #a1a1a1;     /* 次要文字 */
--text-muted: #525252;         /* 弱化文字 */
--accent: #7c3aed;             /* 紫色强调 - SciSpace 风格 */
--accent-hover: #6d28d9;       /* 强调悬停 */
--success: #10b981;            /* 成功/引用高亮 */
--warning: #f59e0b;            /* 警告 */
```

### 字体
- 主字体: Inter (Google Fonts)
- 代码/数学: JetBrains Mono

### 间距系统
- 基础单位: 4px
- 侧边栏宽度: 64px (折叠) / 240px (展开)
- 内容区最大宽度: 1400px
- 卡片圆角: 12px

---

## 📐 页面规范

### 1. Layout (侧边栏 + Header)
```
┌──────────┬─────────────────────────────────────┐
│          │  Header (Breadcrumb + User Avatar)  │
│ Sidebar  ├─────────────────────────────────────┤
│  (Nav)   │                                     │
│          │           Main Content             │
│          │                                     │
└──────────┴─────────────────────────────────────┘
```

**侧边栏导航项**:
- 🏠 Home (首页)
- 💬 Chat with PDF
- 🔍 Literature Review
- ✍️ AI Writer
- 🤖 Agents
- 💡 Find Topics
- 📊 Extract Data
- 📚 Citation Generator
- 🔄 Paraphraser
- 🔍 AI Detector

### 2. 首页 `/`
- Hero 区域：标题 + 搜索框
- 快速入口卡片网格
- 特色功能介绍

### 3. Chat with PDF `/chat-pdf`
```
┌────────────────────────────────────────────────┐
│  [上传 PDF]  [我的文献库]     [仅本文] [所有文献]│
├─────────────────────┬──────────────────────────┤
│                     │                          │
│    PDF 预览区       │     AI 对话区            │
│   (左侧 50%)        │    (右侧 50%)            │
│                     │                          │
│                     │  ┌────────────────────┐  │
│                     │  │ AI 消息气泡         │  │
│                     │  └────────────────────┘  │
│                     │                          │
│                     │  ┌────────────────────┐  │
│                     │  │ [输入框]  [发送]    │  │
│                     │  └────────────────────┘  │
└─────────────────────┴──────────────────────────┘
```

**功能点**:
- PDF 文件上传（拖拽 + 点击）
- PDF.js 渲染
- AI 对话（消息气泡）
- 引用高亮（点击引用跳转到 PDF 位置）
- 搜索范围切换（仅本文 / 所有文献）
- AI 建议问题（Brainstorm Questions）

### 4. 论文搜索 `/search`
```
┌────────────────────────────────────────────────┐
│  [🔍 搜索框........................] [搜索]   │
├────────────────────────────────────────────────┤
│  筛选器                                      │
│  [年份] [期刊] [作者] [引用数] [开放获取]      │
├────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────┐ │
│  │ 📄 论文标题                               │ │
│  │ 作者 · 年份 · 期刊                        │ │
│  │ 摘要预览...                               │ │
│  │ 引用数: 123  |  相关度: 0.95             │ │
│  └──────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────┐ │
│  │ 📄 论文标题                               │ │
│  ...                                          │
└────────────────────────────────────────────────┘
```

**功能点**:
- Semantic Scholar API 集成
- 搜索结果分页
- 筛选器（年份、期刊、作者、引用数）
- 论文卡片（标题、作者、摘要、引用数）
- 点击跳转到详情/Chat with PDF

---

## 🔧 技术实现

### 目录结构
```
src/
├── app/
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # 首页
│   ├── chat-pdf/
│   │   └── page.tsx        # Chat with PDF
│   └── search/
│       └── page.tsx        # 论文搜索
├── components/
│   ├── layout/
│   │   ├── sidebar.tsx     # 侧边栏
│   │   └── header.tsx      # Header
│   ├── chat-pdf/
│   │   ├── pdf-viewer.tsx  # PDF 渲染
│   │   ├── chat-area.tsx   # 对话区
│   │   └── upload-zone.tsx # 上传区
│   └── search/
│       ├── search-bar.tsx  # 搜索框
│       ├── paper-card.tsx  # 论文卡片
│       └── filters.tsx     # 筛选器
├── lib/
│   ├── api/
│   │   └── semantic-scholar.ts  # API 调用
│   └── utils.ts
└── store/
    └── use-app-store.ts    # Zustand 状态
```

### 状态管理 (Zustand)
```typescript
interface AppState {
  // 侧边栏
  sidebarOpen: boolean;
  toggleSidebar: () => void;

  // Chat with PDF
  pdfFile: File | null;
  messages: Message[];
  isLoading: boolean;

  // 搜索
  query: string;
  results: Paper[];
  filters: SearchFilters;
}
```

### API 设计

**Semantic Scholar API**:
```
GET https://api.semanticscholar.org/graph/v1/paper/search
  ?query={keyword}
  &year={year-range}
  &venue={journal}
  &fields=title,authors,abstract,year,citationCount,venue
  &limit=20
  &offset={pagination}
```

### AI 集成（Mock 阶段）
```typescript
// 使用 OpenAI API
// RAG: 将 PDF 文本分块 → embedding → 存储
// 查询时: embedding → 向量检索 → GPT 生成答案
```

---

## 🚀 开发计划

### Phase 1: 基础搭建
- [x] SPEC.md 编写
- [ ] Next.js 项目初始化
- [ ] Tailwind + shadcn/ui 配置
- [ ] 侧边栏组件
- [ ] Header 组件

### Phase 2: 首页 + Chat PDF
- [ ] 首页 `/`
- [ ] Chat with PDF `/chat-pdf`
- [ ] PDF 上传与渲染
- [ ] AI 对话界面

### Phase 3: 论文搜索
- [ ] 搜索页面 `/search`
- [ ] Semantic Scholar API 集成
- [ ] 筛选器
- [ ] 结果展示

### Phase 4: AI 能力
- [ ] OpenAI API 集成
- [ ] PDF RAG 实现
- [ ] 引用溯源

---

## 📝 备注

- P0 阶段使用 Mock 数据模拟 AI 响应
- 后续接入真实 API
- 移动端适配暂不考虑
