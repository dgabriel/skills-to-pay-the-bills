# Canonical routing regression suite

One suite re-evaluates retained case variants against the current **fifteen** skill descriptions. Current recorded result: **94/97 target decisions**, including **4/4** newly authored skill-security-review cases. It keeps 165 retained occurrences as 97 unique request/target/label cases, with every source occurrence mapped. All prior 93 cases and their labels remain unchanged; four separately authored cases were added after the new description was frozen. Exact repetitions are counted once; revised historical prompts remain distinct.

- `descriptions.json`: current descriptions and all entry hashes, frozen before consolidation/evaluation.
- `sources/`: byte-for-byte copies of original input/answer files; originals remain untouched.
- `cases.json`, `source-map.json`: stable opaque IDs, unchanged labels/text, and complete source mappings.
- `routing-input.json`: evaluator-visible descriptions and requests only.
- `routing-answers.json`: target labels hidden from the evaluator.
- `routing-output.json`: actual selections and rationales from one fresh evaluator.
- `evaluator-process.md`: role separation, exact allowed input, result, and limitations.
- `manifest.json`: hashes of this snapshot and the recorded score.

The coordinator is the consolidation role; new case author and fresh evaluator were separate agents. The evaluator saw only fifteen descriptions and opaque requests, without labels, skill bodies, prior results, or work orders. Three current missed positives remain: bare Beads handoff (agent-handoff-prompt and session-start-and-close selected), legacy-ID Beads lookup (none selected), and feature verification (regression-testing target; spec-review selected). New cases scored 4/4. No prompt or expected label changed after scoring. See evaluator-process.md for the full process and limits.

Whenever any skill description changes, freeze the complete updated description/entry set and have a fresh evaluator re-score **all** canonical cases. Preserve the previous canonical snapshot before recording the replacement run. Newly authored cases must likewise be written after descriptions are finalized, with author/evaluator roles separate. Adding cases does not authorize rewriting prior expectations to improve scores.

Run `python3 scripts/replay_evaluations.py` from the repository root. Replay verifies current descriptions/entries against the canonical snapshot, source coverage and byte-for-byte copies, unchanged labels/requests, recorded decisions, score, and all artifact hashes. A mismatch in recorded target selection is reported as a score, not hidden by editing the case; artifact tampering or stale descriptions fail verification. Replay does not call a model.

Historical 32/35, revised 35/35, unchanged rerun 35/35, fresh 28/28, fresh 16/16, and opaque-ID 12/12 results remain frozen under their original description sets. The invalid descriptive-ID run and original ID map remain as-is in their original folder, excluded from the primary suite. Canonical current-file integrity replaces live-versus-historical description comparisons; historical fingerprints remain in place rather than being rewritten when a future current description changes.

## Prior spec-review description revision (91/93)

The owner chose to broaden spec-review to patch review against its issue/specification or documented project rules, without requiring a supplied spec. The prior 91/93 result came from one fresh evaluator after re-freezing all fourteen descriptions and entry hashes. The [complete prior 89/93 snapshot](snapshots/2026-10-18-before-spec-review-broadening/README.md) remains in place, including its manifest, descriptions, inputs, answers, output, process note, sources, and documentation. Current manifests also hash those preserved files. That process note and output are retained in the prior snapshot.

## Accepted tripwires recorded at 91/93

The following policy and outcome table is the retained 91/93-era note; current 94/97 outcomes are listed above.

The owner accepts the two v1-era Beads originals as potential misses: a bare request without tracker context need not select beads-workflow. Their v2 context-establishing revisions are the live task variants and both pass in the current run. The original requests and positive labels remain unchanged and still count in the 93-case score; acceptance does not relabel or omit them. The table records all four misses from the prior 89/93 snapshot together.

| Original retained positive | Current result after Part A | Disposition |
| --- | --- | --- |
| “Prepare an issue handoff for another session.” | Miss: session-start-and-close selected instead of beads-workflow | Accepted boundary tripwire; superseded by “Prepare a Beads issue handoff for another session.”, which passes |
| “Resolve legacy issue OLD-42 to its native tracker ID.” | Pass: beads-workflow selected | Accepted as a potential boundary miss in future runs; superseded by “Resolve legacy issue OLD-42 to its native ID in this Beads project.”, which passes |
| “Give a read-only pre-merge review of these changes.” | Pass: spec-review selected | Owner chose BROADEN; the documented project-rules path now admits patch review without a supplied spec |
| “Review this patch for correctness and security.” | Pass: spec-review selected | Same broadening decision; retained positive now passes |

The other current miss, “Verify this feature and report exact failures without fixing app code.” (regression-testing target; spec-review selected), is **not** covered by the accepted Beads disposition. It remains a reported regression signal. This note changes no case, label, description, output, or score: the current result remains 91/93.

## Current addition: skill-security-review

The [complete prior 91/93 tree](snapshots/2026-10-18-before-skill-security-review/README.md) is preserved in place, including the older 89/93 snapshot. A separate author wrote two positive and two negative selection cases after the fifteen descriptions were frozen. A new evaluator scored the full 97-case input. Static package-review smoke results are retained separately in the skill's evaluation folder; no candidate code was executed.
