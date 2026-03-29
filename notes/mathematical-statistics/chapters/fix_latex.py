#!/usr/bin/env python3
with open('chapter5.tex', 'r') as f:
    content = f.read()

# Find all \end or \begin with possible space issues
import re
# Find \end followed by any whitespace then a letter then }
matches = re.findall(r'\\end\s+[a-zA-Z]+\}', content)
print(f"Found {len(matches)} \\end patterns with space:")
for m in matches[:10]:
    print(f"  {repr(m)}")

# Find \begin followed by any whitespace then [ (not {)
matches2 = re.findall(r'\\begin\s+[a-zA-Z]+\[', content)
print(f"\nFound {len(matches2)} \\begin patterns with space:")
for m in matches2[:10]:
    print(f"  {repr(m)}")