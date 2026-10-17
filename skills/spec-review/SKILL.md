---
name: spec-review
description: Review a patch against its issue/specification and documented design rules, reporting evidence-ranked deviations without fixes by default. Use for read-only acceptance reviews, not implementation or free-form visual critique.
---

# Spec Review

**Inputs:** Diff or before/after code, requirements/issue, target policies, and relevant tests.
**Output:** PASS/FAIL/INCOMPLETE report with severity, exact location, evidence, and verification limits.
**Try:** “Use spec-review to check this patch against its issue without editing it.” (use the skill name in your host's invocation syntax).

Honor the user’s task scope and target-project policy; preserve unrelated work. Use the [procedure](references/procedure.md) for detailed commands/examples and the [shared contract](references/execution-contract.md) when authorization or handoff scope needs clarification.

1. Read the actual diff and relevant surrounding code, issue, design, and test context. Establish what changed before forming a verdict.
2. Trace expected behavior through authorization, state changes, error handling, and test assertions. Compare requirements to effects, not merely return values.
3. Enforce documented design rules even when behavior works: flag off-token colors/fonts and capped-signal violations. Default cap: zero low-severity cosmetic findings unsupported by a project rule; see the procedure for this scope adaptation.
4. Default to diagnosis only: report the violated rule, trigger, effect, and exact location without repair suggestions or patches. Include corrections only when explicitly requested; this restores the source reviewer’s separation of diagnosis from implementation.

Finish with the artifact or report, checks actually run, open decisions, and the next handoff. Resolve output paths in the target project. See [provenance](PROVENANCE.md) for source revisions and adaptations.
