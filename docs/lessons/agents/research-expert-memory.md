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
| L1104 | arXiv ID 与 DOI 验证 | 1 |

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

## L1104: arXiv ID 与 DOI 验证

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
research-expert 下载论文时使用了错误的 arXiv ID (math/0005028)，导致下载到不相关的论文（关于代数方程组的复根）。references.bib 中的页码信息也可能不准确（449-477 vs 实际 599-614）。

**正确流程**:

1. **使用 arxiv skill 搜索论文**
   ```
   使用 Skill tool 调用 arxiv skill：
   - 搜索作者 + 标题关键词
   - 获取正确的 arXiv ID
   ```

2. **交叉验证**
   - 从引用该论文的其他文献（如 Gao-Xiong 2025）确认 arXiv ID
   - 检查 DOI 指向的页面
   - 核对期刊页码（不同卷期页码不同！）

3. **验证论文内容**
   - 下载后用 pdftotext 提取文本
   - 搜索关键词确认是目标论文
   - 搜索 "Theorem X.Y" 确认定理编号

**Graham 论文验证案例**:
```
错误信息：
- arXiv ID math/0005028 → 实际是关于代数方程根的论文
- references.bib: pages 449-477

正确信息：
- arXiv: 无正确 ID（2001年期刊论文）
- DOI: 10.1215/S0022-247X-01-52483-4
- 正确页码: 599-614 (Duke Math J 109(3))
- Gao-Xiong 引用: [8] Graham, Theorem 3.2
```

**操作命令**:
```bash
# 提取 PDF 文本验证
pdftotext paper.pdf /tmp/paper_text.txt
grep -n "Theorem 3.2" /tmp/paper_text.txt

# 搜索关键词验证
grep -n "Schubert\|positivity\|equivariant" /tmp/paper_text.txt
```

**防止措施**:
- 使用 arxiv skill 搜索获取正确 ID
- 从引用该论文的其他文章确认编号
- 下载后立即验证内容
- 检查页码是否与 references.bib 一致

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/research-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是文献管理专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认

---

# 文献验证专家教训记忆（补充）

**适用对象**: research-expert（文献验证专家）

**最后更新**: 2026-03-30

---

## 职责定位

research-expert 是 **文献验证专家**，负责：
1. 对比笔记与原文，确保定义/定理正确
2. 发现笔记中的概念性错误
3. 为 domain expert 提供验证报告

---

## 触发场景

| 场景 | 说明 |
|------|------|
| 定义验证 | 笔记中写了某个定义，需要确认是否与原文一致 |
| 定理核实 | 某个定理的条件、结论需要核实 |
| 公式验证 | 微分/差分计算需要对照原文 |
| Gemini 发现错误 | Gemini 校对后发现疑似错误，需要核实 |

---

## 验证报告格式

```markdown
## 验证报告: [概念/定理名称]

### 1. 原文定义/定理
- **来源**: [书籍/论文名], Chapter X, Page Y
- **内容**: [原文定义或定理]

### 2. 笔记中的定义/定理
- **位置**: [章节/文件]
- **内容**: [笔记中的定义]

### 3. 一致性判断
- [ ] ✓ 一致
- [ ] ✗ 不一致
- [ ] ⚠ 部分差异

### 4. 差异说明
[详细说明差异内容及正确内容]
```

---

## Chapter 1 验证教训（Gemini 发现）

| 位置 | 错误描述 | 正确内容 |
|------|----------|----------|
| Bruhat order | `≥` 方向反 | 应该 `≤` |
| 链比较 | `231 < 312` 不可比较 | 231 和 312 在 Bruhat order 下不可比较 |
| 偏导计算 | ∂₁(x₂²) = x₂+x₁ | 正确是 -(x₁+x₂) |
| 偏导计算 | ∂₁∂₂(x₁) = 1 | 正确是 0 |
| 差分算子 | ∂w/v = ∂w ∘ ∂v⁻¹ | ∂ᵢ⁻¹ 不存在，∂ᵢ²=0 是幂零的 |

---

## 常用搜索命令

```bash
# 搜索 .md 转录文件（搜索性能更好）
grep -r "Bruhat" PDFs/quantum-schubert/transcript/
grep -r "Definition" PDFs/differential-geometry/

# 搜索特定书籍
grep -r "geodesic" PDFs/differential-geometry/Do\ Carmo*.md
grep -r "Potential Outcome" PDFs/causal-inference/transcript/
```
