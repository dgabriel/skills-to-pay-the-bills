# Plan only

Canonical policy: AGENTS.md delegates to docs/git-hygiene.md. Its main-only policy supersedes issue-guide.md's older develop/rebase/automatic-PR guidance. Published branch feature/tool-returns tracks origin/feature/tool-returns; snapshot reports one commit behind main, two unique commits, no active operation, and unrelated untracked notes.txt. Preserve notes.txt; do not stage, discard, or automatically stash it.

No commands executed and no refs refreshed. Snapshot and remote freshness are unverified. When synchronization is authorized with network access:

1. Inspect `git status --short --branch`, `git branch --show-current`, `git branch -vv`, and `git status` to confirm the snapshot, tracking branch, and absence of an in-progress merge/rebase. Inspect named changed paths and check whether incoming files would collide with notes.txt. Stop to preserve that file if a collision exists.
2. Run `git fetch --prune origin`. Review `git log --oneline --left-right HEAD...origin/main` and `git log --oneline --left-right HEAD...origin/feature/tool-returns`; reconcile concurrent feature-branch updates without overwriting them before continuing. Confirm current checkout is feature/tool-returns.
3. Run `git merge origin/main` on that feature branch. Never rebase these published commits or force-push. If conflicts arise, resolve with surrounding intent, inspect `git diff --check`, stage only resolution paths, and complete the merge. If intent is unclear, retain the merge state for review; an authorized `git merge --abort` can return to the pre-merge state without discarding unrelated files.
4. Run required `python3 -m unittest discover -s tests`; inspect `git diff --check`, `git status --short --branch`, `git diff --cached --name-status`, and `git diff origin/main...HEAD`. Verify only intended changes, including both unique commits, survive. Untracked notes.txt remains excluded.
5. Prepare PR title/body with problem, result, exact test evidence, gaps, and explicit base main. Push only when authorized; no push occurs in this planning task. Ask before opening the PR, as canonical policy explicitly requires. Passing tests do not authorize opening or merging it.

Handoff: feature/tool-returns → main; execute this plan only within later authorization. No tests or Git operations ran in this fixture.
