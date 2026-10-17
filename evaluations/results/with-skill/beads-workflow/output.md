# Start and handoff command plan

Snapshot resolves exact legacy reference `https://legacy.example/issues/OLD-42` to native ID `borrow-8x9`, title “Record tool returns”, status open. This is supplied evidence, not a live verification. CLI is unavailable; no commands executed, installed, or initialized.

When CLI is available, read project policy and run `bd prime`; if it returns no context run `bd where`. Inspect `bd list --json` to match the exact external_ref and `bd show borrow-8x9` to verify the current issue and ownership. Stop on ambiguity or contention. Inspect current Git status before starting so unrelated work survives.

Start with `scripts/issue-start.sh borrow-8x9`. The project requires this wrapper, which creates the branch and claims the issue. Do not run `bd update borrow-8x9 --claim` before or after it. If it reports contention or failure, inspect current state before retrying; do not overwrite an owner.

Before later handoff, inspect `bd show borrow-8x9`, current branch/status, and exact test results. Check `bd update --help` for the installed notes field, then, if `--notes` is supported, use:

```sh
bd update borrow-8x9 --notes="Handoff: [actual branch and changed files]; checks: [actual commands and results]; blockers: [actual blockers or none]; decisions: [open decisions]; next: [concrete action]."
```

Replace bracketed fields with observed facts; do not publish placeholders. Leave accurate in-progress/blocking state while code is unmerged. The code completion gate is merge plus passing acceptance checks; tests alone cannot close the task. Only after that gate and authorization use `bd close borrow-8x9 --reason="Merged [verified revision]; acceptance checks [actual evidence] passed"`.

Code branches and tracker database synchronization are separate. Discover the installed synchronization mechanism; do not assume JSONL or a Dolt command. No remote synchronization without separate permission. Handoff here is a command plan only; live state, wrapper availability, CLI field support, branch name, and test evidence remain unverified.
