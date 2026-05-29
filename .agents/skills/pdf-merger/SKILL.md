---
name: pdf-merger
description: 合并多个PDF文件为一个PDF。用于将简历、自我陈述、商业计划书等申请材料整合成一份文件。当用户提到"合并PDF"、"整合PDF"、"把多个PDF合成一个"时使用此skill。
---

# PDF Merger Skill

## 概述

此skill用于将多个PDF文件合并成一个PDF文件。常用于申请材料整合场景（如黄埔班申请需要提交简历+自我陈述+商业计划书）。

## 使用场景

- 用户说"合并PDF"
- 用户说"整合PDF"
- 用户说"把多个PDF合成一个"
- 用户需要将申请材料整合成一份文件提交

## 工作流程

### 步骤1：确认需要合并的PDF文件

询问用户需要合并哪些PDF文件，以及合并后的输出文件名。

典型输入文件（黄埔班申请示例）：
- resume.pdf（简历）
- personal-statement.pdf（自我陈述）
- business-plan.pdf（商业计划书）

### 步骤2：使用Python合并PDF

使用pypdf库合并PDF。确保Python环境已安装pypdf：

```bash
pip3 install pypdf
```

### 步骤3：执行合并

运行以下Python代码：

```python
from pypdf import PdfWriter
import os

# 设置PDF所在目录
base_dir = "/Users/yueyh/Projects/huangpu-application"

# 要合并的PDF文件（按顺序）
pdf_files = [
    "resume.pdf",
    "personal-statement.pdf",
    "business-plan.pdf"
]

# 输出文件名
output_file = "数学学院-大三-数学与应用数学-乐绎华-23363017.pdf"

merger = PdfWriter()

for pdf in pdf_files:
    pdf_path = os.path.join(base_dir, pdf)
    with open(pdf_path, 'rb') as f:
        merger.append(f)

output_path = os.path.join(base_dir, output_file)
with open(output_path, 'wb') as f:
    merger.write(f)

print(f"PDF合并成功: {output_file}")
```

### 步骤4：验证结果

确认合并后的PDF文件已生成，告知用户文件路径。

## 注意事项

1. 确保所有要合并的PDF文件都存在
2. PDF文件按传入顺序合并
3. 输出的PDF文件名应包含有意义的名字（如"姓名-申请项目-学号"）
4. 如果遇到xattr问题，使用open()方式读取文件再传入merger

## 常见问题

**Q: 遇到"xattr"或文件找不到错误？**
A: 使用`with open(file_path, 'rb') as f: merger.append(f)`方式读取文件

**Q: pypdf未安装？**
A: 运行`pip3 install pypdf`安装
