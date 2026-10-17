# BorrowBox visual system — proposed guide

Mood: warm, analog, compact. Utility for 30 neighbors; light surfaces, no existing brand, no external font dependency. References are conceptual: a paper tool inventory and handwritten workshop labels; avoid social-feed decoration. These directions are proposals, not accepted brand decisions.

## Directions
1. Recommended: Paper workshop — cream #FAF7F0, white surfaces, ink #29261F, burnt wood action #805331. Familiar and readable for a practical tool library.
2. Garden ledger — cream #F7F8F0, white surfaces, ink #263328, green action #315B3F, muted #5C6658, border #7A8576. Calmer outdoor association.
3. Clay catalog — cream #FCF5EF, white surfaces, ink #382A27, clay action #8C4433, muted #6B5953, border #927A70. Warmer and more expressive.

All directions retain text/icon status roles. Only recommended direction pairings below were calculated; alternative palette contrast is unverified. Recommend one accent-filled primary action per screen; this is an aesthetic proposal awaiting user review. It does not suppress errors or multiple necessary statuses. Secondary actions use outlined or text treatments.

## Semantic tokens
| Token | Value | Use |
|---|---|---|
| background | #FAF7F0 | Page canvas |
| surface | #FFFFFF | Cards, inputs, primary action text |
| foreground | #29261F | Main text |
| muted | #625E54 | Supporting text on canvas or surface |
| accent | #805331 | Primary action, links, focus |
| accent-hover | #674025 | Hover/pressed primary fill |
| success / success-soft | #285B3B / #E8F0E8 | Returned/accepted label with icon |
| error / error-soft | #9B302B / #FBECE8 | Actionable inline errors with icon |
| warning / warning-soft | #674B13 / #FFF2CE | Pending/overdue status with explicit label |
| border | #857C6C | Required control boundaries |
| focus | #805331 | Visible focus ring on light surface |

Avoid applying opacity to muted labels or status text; that changes computed contrast. Keep status foregrounds on their specified soft backgrounds. Never rely on hue alone: use “Accepted”, “Returned”, “Pending”, or concrete error copy with icons.

## Computed contrast
Executed `python3 calculate_contrast.py`, exit 0. The retained standard-library calculator linearizes sRGB using the WCAG threshold .04045 and weights .2126/.7152/.0722. Ratios rounded to two decimals after calculation:

| Foreground / background | Calculated ratio | Requirement |
|---|---:|---|
| foreground / background | 14.11:1 | ≥4.5:1 normal text |
| foreground / surface | 15.09:1 | ≥4.5:1 normal text |
| muted / background | 6.04:1 | ≥4.5:1 normal text |
| muted / surface | 6.46:1 | ≥4.5:1 normal text |
| surface / accent | 6.56:1 | ≥4.5:1 normal text |
| surface / accent-hover | 8.99:1 | ≥4.5:1 normal text |
| success / success-soft | 6.82:1 | ≥4.5:1 normal text |
| error / error-soft | 6.41:1 | ≥4.5:1 normal text |
| warning / warning-soft | 7.27:1 | ≥4.5:1 normal text |
| border / surface | 4.12:1 | ≥3:1 non-text |
| border / background | 3.85:1 | ≥3:1 non-text |
| focus / surface | 6.56:1 | ≥3:1 non-text |
| focus / background | 6.13:1 | ≥3:1 non-text |


Normal text targets ≥4.5:1, including muted labels and button/status text. 3:1 applies to relevant non-text boundaries/focus and qualifying large text, not small labels. Focus ring must sit outside the filled button with a 2px light offset so it is assessed against the page/surface; do not place the same accent directly against itself. Soft status backgrounds need no independent boundary when text/icons supply all meaning. Contrast is verified for these token pairings only, not a claim of full accessibility conformance.

## Type, spacing and layout
Headings use Georgia, serif; body and controls use system-ui, sans-serif. No remote font request. Body 16px/1.45; supporting labels 14px/1.4; headings 24px/1.2 and 32px/1.15. Weight 600 for controls/headings where available. Avoid all-caps paragraphs. Use a 4px spacing unit with 4/8/12/16/24/32px steps, one 6px radius, 16px card padding, and modest 12px row gaps. Compact density comes from grouping, not tiny type or targets. Interactive targets at least 44px high. At narrow widths, stack tool cards and booking details; do not hide status or date labels. Support 200% zoom and wrapping without horizontal reading scroll.

## Components and states
Buttons: one filled accent primary, white text; hover/pressed uses accent-hover, disabled retains readable muted text on canvas with border and explicit disabled semantics (no opacity-only treatment). Secondary buttons use foreground on surface with border. Loading button keeps its label plus “Working…” and prevents duplicate submission.

Inputs: surface fill, foreground text, persistent visible label, muted helper text, border token, minimum 44px height. Focus uses 2px focus ring plus 2px surface offset. Error uses error text on error-soft with explicit message and aria-describedby; do not use a red border as the sole signal. Checkbox/radio states pair selected indicators and text; check their final rendered boundaries before release.

Tool cards: title, description, availability, and labeled request action in that order. Booking row: tool, date range, written status, and role-appropriate next action. Links use underlines; hover adds no essential information. Provide empty states with a useful next action, e.g. “No tools listed yet. Add the first tool.”

Keyboard: logical DOM tab order, native controls, Enter/Space activation, visible focus, escape/return-focus behavior for dialogs if introduced. Responsive layouts preserve this order. Status changes use a polite live region; errors focus a summary or the invalid field where useful.

## Motion and voice
Use 120–160ms color transitions, no decorative bouncing or parallax. Respect prefers-reduced-motion with instant state changes and a static loading label. Sentence case, direct neighborly language: “Request these dates”, “Mark returned”, “Those dates overlap an accepted booking. Choose another range.” Do not imply a request is accepted before the owner decides.

## Integration checklist and verification
Map these semantic values into the eventual project's existing token mechanism; keep one canonical guide. Build a style tile showing all button, input, error, status and focus states. Verify computed pairings against rendered CSS, keyboard flow, zoom, screen-reader labels, disabled behavior, reduced motion and narrow layouts; assess any new colors before adoption. Review final primary-action emphasis with the owner. Those UI checks were not executed because this task is guide-only and no application exists. No app code was written. Handoff: this proposed guide, contrast-results.md and calculate_contrast.py; acceptance of direction/signal cap and later implementation remain open.
