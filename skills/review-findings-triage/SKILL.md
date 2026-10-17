---
name: review-findings-triage
description: Triage existing automated or adversarial PR findings into fix, approved dismissal, or upstream tool bug, then verify the review gate. Use Flaught by default; not raw patch review, disabling a gate, or automatic merging.
---

# Review Findings Triage

**Inputs:** Current review artifact, reviewed revision, project gate/dismissal policy, code/test evidence, and owner decisions.
**Output:** Complete finding table, tracked dispositions, refreshed review/report evidence, and an upstream draft when useful.
**Try:** “Use review-findings-triage to explain every finding and propose actions before changing anything.” (use the skill name in your host's invocation syntax).

Honor the task scope and target-project policy; preserve unrelated work. Consult the [procedure](references/procedure.md) for operation details and the [shared contract](references/execution-contract.md) for authorization boundaries.

1. Start with every finding in a table: run-local ID, stable identity, severity/confidence, plain description, evidence, and proposed action. Separate proposals from owner approval.
2. Default to owner decisions one finding at a time. Fix valid defects; dismiss only with specific evidence and approved rationale in the tool’s dismissal store. A tool-bug report alone does not resolve a finding.
3. Re-run the relevant review after authorized changes, verify the active dismissal matches, and regenerate the report/dashboard. Never merge past unresolved findings or alter gate policy to obtain green.
4. Draft recurring noise/fingerprint problems upstream, filing only on request. Report reviewer strengths, misses, and incomplete coverage; if progress stalls, hand off the blocker instead of inventing resolution.

Report what actually happened, pending decisions, and the next action. Use target-project paths. [Provenance and pattern evidence](PROVENANCE.md).
