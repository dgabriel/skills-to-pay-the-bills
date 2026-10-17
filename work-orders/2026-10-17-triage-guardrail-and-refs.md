Status: done (commit "docs: clarify triage overrides and work-order references")

# Follow-up: triage override rule and work-order references

Two small changes on `codex/history-skills`, as one commit: `docs: clarify triage overrides and work-order references`. Don't push or open a PR.

## 1. Owner decision: dismissal guardrail in `review-findings-triage`

The owner chose to **keep the guardrail, with an explicit override path**:

- "Code owner understands the risk" is a valid dismissal rationale for design tradeoffs and accepted risks.
- For a **verified defect**, the agent says it is a confirmed defect and asks: fix, or record an explicit owner override for that specific finding? If the owner overrides, dismiss it through the tool's tracked mechanism with the override and the owner's rationale recorded. No blanket dismissals.

Update `skills/review-findings-triage/references/procedure.md` (the "Owner-led disposition" paragraph) so the override path is stated. The current text says valid defects need fixes and gives no override option. Keep SKILL.md within 28 lines; touch it only if step 2 needs one or two words. Add one line to the skill's PROVENANCE.md "Adaptation and boundaries" noting this is an owner decision dated 2026-10-17.

Selection behavior and descriptions don't change, so don't re-run routing. If the replay freezes procedure-file hashes, record the change the same way the earlier editorial update did, rather than editing old evidence.

## 2. Readable work-order references

`work-orders/2026-10-17-history-skills-review.md` says a broken commit-subject revision expression. That doesn't resolve: `git rev-parse` fails because of the trailing `$`. Change it to:

`Status: done (commit "docs: record work orders and refresh validation status")`

Add one line to `work-orders/README.md`: an order completed in its own commit is referenced by commit subject, since a commit can't contain its own hash. Mark this order the same way: `Status: done (commit "docs: clarify triage overrides and work-order references")`.

## Acceptance criteria

- [ ] The procedure states both the guardrail and the explicit per-finding override, and never permits a blanket dismissal.
- [ ] `python3 scripts/check_library.py` and `python3 scripts/replay_evaluations.py` pass. Paste the output.
- [ ] No work order uses Git search-revision syntax.
- [ ] `git status -sb` is clean and nothing is pushed; `git log --oneline origin/main..HEAD` shows one new commit on top of `bdb5847`.

## Hand back

The checklist with evidence and the new procedure paragraph quoted in full.
