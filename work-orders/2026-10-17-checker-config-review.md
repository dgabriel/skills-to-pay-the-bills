Status: done (commit "fix: reject unknown skill names in check config")

# Gatekeeper review: Part A on `codex/checker-config`

Reviews: Part A of [2026-10-17-follow-ups.md](2026-10-17-follow-ups.md), commit `refactor: move per-skill checks into skill config`.

Verdict: **approved after one small fix.** The refactor is correct and limited to `scripts/`. All three scripts pass at HEAD. The reviewer ran the old and new checkers on identical scratch copies with each rule broken (pattern evidence heading, "not" exclusion, em dash in prose-edit). Both checkers reported the same error every time.

## Required (one commit)

Commit message: `fix: reject unknown skill names in check config`

1. **A typo in `scripts/skill_checks.json` silently turns rules off.** The reviewer renamed the `prose-edit` key to `prose-edits` and added an em dash to the prose-edit procedure. The old checker failed; the new one passed. The same thing happens when a skill is renamed or removed. Make `check_library.py` report an error for any config key that doesn't match a folder under `skills/`.
2. Prove it: show the checker failing on a misspelled key in a scratch copy, and passing at HEAD.
3. Commit this review file with the fix. In the same commit, mark Part A in the follow-ups order `done (commit "fix: reject unknown skill names in check config")` and set this file's status the same way.

## Non-blocking (note only)

- The four skills repeat the same two rules, so the config is 64 lines for four rule sets. If Part C adds more skills that need them, a shared rule group that skills opt into would keep the file short. Don't do it now.

## Limits

Don't push, open a PR, amend, or rebase. Don't change skill content.

## Acceptance criteria

- [ ] The checker fails on an unknown config key (scratch copy) and passes at HEAD. Paste both outputs.
- [ ] `python3 scripts/check_library.py`, `python3 scripts/replay_evaluations.py`, and `python3 scripts/replay_history_evaluations.py` pass. Paste the output.
- [ ] `git log --oneline main..HEAD` shows the work-order commit, the refactor, and the fix. `git status -sb` is clean and nothing is pushed.

## Hand back

The checklist with evidence.
