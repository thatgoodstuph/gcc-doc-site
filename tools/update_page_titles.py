#!/usr/bin/env python3
"""
Update page titles to match the new naming convention.
"""

import re
from pathlib import Path

# Page title updates: (old_pattern, new_title)
title_updates = [
    (r'<title>Color - GCC Design System</title>', '<title>1 Color Library - GCC Design System</title>'),
    (r'<title>Iconography - GCC Design System</title>', '<title>Icons - GCC Design System</title>'),
    (r'<title>Spacing & Grid - GCC Design System</title>', '<title>2 Spacing System - GCC Design System</title>'),
]

# Also update h1 titles in content
h1_updates = [
    (r'<h1>Color</h1>', '<h1>1 Color Library</h1>'),
    (r'<h1>Iconography</h1>', '<h1>Icons</h1>'),
    (r'<h1>Spacing & Grid</h1>', '<h1>2 Spacing System</h1>'),
]

def update_file(file_path):
    """Update titles in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update page titles
        for old_pattern, new_title in title_updates:
            content = re.sub(old_pattern, new_title, content)
        
        # Update h1 titles
        for old_pattern, new_h1 in h1_updates:
            content = re.sub(old_pattern, new_h1, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Update all HTML files."""
    project_root = Path('.')
    html_files = list(project_root.rglob('*.html'))
    
    updated_count = 0
    for html_file in html_files:
        if update_file(html_file):
            updated_count += 1
            print(f"Updated: {html_file}")
    
    print(f"\nUpdated {updated_count} files.")

if __name__ == '__main__':
    main()

