# Follow-up skill selection evidence

## Procedure and results

Three new entry points were finalized and their hashes frozen in `final-descriptions.json` after the feature commits and before case authorship. A separate author read only that frozen file and wrote two positive and two negative cases per new skill. A fresh evaluator received fourteen names/descriptions and shuffled request text, without answer labels, skill bodies, previous results, or the work order. Settings were inherited without model/reasoning overrides.

The initial authored IDs named the target skill and followed an ordered pattern. Before calculating any score, the coordinator interrupted the first evaluator, retained its input/output, and normalized only evaluator IDs to opaque values. A different fresh evaluator saw the opaque-ID input. The authored prompts, target labels, and descriptions were never edited after evaluation. `case-id-map.json` and replay preserve exact text equality across the ID normalization.

| Retained run | Target decisions | Interpretation |
| --- | --- | --- |
| Initial descriptive-ID evaluator | 12/12 | Potentially cued by case IDs; retained separately, not counted as independent blind evidence |
| Fresh opaque-ID evaluator | 12/12 | Primary fresh selection result; six positive and six negative target decisions |

The handoff positives cover writing a self-contained brief and assessing another model's critique. Its negatives cover session close and direct patch review against a spec. A target-negative case may correctly select another skill. The score measures target presence/absence, not exact agreement on the complete selected set.

## Checks and limits

All three new packages passed the skill validator and standalone copy/reference checks (12 internal links). Missing Pattern evidence headings were rejected for each new skill in scratch copies. Those are executed structural checks and deliberately broken fixtures, not realistic behavioral tasks. Static review checked the approved rollback/authority, factual-versus-legal, and brief-versus-session/patch boundaries.

No paired behavioral runs, rollback tests, live debugging, legal approval, delivery to another agent, tool initialization, CI setup, or local runtime/device testing were performed for these additions. A routing score does not show quality improvement or native host discovery. Source patterns are supplied reviewer paraphrases with explicit owner decisions, not an independently audited transcript dataset. No public source content was extracted and no transcripts were accessed.

The manifest pins retained evidence hashes. `scripts/replay_history_evaluations.py` (or the main replay command) verifies frozen entry points, all supplied descriptions, request/label integrity, ID-only normalization, case balance, recorded selections, and artifact hashes. It does not call models or rerun the static package-copy experiments.
