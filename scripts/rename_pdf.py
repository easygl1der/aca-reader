#!/usr/bin/env python3
"""
PDF 自动重命名脚本
- 检测 PDFs 文件夹中的新文件
- 从 PDF 元数据或第一页提取标题
- 自动重命名为清晰的文件名
"""

import os
import re
import sys
from pathlib import Path

# 尝试导入 PDF 库
try:
    import fitz  # PyMuPDF
    PDF_LIB = "pymupdf"
except ImportError:
    try:
        import pdfplumber
        PDF_LIB = "pdfplumber"
    except ImportError:
        PDF_LIB = None


def clean_filename(name: str) -> str:
    """清理文件名，移除非法字符"""
    # 移除或替换非法字符
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', ' ', name)
    name = name.strip()
    # 限制长度
    if len(name) > 100:
        name = name[:100]
    return name


def extract_title_from_metadata(pdf_path: str) -> str:
    """从 PDF 元数据中提取标题"""
    if PDF_LIB == "pymupdf":
        try:
            doc = fitz.open(pdf_path)
            metadata = doc.metadata
            title = metadata.get('title', '').strip()
            author = metadata.get('author', '').strip()
            doc.close()

            if title:
                if author:
                    return f"{title} - {author}"
                return title
        except Exception as e:
            print(f"  元数据提取失败: {e}")

    return ""


def extract_title_from_content(pdf_path: str) -> str:
    """从 PDF 第一页内容中提取标题"""
    if PDF_LIB == "pymupdf":
        try:
            doc = fitz.open(pdf_path)
            first_page = doc[0]
            text = first_page.get_text()

            # 尝试找到标题（通常是第一行或较大的文字）
            lines = text.split('\n')
            for line in lines[:10]:  # 检查前10行
                line = line.strip()
                if len(line) > 5 and len(line) < 150:
                    # 跳过页码、数字等
                    if not line.isdigit() and not re.match(r'^\d+\.', line):
                        doc.close()
                        return line

            doc.close()
        except Exception as e:
            print(f"  内容提取失败: {e}")

    return ""


def get_arxiv_title(pdf_path: str) -> str:
    """从 arXiv ID 提取标题（如果文件名是 arXiv ID）"""
    # 匹配 arXiv ID 格式: 2305.18793, 2305.18793v2 等
    match = re.search(r'(\d{4}\.\d{4,5})(v\d+)?', os.path.basename(pdf_path))
    if match:
        arxiv_id = match.group(1)
        # 这里可以扩展为调用 arXiv API 获取标题
        # 目前返回格式化的 ID
        return f"arXiv_{arxiv_id}"

    return ""


def rename_pdf(pdf_path: str) -> str:
    """重命名 PDF 文件"""
    dir_path = os.path.dirname(pdf_path)
    old_name = os.path.basename(pdf_path)

    print(f"\n处理: {old_name}")

    # 1. 优先从内容获取（通常第一页有完整书名）
    title = extract_title_from_content(pdf_path)

    # 2. 如果没有，从元数据获取
    if not title:
        title = extract_title_from_metadata(pdf_path)

    # 3. 如果是 arXiv ID 格式
    if not title:
        title = get_arxiv_title(pdf_path)

    if not title:
        print(f"  无法提取标题，跳过")
        return old_name

    # 清理并生成新文件名
    new_name = clean_filename(title) + ".pdf"
    new_path = os.path.join(dir_path, new_name)

    # 如果名称没变或已存在
    if new_name == old_name:
        print(f"  文件名已是清晰格式: {old_name}")
        return old_name

    if os.path.exists(new_path) and new_path != pdf_path:
        print(f"  目标文件已存在: {new_name}")
        return old_name

    # 重命名
    try:
        os.rename(pdf_path, new_path)
        print(f"  已重命名: {old_name} -> {new_name}")
        return new_name
    except Exception as e:
        print(f"  重命名失败: {e}")
        return old_name


def scan_pdfs(pdfs_dir: str):
    """扫描 PDFs 文件夹并重命名"""
    pdfs_path = Path(pdfs_dir)

    if not pdfs_path.exists():
        print(f"目录不存在: {pdfs_dir}")
        return

    pdf_files = list(pdfs_path.glob("*.pdf"))

    if not pdf_files:
        print("没有找到 PDF 文件")
        return

    print(f"找到 {len(pdf_files)} 个 PDF 文件")

    for pdf_file in pdf_files:
        rename_pdf(str(pdf_file))


def watch_pdfs(pdfs_dir: str, interval: int = 30):
    """监控 PDFs 文件夹，有新文件时自动重命名（简化版）"""
    import time
    from datetime import datetime

    print(f"监控模式: {pdfs_dir}")
    print(f"检查间隔: {interval} 秒")
    print("按 Ctrl+C 退出\n")

    processed = set()

    # 记录已处理的文件
    pdf_files = Path(pdfs_dir).glob("*.pdf")
    for f in pdf_files:
        processed.add(f.name)

    while True:
        try:
            time.sleep(interval)

            pdf_files = Path(pdfs_dir).glob("*.pdf")
            for f in pdf_files:
                if f.name not in processed:
                    print(f"\n检测到新文件: {f.name}")
                    rename_pdf(str(f))
                    processed.add(f.name)

        except KeyboardInterrupt:
            print("\n监控结束")
            break


def main():
    import argparse

    parser = argparse.ArgumentParser(description="PDF 自动重命名工具")
    parser.add_argument("directory", nargs="?", default="PDFs",
                        help="PDF 文件目录 (默认: PDFs)")
    parser.add_argument("--watch", "-w", action="store_true",
                        help="监控模式，持续检测新文件")
    parser.add_argument("--interval", "-i", type=int, default=30,
                        help="监控间隔秒数 (默认: 30)")

    args = parser.parse_args()

    # 获取 PDF 目录的绝对路径
    pdfs_dir = os.path.abspath(args.directory)

    if not os.path.isdir(pdfs_dir):
        print(f"目录不存在: {pdfs_dir}")
        sys.exit(1)

    if args.watch:
        watch_pdfs(pdfs_dir, args.interval)
    else:
        scan_pdfs(pdfs_dir)


if __name__ == "__main__":
    main()
