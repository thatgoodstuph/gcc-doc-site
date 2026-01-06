#!/usr/bin/env python3
"""
Update the site structure to match the updated rules from gcc-figma-docs-rules.mdc
"""

import os
import re
from pathlib import Path

def get_new_nav_html():
    """Return the new navigation HTML structure based on updated rules."""
    return '''            <nav class="sidebar-nav">
                <ul class="nav-list">
                    <li class="nav-section">
                        <a href="{base_path}index.html" class="nav-link">Home</a>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Foundations</span>
                        <ul class="nav-sublist">
                            <li><a href="{base_path}foundations/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="{base_path}foundations/color.html" class="nav-link">Color</a></li>
                            <li class="nav-subsection">
                                <span class="nav-subsection-title">Typography</span>
                                <ul class="nav-subsublist">
                                    <li><a href="{base_path}foundations/typography/gt-walsheim.html" class="nav-link">Typography: GT Walsheim</a></li>
                                    <li><a href="{base_path}foundations/typography/noto-sans-jp.html" class="nav-link">Typography: Noto Sans Japan</a></li>
                                </ul>
                            </li>
                            <li><a href="{base_path}foundations/effects.html" class="nav-link">Effects</a></li>
                            <li><a href="{base_path}foundations/spacing.html" class="nav-link">Spacing</a></li>
                            <li><a href="{base_path}foundations/grid.html" class="nav-link">Grid System</a></li>
                            <li><a href="{base_path}foundations/icons.html" class="nav-link">Icon</a></li>
                            <li><a href="{base_path}foundations/illustrations.html" class="nav-link">Illustration</a></li>
                            <li><a href="{base_path}foundations/logo.html" class="nav-link">Logo</a></li>
                            <li><a href="{base_path}foundations/system-resources.html" class="nav-link">System Resources</a></li>
                        </ul>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Components</span>
                        <ul class="nav-sublist">
                            <li><a href="{base_path}components/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="{base_path}components/accordion.html" class="nav-link">Accordion</a></li>
                            <li><a href="{base_path}components/audio-player.html" class="nav-link">Audio Player</a></li>
                            <li><a href="{base_path}components/badge.html" class="nav-link">Badge / ABO Pin Level Badge</a></li>
                            <li><a href="{base_path}components/breadcrumb.html" class="nav-link">Breadcrumb</a></li>
                            <li><a href="{base_path}components/button.html" class="nav-link">Button</a></li>
                            <li><a href="{base_path}components/carousel.html" class="nav-link">Carousel</a></li>
                            <li><a href="{base_path}components/checkbox.html" class="nav-link">Checkbox</a></li>
                            <li><a href="{base_path}components/context-menu.html" class="nav-link">Context Menu / Ellipsis</a></li>
                            <li><a href="{base_path}components/country-flags.html" class="nav-link">Country Flags</a></li>
                            <li><a href="{base_path}components/date-picker.html" class="nav-link">Date Picker / Calendar</a></li>
                            <li><a href="{base_path}components/drawer.html" class="nav-link">Drawer</a></li>
                            <li><a href="{base_path}components/dropdowns.html" class="nav-link">Dropdowns</a></li>
                            <li><a href="{base_path}components/error-cards.html" class="nav-link">Error / Information Cards</a></li>
                            <li><a href="{base_path}components/header-web.html" class="nav-link">Header Web</a></li>
                            <li><a href="{base_path}components/highlights.html" class="nav-link">Highlights</a></li>
                            <li><a href="{base_path}components/inline-messages.html" class="nav-link">Inline Messages</a></li>
                            <li><a href="{base_path}components/input-fields.html" class="nav-link">Input Fields</a></li>
                            <li><a href="{base_path}components/loaders.html" class="nav-link">Loaders</a></li>
                            <li><a href="{base_path}components/modal.html" class="nav-link">Modal</a></li>
                            <li><a href="{base_path}components/notification.html" class="nav-link">Notification</a></li>
                            <li><a href="{base_path}components/pagination.html" class="nav-link">Pagination</a></li>
                            <li><a href="{base_path}components/pills-chips.html" class="nav-link">Pills / Chips</a></li>
                            <li><a href="{base_path}components/progress-tracker.html" class="nav-link">Progress Tracker / Slider / Stepper</a></li>
                            <li><a href="{base_path}components/quantity-selector.html" class="nav-link">Quantity Selector</a></li>
                            <li><a href="{base_path}components/radio-buttons.html" class="nav-link">Radio Buttons</a></li>
                            <li><a href="{base_path}components/section-divider.html" class="nav-link">Section Divider</a></li>
                            <li><a href="{base_path}components/slide-over.html" class="nav-link">Slide Over</a></li>
                            <li><a href="{base_path}components/tabs.html" class="nav-link">Tabs</a></li>
                            <li><a href="{base_path}components/tags.html" class="nav-link">Tags</a></li>
                            <li><a href="{base_path}components/text-area.html" class="nav-link">Text Area</a></li>
                            <li><a href="{base_path}components/toggle.html" class="nav-link">Toggle</a></li>
                            <li><a href="{base_path}components/tooltip.html" class="nav-link">Tooltip</a></li>
                            <li><a href="{base_path}components/variant-selector.html" class="nav-link">Variant Selector</a></li>
                        </ul>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Patterns</span>
                        <ul class="nav-sublist">
                            <li><a href="{base_path}patterns/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="{base_path}patterns/article.html" class="nav-link">Article</a></li>
                            <li><a href="{base_path}patterns/cart.html" class="nav-link">Cart</a></li>
                            <li><a href="{base_path}patterns/checkout.html" class="nav-link">Checkout</a></li>
                            <li><a href="{base_path}patterns/coupons-promo-cards.html" class="nav-link">Coupons & Promo Cards</a></li>
                            <li><a href="{base_path}patterns/data-visualization.html" class="nav-link">Data Visualization</a></li>
                            <li><a href="{base_path}patterns/education-cards.html" class="nav-link">Education Cards</a></li>
                            <li><a href="{base_path}patterns/footer.html" class="nav-link">Footer</a></li>
                            <li><a href="{base_path}patterns/ingredient-card.html" class="nav-link">Ingredient Card</a></li>
                            <li><a href="{base_path}patterns/list.html" class="nav-link">List</a></li>
                            <li><a href="{base_path}patterns/mobile-phone-verification.html" class="nav-link">Mobile Phone Verification</a></li>
                            <li><a href="{base_path}patterns/product-cards.html" class="nav-link">Product Cards</a></li>
                            <li><a href="{base_path}patterns/pdp-product-details.html" class="nav-link">PDP Product Details</a></li>
                            <li><a href="{base_path}patterns/ratings-reviews.html" class="nav-link">Ratings & Reviews</a></li>
                            <li><a href="{base_path}patterns/rich-text-editor.html" class="nav-link">Rich Text Editor</a></li>
                            <li><a href="{base_path}patterns/search.html" class="nav-link">Search</a></li>
                            <li><a href="{base_path}patterns/share-bar.html" class="nav-link">Share Bar</a></li>
                            <li><a href="{base_path}patterns/sop-components.html" class="nav-link">SOP Components</a></li>
                            <li><a href="{base_path}patterns/sort-filter.html" class="nav-link">Sort / Filter</a></li>
                            <li><a href="{base_path}patterns/table.html" class="nav-link">Table</a></li>
                            <li><a href="{base_path}patterns/user-name-password.html" class="nav-link">User Name / Password / Password Strength</a></li>
                        </ul>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Product / Market</span>
                        <ul class="nav-sublist">
                            <li><a href="{base_path}product-specific/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="{base_path}product-specific/abo-business-tools.html" class="nav-link">ABO Business Tools</a></li>
                            <li><a href="{base_path}product-specific/account-management.html" class="nav-link">Account Management Components</a></li>
                            <li><a href="{base_path}product-specific/ai-components.html" class="nav-link">AI Components</a></li>
                            <li><a href="{base_path}product-specific/amway-plus.html" class="nav-link">Amway+</a></li>
                            <li><a href="{base_path}product-specific/jtx-qualitative-research.html" class="nav-link">JTX 定性調査 UJ 1-3</a></li>
                            <li><a href="{base_path}product-specific/wellbeing-plus.html" class="nav-link">Wellbeing+</a></li>
                        </ul>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Meta</span>
                        <ul class="nav-sublist">
                            <li><a href="{base_path}meta/about.html" class="nav-link">About GCC Design System</a></li>
                            <li><a href="{base_path}meta/how-to-use.html" class="nav-link">How to Use These Docs</a></li>
                            <li><a href="{base_path}meta/changelog.html" class="nav-link">Changelog</a></li>
                            <li><a href="{base_path}meta/contribution.html" class="nav-link">Contribution & Governance</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>'''

def calculate_base_path(file_path):
    """Calculate the base path for navigation links based on file location."""
    path = Path(file_path)
    depth = len(path.parts) - 1  # Subtract 1 for filename
    
    if depth == 1:  # Root level (index.html)
        return ""
    elif depth == 2:  # One level deep (foundations/, components/, etc.)
        return "../"
    elif depth == 3:  # Two levels deep (foundations/typography/, etc.)
        return "../../"
    else:
        return "../" * (depth - 1)

def update_navigation_in_file(file_path):
    """Update navigation in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Calculate base path
        base_path = calculate_base_path(file_path)
        
        # Get new navigation HTML
        new_nav = get_new_nav_html().format(base_path=base_path)
        
        # Find and replace the navigation section
        # Match from <nav class="sidebar-nav"> to </nav>
        nav_pattern = r'<nav class="sidebar-nav">.*?</nav>'
        content = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)
        
        # Also update section titles
        replacements = [
            (r'<span class="nav-section-title">Core Components</span>', 
             '<span class="nav-section-title">Components</span>'),
            (r'<span class="nav-section-title">Content & Commerce Patterns</span>', 
             '<span class="nav-section-title">Patterns</span>'),
            (r'<span class="nav-section-title">Product / Market Specific</span>', 
             '<span class="nav-section-title">Product / Market</span>'),
        ]
        
        for old, new in replacements:
            content = re.sub(old, new, content)
        
        # Update navigation link labels
        link_replacements = [
            (r'<a href="[^"]*color\.html" class="nav-link[^"]*">1 Color Library</a>', 
             lambda m: m.group(0).replace('1 Color Library', 'Color')),
            (r'<a href="[^"]*typography/gt-walsheim\.html" class="nav-link[^"]*">GT Walsheim</a>', 
             lambda m: m.group(0).replace('GT Walsheim', 'Typography: GT Walsheim')),
            (r'<a href="[^"]*typography/noto-sans-jp\.html" class="nav-link[^"]*">Noto Sans Japan \(JP\)</a>', 
             lambda m: m.group(0).replace('Noto Sans Japan (JP)', 'Typography: Noto Sans Japan')),
            (r'<a href="[^"]*spacing\.html" class="nav-link[^"]*">2 Spacing System</a>', 
             lambda m: m.group(0).replace('2 Spacing System', 'Spacing')),
            (r'<a href="[^"]*grid\.html" class="nav-link[^"]*">2 Grid System</a>', 
             lambda m: m.group(0).replace('2 Grid System', 'Grid System')),
            (r'<a href="[^"]*icons\.html" class="nav-link[^"]*">Icons GCC Component</a>', 
             lambda m: m.group(0).replace('Icons GCC Component', 'Icon')),
            (r'<a href="[^"]*illustrations\.html" class="nav-link[^"]*">Illustrations GCC Component</a>', 
             lambda m: m.group(0).replace('Illustrations GCC Component', 'Illustration')),
            (r'<a href="[^"]*logo\.html" class="nav-link[^"]*">Logo GCC Component</a>', 
             lambda m: m.group(0).replace('Logo GCC Component', 'Logo')),
            (r'<a href="[^"]*system-resources\.html" class="nav-link[^"]*">System Resources GCC Component</a>', 
             lambda m: m.group(0).replace('System Resources GCC Component', 'System Resources')),
        ]
        
        for pattern, replacement in link_replacements:
            content = re.sub(pattern, replacement, content)
        
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
        if update_navigation_in_file(html_file):
            updated_count += 1
            print(f"Updated: {html_file}")
    
    print(f"\nUpdated {updated_count} files.")

if __name__ == '__main__':
    main()

