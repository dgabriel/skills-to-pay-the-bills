# Skill catalog

Use this catalog to select a workflow; read the selected skill's `SKILL.md` before execution. Paths below are relative to this library, while output paths are relative to the user's target project. No skill depends on another being installed.

| Skill / entry point | Select when | Inputs | Outputs and handoff | Skip when |
| --- | --- | --- | --- | --- |
| [product-requirements-interview](skills/product-requirements-interview/SKILL.md) | Defining or revising a product's users, value, or MVP scope | Idea, brief, existing discovery, constraints | PRD; hand off its location, status, and open constraints to technical or visual design | Implementing a feature whose requirements are already clear |
| [technical-design-interview](skills/technical-design-interview/SKILL.md) | Planning or revising system architecture | PRD or equivalent concrete requirements; existing code/stack | Technical design; hand off requirements reference, decisions, unresolved issues, and implementation prerequisites | Routine debugging or implementation within established architecture |
| [design-system-workshop](skills/design-system-workshop/SKILL.md) | Creating or deliberately revising a visual system | Product/audience context, preferences, existing brand/tokens | Style guide; when requested, integrated tokens and preview, plus verification status | Creating a screen that should simply use an existing system |

## Compose only when useful

For a new product, begin with requirements. Technical design and visual design consume that context and can follow in either order. Skip completed stages, read their existing outputs, and ask only about consequential gaps. A complete PRD is useful but not mandatory if equivalent requirements are supplied. The design workshop can run directly from a visual brief.

Carry forward artifact paths, draft/accepted status, user constraints, decisions, and open questions. Do not silently restart interviews or treat a proposal as approved. Resolve contradictions with the user rather than overwriting an earlier decision.

## Execution contract

Use the target project's existing document structure and the user's requested delivery format. Default paths are suggestions, not mandatory scaffolding. Write drafts when authorized, ask focused questions where answers matter, and preserve partial progress when paused. In a headless run, produce a clearly marked draft with assumptions and unresolved questions instead of simulating user answers.

A planning request ends with reviewable planning artifacts. UI integration happens only when requested; deployment, publication, and Git mutations require authorization in the task context. Existing host and target-project instructions still apply. These skills do not require delegation, a particular model, or an external connector.

For human setup and explicit invocation examples, see [README.md](README.md).
