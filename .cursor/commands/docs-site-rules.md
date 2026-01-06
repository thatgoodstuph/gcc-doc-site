---
name: "gcc-docs-site-rules"
description: "Information Architecture, Sidebar structure, and URL routing for the GCC design system documentation site"
alwaysApply: false
---

# Context

This file defines the **site structure, navigation, and routing** for the GCC design system documentation site.  
It is inspired by Primer's IA (Foundations → Components → Patterns → Meta) and mirrors the GCC component and pattern list from Figma.

# Information Architecture

The site must use a **persistent sidebar** with the following top-level sections, in this exact order:

## 1. Foundations

Global design primitives and libraries.

- **Color**
  - Color
- **Typography**
  - Typography: GT Walsheim
  - Typography: Noto Sans Japan
- **Effects**
  - Effects (shadows, blurs, overlays)
- **Spacing**
  - Spacing
- **Grid**
  - Grid System
- **Icons**
  - Icon
- **Illustrations**
  - Illustration
- **Logo**
  - Logo
- **System Resources**
  - System Resources

## 2. Components

Reusable UI building blocks, listed alphabetically.

- Accordion
- Audio Player
- Badge / ABO Pin Level Badge
- Breadcrumb
- Button
- Carousel
- Checkbox
- Context Menu / Ellipsis
- Country Flags
- Date Picker / Calendar
- Drawer
- Dropdowns
- Error / Information Cards
- Header Web
- Highlights
- Inline Messages
- Input Fields
- Loaders
- Modal
- Notification
- Pagination
- Pills / Chips
- Progress Tracker / Slider / Stepper
- Quantity Selector
- Radio Buttons
- Section Divider
- Slide Over
- Tabs
- Tags
- Text Area
- Toggle
- Tooltip
- Variant Selector

## 3. Patterns

Flows and compositions built from core components.

- Article
- Cart
- Checkout
- Coupons & Promo Cards
- Data Visualization
- Education Cards
- Footer
- Ingredient Card
- List
- Mobile Phone Verification
- Product Cards
- PDP Product Details
- Ratings & Reviews
- Rich Text Editor
- Search
- Share Bar
- SOP Components
- Sort / Filter
- Table
- User Name / Password / Password Strength

## 4. Product / Market

Product-specific implementations built from GCC components.

- ABO Business Tools
- Account Management Components
- AI Components
- Amway+
- JTX 定性調査 UJ 1-3
- Wellbeing+

## 5. Meta

System-level information and governance.

- About GCC Design System
- How to Use These Docs
- Changelog
- Contribution & Governance

# Sidebar Behavior

- The sidebar must be **sticky/persistent** on desktop viewports.
- On smaller viewports (mobile/tablet), the sidebar may collapse into a drawer or hamburger menu.
- Sidebar categories (Foundations, Components, Patterns, Product / Market, Meta) must be **collapsible**.
- Nested items (e.g., Typography: GT Walsheim, Typography: Noto Sans Japan) must be shown under their parent category when expanded.

# URL Structure

Use semantic, predictable routing so designers and developers can guess URLs.

## Foundations
- `/foundations/color`
- `/foundations/typography/gt-walsheim`
- `/foundations/typography/noto-sans-japan`
- `/foundations/effects`
- `/foundations/spacing`
- `/foundations/grid`
- `/foundations/icons`
- `/foundations/illustrations`
- `/foundations/logo`
- `/foundations/system-resources`

## Components
- `/components/accordion`
- `/components/audio-player`
- `/components/badge`
- `/components/breadcrumb`
- `/components/button`
- `/components/carousel`
- `/components/checkbox`
- `/components/context-menu`
- `/components/country-flags`
- `/components/date-picker`
- `/components/drawer`
- `/components/dropdowns`
- `/components/error-cards`
- `/components/header-web`
- `/components/highlights`
- `/components/inline-messages`
- `/components/input-fields`
- `/components/loaders`
- `/components/modal`
- `/components/notification`
- `/components/pagination`
- `/components/pills`
- `/components/progress-tracker`
- `/components/quantity-selector`
- `/components/radio-buttons`
- `/components/section-divider`
- `/components/slide-over`
- `/components/tabs`
- `/components/tags`
- `/components/text-area`
- `/components/toggle`
- `/components/tooltip`
- `/components/variant-selector`

## Patterns
- `/patterns/article`
- `/patterns/cart`
- `/patterns/checkout`
- `/patterns/coupons-promo-cards`
- `/patterns/data-visualization`
- `/patterns/education-cards`
- `/patterns/footer`
- `/patterns/ingredient-card`
- `/patterns/list`
- `/patterns/mobile-phone-verification`
- `/patterns/product-cards`
- `/patterns/pdp-product-details`
- `/patterns/ratings-reviews`
- `/patterns/rich-text-editor`
- `/patterns/search`
- `/patterns/share-bar`
- `/patterns/sop-components`
- `/patterns/sort-filter`
- `/patterns/table`
- `/patterns/user-name-password`

## Product / Market
- `/product/abo-business-tools`
- `/product/account-management`
- `/product/ai-components`
- `/product/amway-plus`
- `/product/jtx-uj-1-3`
- `/product/wellbeing-plus`

## Meta
- `/meta/about`
- `/meta/how-to-use`
- `/meta/changelog`
- `/meta/contribution`

# Naming Conventions

- Page titles in the UI must drop the literal "GCC Component" suffix (e.g., display "Button" not "Button GCC Component").
- The association with GCC should be kept in metadata, descriptions, or breadcrumbs.
- URL slugs should be lowercase, hyphenated, and semantic (e.g., `/components/date-picker`, not `/components/DatePicker` or `/components/date_picker`).

# Alignment with Figma / Storybook

- For each component/pattern page, include links or references to:
  - The relevant Figma page (e.g., "Button GCC Component" in Figma).
  - The corresponding Storybook story (when available).
- If Figma and implementation disagree, the docs must call out the discrepancy and prefer the implemented code behavior until the system is reconciled.