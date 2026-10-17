# Beads procedure and defaults

## Discover and inspect

Prefer the `bd` CLI. Obtain current command/context from `bd prime`, `bd where`, and command-specific `--help` when the installed version differs. If unavailable, report the missing prerequisite and provide a plan; do not install, initialize, or migrate a tracker as an interview side effect.

Use `bd ready`, `bd list --status=open`, `bd list --status=in_progress`, and `bd show <native-id>` to inspect current state. Prefer `--json` where supported for machine parsing. Do not use interactive `bd edit`; use `bd update` fields.

For a legacy identifier, search by title or inspect `external_ref` using `bd list --json`. Match the exact legacy reference and verify the result with `bd show`; flag ambiguous or missing matches. Never manufacture a native hash ID. A reference to a retired tracker is a lookup key, not permission to write to it.

## Start, update, and complete

Default to durable Beads tasks for work that survives a turn: blockers, dependencies, discovered follow-up work, and shared status. An ephemeral personal checklist can remain local; do not create a competing durable Markdown tracker.

When starting implementation, use a target-required branch-and-claim wrapper first. Do not pre-claim and then run a wrapper that also claims. Otherwise use `bd update <id> --claim`, handle an already-claimed issue as contention, and do not overwrite someone else's ownership. Defaults for new tasks: meaningful title and acceptance context, type `task`, priority 2 unless urgency differs; priorities are 0–4, not words. Example: `bd create "Record tool return" --description="Acceptance criteria and why this matters" --type=task --priority=2`.

Record discovered work with rationale and dependencies. Mark blockers explicitly. Close with `bd close <id> --reason="Evidence of completion"` only when the project's actual done gate is met; if merge is required, tests alone do not justify closing. Otherwise leave an accurate in-progress/blocking state.

## Handoff and synchronization

Handoff includes native ID, current status, changed code/branch, checks actually run, unresolved decisions, blockers, and the next concrete step. Use notes/update fields supported by the current CLI.

Code branches and the issue database are different state axes. Checkout does not change issue state; do not mirror every feature branch into a Beads database branch without a project need. Discover the installed sync mechanism: Dolt-based projects may use `bd dolt pull/push`; do not assume JSONL files are the live sync protocol. A database pull can merge state, and a database push can publish it, so use the target's rules and current authorization. Do not close and sync ahead of the code gate. Keep personal cross-project preferences separate from shared repository facts without duplicating stores.
