---
name: agent-handoff-prompt
description: Write a self-contained copy-pastable brief or work order for another agent/developer, or assess another agent’s output or critique against the request and repository with a verdict and required fixes. Not session close/orientation or direct patch review against a spec.
---

# Agent Handoff Prompt

**Inputs:** Original request, relevant repository evidence, intended recipient, constraints, and existing agent output when assessment is requested.
**Output:** A self-contained copy-pastable brief, or an evidence-backed verdict with required fixes and verification limits.
**Try:** “Assess this model’s review, then write a work order for the next agent.” (use the skill name in your host's invocation syntax).

Honor task scope and project policy; preserve unrelated work. Read the [procedure](references/procedure.md) for details and the [shared contract](references/execution-contract.md) for authority boundaries.

1. Identify the mode: write a brief, assess supplied agent output, or do both. Read the original request, constraints, and relevant repository evidence.
2. For a brief, include goal, context, source/artifact references, permitted scope, constraints, acceptance criteria, and exactly what to hand back.
3. For assessment, verify claims against the request and repository. Give a verdict, supported agreements/disagreements, required fixes, and unverified checks; do not silently implement.
4. When requested, use an owner-directed build/review/fix/approve loop. Drafting a prompt does not authorize sending it, spawning agents, or publishing changes.

Report actual checks, unresolved decisions, and the next handoff. See [provenance and pattern evidence](PROVENANCE.md).
