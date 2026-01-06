---
name: "gcc-component-docs-rules"
description: "Authoring guide for GCC component and pattern documentation pages"
alwaysApply: false
---

# Context

This file defines the **content structure and authoring rules** for individual component and pattern pages in the GCC design system documentation site.

It applies to pages under:
- **Components** (section 2)
- **Patterns** (section 3)
- **Product / Market** (section 4)

All pages must follow a consistent, Material/Primer-style structure to ensure clarity, discoverability, and maintainability.

# Required Page Structure

Every component, pattern, and product-specific page must include the following 9 sections, in this exact order.

## 1. Overview

**Purpose:** Introduce the component/pattern and explain what problem it solves.

**Content requirements:**
- 2–4 sentences describing what it is.
- Primary use cases and contexts where it appears (e.g., checkout, PDP, navigation, account profile, Wellbeing+ flows).
- For **Product / Market** pages, add a short **Product Context** subsection explaining:
  - Which product or market uses this.
  - Which core GCC components it is built from.

**Example:**
> The Button component is the primary interactive element for triggering actions in GCC products. Use it for form submissions, navigation, and calls-to-action across checkout, account management, and product detail pages.

---

## 2. Usage

**Purpose:** Provide clear guidance on when to use (and when not to use) this component/pattern.

**Content requirements:**
- **"When to use"** – bullet list of appropriate scenarios.
- **"When not to use"** – bullet list of inappropriate scenarios or alternatives.
- **Dos & Don'ts** – clear, actionable examples to prevent common mistakes.
- **Content guidance** – rules for labels, helper text, error text, truncation, tone, capitalization, etc. (where relevant).

**Example:**
> **When to use:**
> - For primary actions on a page (e.g., "Add to Cart", "Submit Order").
> - When the action requires user confirmation or triggers a state change.
>
> **When not to use:**
> - For navigation between pages (use a link instead).
> - For tertiary or low-priority actions (use a text link or ghost button).
>
> **Dos:**
> - Use clear, action-oriented labels ("Save Changes", not "OK").
> - Limit to one primary button per screen section.
>
> **Don'ts:**
> - Don't use vague labels like "Click Here" or "Submit".
> - Don't stack multiple primary buttons vertically without clear hierarchy.

---

## 3. Anatomy

**Purpose:** Break down the component/pattern into its key parts and establish shared terminology.

**Content requirements:**
- Labeled diagram or description of key parts.
- Names must map cleanly to the code API / props / slots (e.g., `leadingIcon`, `trailingIcon`, `label`, `supportingText`, `helperText`).
- Indicate which parts are **required** vs **optional**.

**Example:**
> **Button anatomy:**
> - `leadingIcon` (optional) – Icon displayed before the label.
> - `label` (required) – Text describing the action.
> - `trailingIcon` (optional) – Icon displayed after the label.
> - `container` – The clickable surface with padding, background, and border.

---

## 4. Behavior & States

**Purpose:** Document how the component/pattern behaves across interaction states and contexts.

**Content requirements:**
- **Required states:** default, hover, focus, pressed/active, disabled, loading, error (and success where relevant).
- **Interaction behavior:** click/tap, keyboard activation, focus order.
- **Keyboard behavior:** especially for modals, drawers, menus, form controls (e.g., tab order, activation keys like Enter/Space, focus traps, ESC to close).
- **Responsive notes:** if layout or density changes on mobile vs desktop.

**Example:**
> **States:**
> - **Default:** Neutral background, visible label.
> - **Hover:** Background darkens slightly, cursor changes to pointer.
> - **Focus:** Visible focus ring (3px outline, color token `focus-ring`).
> - **Pressed/Active:** Background darkens further, slight scale transform.
> - **Disabled:** Reduced opacity, no pointer events, grayed-out appearance.
> - **Loading:** Spinner replaces label, button remains disabled.
>
> **Keyboard:**
> - Focusable via Tab.
> - Activates on Enter or Space.
>
> **Responsive:**
> - On mobile, buttons may expand to full width in forms.

---

## 5. Variants

**Purpose:** List all supported visual and behavioral variations and explain when to use each.

**Content requirements:**
- List of supported variants (e.g., Primary / Secondary / Tertiary, Destructive, Ghost, size variants like Small / Medium / Large).
- For patterns, list common configuration options (e.g., forms with/without optional fields, compact vs full cards).
- Provide guidance on when to use each variant, with 1–2 concise, concrete examples.

**Example:**
> **Visual variants:**
> - **Primary:** High-emphasis actions (e.g., "Add to Cart", "Submit Order").
> - **Secondary:** Medium-emphasis actions (e.g., "Save for Later", "View Details").
> - **Tertiary / Ghost:** Low-emphasis actions (e.g., "Cancel", "Learn More").
> - **Destructive:** Dangerous actions (e.g., "Delete Account", "Remove Item").
>
> **Size variants:**
> - **Small:** Compact UIs, mobile toolbars.
> - **Medium (default):** Most use cases.
> - **Large:** Hero CTAs, landing pages.

---

## 6. Accessibility

**Purpose:** Ensure the component/pattern is usable by everyone, including keyboard and screen reader users.

**Content requirements:**
- Expected **semantic elements** and **ARIA roles** (e.g., `<button>`, `<a>`, `role="dialog"`, `role="alert"`, `aria-expanded`, `aria-describedby`).
- **Keyboard requirements:** focus order, activation keys, focus trapping (for dialogs/drawers), ESC to close.
- **Contrast requirements:** minimum contrast ratios for text and interactive elements.
- **Component-specific a11y rules** (e.g., modals must trap focus, form inputs must have visible labels or `aria-label`).

**Example:**
> **Semantic element:** Use `<button>` for buttons, not `<div>` or `<span>`.
>
> **ARIA:**
> - If the button triggers a disclosure (e.g., dropdown), use `aria-expanded="true/false"`.
> - If the button has no visible label (icon-only), provide `aria-label`.
>
> **Keyboard:**
> - Must be focusable via Tab.
> - Must activate on Enter or Space.
>
> **Contrast:**
> - Text and background must meet WCAG AA contrast ratio (4.5:1 for normal text, 3:1 for large text).
> - Focus ring must be clearly visible against all backgrounds.

---

## 7. Tokens & Theming

**Purpose:** Document which design tokens control the component/pattern and how to customize it.

**Content requirements:**
- List the key design tokens that control the element:
  - **Colors** (background, text, border, focus ring, etc.)
  - **Typography** (font family, size, weight, line height)
  - **Spacing** (padding, margin, gap)
  - **Radius** (border-radius)
  - **Elevation** (box-shadow, z-index)
  - **Motion** (transition duration, easing)
- Show how to customize appearance via tokens or theme APIs.
- **Explicit rule:** No hard-coded hex values or arbitrary spacing values. Always use design tokens.
- Link to the relevant **Foundations** pages (Color, Typography, Spacing, etc.) instead of duplicating full explanations.

**Example:**
> **Tokens:**
> - `color.action.primary` – Background color for primary buttons.
> - `color.text.on-primary` – Text color on primary buttons.
> - `spacing.md` – Horizontal padding inside buttons.
> - `radius.sm` – Border radius for buttons.
> - `motion.duration.fast` – Transition duration for hover/focus states.
>
> **Theming:**
> - Customize button colors by overriding `color.action.primary` in your theme.
> - Do not hard-code hex values like `#0066CC` directly in component styles.
>
> See [Color](/foundations/color) and [Spacing](/foundations/spacing) for full token reference.

---

## 8. Code & API

**Purpose:** Provide canonical code examples and a clear API reference for developers.

**Content requirements:**
- **Canonical code examples** using the real GCC component library imports (e.g., `import { Button } from "@gcc/components";`).
- **API / props table** that matches the implementation:
  - Prop name
  - Type
  - Required vs optional
  - Default value
  - Description
- Show at least:
  - One **"happy path"** example (simplest, most common usage).
  - One **advanced configuration** example (e.g., with icons, error state, async loading, additional slots).

**Example:**

```jsx
import { Button } from "@gcc/components";

// Basic usage
<Button variant="primary" onClick={handleSubmit}>
  Add to Cart
</Button>

// Advanced usage with icon and loading state
<Button 
  variant="primary" 
  leadingIcon={<CartIcon />}
  loading={isLoading}
  onClick={handleSubmit}
>
  Add to Cart
</Button>