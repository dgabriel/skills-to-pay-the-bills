# Design workshop procedure

## Direction and defaults

Start with three mood adjectives, references or counterexamples, background preference, and density. Read existing tokens and guide before suggesting changes. For an existing screen request within an established system, apply that system rather than run a workshop.

Default to two or three candidate palettes covering background/surface, foreground, accent/action, muted text, borders, and status. An accent-soft role can be derived. Recommend a signal color capped at one meaningful emphasis per screen; record whether the user accepts or overrides this aesthetic rule. Status/error communication must remain intelligible through text/icons and must not disappear to satisfy a decorative cap. Do not import any source project's exact palette or motifs.

Propose a heading/body type pairing matched to mood, with system fonts a valid default when loading and budget favor them. Keep typography restrained, pick a base spacing unit and radius, and define a consistent input/button treatment. Explicit user/brand choices override workshop defaults.

## Contrast and states

Compute contrast using WCAG relative luminance: linearize each sRGB channel (c/12.92 for c ≤ 0.04045, otherwise ((c+0.055)/1.055)^2.4), luminance = .2126R + .7152G + .0722B, ratio = (lighter+.05)/(darker+.05). Use computed values, not rounded hex intuition. Normal text including muted labels targets ≥4.5:1; qualifying large text and relevant non-text UI targets ≥3:1. Check text on accent/status surfaces, focus treatment, and adjacent surfaces as relevant. Label unavailable checks rather than fabricating them. Contrast alone is not full accessibility conformance.

Define focus, hover, disabled, error, keyboard navigation, responsive layout, and reduced-motion behavior. UI copy needs consistent casing, tone, and actionable error wording. Avoid color-only status.

## Guide and integration

Write principles, semantic values with usage rules and intended pairings, typography, spacing, components/states, motion, voice, and verification status. Default path `docs/design/style-guide.md`; use the requested format/path otherwise, or inline in chat-only use. Distinguish proposed versus accepted choices.

For a guide-only task, include a concrete integration checklist and stop there. For an implementation request, update the actual token source and in-scope components; use Tailwind tokens in a Tailwind project, CSS variables in a plain CSS project, or the established equivalent. Link project instructions to the canonical guide instead of maintaining repeated token tables. Provide a representative style tile/preview when tools permit. Run existing code checks after token changes and inspect relevant component states; report missing UI/keyboard checks honestly.

Primary references: [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). Evaluate unrounded ratios against the threshold; rounded display values must not turn a failing pairing into a pass.
