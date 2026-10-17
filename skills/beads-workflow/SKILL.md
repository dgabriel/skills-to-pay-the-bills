---
name: beads-workflow
description: Use Beads (bd) for durable tasks, blockers, legacy issue lookup, claiming, completion, and session handoff in a repository that already uses Beads. Not for ephemeral checklists or adopting a new tracker.
---

# Beads Workflow

**Inputs:** Existing Beads project, task or legacy identifier, repo workflow, and current task state.
**Output:** Resolved native IDs, accurate task state or a command plan, and durable handoff notes.
**Try:** “Use beads-workflow to find ready work and prepare a handoff for this Beads project.” (use the skill name in your host's invocation syntax).

Honor the user’s task scope and target-project policy; preserve unrelated work. Use the [procedure](references/procedure.md) for detailed commands/examples and the [shared contract](references/execution-contract.md) when authorization or handoff scope needs clarification.

1. Read project issue/Git policy and run `bd prime`; if it produces no context, check `bd where`. Do not initialize or migrate a tracker implicitly.
2. Inspect the issue before action; resolve legacy references to real native IDs rather than constructing an ID.
3. Use the project start wrapper when required; otherwise claim atomically. Keep turn-local planning separate from durable tracker state.
4. Close only at the target project's completion gate. Record blockers and next steps; keep code Git state separate from issue database synchronization.

Finish with the artifact or report, checks actually run, open decisions, and the next handoff. Resolve output paths in the target project. See [provenance](PROVENANCE.md) for source revisions and adaptations.
