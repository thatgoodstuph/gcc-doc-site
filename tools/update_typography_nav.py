#!/usr/bin/env python3
"""Update navigation to use flat Typography link instead of nested structure."""

import os
import re
from pathlib import Path

def update_typography_nav(file_path):
    """Replace nested Typography nav with flat link."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern for nested Typography subsection
    # Matches the entire nested structure
    pattern = r'''<li class="nav-subsection">\s*<span class="nav-subsection-title">Typography</span>\s*<ul class="nav-subsublist">\s*<li><a href="[^"]*typography[^"]*" class="nav-link">[^<]*</a></li>\s*<li><a href="[^"]*typography[^"]*" class="nav-link">[^<]*</a></li>\s*</ul>\s*</li>'''
    
    # Determine the correct path based on file location
    if 'foundations/' in file_path or file_path.startswith('foundations/'):
        replacement = '<li><a href="typography.html" class="nav-link">Typography</a></li>'
    elif 'components/' in file_path or file_path.startswith('components/'):
        replacement = '<li><a href="../foundations/typography.html" class="nav-link">Typography</a></li>'
    elif 'patterns/' in file_path or file_path.startswith('patterns/'):
        replacement = '<li><a href="../foundations/typography.html" class="nav-link">Typography</a></li>'
    elif 'tools/meta/' in file_path or file_path.startswith('tools/meta/'):
        replacement = '<li><a href="../../foundations/typography.html" class="nav-link">Typography</a></li>'
    elif file_path == 'index.html':
        replacement = '<li><a href="foundations/typography.html" class="nav-link">Typography</a></li>'
    else:
        replacement = '<li><a href="typography.html" class="nav-link">Typography</a></li>'
    
    # Try multiline pattern
    pattern_multiline = r'''<li class="nav-subsection">.*?<span class="nav-subsection-title">Typography</span>.*?<ul class="nav-subsublist">.*?<li><a href="[^"]*typography[^"]*" class="nav-link">[^<]*</a></li>.*?<li><a href="[^"]*typography[^"]*" class="nav-link">[^<]*</a></li>.*?</ul>.*?</li>'''
    
    new_content = re.sub(pattern_multiline, replacement, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    """Update all HTML files."""
    updated = []
    
    # Find all HTML files
    for root, dirs, files in os.walk('.'):
        # Skip the typography subdirectory and tools/meta
        if 'typography' in root and root != '.':
            continue
        if 'tools/meta' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if update_typography_nav(file_path):
                    updated.append(file_path)
    
    print(f"Updated {len(updated)} files:")
    for f in updated:
        print(f"  - {f}")

if __name__ == '__main__':
    main()

