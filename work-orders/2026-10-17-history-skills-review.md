Status: done (commit "docs: record work orders and refresh validation status")

The status identifies the completing commit by subject so this record can be completed in that commit itself without amending or adding a second commit.

# Gatekeeper review: `codex/history-skills`

Reviews: [2026-10-17-history-skills.md](2026-10-17-history-skills.md)

Verdict: **approved after one small fix commit.** The four skills meet the order. The reviewer re-ran both scripts at HEAD and at every one of the six commits from an isolated worktree; all pass. Fresh routing (16/16) and the paired results are reported honestly, including "no quality gain demonstrated" for both paired skills.

## Accepted pushback

- The literal "no hostnames or people's names" criterion conflicts with pinned public source URLs and MIT notices. Your narrower interpretation (no operational endpoints, credentials, session identifiers, or real personal names in new content) is accepted.
- Redacting the two fictional personal labels in one retained output, with digests preserved, is accepted.

## Required (one commit)

Commit message: `docs: record work orders and refresh validation status`

1. **Commit `work-orders/` and the AGENTS.md work-order rule.** The order asked for them in the docs commit; they are still untracked/modified in the checkout.
2. **Ignore Python caches.** Add `__pycache__/` to `.gitignore` (the replay scripts create `scripts/__pycache__/`).
3. **Fix stale statements in validation.md:**
   - The history section says PR #1 was open. It has since merged as a merge commit (`4d76fc9`) whose parent is `930407d`, so `origin/main..HEAD` is exactly the six new commits and no rebase is needed. Say that instead.
   - The older "Checks actually executed" and "Limits and replay" sections still say "seven packages" and "five local commits await the owner's reviewer gate". Mark them as historical (that pass is merged) or update the counts so nothing reads as current when it isn't.
4. **Update work order statuses:**
   - `2026-10-17-history-skills.md` → `Status: done (38ffa07)`
   - this file → `Status: done (<your fix commit>)`

## Non-blocking (note in your hand-back, don't fix now)

- `check_library.py` hard-codes the four new skill names and a prose-edit-only em-dash rule. As the library grows, per-skill rules should live in skill metadata or a small config, not in the checker. Propose a shape in two or three sentences; don't implement it.
- validation.md is becoming an append-only log. Suggest (don't do) a structure: current status at the top, history below.

## Owner decision (not yours)

`review-findings-triage` says "code owner understands the risk" is decision context but not a blanket reason to dismiss a verified defect. The owner used that phrase as her dismissal rationale. The reviewer thinks the guardrail is reasonable; the owner decides whether to keep it. Leave the text as is.

## Limits

- Don't push, open a PR, amend, or rebase. The owner decides on the PR after this commit.
- Don't change skill content.

## Acceptance criteria

- [ ] `git status -sb` is clean (no untracked `work-orders/`, no `__pycache__/`), and the branch is ahead of origin, nothing pushed.
- [ ] `git log --oneline origin/main..HEAD` shows the six commits plus the one fix commit.
- [ ] `python3 scripts/check_library.py` and `python3 scripts/replay_evaluations.py` pass. Paste the output.
- [ ] `git grep -n "PR #1 was open\|five local commits await"` returns nothing current (historical labels are fine).
- [ ] Both work orders show `done (<commit>)`.

## Hand back

The checklist with evidence, `git log --oneline origin/main..HEAD`, and your two non-blocking proposals.
