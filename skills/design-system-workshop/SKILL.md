---
name: design-system-workshop
description: Turn visual direction into reusable design tokens and component rules, optionally integrating them into an existing UI. Use to create or deliberately revise a design system; not for routine screens that should follow an established system.
---

# Design System Workshop

## Use this skill

Human prompt: “Use $design-system-workshop to define a warm, compact visual system for my tool-sharing app. Create a guide first; do not change the UI yet.”

Inputs: product/audience context, visual preferences or references, and any existing brand, style guide, token files, and UI framework. A PRD or technical design helps but is optional; this skill stands alone.

Output: a style guide, normally `docs/design/style-guide.md` in the target project, with semantic tokens and component rules. When implementation is requested, also integrate agreed tokens and provide a representative style tile or equivalent existing preview. Follow user paths and project structure; use an inline guide if file tools are unavailable.

## Establish direction

Read the existing system and code before proposing changes. For an established brand, preserve its rules unless revision is requested. If the request is merely to build or fix a screen within that system, apply the existing guide instead of running a rebranding interview.

Ask one short round about mood, audience, references, light/dark preference, and density. Use supplied answers rather than repeating questions. Propose two or three concrete directions when the user needs options; narrow or skip options when they already chose a direction.

## Make the system concrete

- **Color:** define semantic background, surface, foreground, muted text, action, border, and status roles as needed. Show values, intended pairings, and usage. Compute contrast for actual text/background combinations before calling them verified. Target at least 4.5:1 for normal text, including muted labels; 3:1 applies to qualifying large text and relevant non-text UI elements. Do not use color alone to convey status. If tools are unavailable, label contrast unverified and provide the required check rather than fabricate ratios.
- **Typography and layout:** choose a restrained type hierarchy, spacing scale, radii, and density. Respect existing fonts; system fonts are a valid choice. Consider font availability and loading before adding external resources.
- **Components:** describe buttons, links, inputs, cards or surfaces, and error/status treatment, including focus, hover, disabled, and validation states. Include keyboard usability, motion/reduced-motion behavior, and responsive expectations.
- **Emphasis and voice:** define what draws attention and how UI text sounds. A capped signal color is an optional aesthetic decision, not a universal rule; preserve required error/status communication and existing brand rules.

Present proposals for feedback. Do not interpret elapsed time as acceptance. If asked for a draft without discussion, label proposed choices and unresolved decisions. On pause, preserve partial choices and the next question.

## Deliver and verify

Write principles, semantic token values and usage, typography, spacing, components/states, accessibility checks, motion, and voice in the guide. Keep approved decisions distinct from proposals.

For a guide-only task, finish with the guide and a specific integration checklist. When the user requests implementation, wire the agreed tokens into the actual framework or CSS token source, adapt components within scope, and link existing project instructions to the guide rather than duplicating token tables. Do not assume Tailwind or create a new agent configuration as a prerequisite.

Use a style tile or representative screen to review color, type, components, and states when preview tools are available. Run appropriate existing checks after code changes, inspect keyboard/focus and relevant contrast pairings, and report verification gaps. A guide-only draft is not an implemented or accessibility-certified UI. Hand off the guide path, token source if changed, preview location, and unresolved decisions. Do not commit, push, publish, or deploy automatically. Work in the target project, not the installed skill folder.

## Source

Adapted from [docs/design/style-guide-interview.md](https://github.com/dgabriel/claude-code-project-template/blob/59616904f514d6351b8d8de1d6e16ae708057dc3/docs/design/style-guide-interview.md). See [PROVENANCE.md](PROVENANCE.md) for revision and adaptation details.
