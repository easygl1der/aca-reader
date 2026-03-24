#!/usr/bin/env python3
"""
Literature Reference Manager
自动化的参考文献处理工作流
"""

import os
import re
import json
import sys
import argparse
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request
import time
import ssl

# 禁用 SSL 验证（解决 macOS 证书问题）
ssl._create_default_https_context = ssl._create_unverified_context

# 配置
CONFIG_PATH = Path.home() / ".literature-refs" / "config.json"
BIB_TEMPLATE = """@{citetype}{{{key},
  author = {{{author}}},
  title = {{{title}}},
  year = {{{year}}},
  publisher = {{{publisher}}}
{doi_line}
{arxiv_line}
}}"""

class LiteratureReferenceManager:
    def __init__(self, pdfs_dir=None):
        if pdfs_dir is None:
            self.pdfs_dir = Path("/Users/yueyh/Projects/aca-workflow/PDFs")
        else:
            self.pdfs_dir = Path(pdfs_dir)

        self.config = self.load_config()
        self.references = []

    def load_config(self):
        """加载配置"""
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH) as f:
                return json.load(f)

        # 创建默认配置
        config = {
            "default_format": "bibtex",
            "citation_style": "authoryear",
            "auto_save": True,
            "crossref_email": ""
        }
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f, indent=2)
        return config

    def scan_topic(self, topic):
        """扫描主题目录"""
        topic_dir = self.pdfs_dir / topic

        if not topic_dir.exists():
            print(f"❌ 主题不存在: {topic}")
            print(f"📁 可用主题: {', '.join(self.list_topics())}")
            return None

        files = []
        for f in topic_dir.rglob("*.pdf"):
            # 检查是否有对应的 md 转录文件
            md_file = f.with_suffix('.md')
            transcript_dir = f.parent / "transcript"

            has_transcript = md_file.exists() or transcript_dir.exists()

            files.append({
                "name": f.name,
                "path": str(f),
                "size": f.stat().st_size,
                "has_transcript": has_transcript
            })

        return {
            "topic": topic,
            "path": str(topic_dir),
            "files": files
        }

    def list_topics(self):
        """列出所有主题"""
        if not self.pdfs_dir.exists():
            return []
        return [d.name for d in self.pdfs_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]

    def extract_references_from_md(self, md_path):
        """从 md 文件提取参考文献"""
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找 REFERENCES 或 Bibliography 部分
        ref_pattern = r'# References\s*\n(.*?)(?:\n# |\Z)'
        match = re.search(ref_pattern, content, re.DOTALL | re.IGNORECASE)

        if not match:
            return []

        ref_section = match.group(1)

        # 提取参考文献条目
        # 格式: Author, A. (Year). Title. Journal.
        # 或: Author, A. and Author, B. (Year). Title. Journal.
        references = []

        # 按行分割，每行是一条引用
        lines = ref_section.strip().split('\n')

        for line in lines:
            line = line.strip()
            if not line or len(line) < 10:
                continue

            # 跳过空行或太短的行
            if line.startswith('#') or line.startswith('The literature'):
                continue

            # 尝试匹配格式: Author (Year)
            # 格式: Author, A. (Year). Title.
            pattern = r'^([^(]+)\s*\((\d{4})\)\.\s*([^.]+)'
            match = re.match(pattern, line)

            if match:
                authors = match.group(1).strip()
                year = match.group(2).strip()
                title = match.group(3).strip()

                # 去除末尾的期刊信息
                title = re.sub(r'\.\s*[A-Z][^.]+\.$', '', title).strip()

                references.append({
                    "id": len(references) + 1,
                    "authors": authors,
                    "title": title,
                    "year": year,
                    "raw": line[:100]  # 保存原始行用于调试
                })

        return references

    def search_crossref(self, query, author=None, year=None):
        """使用 CrossRef API 搜索"""
        # 构建搜索查询
        search_terms = []
        if author:
            search_terms.append(author.split(',')[0].split(' et ')[0])
        if year:
            search_terms.append(year)
        if query:
            search_terms.append(query[:50])

        search_query = ' '.join(search_terms[:3])
        url = f"https://api.crossref.org/works?query={urllib.parse.quote(search_query)}&rows=5"

        if self.config.get("crossref_email"):
            url += f"&mailto={urllib.parse.quote(self.config['crossref_email'])}"

        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read())

                if data['message']['items']:
                    item = data['message']['items'][0]

                    # 提取 DOI
                    doi = item.get('DOI', '')

                    # 提取作者
                    authors = []
                    for a in item.get('author', []):
                        given = a.get('given', '')
                        family = a.get('family', '')
                        if family:
                            authors.append(f"{family}, {given}" if given else family)
                    author_str = ' and '.join(authors[:3]) if authors else 'Unknown'

                    # 提取标题
                    title = item.get('title', [''])[0] if item.get('title') else ''

                    # 提取年份
                    pub_year = item.get('published-print', {}).get('date-parts', [[None]])[0][0]
                    if not pub_year:
                        pub_year = item.get('created', {}).get('date-parts', [[None]])[0][0]

                    # 提取期刊/出版社
                    container = item.get('container-title', [''])[0]
                    publisher = item.get('publisher', container)

                    return {
                        "found": True,
                        "doi": doi,
                        "author": author_str,
                        "title": title,
                        "year": str(pub_year) if pub_year else year or '',
                        "publisher": publisher,
                        "type": item.get('type', 'article')
                    }

        except Exception as e:
            print(f"  ⚠️ CrossRef 查询失败: {e}")

        return {"found": False}

    def generate_bibtex(self, ref_data, custom_key=None):
        """生成 BibTeX 引用"""
        if not ref_data.get("found"):
            return None

        # 生成 cite key
        if custom_key:
            key = custom_key
        else:
            first_author = ref_data.get("author", "Unknown").split(',')[0].split(' ')[0]
            year = ref_data.get("year", "0000")
            key = f"{first_author}{year}"

        # 确定引用类型
        ref_type = ref_data.get("type", "article")
        type_map = {
            "journal-article": "article",
            "book-chapter": "incollection",
            "book": "book",
            "proceedings-article": "inproceedings"
        }
        cite_type = type_map.get(ref_type, "misc")

        # 构建 BibTeX
        doi_line = f"  doi = {{{ref_data.get('doi', '')}}}," if ref_data.get('doi') else ""
        arxiv_line = ""

        bib = BIB_TEMPLATE.format(
            citetype=cite_type,
            key=key,
            author=ref_data.get("author", "Unknown"),
            title=ref_data.get("title", "Unknown"),
            year=ref_data.get("year", ""),
            publisher=ref_data.get("publisher", ""),
            doi_line=doi_line,
            arxiv_line=arxiv_line
        )

        return bib

    def process_references(self, references, output_path=None):
        """处理参考文献列表"""
        results = []
        total = len(references)

        for i, ref in enumerate(references, 1):
            print(f"\n[{i}/{total}] 处理: {ref.get('authors', 'Unknown')} ({ref.get('year', '')})")

            # 搜索
            result = self.search_crossref(
                ref.get('title', ''),
                ref.get('authors', ''),
                ref.get('year', '')
            )

            if result.get("found"):
                # 生成 BibTeX
                bib = self.generate_bibtex(result)
                result["bibtex"] = bib
                print(f"  ✓ 找到: {result.get('title', '')[:50]}...")
                print(f"    DOI: {result.get('doi', 'N/A')}")
            else:
                print(f"  ❌ 未找到")

            results.append(result)
            time.sleep(0.5)  # 速率限制

        # 保存结果
        if output_path:
            self.save_bibtex(results, output_path)

        return results

    def save_bibtex(self, results, output_path):
        """保存 BibTeX 文件"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("% Generated by Literature Reference Manager\n\n")

            found_count = 0
            for r in results:
                if r.get("bibtex"):
                    f.write(r["bibtex"])
                    f.write("\n\n")
                    found_count += 1

            f.write(f"% Total: {found_count}/{len(results)} references found\n")

        print(f"\n📁 已保存: {output_path}")
        print(f"✓ 成功获取: {found_count}/{len(results)} 篇")


def main():
    parser = argparse.ArgumentParser(description="Literature Reference Manager")
    parser.add_argument("topic", nargs="?", help="文献主题或文件路径")
    parser.add_argument("--scan", action="store_true", help="扫描文献库")
    parser.add_argument("--list", action="store_true", help="列出所有主题")
    parser.add_argument("--extract", help="从 md 文件提取参考文献")
    parser.add_argument("--process", help="处理参考文献文件")
    parser.add_argument("--output", "-o", help="输出文件路径")

    args = parser.parse_args()

    manager = LiteratureReferenceManager()

    # 列出所有主题
    if args.list:
        topics = manager.list_topics()
        print("\n📚 可用主题:")
        for t in topics:
            print(f"  - {t}")
        return

    # 扫描主题
    if args.scan and args.topic:
        result = manager.scan_topic(args.topic)
        if result:
            print(f"\n📁 主题: {result['topic']}")
            print(f"📂 路径: {result['path']}")
            print(f"\n📄 文献列表 ({len(result['files'])} 个):\n")

            for i, f in enumerate(result['files'], 1):
                size_mb = f['size'] / (1024 * 1024)
                status = "✅" if f['has_transcript'] else "❌"
                print(f"[{i}] {f['name']}")
                print(f"    大小: {size_mb:.1f} MB | 转录: {status}")
        return

    # 提取参考文献
    if args.extract:
        refs = manager.extract_references_from_md(args.extract)
        print(f"\n找到 {len(refs)} 篇参考文献:")
        for r in refs:
            print(f"  [{r['id']}] {r.get('authors', 'Unknown')} ({r.get('year', '')})")
            print(f"      {r.get('title', '')[:60]}...")
        return

    # 处理参考文献
    if args.process:
        import json
        with open(args.process) as f:
            refs = json.load(f)

        output = args.output or "references.bib"
        manager.process_references(refs, output)
        return

    # 默认：扫描
    print("📚 Literature Reference Manager\n")
    print("用法:")
    print("  /文献引用管理器 --list                    # 列出所有主题")
    print("  /文献引用管理器 bayesian --scan            # 扫描 bayesian 主题")
    print("  /文献引用管理器 --extract <md文件>         # 提取参考文献")
    print("\n示例:")
    print("  /文献引用管理器 bayesian")


if __name__ == "__main__":
    main()
