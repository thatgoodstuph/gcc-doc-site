import os
from datetime import datetime

# Configuration
PARTIALS_DIR = 'tools/partials'
TARGET_DIRS = ['components', 'foundations', 'patterns', 'product-specific', 'meta']
TODAY = datetime.now().strftime('%Y-%m-%d')

def get_root_prefix(file_path):
    depth = len(file_path.split(os.sep)) - 1
    return '../' * depth if depth > 0 else ''

def sync():
    # Load partials
    with open(os.path.join(PARTIALS_DIR, 'sidebar.html'), 'r') as f:
        sidebar_template = f.read()
    with open(os.path.join(PARTIALS_DIR, 'component-header.html'), 'r') as f:
        header_template = f.read()

    # Process all HTML files
    files_to_process = ['index.html']
    for d in TARGET_DIRS:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith('.html'):
                    files_to_process.append(os.path.join(d, f))

    for file_path in files_to_process:
        print(f"Processing {file_path}...")
        with open(file_path, 'r') as f:
            content = f.read()

        root = get_root_prefix(file_path)

        # 1. Inject Sidebar
        if '<!-- GCC:SIDEBAR_START -->' in content:
            sidebar = sidebar_template.replace('{ROOT}', root)
            start_marker = '<!-- GCC:SIDEBAR_START -->'
            end_marker = '<!-- GCC:SIDEBAR_END -->'
            parts = content.split(start_marker)
            after_end = parts[1].split(end_marker)[1]
            content = f"{parts[0]}{start_marker}\n{sidebar}\n{end_marker}{after_end}"

        # 2. Inject Header (only for components/patterns/product-specific)
        if '<!-- GCC:HEADER_START -->' in content:
            header = header_template.format(
                STATUS="Stable",
                STATUS_CLASS="stable",
                OWNER="GCC Design System",
                LAST_UPDATED=TODAY,
                LAST_REVIEWED=TODAY,
                FIGMA_URL="#",
                IMPLEMENTATION_URL="#",
                CHANGELOG_URL=f"{root}meta/changelog.html",
                ROOT=root
            )
            start_marker = '<!-- GCC:HEADER_START -->'
            end_marker = '<!-- GCC:HEADER_END -->'
            parts = content.split(start_marker)
            after_end = parts[1].split(end_marker)[1]
            content = f"{parts[0]}{start_marker}\n{header}\n{end_marker}{after_end}"

        with open(file_path, 'w') as f:
            f.write(content)

    print("Done! All files synced.")

if __name__ == "__main__":
    sync()