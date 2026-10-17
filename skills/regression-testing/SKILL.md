---
name: regression-testing
description: Write and execute regression tests for a changed behavior, bug, endpoint, or threshold, using specification-derived expectations and reproducible failures. Not prose edits, general testing theory, or a read-only review without test execution.
---

# Regression Testing

**Inputs:** Behavior/specification, changed implementation, existing tests/config, and environment prerequisites.
**Output:** Focused tests plus exact commands/results and a failure handoff; application fixes only if separately requested.
**Try:** “Use regression-testing to verify this booking change and report failures without fixing app code.” (use the skill name in your host's invocation syntax).

Honor the user’s task scope and target-project policy; preserve unrelated work. Use the [procedure](references/procedure.md) for detailed commands/examples and the [shared contract](references/execution-contract.md) when authorization or handoff scope needs clarification.

1. Derive outcomes from the spec or independent fixtures. For externally defined domain values, cite the oracle next to each expectation; if it is unavailable, stop those assertions and report the gap rather than synthesizing values.
2. Cover happy/edge/error paths. For each changed API operation, check request validation, response shape, status codes, and error handling by default; mark inapplicable checks with a reason. At thresholds test below/on/above, and assert unchanged state after rejected mutations.
3. Run focused tests during iteration, then required wider checks when ready. Keep shared-database runs serial and mock external services.
4. Report exact failures, expected/actual behavior, and verification gaps. Preserve failing evidence instead of silently changing implementation or expectations.

Finish with the artifact or report, checks actually run, open decisions, and the next handoff. Resolve output paths in the target project. See [provenance](PROVENANCE.md) for source revisions and adaptations.
