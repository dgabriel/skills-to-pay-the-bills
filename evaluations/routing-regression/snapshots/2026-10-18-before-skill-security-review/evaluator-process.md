# Spec-review broadening: canonical rerun process

Owner decision: BROADEN. On 2026-10-18 the coordinator preserved the complete 89/93 canonical snapshot in snapshots/2026-10-18-before-spec-review-broadening before editing spec-review. Only its description line changed; existing exclusions and all other entry-point text were preserved. The stale-description tripwire was run before re-freezing and failed with: `AssertionError: Current description changed; rerun the full canonical suite` (exit 1).

The coordinator then froze all fourteen updated descriptions and entry hashes, changed only the description set in routing-input.json, and kept all 93 opaque request IDs/prompts and all expected labels byte-for-byte equivalent to the prior snapshot. The coordinator performed the author/consolidator role. A separate fresh evaluator had no inherited conversation history and was explicitly instructed to read only routing-input.json and overwrite routing-output.json, without reading existing output, labels, skill bodies, prior results, cases, work orders, or snapshots. No new cases were authored.

The evaluator returned that it read only routing-input.json, answered all 93 requests, did not read existing output, encountered no access limitations, inherited settings without overrides, and did no browsing, scoring, or additional agent work. This documents tool-call sequence and evaluator self-report, not a file-access audit. Scoring occurred only after completion. No case, expected label, description, or response was edited after observing the result, and no repeated trial was run.

Result: **91/93 target decisions**. Both old broad spec-review positives now select spec-review. The remaining expected positives are:

- `r-1cd22973978fafe0`: “Prepare an issue handoff for another session.” Target beads-workflow; selected session-start-and-close.
- `r-94f22aba78a0460b`: “Verify this feature and report exact failures without fixing app code.” Target regression-testing; selected spec-review.

The old legacy-ID Beads request now selects beads-workflow. The regression-testing miss was not one of the prior four misses and is reported without reclassification. A single run with a changed description does not establish causality, behavioral improvement, or a stable gain. Previous 89/93 output and all historical scores remain preserved separately; the invalid descriptive-ID run and its ID map are untouched.
