#!/usr/bin/env python3
"""
Create missing foundation pages and update page titles based on updated rules.
"""

import os
from pathlib import Path

# Get the navigation HTML from a template file
def get_nav_html():
    """Return the standard navigation HTML structure."""
    return '''            <nav class="sidebar-nav">
                <ul class="nav-list">
                    <li class="nav-section">
                        <a href="../index.html" class="nav-link">Home</a>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Foundations</span>
                        <ul class="nav-sublist">
                            <li><a href="../foundations/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="../foundations/color.html" class="nav-link">1 Color Library</a></li>
                            <li class="nav-subsection">
                                <span class="nav-subsection-title">Typography</span>
                                <ul class="nav-subsublist">
                                    <li><a href="../foundations/typography/gt-walsheim.html" class="nav-link">GT Walsheim</a></li>
                                    <li><a href="../foundations/typography/noto-sans-jp.html" class="nav-link">Noto Sans Japan (JP)</a></li>
                                </ul>
                            </li>
                            <li><a href="../foundations/effects.html" class="nav-link">Effects</a></li>
                            <li><a href="../foundations/spacing.html" class="nav-link">2 Spacing System</a></li>
                            <li><a href="../foundations/grid.html" class="nav-link">2 Grid System</a></li>
                            <li><a href="../foundations/icons.html" class="nav-link">Icons GCC Component</a></li>
                            <li><a href="../foundations/illustrations.html" class="nav-link">Illustrations GCC Component</a></li>
                            <li><a href="../foundations/logo.html" class="nav-link">Logo GCC Component</a></li>
                            <li><a href="../foundations/system-resources.html" class="nav-link">System Resources GCC Component</a></li>
                        </ul>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Core Components</span>
                        <ul class="nav-sublist">
                            <li><a href="../components/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="../components/accordion.html" class="nav-link">Accordion</a></li>
                            <li><a href="../components/audio-player.html" class="nav-link">Audio Player</a></li>
                            <li><a href="../components/badge.html" class="nav-link">Badge / ABO Pin Level Badge</a></li>
                            <li><a href="../components/breadcrumb.html" class="nav-link">Breadcrumb</a></li>
                            <li><a href="../components/button.html" class="nav-link">Button</a></li>
                            <li><a href="../components/carousel.html" class="nav-link">Carousel</a></li>
                            <li><a href="../components/checkbox.html" class="nav-link">Checkbox</a></li>
                            <li><a href="../components/context-menu.html" class="nav-link">Context Menu / Ellipsis</a></li>
                            <li><a href="../components/country-flags.html" class="nav-link">Country Flags</a></li>
                            <li><a href="../components/date-picker.html" class="nav-link">Date Picker / Calendar</a></li>
                            <li><a href="../components/drawer.html" class="nav-link">Drawer</a></li>
                            <li><a href="../components/dropdowns.html" class="nav-link">Dropdowns</a></li>
                            <li><a href="../components/error-cards.html" class="nav-link">Error / Information Cards</a></li>
                            <li><a href="../components/header-web.html" class="nav-link">Header Web</a></li>
                            <li><a href="../components/highlights.html" class="nav-link">Highlights</a></li>
                            <li><a href="../components/inline-messages.html" class="nav-link">Inline Messages</a></li>
                            <li><a href="../components/input-fields.html" class="nav-link">Input Fields</a></li>
                            <li><a href="../components/loaders.html" class="nav-link">Loaders</a></li>
                            <li><a href="../components/modal.html" class="nav-link">Modal</a></li>
                            <li><a href="../components/notification.html" class="nav-link">Notification</a></li>
                            <li><a href="../components/pagination.html" class="nav-link">Pagination</a></li>
                            <li><a href="../components/pills-chips.html" class="nav-link">Pills / Chips</a></li>
                            <li><a href="../components/progress-tracker.html" class="nav-link">Progress Tracker / Slider / Stepper</a></li>
                            <li><a href="../components/quantity-selector.html" class="nav-link">Quantity Selector</a></li>
                            <li><a href="../components/radio-buttons.html" class="nav-link">Radio Buttons</a></li>
                            <li><a href="../components/section-divider.html" class="nav-link">Section Divider</a></li>
                            <li><a href="../components/slide-over.html" class="nav-link">Slide Over</a></li>
                            <li><a href="../components/tabs.html" class="nav-link">Tabs</a></li>
                            <li><a href="../components/tags.html" class="nav-link">Tags</a></li>
                            <li><a href="../components/text-area.html" class="nav-link">Text Area</a></li>
                            <li><a href="../components/toggle.html" class="nav-link">Toggle</a></li>
                            <li><a href="../components/tooltip.html" class="nav-link">Tooltip</a></li>
                            <li><a href="../components/variant-selector.html" class="nav-link">Variant Selector</a></li>
                        </ul>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Content & Commerce Patterns</span>
                        <ul class="nav-sublist">
                            <li><a href="../patterns/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="../patterns/article.html" class="nav-link">Article</a></li>
                            <li><a href="../patterns/cart.html" class="nav-link">Cart</a></li>
                            <li><a href="../patterns/checkout.html" class="nav-link">Checkout</a></li>
                            <li><a href="../patterns/coupons-promo-cards.html" class="nav-link">Coupons & Promo Cards</a></li>
                            <li><a href="../patterns/data-visualization.html" class="nav-link">Data Visualization</a></li>
                            <li><a href="../patterns/education-cards.html" class="nav-link">Education Cards</a></li>
                            <li><a href="../patterns/footer.html" class="nav-link">Footer</a></li>
                            <li><a href="../patterns/ingredient-card.html" class="nav-link">Ingredient Card</a></li>
                            <li><a href="../patterns/list.html" class="nav-link">List</a></li>
                            <li><a href="../patterns/mobile-phone-verification.html" class="nav-link">Mobile Phone Verification</a></li>
                            <li><a href="../patterns/product-cards.html" class="nav-link">Product Cards</a></li>
                            <li><a href="../patterns/pdp-product-details.html" class="nav-link">PDP Product Details</a></li>
                            <li><a href="../patterns/ratings-reviews.html" class="nav-link">Ratings & Reviews</a></li>
                            <li><a href="../patterns/rich-text-editor.html" class="nav-link">Rich Text Editor</a></li>
                            <li><a href="../patterns/search.html" class="nav-link">Search</a></li>
                            <li><a href="../patterns/share-bar.html" class="nav-link">Share Bar</a></li>
                            <li><a href="../patterns/sop-components.html" class="nav-link">SOP Components</a></li>
                            <li><a href="../patterns/sort-filter.html" class="nav-link">Sort / Filter</a></li>
                            <li><a href="../patterns/table.html" class="nav-link">Table</a></li>
                            <li><a href="../patterns/user-name-password.html" class="nav-link">User Name / Password / Password Strength</a></li>
                        </ul>
                    </li>
                    <li class="nav-section">
                        <span class="nav-section-title">Product / Market Specific</span>
                        <ul class="nav-sublist">
                            <li><a href="../product-specific/overview.html" class="nav-link">Overview</a></li>
                            <li><a href="../product-specific/abo-business-tools.html" class="nav-link">ABO Business Tools</a></li>
                            <li><a href="../product-specific/account-management.html" class="nav-link">Account Management Components</a></li>
                            <li><a href="../product-specific/ai-components.html" class="nav-link">AI Components</a></li>
                            <li><a href="../product-specific/amway-plus.html" class="nav-link">Amway+</a></li>
                            <li><a href="../product-specific/jtx-qualitative-research.html" class="nav-link">JTX 定性調査 UJ 1-3</a></li>
                            <li><a href="../product-specific/wellbeing-plus.html" class="nav-link">Wellbeing+</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>'''

def create_foundation_page(filename, title, ui_title, description, content_sections):
    """Create a foundation page with the standard structure."""
    nav_html = get_nav_html()
    
    # Determine if this is the active page
    active_class = ' active' if filename.endswith('.html') else ''
    page_name = filename.replace('.html', '').replace('foundations/', '')
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GCC Design System</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h1 class="sidebar-title">GCC Design System</h1>
                <button class="sidebar-toggle" id="sidebarToggle" aria-label="Toggle navigation">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
{nav_html}
        </aside>

        <main class="main-content">
            <div class="content-wrapper">
                <h1>{ui_title}</h1>
                <p class="lead">{description}</p>
{content_sections}
            </div>
        </main>
    </div>

    <script src="../script.js"></script>
</body>
</html>'''
    
    return html_content

# Define pages to create
pages = {
    'effects.html': {
        'title': 'Effects - GCC Design System',
        'ui_title': 'Effects',
        'description': 'Shadows, blurs, overlays, and other visual effects used throughout the GCC Design System.',
        'content': '''                <section class="section">
                    <h2>Overview</h2>
                    <p>Effects provide depth, hierarchy, and visual interest to the interface. This page documents shadows, blurs, overlays, and other visual effects used in the GCC Design System.</p>
                </section>

                <section class="section">
                    <h2>Shadows</h2>
                    <p>Shadow effects are used to create elevation and depth. Use design tokens for shadow values—never hard-code shadow properties.</p>
                </section>

                <section class="section">
                    <h2>Blurs</h2>
                    <p>Blur effects are used for overlays, modals, and background elements to create focus and depth.</p>
                </section>

                <section class="section">
                    <h2>Overlays</h2>
                    <p>Overlay effects provide visual separation and focus for modal dialogs, drawers, and other layered components.</p>
                </section>'''
    },
    'spacing.html': {
        'title': '2 Spacing System - GCC Design System',
        'ui_title': '2 Spacing System',
        'description': 'The spacing scale and system used for consistent spacing throughout the GCC Design System.',
        'content': '''                <section class="section">
                    <h2>Overview</h2>
                    <p>The spacing system provides a consistent scale for margins, padding, and gaps throughout the design system. Always use design tokens for spacing—never hard-code spacing values.</p>
                </section>

                <section class="section">
                    <h2>Spacing Scale</h2>
                    <p>The spacing scale uses a consistent progression to ensure visual harmony and rhythm across all components and layouts.</p>
                </section>

                <section class="section">
                    <h2>Usage Guidelines</h2>
                    <h3>Do</h3>
                    <ul>
                        <li>Use spacing tokens consistently across components</li>
                        <li>Maintain consistent spacing relationships</li>
                        <li>Use spacing tokens for all margins, padding, and gaps</li>
                    </ul>

                    <h3>Don't</h3>
                    <ul>
                        <li>Hard-code spacing values in components</li>
                        <li>Create custom spacing values outside the defined scale</li>
                        <li>Mix different spacing scales within the same component</li>
                    </ul>
                </section>'''
    },
    'grid.html': {
        'title': '2 Grid System - GCC Design System',
        'ui_title': '2 Grid System',
        'description': 'The layout grid system used for consistent page and component layouts in the GCC Design System.',
        'content': '''                <section class="section">
                    <h2>Overview</h2>
                    <p>The grid system provides a flexible, responsive layout structure for pages and components. Always use the grid system for layout—never create custom grid structures.</p>
                </section>

                <section class="section">
                    <h2>Grid Structure</h2>
                    <p>The grid system defines columns, gutters, and breakpoints for consistent layouts across different screen sizes.</p>
                </section>

                <section class="section">
                    <h2>Breakpoints</h2>
                    <p>Responsive breakpoints define how the grid adapts to different screen sizes, ensuring optimal layouts on mobile, tablet, and desktop devices.</p>
                </section>

                <section class="section">
                    <h2>Usage Guidelines</h2>
                    <h3>Do</h3>
                    <ul>
                        <li>Use the grid system for all page layouts</li>
                        <li>Follow grid breakpoints for responsive design</li>
                        <li>Maintain consistent gutters and column widths</li>
                    </ul>

                    <h3>Don't</h3>
                    <ul>
                        <li>Create custom grid structures outside the system</li>
                        <li>Hard-code column widths or gutters</li>
                        <li>Ignore grid breakpoints in responsive layouts</li>
                    </ul>
                </section>'''
    },
    'icons.html': {
        'title': 'Icons - GCC Design System',
        'ui_title': 'Icons',
        'description': 'The icon system, sizes, and usage guidelines for the GCC Design System.',
        'content': '''                <section class="section">
                    <h2>Overview</h2>
                    <p>The icon system provides a consistent set of icons for use throughout the GCC Design System. Icons are available in multiple sizes and should be used consistently to maintain visual harmony.</p>
                </section>

                <section class="section">
                    <h2>Icon Sizes</h2>
                    <p>Icons are available in standard sizes that align with the typography and spacing system. Always use design tokens for icon sizes.</p>
                </section>

                <section class="section">
                    <h2>Usage Guidelines</h2>
                    <h3>Do</h3>
                    <ul>
                        <li>Use icons from the GCC icon library</li>
                        <li>Maintain consistent icon sizes within components</li>
                        <li>Use icons to enhance understanding, not replace text</li>
                    </ul>

                    <h3>Don't</h3>
                    <ul>
                        <li>Mix icon styles from different icon sets</li>
                        <li>Use custom icons outside the system</li>
                        <li>Scale icons arbitrarily—use defined sizes</li>
                    </ul>
                </section>'''
    },
    'illustrations.html': {
        'title': 'Illustrations - GCC Design System',
        'ui_title': 'Illustrations',
        'description': 'Illustration system and usage guidelines for the GCC Design System.',
        'content': '''                <section class="section">
                    <h2>Overview</h2>
                    <p>The illustration system provides consistent visual elements for use throughout the GCC Design System. Illustrations help communicate concepts, guide users, and add visual interest to interfaces.</p>
                </section>

                <section class="section">
                    <h2>Illustration Styles</h2>
                    <p>Illustrations follow a consistent style guide to ensure visual harmony across all uses.</p>
                </section>

                <section class="section">
                    <h2>Usage Guidelines</h2>
                    <h3>Do</h3>
                    <ul>
                        <li>Use illustrations from the GCC illustration library</li>
                        <li>Maintain consistent illustration styles</li>
                        <li>Use illustrations to support content, not replace it</li>
                    </ul>

                    <h3>Don't</h3>
                    <ul>
                        <li>Mix illustration styles from different sources</li>
                        <li>Use custom illustrations outside the system</li>
                        <li>Overuse illustrations—use them purposefully</li>
                    </ul>
                </section>'''
    },
    'logo.html': {
        'title': 'Logo - GCC Design System',
        'ui_title': 'Logo',
        'description': 'Logo usage guidelines and specifications for the GCC Design System.',
        'content': '''                <section class="section">
                    <h2>Overview</h2>
                    <p>The logo is a key element of the GCC brand identity. This page documents proper logo usage, sizing, spacing, and placement guidelines.</p>
                </section>

                <section class="section">
                    <h2>Logo Variations</h2>
                    <p>The logo is available in multiple variations for different use cases, including light and dark backgrounds.</p>
                </section>

                <section class="section">
                    <h2>Usage Guidelines</h2>
                    <h3>Do</h3>
                    <ul>
                        <li>Use approved logo files from the system</li>
                        <li>Maintain proper logo spacing and clear space</li>
                        <li>Use appropriate logo variations for context</li>
                    </ul>

                    <h3>Don't</h3>
                    <ul>
                        <li>Modify or distort the logo</li>
                        <li>Use unapproved logo variations</li>
                        <li>Place the logo too close to other elements</li>
                    </ul>
                </section>'''
    },
    'system-resources.html': {
        'title': 'System Resources - GCC Design System',
        'ui_title': 'System Resources',
        'description': 'System resources, assets, and design files available for the GCC Design System.',
        'content': '''                <section class="section">
                    <h2>Overview</h2>
                    <p>System resources include design files, assets, templates, and other resources available for working with the GCC Design System.</p>
                </section>

                <section class="section">
                    <h2>Design Files</h2>
                    <p>Figma files and other design resources are available for designers working with the GCC Design System.</p>
                </section>

                <section class="section">
                    <h2>Assets</h2>
                    <p>Icons, illustrations, images, and other assets are available for use in GCC projects.</p>
                </section>

                <section class="section">
                    <h2>Resources</h2>
                    <p>Additional resources, including templates, guidelines, and documentation, are available to support design and development work.</p>
                </section>'''
    },
}

def main():
    """Create missing foundation pages."""
    foundations_dir = Path('foundations')
    foundations_dir.mkdir(exist_ok=True)
    
    created_count = 0
    for filename, page_info in pages.items():
        file_path = foundations_dir / filename
        
        # Only create if file doesn't exist
        if not file_path.exists():
            html_content = create_foundation_page(
                filename,
                page_info['title'],
                page_info['ui_title'],
                page_info['description'],
                page_info['content']
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            created_count += 1
            print(f"Created: {file_path}")
        else:
            print(f"Already exists: {file_path}")
    
    print(f"\nCreated {created_count} new foundation pages.")

if __name__ == '__main__':
    main()

