---
name: "gcc-component-docs-rules"
description: "Authoring standard for GCC component, pattern, and product/market documentation pages"
alwaysApply: false
---

# GCC Component Docs Rules (Material/Primer-inspired)

## Scope

Applies to documentation pages under:
- `components/` (Components)
- `patterns/` (Patterns)
- `product-specific/` (Product / Market)

Goal: Pages must be consistent, scannable, and maintainable at scale (Material/Primer-style).

---

## Required: Page Header Block (before Section 1)

Every page MUST start with a compact "header block" immediately after the page title.

**Required fields:**
- **Status:** `Stable` | `Beta` | `Deprecated` | `Draft`
- **Last reviewed:** `YYYY-MM-DD`
- **Owner:** team or individual (e.g., Design Systems, Web Platform)
- **Source links:** at least one of:
  - Figma link
  - Implementation link (repo / Storybook)
  - Changelog link (or "No changes recorded yet")

**Why this is required:**
- Prevents doc drift (“Is this authoritative?”)
- Clarifies who maintains the component
- Provides a single source of truth for designers + engineers

---

## Required Page Structure (9 sections, exact order)

All pages MUST include the following 9 sections in this exact order.
If a section is not applicable, include the heading and write: "Not applicable for this component/pattern" with a 1-sentence reason.
Do NOT pad with filler content.

### 1. Overview

**Purpose:** Define what it is and why it exists.

**Requirements:**
- 2–4 sentences describing what it is and the problem it solves
- 1 sentence listing real GCC contexts where it appears (checkout, PDP, account, Wellbeing+, etc.)

**Page-type additions:**
- **Patterns:** include a short "Composed of" list (which core components form the pattern)
- **Product / Market:** include "Product context" + note any deviations from core GCC standards

---

### 2. Usage

**Purpose:** Decision guidance ("when to use / not use") and content rules.

**Requirements (all pages):**
- **When to use** (5–8 bullets)
- **When not to use** (3–6 bullets) + recommended alternative component/pattern
- **Dos & Don’ts** (min 3 each; must be actionable)
- **Content guidance**: labels, tone, capitalization, truncation, helper/error text, i18n considerations

**Guardrails:**
- Avoid restating anatomy or props here—this section is about choices and UX outcomes.
- Avoid vague labels like “Click here”; prefer verbs and specificity.

---

### 3. Anatomy

**Purpose:** Shared terminology for designers + engineers.

**Requirements:**
- Parts list with **required vs optional**
- Naming MUST map to implementation API (props/slots), where applicable
- Include one of:
  - labeled diagram/image, OR
  - annotated markup snippet that labels parts

---

### 4. Behavior & States

**Purpose:** Interaction rules, state model, keyboard, responsiveness.

**Required baseline states (interactive components):**
- Default
- Hover (or note “not applicable on touch-only”)
- Focus (must describe focus-visible behavior)
- Pressed/Active
- Disabled (ONLY if supported)

**Conditional states (include ONLY if supported):**
- Loading
- Selected/On (toggles)
- Error/Invalid (form controls)
- Success/Confirmed (rare; only when product behavior requires it)
- Skeleton/Placeholder (data-loading components)

**Also required:**
- Keyboard behavior (Tab order, activation keys)
- Focus management notes (especially for menus/dialogs/drawers)
- Responsive behavior notes (layout/density changes; touch target guidance)

---

### 5. Variants

**Purpose:** Enumerate variants + how to choose them.

**Requirements:**
- List variants grouped by dimension (Type / Size / Emphasis / Semantic)
- For each variant: **Use when** + 1 concrete example

**Guardrail:**
- If you can’t explain when to use a variant, the variant is likely unnecessary or needs consolidation.

---

### 6. Accessibility

**Purpose:** Implementation-ready accessibility requirements.

**Requirements:**
- Correct semantic element(s) + prohibited alternatives
- ARIA usage (ONLY where needed; avoid ARIA-by-default)
- Keyboard interaction requirements (keys + expected outcomes)
- Focus indicator requirements (visibility and contrast)
- Touch target guidance (recommend minimum 44×44 px)
- Screen reader expectations for dynamic states (loading, errors) where relevant

---

### 7. Tokens & Theming

**Purpose:** Define the token contract and customization path.

**Requirements:**
- List the minimal **token contract** that controls the component:
  - Colors (bg/text/border/focus)
  - Typography
  - Spacing (padding/gap/height)
  - Radius
  - Motion (if animated)
  - Elevation/z-index (if layered)
- **Rule:** Do not hard-code hex values or arbitrary px spacing in docs (unless explicitly marked legacy).
- Link to Foundations pages instead of duplicating token catalogs.

**Guardrail:**
- Keep token lists tight and implementable—prefer “these tokens control the component” over enumerating every possible palette option.

---

### 8. Code & API

**Purpose:** Canonical developer usage + API reference.

**Requirements:**
- 1 "happy path" example
- 1 "advanced" example demonstrating meaningful configuration
- API/props table:
  - prop name
  - type
  - required
  - default
  - description
- Include events/handlers and accessibility props where relevant

**Governance rule (required):**
If the GCC component library API is not shipped or not stable, label clearly:
- `Implementation status: Spec-only / Draft / Experimental`
…and provide a fallback snippet using native HTML semantics.

---

### 9. Examples

**Purpose:** Real-world usage patterns and edge cases.

**Requirements:**
- 2–4 real GCC workflow examples
- Include at least one edge case:
  - long labels
  - disabled with reason
  - loading/async
  - localization (long translations)
- Strongly recommended: visual examples (screenshots or Figma embeds)

---

## Cross-cutting Policies (apply to all pages)

### Buttons vs Links (clarity rule)
- **Buttons** trigger actions (submit, open modal, change state).
- **Links (`<a>`)** navigate to URLs/pages.
- “Link styled as button” is allowed only when visual hierarchy demands it; still must behave like navigation.

### Consistency + Single source of truth
- Token names referenced in components MUST match Foundations token naming exactly.
- If a token is renamed, update Foundations first, then update all dependent component docs.

### Avoid duplication
- Don’t duplicate full token catalogs or foundation explanations inside component pages.
- Link to the relevant Foundations page and reference only the token contract.

---