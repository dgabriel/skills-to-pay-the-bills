---
name: diagnose-first
description: Investigate a reported bug or repeated failed fix before changing code; reproduce it, compare the last working state, and explain evidence and uncertainty. Not patch review against a spec, session orientation, or implementing an already agreed fix.
---

# Diagnose First

**Inputs:** Reported symptom, expected behavior, relevant code/logs, environment, recent changes, and last known working revision when available.
**Output:** Evidence-backed diagnosis or explicit uncertainty, a safe comparison plan, and the next scoped action.
**Try:** “Explain why this started failing before attempting another fix.” (use the skill name in your host's invocation syntax).

Honor task scope and project policy; preserve unrelated work. Read the [procedure](references/procedure.md) for details and the [shared contract](references/execution-contract.md) for authority boundaries.

1. Establish the symptom, expected behavior, reproduction, and impact. Inspect relevant evidence; separate a confirmed problem from a hypothesis before proposing repair.
2. Ask what changed since the last working version, reusing repository history and supplied answers. Verify version-sensitive assumptions against current primary documentation when needed.
3. Offer a previous-version comparison when useful. Any rollback test requires explicit owner approval and a separate worktree or branch; never discard or reset current work.
4. Explain the issue and evidence before fixing. If attempts repeat without new evidence, stop with short bullets: confirmed facts, failed attempts, uncertainties, and next decision.

Report actual checks, unresolved decisions, and the next handoff. See [provenance and pattern evidence](PROVENANCE.md).
