---
name: design-system-workshop
description: Create or deliberately revise a visual system from mood and product context, with semantic tokens and component rules; integrate agreed tokens when requested. Not routine screen work within an established system.
---

# Design System Workshop

**Inputs:** Audience/product context, mood/references, existing brand/tokens, and framework when present.
**Output:** Style guide, default `docs/design/style-guide.md`; integrated tokens/style tile when requested.
**Try:** “Use design-system-workshop to define a warm visual system; produce a guide before changing UI code.” (use the skill name in your host's invocation syntax).

Honor the user’s task scope and target-project policy; preserve unrelated work. Use the [procedure](references/procedure.md) for detailed commands/examples and the [shared contract](references/execution-contract.md) when authorization or handoff scope needs clarification.

1. Read the current system. Collect mood, references, density, and light/dark preference; preserve the brand unless revision is requested.
2. Propose two or three concrete directions. Default to a restrained semantic palette, one heading/body type pair, a spacing scale, one radius token, and a capped signal color for the most important action. Make that cap an explicit design choice, preserving error/status semantics.
3. Calculate contrast for actual pairings, including muted labels. Normal text needs 4.5:1; 3:1 is reserved for qualifying large text/relevant non-text controls. Never label an uncomputed ratio verified.
4. Define components/states, motion and voice. For implementation requests, wire agreed tokens into actual project code and verify a style tile; for guide-only requests, deliver the guide and integration checklist.

Finish with the artifact or report, checks actually run, open decisions, and the next handoff. Resolve output paths in the target project. See [provenance](PROVENANCE.md) for source revisions and adaptations.
