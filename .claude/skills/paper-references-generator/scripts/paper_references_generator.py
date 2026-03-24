#!/usr/bin/env python3
"""
Paper References Generator
从 md 转录文件提取参考文献，使用 CrossRef API 生成 BibTeX
"""

import re
import json
import time
import sys
import subprocess
from urllib.parse import quote

def search_crossref(query, limit=3):
    """搜索 CrossRef API - 免费无需 API key"""
    url = f"https://api.crossref.org/works?query={quote(query)}&rows={limit}"

    try:
        result = subprocess.run(
            ['curl', '-s', '-k', url],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0 and result.stdout:
            return json.loads(result.stdout)
    except Exception as e:
        print(f"Error searching: {e}", file=sys.stderr)
    return None

def extract_references(md_content):
    """从 md 内容中提取参考文献"""
    lines = md_content.split('\n')

    # 找到 REFERENCES 开始位置
    ref_start = -1
    for i, line in enumerate(lines):
        if re.match(r'^#*\s*REFERENCES\s*$', line, re.IGNORECASE) or \
           re.match(r'^#*\s*BIBLIOGRAPHY\s*$', line, re.IGNORECASE):
            ref_start = i
            break

    if ref_start == -1:
        return []

    # 提取参考文献条目 - 合并多行
    references = []
    current_ref = []

    for line in lines[ref_start+1:]:
        # 遇到空行或新的一级标题则停止
        if line.strip() == '' or (line.strip().startswith('# ') and not line.strip().startswith('##')):
            if current_ref:
                ref_text = ' '.join(current_ref).strip()
                if ref_text:
                    references.append(ref_text)
                current_ref = []
        elif re.match(r'^\[\d+\]', line.strip()):
            # 新的参考文献条目开始
            if current_ref:
                ref_text = ' '.join(current_ref).strip()
                if ref_text:
                    references.append(ref_text)
            current_ref = [line.strip()]
        else:
            current_ref.append(line.strip())

    # 处理最后一个
    if current_ref:
        ref_text = ' '.join(current_ref).strip()
        if ref_text:
            references.append(ref_text)

    # 解析每条参考文献
    parsed_refs = []
    for ref in references:
        # 匹配 [数字] 开头
        match = re.match(r'\[(\d+)\]\s*(.+)', ref)
        if match:
            num = match.group(1)
            text = match.group(2)

            # 提取搜索查询 - 取前100字符
            search_query = text.split('.')[0].strip() if '.' in text else text[:100]
            # 移除多余空格
            search_query = ' '.join(search_query.split())

            parsed_refs.append({
                'number': num,
                'raw': ref,
                'search_query': search_query
            })

    return parsed_refs

def parse_crossref_result(item):
    """解析 CrossRef 结果"""
    title = item.get('title', [''])[0] if item.get('title') else ''
    authors = item.get('author', [])
    year = None
    if item.get('published-print'):
        year = item.get('published-print', {}).get('date-parts', [[None]])[0][0]
    elif item.get('published-online'):
        year = item.get('published-online', {}).get('date-parts', [[None]])[0][0]
    elif item.get('created'):
        year = item.get('created', {}).get('date-parts', [[None]])[0][0]

    doi = item.get('DOI', '')
    container = item.get('container-title', [''])[0] if item.get('container-title') else ''
    volume = item.get('volume', '')
    issue = item.get('issue', '')
    pages = item.get('page', '')

    return {
        'title': title,
        'authors': authors,
        'year': year,
        'doi': doi,
        'container': container,
        'volume': volume,
        'issue': issue,
        'pages': pages
    }

def generate_bibtex(paper, ref_num):
    """根据 CrossRef 结果生成 BibTeX"""
    title = paper.get('title', '')
    authors = paper.get('authors', [])
    year = paper.get('year', '')
    doi = paper.get('doi', '')
    container = paper.get('container', '')
    volume = paper.get('volume', '')
    issue = paper.get('issue', '')
    pages = paper.get('pages', '')

    # 生成作者字符串
    author_str = ''
    if authors:
        author_list = []
        for a in authors[:3]:  # 最多3个作者
            family = a.get('family', '')
            given = a.get('given', '')
            if family and given:
                author_list.append(f"{family}, {given[0]}.")
            elif family:
                author_list.append(family)
        author_str = ' and '.join(author_list)
        if len(authors) > 3:
            author_str += ' and others'

    # 确定引用键
    first_author = authors[0].get('family', 'unknown').lower() if authors else 'ref'
    bib_key = f"{first_author}{year}" if year else f"{first_author}ref{ref_num}"

    # 确定类型
    if container:
        bib_type = 'article'
    else:
        bib_type = 'book'

    # 构建 BibTeX
    bibtex = f"@{bib_type}{{{bib_key},\n"
    if author_str:
        bibtex += f"  author = {{{author_str}}},\n"
    if title:
        bibtex += f"  title = {{{title}}},\n"
    if year:
        bibtex += f"  year = {{{year}}},\n"
    if container:
        bibtex += f"  journal = {{{container}}},\n"
    if volume:
        bibtex += f"  volume = {{{volume}}},\n"
    if issue:
        bibtex += f"  number = {{{issue}}},\n"
    if pages:
        bibtex += f"  pages = {{{pages}}},\n"
    if doi:
        bibtex += f"  doi = {{{doi}}},\n"

    bibtex = bibtex.rstrip(',\n') + "\n}"

    return bib_key, bibtex

def process_file(md_file_path):
    """处理单个 md 文件"""
    print(f"处理文件: {md_file_path}")

    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    refs = extract_references(content)
    print(f"找到 {len(refs)} 篇参考文献\n")

    results = []

    for ref in refs:
        print(f"处理 [{ref['number']}] {ref['search_query'][:50]}...")

        # 搜索
        data = search_crossref(ref['search_query'])

        if data and data.get('message', {}).get('items'):
            item = data['message']['items'][0]
            paper = parse_crossref_result(item)
            bib_key, bibtex = generate_bibtex(paper, ref['number'])

            results.append({
                'number': ref['number'],
                'title': paper.get('title', ref['search_query']),
                'bib_key': bib_key,
                'bibtex': bibtex,
                'success': True
            })

            print(f"  ✓ 找到: {paper.get('title', '')[:50]}")
        else:
            results.append({
                'number': ref['number'],
                'title': ref['search_query'],
                'success': False
            })
            print(f"  ✗ 未找到")

        time.sleep(0.5)  # 速率限制

    return results

def main():
    if len(sys.argv) < 2:
        print("用法: python paper_references_generator.py <md文件路径>")
        sys.exit(1)

    md_file = sys.argv[1]
    results = process_file(md_file)

    # 输出结果
    print("\n" + "="*60)
    print("BibTeX 参考文献")
    print("="*60 + "\n")

    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]

    for r in successful:
        print(f"### [{r['number']}] {r['title'][:60]}")
        print(f"BibTeX key: {r['bib_key']}")
        print("```bibtex")
        print(r['bibtex'])
        print("```\n")

    if failed:
        print("### 未找到的参考文献（需手动处理）")
        for r in failed:
            print(f"- [{r['number']}] {r['title']}")

if __name__ == '__main__':
    main()
