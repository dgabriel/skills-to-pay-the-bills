Status: done (commit "docs: add second-opinion order review")

# Gatekeeper review: second-opinion follow-ups, all six parts

Reviews: every part of [2026-10-17-second-opinion-follow-ups.md](2026-10-17-second-opinion-follow-ups.md), as built on branches `codex/second-opinion-a-bookkeeping` (`1aeb837`), `codex/second-opinion-f-subject-guidance` (`c556516`, stacked on A), `codex/second-opinion-c-replay` (`7db5982`), `codex/second-opinion-b-routing` (`6dc758c`, stacked on C), `codex/second-opinion-d-rule-groups` (`787a9e5`), and `codex/second-opinion-e-independent-review` (`27ad46d`).

Verdict: **approved, all parts.** Checks were re-executed independently from isolated archives, not trusted from the hand-back.

## Approved as committed

- **A** closes the earlier follow-ups order correctly: Part B marked done with the recorded owner acceptance, Part C and the order marked done, and [README.md](README.md) gains the loop-closure line.
- **C** moves replay logic into `scripts/replay_evaluations.py` without duplication; `replay_history_evaluations.py` is a documented forwarding stub; README, both evaluations READMEs, and validation.md current-status wording updated; historical command references preserved as records.
- **B** builds the canonical suite to spec: 161 retained occurrences mapped to 93 unique request/target/label cases with stable content-derived IDs; byte-for-byte source copies under `sources/` with originals untouched; manifest pins the description set and all artifacts; the invalid descriptive-ID run and ID map retained as-is; replay asserts the recorded 89/93 score, full source coverage, and unchanged labels/requests, and fails with "rerun the full canonical suite" when a current description drifts. The four missed positives (two older Beads, two broad spec-review requests; one Beads case now selects agent-handoff-prompt) are retained as visible tripwires with no relabeling. README, evaluations/README.md, and validation.md lead with the 89/93 canonical result while keeping historical scores separate.
- **D** shrinks `scripts/skill_checks.json` via a `history-derived` group with per-skill extras; composition cannot silently drop a shared check; unknown config keys, unknown rules, and unknown group references are all rejected.
- **E** adds the independent-verification section to `skills/agent-handoff-prompt/references/procedure.md` only; every `SKILL.md` is byte-identical to the freeze on all six branches.
- **F** adds the commit-subject fallback guidance to [README.md](README.md) and records final part statuses; each recorded hash matches its branch tip.

## Executed verification

- All six branch tips pass `check_library.py`, `replay_evaluations.py`, and the forwarding stub, each run from a fresh isolated archive.
- Scratch negatives all fail as required: flipped canonical decision; tampered `sources/` copy; a current description edited (the new regression tripwire, firing correctly); Pattern-evidence heading removed from a member skill; misspelled skill key; unknown group reference; em dash in the prose-edit package.
- Canonical suite independently recounted from the JSON (not via the builder's replay): 93 unique cases, 161 occurrences, 89 correct — matching the manifest; stable-ID derivation spot-checked; `descriptions_sha256` verifies.
- Privacy scan clean: the checker's absolute-path hygiene rule passed over every branch, and new content contains only fictional fixtures and relative paths.
- Nothing pushed; no branch carries an upstream; working tree left clean.

## Trusted, not re-executed

The consolidated evaluator's isolation is a self-report recorded in `evaluations/routing-regression/evaluator-process.md`, the same epistemic status as prior passes; no model evaluation was re-run for this review.

## Follow-ups for the owner (non-blocking)

1. Merge order `a → f → c → b → d → e`. Expect textual conflicts only in `work-orders/2026-10-17-second-opinion-follow-ups.md` between the per-part subject-form status lines and F's hash-form; resolve toward F's version, which is the accurate final record.
2. The 89/93 exposes pre-existing description drift: terse Beads-era and spec-review-era positives misroute under fourteen descriptions. Fixing descriptions requires re-freezing and a fresh full-suite evaluator run, which the canonical suite now supports. This is a product decision, not a defect in the reviewed work; candidate for a future order.
3. Convention note: part-status lines were written twice (subject-form per part, hash-form in the final closer). Harmless; future orders may simply have the closer record hashes.

## Limits

This review changes nothing but this file. No skill content, evaluation evidence, or historical work-order bodies were edited. The reviewed branches remain local and unmerged at the owner's gate.
