# LaTeX Label/Reference 验证工具

验证笔记中的 label 定义和 cref 引用与原论文编号是否一致，确保 LaTeX 编译无误。

## 触发条件

当用户说以下内容时使用此 skill：
- "修正一下原文总的 label, ref 对应关系是否合理"
- "检查 label 引用"
- "验证定理编号"
- "编译报错"（编译前先执行此验证）

## 工作流程

### 步骤 1：提取笔记中所有 label 定义

```bash
grep -nE '\\\\label\{[^}]+\}' <笔记文件> | grep -v '^(eq:|rem:|app:|sec:|chap:)'
```

重点关注以下类型的 label：
- `def:` - 定义环境
- `thm:` - 定理环境
- `lem:` / `Lemma` - 引理环境
- `cor:` / `Corollary` - 推论环境
- `conj:` - 猜想环境

### 步骤 2：提取笔记中所有 cref 引用

```bash
grep -nE '\\\\cref\{[^}]+\}' <笔记文件>
```

### 步骤 3：检查原论文中的编号

在原文转录文件（`PDFs/<topic>/transcript/<paper>/`）中搜索：
1. 论文中的 Theorem/Lemma/Corollary/Definition 编号
2. 论文中的 cite 引用（如 `\cite[ Theorem 1.1]{author}`）

### 步骤 4：建立编号映射表

对比笔记中的 label 命名与论文中的编号，建立映射：

| 论文编号 | 笔记 label | 笔记标题 | 是否一致 |
|---------|-----------|---------|---------|
| Theorem 1.1 | def:Theorem12 | ... | ✗ |

### 步骤 5：识别问题

常见问题类型：
1. **编号不一致**：论文中是 Theorem 1.1，笔记中 label 是 `def:Theorem12`
2. **引用错误**：笔记引用 `\cite[ Theorem 1.1]` 但实际应该是 Theorem 2.3
3. **环境不匹配**：定义为 Corollary 但结束标签写成 Theorem
4. **缺失/重复**：论文有某个定理但笔记缺失，或重复出现

### 步骤 6：编译验证

修改前先编译确认当前状态：
```bash
cd <笔记目录> && bash compile.sh
```

### 步骤 7：报告问题并请求修复

报告格式：
```
发现 X 个问题：

1. 位置:行号
   当前: \cref{def:Theorem12} 引用 \cite[ Theorem 1.1]{GX2025}
   问题: 论文中 Theorem 1.1 是 triple Schubert positivity，但这里引用的是 Refined Graham (Theorem 2.3)
   建议: 改为 \cite[ Theorem 2.3]{GX2025}

是否修复？ (yes/no)
```

### 步骤 8：用户确认后执行修复

收到用户确认后，使用 Edit 工具执行修正。

## 修正规则

| 问题类型 | 修正方式 |
|---------|---------|
| 编号不一致 | 修正引用中的编号 |
| 环境标签错误 | 修正 \\begin{xxx} 和 \\end{xxx} |
| 证明逻辑错误 | 重写证明（基于原文） |
| 重复内容 | 删除重复部分 |

## 注意事项

1. **先读原文再修正**：必须对照原论文确认正确内容
2. **单次修正不超过 3 个问题**：避免一次太多修改难以 review
3. **修正后重新编译**：验证修改没有引入新问题
4. **保持 label 命名一致**：同一概念全程使用相同的 label

## 示例对话

用户: "修正一下原文总的 label, ref 对应关系是否合理"

助手: [执行验证流程，发现问题，报告]

用户: "应该参考原文献,修正错误"

助手: [执行修正，编译验证]

用户: "把你刚才的操作封装成一个 skill"

助手: [创建此 skill]
