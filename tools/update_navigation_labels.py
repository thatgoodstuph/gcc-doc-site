#!/usr/bin/env python3
"""
Update navigation labels in all HTML files to match the updated rules.
"""

import os
import re
from pathlib import Path

# Define the new navigation labels based on docs-site-rules.md
nav_updates = {
    'Color': '1 Color Library',
    'Effects': 'Effects',
    'Spacing': '2 Spacing System',
    'Grid': '2 Grid System',
    'Icons': 'Icons GCC Component',
    'Illustrations': 'Illustrations GCC Component',
    'Logo': 'Logo GCC Component',
    'System Resources': 'System Resources GCC Component',
}

# Typography labels are already correct, but ensure they're right
typography_labels = {
    'GT Walsheim': 'GT Walsheim',
    'Noto Sans Japan (JP)': 'Noto Sans Japan (JP)',
}

def update_navigation_in_file(file_path):
    """Update navigation labels in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update each navigation label
        for old_label, new_label in nav_updates.items():
            # Pattern to match navigation links with the old label
            # Match both the link text and the href
            patterns = [
                # Pattern for nav links: <a href="..." class="nav-link">Old Label</a>
                (rf'(<a href="[^"]*" class="nav-link">){re.escape(old_label)}(</a>)', 
                 lambda m: f'{m.group(1)}{new_label}{m.group(2)}'),
                # Pattern for active nav links: <a href="..." class="nav-link active">Old Label</a>
                (rf'(<a href="[^"]*" class="nav-link active">){re.escape(old_label)}(</a>)', 
                 lambda m: f'{m.group(1)}{new_label}{m.group(2)}'),
            ]
            
            for pattern, replacement in patterns:
                content = re.sub(pattern, replacement, content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Update all HTML files in the project."""
    project_root = Path('.')
    html_files = list(project_root.rglob('*.html'))
    
    updated_count = 0
    for html_file in html_files:
        if update_navigation_in_file(html_file):
            updated_count += 1
            print(f"Updated: {html_file}")
    
    print(f"\nUpdated {updated_count} files.")

if __name__ == '__main__':
    main()

