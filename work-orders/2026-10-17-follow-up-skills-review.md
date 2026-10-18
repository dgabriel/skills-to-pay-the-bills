Status: done (commit "test: add routing evidence for diagnose-first, docs-audit, agent-handoff-prompt")

# Gatekeeper review: Part C on `codex/checker-config`

Reviews: Part C of [2026-10-17-follow-ups.md](2026-10-17-follow-ups.md), commits `feat: add diagnose-first skill` through `docs: add project bootstrap stage to new-project prompt`.

Verdict: **changes required. The skill content is approved; the evidence isn't finished.**

## Approved as committed

- `diagnose-first`: the rollback guardrail is stated in SKILL.md and procedure (owner approval, separate worktree or branch, never reset or discard, isolate data and deployments).
- `docs-audit`: factual mismatches only, never legal approval; doesn't touch production data or credentials.
- `agent-handoff-prompt`: two modes, explicit exclusions for session close and patch-versus-spec review, and drafting a prompt doesn't authorize sending it.
- The new-project bootstrap section points to existing skills instead of duplicating them.
- README, catalog, extraction ledger, and `skill_checks.json` entries match the three packages.
- The reviewer ran all three scripts from an isolated archive of each of the four commits; all pass. Privacy grep over the new and changed files is clean.

## Required

1. **Show the routing evaluator didn't see target hints.** `evaluations/follow-up-skills/` has two inputs: `routing-input.json` uses opaque request IDs, and `routing-input-authored-ids.json` uses IDs like `fresh-docs-01`, which name the target skill. File times suggest the evaluator answered the authored-ID input and its output was converted to opaque IDs afterward. Say which input the evaluator actually received.
   - If it received opaque IDs: delete the authored-ID input and output files, or explain why they're kept.
   - If it received authored IDs: that result is invalid. Run a fresh evaluator on `routing-input.json` only, with cases and descriptions unchanged, and retain the earlier run labeled as invalid with the reason.
2. **Commit the evidence** as `test: add routing evidence for diagnose-first, docs-audit, agent-handoff-prompt`. Include this review file, with its status set to `done (commit "<that subject>")`.
3. **Make it replayable.** Extend `scripts/replay_history_evaluations.py`, or add an equivalent check, to score the retained decisions against the answers and verify the frozen descriptions still match the SKILL.md files. The replay should fail if a decision or description changes.
4. **Update validation.md** in the same commit:
   - Current status: record the new score as the latest fresh routing, kept separate from 16/16, 28/28, and the historical sets. Remove "until fresh routing is recorded".
   - Fix the "Open limits" sentence ("…no behavioral comparison.  no repeated…": double space and lowercase start).
   - History: replace the three identical "Added X" lines with one entry that gives the routing result, notes that it includes negatives separating agent-handoff-prompt from session-start-and-close and spec-review, and states that no paired behavioral run was done.

## Non-blocking (note only)

- `skill_checks.json` now repeats the same two rules for seven skills. The shared rule group from the Part A review is now worth proposing in a later order. Don't build it here.
- The order allowed extending `work-orders/README.md` with the gatekeeper loop. Skipping it is fine; the skill's procedure covers it.

## Limits

Don't push, open a PR, amend, or rebase. Don't change skill content or routing cases. Leave status lines in the follow-ups order alone.

## Acceptance criteria

- [ ] Written answer to item 1, with evidence.
- [ ] All three scripts pass, and the replay fails in a scratch copy when one retained decision is flipped. Paste both.
- [ ] `git status -sb` is clean; `git log --oneline origin/main..HEAD` shows the eight existing commits plus the test commit. Nothing pushed.

## Hand back

The checklist with evidence and the routing score.
