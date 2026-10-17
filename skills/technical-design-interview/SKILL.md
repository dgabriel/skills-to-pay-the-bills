---
name: technical-design-interview
description: Derive or revise system architecture and a technical design from a PRD or concrete requirements, proposing data, access, API, and operational decisions. Not routine debugging or implementing a settled design.
---

# Technical Design Interview

**Inputs:** PRD or equivalent requirements, existing stack/code, and operating constraints.
**Output:** Reviewable design, default `docs/technical/technical-design.md`, with decisions and acceptance checks.
**Try:** “Use technical-design-interview to propose the smallest architecture that serves this PRD.” (use the skill name in your host's invocation syntax).

Honor the user’s task scope and target-project policy; preserve unrelated work. Use the [procedure](references/procedure.md) for detailed commands/examples and the [shared contract](references/execution-contract.md) when authorization or handoff scope needs clarification.

1. Read requirements and existing architecture first. Propose a design; ask the user about genuinely open decisions rather than making them design the database.
2. For a greenfield web app, default to FastAPI, async SQLAlchemy, Postgres, Alembic, pydantic-settings, React/TypeScript, and environment-driven flags. Existing stack or explicit user choices override these defaults; state departures and why.
3. Work through data/invariants → access → APIs/integrations → operations. Add queues, caches, or realtime only for a named requirement.
4. Record decisions, rejected alternatives, deliberate simplifications, test gates, and open questions. Draft immediately when requested; unknowns remain explicit.

Finish with the artifact or report, checks actually run, open decisions, and the next handoff. Resolve output paths in the target project. See [provenance](PROVENANCE.md) for source revisions and adaptations.
