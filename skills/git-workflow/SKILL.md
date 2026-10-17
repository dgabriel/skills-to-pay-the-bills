---
name: git-workflow
description: Discover and apply a repository’s Git policy when starting or syncing branches, preparing commits or PRs, resolving conflicts, or recovering missing work. Not for ordinary file edits without Git operations.
---

# Git Workflow

**Inputs:** Target checkout, requested Git operation, current authorization, and issue ID when applicable.
**Output:** A policy-grounded plan or authorized Git operation, with branch/base, checks, and remaining actions.
**Try:** “Use git-workflow to bring my published feature branch current and prepare a PR plan.” (use the skill name in your host's invocation syntax).

Honor the user’s task scope and target-project policy; preserve unrelated work. Use the [procedure](references/procedure.md) for detailed commands/examples and the [shared contract](references/execution-contract.md) when authorization or handoff scope needs clarification.

1. Inspect branch, status, in-progress operations, and canonical project policy before changing state.
2. Identify branch base, publication status, required issue wrapper, checks, and merge/release rules. A Git default branch does not prove the feature-branch policy.
3. Route to the procedure for branch setup/sync, commit/PR preparation, or conflict/recovery. Prefer a merge to preserve published history unless the user has explicitly authorized a rewrite.
4. Preserve unrelated work and reconcile changed files before branch cleanup. A green check is evidence, not an independent grant of authority.

Finish with the artifact or report, checks actually run, open decisions, and the next handoff. Resolve output paths in the target project. See [provenance](PROVENANCE.md) for source revisions and adaptations.
