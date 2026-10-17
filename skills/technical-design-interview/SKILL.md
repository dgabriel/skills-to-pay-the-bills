---
name: technical-design-interview
description: Derive a practical technical design from product requirements and resolve architecture decisions through focused questions. Use for planning or revising system architecture, not routine implementation or debugging.
---

# Technical Design Interview

## Use this skill

Human prompt: “Use $technical-design-interview with docs/prd/prd.md to propose the smallest architecture that supports the MVP.”

Inputs: a PRD, feature brief, or sufficiently concrete requirements; existing code and architecture when available. An installed requirements skill is not required. If requirements are missing, clarify the core journey and constraints before choosing architecture. Do not force a separate interview or invent product scope.

Output: a reviewable technical design, normally `docs/technical/technical-design.md` in the target project. Follow existing structure and the user's requested destination; use an inline draft in chat-only environments.

## Derive, then ask

Read the supplied requirements and relevant project conventions first. Preserve existing stack choices unless the task calls for changing them. Propose the simplest design that meets actual requirements and explain meaningful tradeoffs. Do not ask the user to design the database for you.

Discuss only unresolved decisions in short rounds:

1. **Data and invariants:** propose entities, relationships, ownership, uniqueness, state transitions, and the boundary between user-created and derived data. Clarify retention, deletion, and audit needs where relevant.
2. **Access:** propose sign-in and role boundaries, distinguish public/private operations, and identify enforcement points. Do not add authentication where the product does not need it.
3. **Interfaces and integrations:** map required features to API or local interfaces. Identify required versus optional dependencies, failure behavior, and work that genuinely requires background processing or real-time updates.
4. **Operations:** establish deployment constraints, realistic scale, data-loss tolerance, recovery expectations, and the first likely scaling limit. Leave undecided infrastructure explicit.

Use the project's actual frameworks and conventions. Queues, caches, external services, and additional layers need a requirement or observed constraint that justifies them. If asked to draft immediately, label assumptions rather than waiting for every answer. If paused, save decisions and remaining questions without claiming approval.

## Produce and check the design

Cover overview, architecture, data/invariants, interfaces, access, configuration, operations, and testing strategy. Record consequential decisions with rationale and rejected alternatives, deliberate simplifications, limits, and open questions. Relate major components to requirements; flag requirements that the design does not yet satisfy.

Describe schema migration and rollback verification where persistent data changes are proposed, using the target project's tooling. List proposed configuration keys without secret values and identify example-config updates needed during implementation. Designing alone does not authorize migrations, infrastructure changes, or edits to runtime configuration.

Check consistency between ownership rules, interfaces, data model, failure handling, and tests. Name observable acceptance checks for the critical journey and invariants. Present the draft, revise on feedback, and distinguish recommendations from accepted decisions. Hand off the design path, PRD reference, open questions, and implementation prerequisites. Do not implement, commit, push, or deploy as an automatic follow-up. Work in the target project, not the installed skill folder.

## Source

Adapted from [docs/technical/technical-design-interview.md](https://github.com/dgabriel/claude-code-project-template/blob/59616904f514d6351b8d8de1d6e16ae708057dc3/docs/technical/technical-design-interview.md). See [PROVENANCE.md](PROVENANCE.md) for revision and adaptation details.
