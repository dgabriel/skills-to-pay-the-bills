# BorrowBox visual system

A warm, compact utility inspired by paper labels and a neighborhood tool shelf. Use light surfaces, quiet borders, short labels, and clear actions. No social feed or app implementation.

## Tokens
| Token | Value | Use |
|---|---|---|
| paper | #FAF6ED | Main surface |
| ink | #302C26 | Primary text |
| muted | #6E665B | Secondary text, dates, metadata |
| accent | #805336 | Primary buttons and links |
| success / background | #365C40 / #E7EFE2 | Accepted, returned |
| warning / background | #76521C / #F7EBCB | Pending, due soon |
| danger / background | #943E32 / #F8E7DF | Error, overdue |

Use system sans-serif for controls and body (`system-ui, sans-serif`); system serif for occasional section titles (`Georgia, serif`). No font service. Body 16px/1.5, metadata 14px/1.4, labels 14px/1.4 at weight 600, section titles 22px/1.25, page title 28px/1.2. Use tabular numerals for dates and counts.

Spacing scale: 4, 8, 12, 16, 24, 32px. Control height 44px; compact rows use 12px vertical padding and retain generous action targets. Content width 960px, reading width 640px, mobile page padding 16px. Corners: 4px controls, 8px cards. Borders: 1px muted for interactive boundaries; quiet decorative dividers may be lighter. Avoid texture behind text and heavy shadows.

## Calculated contrast
Calculated with standard sRGB linearization, relative luminance `0.2126R + 0.7152G + 0.0722B`, and `(Llighter + .05)/(Ldarker + .05)`:

| Foreground / background | Ratio |
|---|---:|
| ink / paper | 12.86:1 |
| muted / paper | 5.24:1 |
| accent / paper | 6.07:1 |
| paper / accent | 6.07:1 |
| success / success background | 6.46:1 |
| warning / warning background | 5.91:1 |
| danger / danger background | 5.84:1 |

All specified text pairs exceed 4.5:1 for normal text. These calculations were executed locally; no rendered UI or assistive-technology test was run. Keep text fully opaque; opacity changes require recalculation. Muted text remains readable and is never used to hide required information.

## Components and states
Use paper text on accent buttons; secondary buttons use accent text and border on paper. Underline text links. Focus uses a 2px ink outline with a 2px paper offset, independent of color-only state. Provide keyboard-visible focus, logical tab order, persistent labels, and error text linked to inputs. Disabled controls include a reason where relevant and do not remove required instructions.

Tool cards show title, condition, owner, and one request action. Date inputs have explicit start/end labels and inline validation. Booking rows show dates and a text status badge. Accepted and returned use success colors with distinct text; pending uses warning; rejected uses muted text on paper; overdue/errors use danger. Add a symbol where useful, but never rely on hue or a symbol alone. Success tint against paper is decorative, not an interactive boundary. Keep return actions and owner decisions visually distinct, and confirm the resulting state in text.

Completion checks for a future UI: verify all text/state pairs, zoom to 200%, keyboard the entire request-and-return flow, inspect narrow-screen wrapping, and test error announcements. These are proposed checks, not completed behavioral validation.
