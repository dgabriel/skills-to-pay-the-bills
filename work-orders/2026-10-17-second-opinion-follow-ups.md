Status: open

# Second-opinion follow-ups: routing consolidation, replay merge, process hygiene

From an external second-opinion review of the merged `codex/checker-config` work (Parts A–C of [2026-10-17-follow-ups.md](2026-10-17-follow-ups.md)), approved by the owner on 2026-10-17. The review found the three new skills and the gatekeeper loop sound; the items below are the improvements, two process fixes, and an explicit skip list.

Recorded and resolved at review time, no action needed: the branch reached origin only through the owner's own PR #6 merge after the hand-backs, so the "don't push" limits bound the agents during the loop as intended. The two near-identical test-commit subjects (`5494e2a`, `a132665`) resulted from a mandated exact subject plus the no-amend limit; Part F prevents repeats.

Each part below is separate work. Do one part only when the owner names it, on its own branch from `main`, and hand back for review before any PR. When a part is done, mark it here with its commit. Mark this order `done` when all parts are done or dropped.

Shared rules for every part: follow AGENTS.md and the existing package format. Don't push, open a PR, or touch remote history unless the owner says so. Historical work-order bodies stay unchanged; only the status lines named in Part A may be marked. Push back in writing on anything you disagree with.

## Part A: close out the follow-ups order

Status: open

The `validation.md` restructure (`docs: put current validation status first`) shipped without a gatekeeper review, and Parts B and C of [2026-10-17-follow-ups.md](2026-10-17-follow-ups.md) carry no status lines; the order itself is still `open`. There was also a process trap: the Part C review told the builder to leave status lines alone, so no agent was ever authorized to mark Part C done.

- With the owner's disposition on record (accept Part B as-is, or complete a retro review first):
  - Mark Part B `done` with commit `docs: put current validation status first`, noting owner acceptance without a separate review pass (or the retro-review outcome).
  - Mark Part C `done` with commit `test: add routing evidence for diagnose-first, docs-audit, agent-handoff-prompt`.
  - Mark the follow-ups order itself `done`.
- Add one line to [work-orders/README.md](README.md): a review that forbids touching status lines must name who closes the loop and when.
- Commit: `docs: close out follow-ups work order`

## Part B: one canonical routing regression suite

Status: open

The real coverage gap: replay scores frozen outputs against frozen descriptions. A new or edited description that cannibalizes another skill's routing is never detected, because the 35-case, 28-case, 16-case, and 12-case sets are never re-run against the current fourteen descriptions. The follow-up negatives cover one direction of one boundary only, and incidentally.

Propose the layout before building; one acceptable shape:

- One canonical routing set in a single folder with stable case IDs, accumulating all retained positive/negative cases from [evaluations/results](../evaluations/results/), [evaluations/history-skills](../evaluations/history-skills/), and [evaluations/follow-up-skills](../evaluations/follow-up-skills/), with expected labels unchanged.
- The manifest also hashes the current description set, so replay verifies the recorded consolidated score was produced against today's descriptions.
- Whenever any `SKILL.md` description changes, a fresh evaluator (separate author/evaluator roles per [evaluations/README.md](../evaluations/README.md)) re-scores the full canonical set and the output is recorded; this is what catches cross-skill cannibalization.
- The replay entry point scores the retained consolidated output and keeps the historical set scores as frozen history. Historical folders and scores stay untouched and stay labeled by their description sets.
- Retain the invalid descriptive-ID run and its ID map as-is; invalid evidence is part of the record.
- Update evaluations/README.md, the root README maintenance table, and validation.md current-status text. Keep historical scores separate per existing policy.
- Commit: `test: consolidate routing evidence into one regression suite`

## Part C: merge the replay scripts

Status: open

`replay_evaluations.py` already executes `replay_history_evaluations.py` via runpy, and the "history" script is now the general replay under a history-specific name. Keep one entry point.

- Move all checks into `scripts/replay_evaluations.py` (or propose a neutral name first); delete `replay_history_evaluations.py` or leave a thin forwarding stub — builder's call, stated in the hand-back.
- Update references in the root [README.md](../README.md) maintenance table, the evaluations READMEs, and validation.md current-status wording. Historical work orders and validation history keep the old names; they are records, so don't rewrite them.
- Prove behavior is unchanged: the merged script passes at HEAD and fails in a scratch copy with one tampered artifact. Paste both.
- Commit: `refactor: merge replay scripts into one entry point`

## Part D: shared rule group in `scripts/skill_checks.json`

Status: open

Seven skills repeat the same two rules; both earlier gatekeeper reviews deferred a shared group until more skills needed it. They do now.

- Add a named rule-group mechanism (for example a top-level `"groups"` key, with per-skill `"groups": [...]` membership). Keep per-skill extras, such as the prose-edit em-dash rule, as per-skill overrides.
- Behavior stays identical: in scratch copies, a missing Pattern evidence heading still fails for each member skill, an unknown config key still fails, and the prose package em-dash check still fails. Paste the scratch runs.
- The `"not "` description-substring tripwire may move into the group unchanged; do not weaken it in this part.
- Commit: `refactor: share common skill check rules`

## Part E: independent verification review in agent-handoff-prompt

Status: done (commit "docs: add independent verification review to agent-handoff-prompt")

The library has no first-class "re-execute the evidence before endorsing a verdict" posture — what the gatekeeper did on this repo: isolated-archive reruns, scratch negative tests, privacy greps. Per the library overlap rule, this belongs as a section in an existing skill, not a new skill.

- Add a short `## Independent verification review` section to `skills/agent-handoff-prompt/references/procedure.md`: when assessing another agent's completion claims, re-run the stated checks from an isolated copy where feasible, use negative scratch tests for checker claims, and report executed versus trusted evidence separately in the verdict.
- Do **not** edit `skills/agent-handoff-prompt/SKILL.md`: its hash is frozen in `evaluations/follow-up-skills/final-descriptions.json` and replay asserts equality. Change procedure.md only. If the owner wants the entry point changed, that requires re-freezing and a fresh consolidated routing run — sequence it after Part B and say so before starting.
- No catalog or routing changes are needed while the description is untouched.
- Commit: `docs: add independent verification review to agent-handoff-prompt`

## Part F: commit-subject fallback guidance

Status: open

Add two lines to [work-orders/README.md](README.md): when a review mandates an exact commit subject, name the fallback for the case where that subject already exists (a distinct follow-up subject, recorded in the review), since amending is forbidden.

- Commit: `docs: note commit-subject fallback in work-order guidance`

## Do not do (explicit skips)

- No repeated statistical trials or blinding additions to routing runs; the sets are tripwires and are correctly framed as such.
- No history rewriting to fix the duplicate test-commit subjects; Part F is guidance only.
- No removal of retained invalid evidence, and no edits to historical work-order bodies.
- No `SKILL.md` entry-point changes anywhere in this order; Part E explains the freeze constraint.
- No combining these refactors with new-skill creation.

## Acceptance criteria (each part)

- [ ] `python3 scripts/check_library.py` and the replay entry point(s) pass. Paste the output.
- [ ] Privacy grep over tracked files is clean: no private or local-only repository names, absolute personal paths, session identifiers, or credentials. Paste the command and output.
- [ ] `git status -sb` is clean and nothing is pushed.
- [ ] Part B additionally: consolidated fresh score recorded with its evaluator process note, and the replay fails in a scratch copy with one tampered canonical file. Paste both.
- [ ] Part C additionally: scratch-copy tamper failure pasted.

## Hand back

Which part you did, the checklist with evidence, `git log --oneline main..HEAD`, and anything you disagree with.
