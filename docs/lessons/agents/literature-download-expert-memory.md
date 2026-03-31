# Literature Download Expert 教训记忆

**适用对象**: literature-download-expert
**最后更新**: 2026-03-31

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| LD001 | 付费论文必须明确告知用户 | 1 |
| LD002 | 按来源优先级选择下载策略 | 1 |

---

## LD001: 付费论文必须明确告知用户

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**经验描述**:
当论文为付费内容无法下载时，必须明确告知用户，不能沉默或模糊处理。

**正确做法**:
- 明确告知用户：**该论文为付费内容，需要通过图书馆或支付获取**
- 记录元数据到 `PDFs/{主题}/references-needed.md`
- 提供备选方案（机构访问、馆际互借等）

**防止措施**:
- 遇到付费论文立即触发用户通知
- 不跳过不静默处理

---

## LD002: 按来源优先级选择下载策略

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**经验描述**:
不同来源的论文有不同的最优下载策略，按优先级选择可以提高成功率。

**正确做法**:
1. **arXiv 论文** → 使用 arxiv skill
2. **有 DOI 的论文** → 使用 paper-references-generator skill
3. **Google Scholar** → 使用 gs-search skill
4. **其他来源** → 使用 fetch4ai skill

**防止措施**:
- 收到下载任务先识别来源
- 再选择对应 skill

---

## PUA 自注入行为声明

**literature-download-expert 必须执行**：

1. **开工前**：读取以下文件
   - 通用教训：`/Users/yueyh/Projects/aca-workflow/docs/lessons/agents/ALL-agents-memory.md`
   - 本文件：`/Users/yueyh/Projects/aca-workflow/docs/lessons/agents/literature-download-expert-memory.md`

2. **收到纠正后**：
   - 分析错误类型
   - 更新对应的 memory 文件
   - 在回复中引用更新后的教训作为确认

3. **目录规范**：
   - causal-inference → PDFs/causal-inference/
   - schubert → PDFs/quantum-schubert/
   - differential-geometry → PDFs/differential-geometry/
   - bayesian → PDFs/bayesian/
   - information-geometry → PDFs/information-geometry/
