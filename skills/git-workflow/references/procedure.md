# Git procedure

## Policy discovery

Read target `AGENTS.md`, `CLAUDE.md`, linked Git hygiene/CI documents, and relevant hooks/scripts. Follow the canonical policy when an older issue guide disagrees; identify the conflict in the report. A project wrapper that creates a branch and claims an issue takes precedence over a manual duplicate sequence. Do not run source-project commands in the target by analogy.

Inspect `git status --short --branch`, `git branch --show-current`, tracking refs, and any merge/rebase in progress. Refresh remote-tracking refs with `git fetch --prune` when network access and task scope allow; if unavailable or plan-only, state that refs are unverified. Discover protected/integration/release branch roles rather than inferring them from names. If policy is absent, propose a feature branch from the confirmed default branch and ask only about material uncertainty before a mutation.

## Branch setup and synchronization

Default: branch before implementation, one logical change per branch, start from the repository's current integration base. Existing project policy and explicit user choices override these defaults. Name the branch per target conventions. Do not impose `develop` or a staging tier on a main-only project.

Inspect unrelated changes before checkout or synchronization. Preserve them; do not automatically stash, discard, or stage them. For unpublished work, use the target's preferred synchronization method. For published/shared commits, merge the updated base by default and retain history. If the user authorizes a rewrite, review exact affected commits and use a lease tied to the observed remote head rather than an unconditional force push.

## Commits and PRs

Default to one logical change and Conventional Commits unless the target says otherwise. Inspect staged diff and named paths, run required checks, and retain hooks. Do not invent attribution identities or issue trailers. Check environment prerequisites when a hook fails; distinguish infrastructure failure from regression rather than bypassing it.

Before a PR, state the explicit base, change intent, test evidence, and known gaps. Keep production promotion distinct from ordinary integration when the repo uses that model. Discover merge strategy and approval gates from current target policy; no automatic merge rule is inherited from a source document.

## Conflicts, recovery, and reconciliation

Resolve conflicts in the feature branch with surrounding intent and relevant tests. Avoid hand-resolving a squash merge at the final merge step; synchronize first using the publication-safe method, then let the merge apply cleanly. Keep recovery refs until the result is verified.

For lost work, inspect logs, original branch refs, and `git reflog` before recreating code. Before deleting a branch, compare the intended changes with the merged target, accounting for later unrelated target edits. An empty whole-file diff is strong evidence when no later edits exist, but it is not a universal requirement: inspect every difference for retained behavior, compare patches/history, and run relevant tests. Never treat squash commit ancestry alone as proof that all hunks survived. Stop and report uncertain reconciliation rather than deleting the recovery source.

Report branch/base, policy consulted, current dirty paths, refs refreshed or stale, checks, operation result, and pending authorized actions.
