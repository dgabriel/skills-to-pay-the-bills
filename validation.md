# Validation

## Scope

The initial three skills have frontmatter/name/scaffold validation and local Markdown link/metadata checks. They have also received a static scenario review against the cases below. These are authored acceptance scenarios, not independent agent executions or proof of output quality across hosts.

| Skill | Representative request | Expected behavior reviewed |
| --- | --- | --- |
| Requirements | “Help define a tool-sharing MVP.” | Ask about audience/problem first; produce a scoped PRD after short rounds. |
| Requirements | “Here is a detailed brief; draft without interviewing.” | Use supplied evidence, label unknowns, avoid asking answered questions. |
| Requirements | “Implement the specified password-reset endpoint.” | Do not launch a product interview. |
| Technical | “Design a 20-user service using our existing Django app.” | Preserve the stack; map components to requirements rather than introduce FastAPI or a queue. |
| Technical | “Design my app” with no product context | Clarify core journey/constraints; do not invent requirements or require another installed skill. |
| Technical | “Fix a typo in this API handler.” | Do not initiate architecture planning. |
| Design | “Create a warm, compact guide only.” | Propose tokens and rules; leave UI code unchanged; distinguish proposed from accepted choices. |
| Design | “Wire our agreed tokens into existing CSS variables.” | Use actual token source and relevant checks; do not assume Tailwind. |
| Design | “Make a new screen using our approved system.” | Apply existing guide; do not start a rebrand workshop. |
| All | “Pause here,” chat-only host, or unattended draft request | Preserve partial progress or inline output; do not fabricate approval or answers. |
| Combined | Existing PRD, no technical design, established visual system | Reuse PRD and visual system; run only architecture planning. |

## Limits and next checks

No live product interview, generated-app build, host installation, UI integration, or independent behavioral evaluation was run for this library change. Contrast rules are instructions for future outputs; no palette is shipped to certify here. Verify effectiveness through real use and add observed failures as focused scenarios. Repeat structural and link checks after subsequent edits.
