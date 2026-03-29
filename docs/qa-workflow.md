# QA 工作流

## QA Specialist Agent

### 简介
QA Specialist 是一个**项目专属**的 agent，负责处理学习过程中的问答记录。

### 工作流程
当用户提问时，QA Specialist 自动执行：
1. **识别 topic** → 确定问题属于哪个领域
2. **转发给 domain expert** → 如因果推断问题发给 causal-expert
3. **接收回答** → expert 回复（或 fallback 直接回答）
4. **记录到 qa.tex** → 使用标准格式
5. **添加脚注引用** → 在正文首次出现处
6. **重新编译 PDF** → 使用 `compile.sh`

### Topic → Expert 映射
| Topic | Expert |
|-------|--------|
| 因果推断 | causal-expert |
| 微分几何 | geometry-expert |
| 贝叶斯统计 | bayesian-expert |
| 信息几何 | info-geo-expert |
| Schubert | schubert-expert |

### Topic → qa.tex 映射（关键！必须根据问题主题选择正确的文件）
- 因果推断 → notes/A-First-Course-in-Causal-Inference/appendix/qa.tex
- 微分几何 → notes/differential-geometry/do-carmo-curves-surfaces/appendix/qa.tex
- 贝叶斯统计 → notes/bayesian/appendix/qa.tex
- 信息几何 → notes/information-geometry/appendix/qa.tex
- Schubert演算 → notes/Schubert-Polynomials/appendix/qa.tex

### 容错机制
- 如果 expert 无响应，QA Specialist 直接回答作为 fallback
- 复杂问题可触发 `/gemini-browser-chat` 获取更全面回答

### QA 格式（必须遵循）
```latex
\subsection{Question Title}\label{sec:qa-descriptive-key}

\textbf{问}：User's question?

\textbf{答}：Answer content...
```

### 脚注引用格式
```latex
...概念...\footnote{问：What is X? 见附录 \cref{sec:qa-descriptive-key}。}
```

### 使用方式
在新对话中，直接描述问题即可。QA Specialist 会自动处理完整工作流。

---

## 每次用户提问后必须执行以下步骤

1. 口语化回答用户
2. ✅ **记录到 `appendix/qa.tex`**（强制要求，不要忘记！）
3. 如有正式定义需要，添加到正文对应章节
4. 重新编译 PDF
