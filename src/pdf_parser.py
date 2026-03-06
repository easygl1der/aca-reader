#!/usr/bin/env python3
"""
PDF Parser for Literature Reading Workflow
Extracts chapter structure and core theorems/definitions from PDF files.
"""

import sys
import json
import re
from pathlib import Path

# Try to import pdf libraries, fallback gracefully
try:
    import fitz  # PyMuPDF
    PDF_LIB = "pymupdf"
except ImportError:
    try:
        import pdfplumber
        PDF_LIB = "pdfplumber"
    except ImportError:
        PDF_LIB = None


def extract_chapter_structure(text: str) -> list:
    """Extract chapter/section structure from text."""
    structure = []

    # Pattern for chapters (Chapter X, 第X章)
    chapter_pattern = re.compile(r'^(?:Chapter\s+(\d+)|第(\d+)章)\s*(.+)$', re.MULTILINE)

    # Pattern for sections (Section X.X, X.X)
    section_pattern = re.compile(r'^(\d+\.\d+)\s+(.+)$', re.MULTILINE)

    # Pattern for theorems/definitions
    theorem_pattern = re.compile(
        r'^(Theorem|Definition|Lemma|Corollary|Proposition)\s+(\d+\.\d+)',
        re.MULTILINE | re.IGNORECASE
    )

    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Check for chapter
        chapter_match = chapter_pattern.match(line.strip())
        if chapter_match:
            num = chapter_match.group(1) or chapter_match.group(2)
            title = chapter_match.group(3)
            structure.append({
                "type": "chapter",
                "number": num,
                "title": title.strip(),
                "line": i
            })
            continue

        # Check for section
        section_match = section_pattern.match(line.strip())
        if section_match:
            num = section_match.group(1)
            title = section_match.group(2)
            structure.append({
                "type": "section",
                "number": num,
                "title": title.strip(),
                "line": i
            })
            continue

        # Check for theorem/definition
        theorem_match = theorem_pattern.match(line.strip())
        if theorem_match:
            theorem_type = theorem_match.group(1)
            theorem_num = theorem_match.group(2)
            structure.append({
                "type": "theorem",
                "theorem_type": theorem_type,
                "number": theorem_num,
                "line": i
            })

    return structure


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF using available library."""
    if PDF_LIB == "pymupdf":
        return extract_with_pymupdf(pdf_path)
    elif PDF_LIB == "pdfplumber":
        return extract_with_pdfplumber(pdf_path)
    else:
        raise ImportError("Please install PyMuPDF: pip install pymupdf")


def extract_with_pymupdf(pdf_path: str) -> str:
    """Extract text using PyMuPDF."""
    text_parts = []
    doc = fitz.open(pdf_path)
    for page in doc:
        text_parts.append(page.get_text())
    doc.close()
    return '\n'.join(text_parts)


def extract_with_pdfplumber(pdf_path: str) -> str:
    """Extract text using pdfplumber."""
    text_parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_parts.append(page.extract_text() or '')
    return '\n'.join(text_parts)


def analyze_pdf(pdf_path: str) -> dict:
    """Main function to analyze PDF and extract structure."""
    if not Path(pdf_path).exists():
        return {"error": f"File not found: {pdf_path}"}

    if PDF_LIB is None:
        return {
            "error": "No PDF library available. Please install: pip install pymupdf"
        }

    try:
        text = extract_text_from_pdf(pdf_path)
        structure = extract_chapter_structure(text)

        # Extract first page as overview
        first_page = text.split('\n')[:50]

        return {
            "pdf_path": pdf_path,
            "library_used": PDF_LIB,
            "total_chars": len(text),
            "structure": structure,
            "overview": '\n'.join(first_page)
        }
    except Exception as e:
        return {"error": str(e)}


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_parser.py <pdf_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    result = analyze_pdf(pdf_path)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
