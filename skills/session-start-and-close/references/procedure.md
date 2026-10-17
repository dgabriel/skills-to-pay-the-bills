# Session orientation and close procedure

## Start or resume

Read the target’s AGENTS.md/CLAUDE.md and linked Git hygiene, architecture/design, and task guidance relevant to the work. Treat them as current policy; do not run commands merely because a source project used them. Inspect branch, tracking relationship, dirty/staged/untracked paths, and in-progress merge/rebase. Read current PR state through an available read-only interface; if network/CLI is absent, mark PR and remote freshness unverified. Do not switch branches or clean unrelated files to make orientation look tidy.

Read existing tracker state: open/ready, in progress, and blocked work. With Beads, use `bd prime` for current command context, then `bd ready`, `bd list --status=in_progress`, and issue details where appropriate. No Beads installation, initialization, adoption, claim, database pull, or remote sync is implicit in “get your bearings.” If another tracker is configured, use it instead. If none exists, report that fact without building a replacement tracker.

For interrupted work, reconcile the prior handoff with actual code changes, logs/check evidence, and task status. Do not assume the last narrative finished successfully. Identify partial work, an interrupted operation, or an environment prerequisite before resuming. Carry forward accepted decisions and open questions without inventing a new objective.

Default response is short bullets: checkout/branch and PR state; active and ready tasks; blockers or interrupted operations; next scoped action. Mid-session “where are we?” gets the same concrete format. Read-only orientation can finish before implementation scope is chosen; it does not require another skill to be installed.

## Close without losing state

Inspect current diffs/status and tests actually run. Create discovered follow-ups in the existing tracker when within task authorization, with acceptance context and dependencies; otherwise provide ready-to-file items explicitly marked pending. Do not replace durable shared tasks with loose scratch notes. Update task status at its real completion gate, which may require merge. Preserve native IDs and relevant code/artifact references in the handoff.

Check whether scoped work is committed. When commits are authorized, commit only intended paths using target policy; if authority is absent or checks are blocked, preserve the working tree and report the exact pending step. A close request is not blanket authority to push, sync issue state, or merge. If those actions are authorized, perform the target’s checks and verify the resulting state; otherwise give exact pending actions without claiming remote completion. Do not import an automatic `pull --rebase` or destructive cleanup from a source session block.

Leave a next-developer note in the target’s established handoff location or tracker: task/branch, completed behavior, changed paths, actual validation results, unfinished work, blockers, open decisions, and next command/action. Keep facts needed for another session durable, without storing secrets or personal cross-project configuration. End with a brief status, not a long session narrative.
