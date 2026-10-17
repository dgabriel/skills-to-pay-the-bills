# Execution contract

This workflow supports the user's current task and authorization. Read existing target-project instructions; preserve explicit user choices, unrelated work, and chosen deliverable format. The target project owns outputs; installed skill folders hold instructions.

A planning or review request does not authorize implementation, scaffold deletion, commits, pushes, PRs, publication, deployment, tracker mutation, or remote synchronization. Perform those only within authorization already present in the task. Ask before destructive actions or history rewrites when authorization is absent. Do not repeat approval requests for actions already authorized.

Record assumptions, partial progress, and checks actually run. Silence is not approval. In an unattended draft, leave unresolved decisions explicit rather than inventing answers. Apply recommended defaults when no existing project or user choice overrides them, and state consequential overrides.

Maintainers: edit `shared/execution-contract.md` and run `python3 scripts/sync_contract.py`. Packaged copies are generated so a single skill remains usable when copied without the rest of this library.
