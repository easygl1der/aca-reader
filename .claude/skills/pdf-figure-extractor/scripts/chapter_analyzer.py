#!/usr/bin/env python3
"""
PDF 章节信息查询工具
查询指定章节的 Figure 列表、页码及上下文，并可导出单页 PDF
"""

import os
import re
import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def analyze_chapter(pdf_path: str, chapter_num: int, context_lines: int = 5):
    """
    分析指定章节的 Figure 信息

    Args:
        pdf_path: PDF 文件路径
        chapter_num: 章节编号
        context_lines: 上下文行数

    Returns:
        list: [{"figure": "2-1", "page": 70, "context": "..."}, ...]
    """
    reader = PdfReader(pdf_path)
    results = []

    # 匹配 Figure X-YY 或 Figure X.YY 格式
    pattern = rf'Figure\s*{chapter_num}[\.\-](\d+)'

    for page_num, page in enumerate(reader.pages, 1):
        text = page.extract_text()
        if not text:
            continue

        # 查找该页所有 Figure 引用
        matches = re.finditer(pattern, text, re.IGNORECASE)

        for match in matches:
            fig_num = match.group(1)
            fig_id = f"{chapter_num}-{fig_num}"

            # 提取上下文
            pos = match.start()
            lines = text.split('\n')

            # 找到包含该 figure 的行
            context = ""
            for i, line in enumerate(lines):
                if f"Figure {chapter_num}-{fig_num}" in line or f"Figure {chapter_num}.{fig_num}" in line:
                    start = max(0, i - context_lines)
                    end = min(len(lines), i + context_lines + 1)
                    context = '\n'.join(lines[start:end])
                    break

            results.append({
                "figure": fig_id,
                "page": page_num,
                "context": context.strip()
            })

    return results


def extract_pages(pdf_path: str, pages: list, output_dir: str):
    """
    提取指定页面为单页 PDF

    Args:
        pdf_path: 源 PDF 路径
        pages: 页码列表 [70, 71, 73, ...]
        output_dir: 输出目录
    """
    os.makedirs(output_dir, exist_ok=True)

    reader = PdfReader(pdf_path)

    for page_num in pages:
        if page_num < 1 or page_num > len(reader.pages):
            print(f"⚠️  页码 {page_num} 超出范围，跳过")
            continue

        writer = PdfWriter()
        writer.add_page(reader.pages[page_num - 1])  # 转换为 0-based

        output_path = os.path.join(output_dir, f"page-{page_num:03d}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"✅ 提取: page-{page_num:03d}.pdf")

    print(f"\n📁 已保存到: {output_dir}")


def print_results(results: list):
    """打印查询结果"""
    if not results:
        print("❌ 未找到相关 Figure")
        return

    # 按页码排序
    results.sort(key=lambda x: x["page"])

    print(f"\n共找到 {len(results)} 个 Figure:\n")

    for r in results:
        print(f"Figure {r['figure']}: Page {r['page']}")
        print("-" * 40)
        print(r["context"][:300] + "..." if len(r["context"]) > 300 else r["context"])
        print("=" * 40 + "\n")


def main():
    parser = argparse.ArgumentParser(description="PDF 章节信息查询工具")
    parser.add_argument("pdf", type=str, help="PDF 文件路径")
    parser.add_argument("--chapter", "-c", type=int, required=True, help="章节编号 (如 2)")
    parser.add_argument("--figure", "-f", type=str, help="指定 Figure 编号 (如 2-1)")
    parser.add_argument("--page", "-p", type=int, help="指定页码")
    parser.add_argument("--extract", "-e", type=str, help="导出页面到指定目录")
    parser.add_argument("--context", "-n", type=int, default=5, help="上下文行数 (默认 5)")
    parser.add_argument("--list", "-l", action="store_true", help="仅列出 Figure 列表")

    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"❌ 文件不存在: {args.pdf}")
        return

    # 分析章节
    results = analyze_chapter(args.pdf, args.chapter, args.context)

    if args.figure:
        # 筛选特定 Figure
        results = [r for r in results if r["figure"] == args.figure]

    if args.page:
        # 筛选特定页码
        results = [r for r in results if r["page"] == args.page]

    if args.list:
        # 仅列出 Figure 列表
        results.sort(key=lambda x: x["page"])
        for r in results:
            print(f"Figure {r['figure']}: Page {r['page']}")
        return

    # 打印结果
    print_results(results)

    # 导出页面
    if args.extract:
        pages = list(set(r["page"] for r in results))
        print(f"\n正在导出 {len(pages)} 页到 {args.extract}...")
        extract_pages(args.pdf, pages, args.extract)


if __name__ == "__main__":
    main()
