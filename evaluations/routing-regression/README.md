# Canonical routing regression suite

One suite re-evaluates all retained valid case variants against the current fourteen skill descriptions. Current recorded result: **91/93 target decisions**. It keeps 161 retained occurrences as 93 unique request/target/label cases, with every source occurrence mapped. Exact repetitions are counted once; the two revised historical prompts remain distinct. Expected target labels and request text are unchanged.

- `descriptions.json`: current descriptions and all entry hashes, frozen before consolidation/evaluation.
- `sources/`: byte-for-byte copies of original input/answer files; originals remain untouched.
- `cases.json`, `source-map.json`: stable opaque IDs, unchanged labels/text, and complete source mappings.
- `routing-input.json`: evaluator-visible descriptions and requests only.
- `routing-answers.json`: target labels hidden from the evaluator.
- `routing-output.json`: actual selections and rationales from one fresh evaluator.
- `evaluator-process.md`: role separation, exact allowed input, result, and limitations.
- `manifest.json`: hashes of this snapshot and the recorded score.

The coordinator is the consolidation/author role; a separate fresh evaluator saw no labels, skill bodies, prior results, or work orders. No case or description was edited after scoring. The two current missed positives are the bare issue-handoff request (Beads target; session-start-and-close selected) and feature-verification request (regression-testing target; spec-review selected). Both broad spec-review positives now pass. No target labels changed. See evaluator-process.md for details.

Whenever any skill description changes, freeze the complete updated description/entry set and have a fresh evaluator re-score **all** canonical cases. Preserve the previous canonical snapshot before recording the replacement run. Newly authored cases must likewise be written after descriptions are finalized, with author/evaluator roles separate. Adding cases does not authorize rewriting prior expectations to improve scores.

Run `python3 scripts/replay_evaluations.py` from the repository root. Replay verifies current descriptions/entries against the canonical snapshot, source coverage and byte-for-byte copies, unchanged labels/requests, recorded decisions, score, and all artifact hashes. A mismatch in recorded target selection is reported as a score, not hidden by editing the case; artifact tampering or stale descriptions fail verification. Replay does not call a model.

Historical 32/35, revised 35/35, unchanged rerun 35/35, fresh 28/28, fresh 16/16, and opaque-ID 12/12 results remain frozen under their original description sets. The invalid descriptive-ID run and original ID map remain as-is in their original folder, excluded from the primary suite. Canonical current-file integrity replaces live-versus-historical description comparisons; historical fingerprints remain in place rather than being rewritten when a future current description changes.

## Current description revision

The owner chose to broaden spec-review to patch review against its issue/specification or documented project rules, without requiring a supplied spec. The current 91/93 result comes from one fresh evaluator after re-freezing all fourteen descriptions and entry hashes. The [complete prior 89/93 snapshot](snapshots/2026-10-18-before-spec-review-broadening/README.md) remains in place, including its manifest, descriptions, inputs, answers, output, process note, sources, and documentation. Current manifests also hash those preserved files. The current process note records the expected pre-freeze tripwire failure and the exact remaining misses.
