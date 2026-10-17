---
name: session-start-and-close
description: Orient or resume repository work after an interruption, give a concise where-we-are status, or close a session with durable task and Git handoff. Use Beads when present; not feature implementation, generic planning, or adopting a tracker.
---

# Session Start and Close

**Inputs:** Target checkout, current request, project instructions, Git/PR state, and existing tracker when available.
**Output:** Brief start/resume status or a durable close handoff with verified checks, task state, and remaining actions.
**Try:** “Use session-start-and-close to get your bearings and show ready work before continuing.” (use the skill name in your host's invocation syntax).

Honor the task scope and target-project policy; preserve unrelated work. Consult the [procedure](references/procedure.md) for operation details and the [shared contract](references/execution-contract.md) for authorization boundaries.

1. Read current project instructions and linked Git/task policy. Inspect checkout, branch, dirty paths, in-progress operations, and PR state before proposing work; label unavailable/stale observations.
2. Inspect ready/open/in-progress tasks and blockers using the existing tracker; with Beads, load `bd prime` and read state without claiming tasks or syncing remotely as a side effect of orientation.
3. On resume, reconcile the last durable handoff with actual diffs, task state, and checks. Return short bullets: where we are, next scoped task, blockers, and what needs a decision.
4. On close, record follow-ups in the tracker, preserve a next-developer handoff, and ensure scoped work is committed when authorized. Push/sync only within current authority; otherwise report those actions as pending rather than claiming a clean shared handoff.

Report what actually happened, pending decisions, and the next action. Use target-project paths. [Provenance and pattern evidence](PROVENANCE.md).
