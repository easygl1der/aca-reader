# latex-debug

## 功能

自动检测并修复 LaTeX 编译错误，每次修改后自动提交 git。

## 触发条件

- LaTeX 编译报错
- 用户请求调试 LaTeX 错误

## 工作流程

### 步骤 1: 编译检测

1. 运行 `xelatex -interaction=nonstopmode main.tex` 编译
2. 检查输出中的错误信息
3. 如果有错误，记录错误类型和位置

### 步骤 2: 分析错误

常见错误类型：
- `Undefined reference`: 引用未定义 → 检查 label
- `Missing $`: 数学模式错误 → 检查公式
- `Extra }`: 多余的括号 → 检查括号配对
- `Undefined control sequence`: 未定义命令 → 检查宏包
- `Label(s) may have changed`: 需要重新编译

### 步骤 3: 修复错误

根据错误类型进行修复：
1. **Undefined reference**:
   - 检查对应的 label 是否存在
   - 格式必须是 `\label{name}`（不是 `\label_name}` 或 `\label{name}}`）
   - 重新编译

2. **Missing $ / Extra }**:
   - 找到报错行号
   - 检查该行的括号配对
   - 特别注意 label、cref、equation 环境

3. **Package not found**:
   - 检查是否正确加载宏包

### 步骤 4: Git 提交

每次修复后：
```bash
git add -A
git commit -m "fix: 修复 LaTeX 编译错误"
```

### 步骤 5: 验证

再次编译确认无错误。如果还有错误，重复步骤 2-4。

## 注意事项

- 每次修改都必须提交 git
- 仔细阅读错误信息中的行号
- 如果是 "Label(s) may have changed"，重新编译即可
- Label 格式必须是 `\label{name}`，不能用 `\label_name}` 或 `\label{name}}`
