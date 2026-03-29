# 文献管理专家教训记忆

**适用对象**: research-expert, research-expert-2
**最后更新**: 2026-03-30

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L1101 | PDF 命名规范 | 2 |
| L1102 | Git 大文件禁止 | 1 |
| L1103 | Transcript 目录命名 | 1 |

---

## L1101: PDF 命名规范

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
PDF 文件命名不符合规范（年份缺失、标题空格、作者分隔符错误）。

**正确格式**:
```
{作者标识}-{年份}-{简短标题}.pdf
```

| 场景 | 格式 | 示例 |
|------|------|------|
| 单作者 | `{姓}-{年份}-{简短标题}` | `Samuel-2024-MolevSaganFormula` |
| 双作者 | `{姓1姓2}-{年份}-{简短标题}` | `GaoXiong-2025-TripleSchubertPositivity` |
| 多作者 | `{姓1姓2...}-{年份}-{简短标题}` | `BilleyGaoPawlowski-2023-IntroductionToCohomology` |

**规则**:
- 作者标识：姓连写，首字母大写
- 年份：4位数字
- 标题：2-4 个关键词，CamelCase
- 分隔符：`-`（连字符）

**错误示例**:
```
Samuel-2024-MolevSagan.pdf     ❌（标题 CamelCase 连写）
Li-QuantumSchubertIdentities.pdf  ❌（缺少年份）
Molev-Sagan-Formula.pdf       ❌（作者分隔符应为连写）
```

**防止措施**:
- 下载后立即按规范重命名
- 参考 CLAUDE.md 的 PDF 命名规范

---

## L1102: Git 大文件禁止

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
将超过 50MB 的 PDF 提交到 git。

**正确做法**:
- **超过 50MB 的 PDF 不要提交到 git**
- 备份到 Google Drive 或其他外部存储
- 或使用 GitHub LFS（需付费）

**Git LFS 限制**:
- 免费额度仅 1GB
- 超过 100MB 的文件无法 push 到 GitHub

**如果已提交**:
- 使用 git worktree 隔离操作
- 不要用 `git filter-repo`（会删除历史）

**防止措施**:
- 下载后检查文件大小
- 大文件单独备份

---

## L1103: Transcript 目录命名

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
Transcript 目录命名与 PDF 命名不一致。

**正确格式**:
```
PDFs/quantum-schubert/Samuel-2024-MolevSaganFormula.pdf
PDFs/quantum-schubert/transcript/Samuel-2024-MolevSaganFormula/
```

**规则**:
- Transcript 目录名与 PDF 文件名（去掉 `.pdf`）一致
-Transcript 目录放在 `transcript/` 子目录下

**防止措施**:
- 转录前先确认 PDF 文件名
- 保持命名一致性

---

## 核心检查清单

- [ ] PDF 命名符合 `{姓}-{年份}-{简短标题}.pdf` 格式
- [ ] 文件大小 < 50MB（或单独备份）
- [ ] Transcript 目录与 PDF 命名一致
- [ ] 存放路径符合主题分类

---

## 文献库路径规范

| 主题 | PDF 库路径 | Transcript 路径 |
|------|------------|-----------------|
| causal-inference | PDFs/causal-inference/ | PDFs/causal-inference/transcript/ |
| schubert / quantum-schubert | PDFs/quantum-schubert/ | PDFs/quantum-schubert/transcript/ |
| differential-geometry | PDFs/differential-geometry/ | PDFs/differential-geometry/transcript/ |
| bayesian | PDFs/bayesian/ | PDFs/bayesian/transcript/ |
| information-geometry | PDFs/information-geometry/ | PDFs/information-geometry/transcript/ |

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/research-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是文献管理专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
