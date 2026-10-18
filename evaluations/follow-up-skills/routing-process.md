# Routing input and evaluator sequence

## Answer to the gatekeeper

The primary evaluator received **routing-input.json with opaque IDs only**. It did not receive routing-input-authored-ids.json or an output converted from descriptive IDs.

The execution sequence was:

1. Freeze three entry hashes and fourteen descriptions before the separate case-author task.
2. The author wrote twelve cases with descriptive IDs. A first evaluator was started on the initial input. Those IDs exposed target names and ordering, so the coordinator interrupted it before calculating any score. It had already saved a complete output.
3. Preserve that input/output under the authored-ID filenames. Normalize only request IDs and save the mapping, without changing requests, descriptions, or labels.
4. Start a **different fresh evaluator**, with no inherited task history, explicitly instructed to read only routing-input.json and write routing-output.json. The task prohibited access to other files, labels, earlier results, skill bodies, or work orders. It returned that it had written independent selections and rationales for all twelve requests and had read or changed no other files.
5. Only after the second evaluator completed, calculate both scores. Both were 12/12. All twelve rationales differ between the two outputs after matching the ID map. The second output was not produced by converting the first output's IDs.

This sequence is recorded from the coordinator's tool calls and evaluator completion response in the current task, not inferred from filesystem timestamps or retrieved session transcripts. The evaluator's file-access statement is a self-report, not a sandbox audit. Distinct rationales support separate generation but do not by themselves prove information isolation. File times alone cannot establish which input a model saw.

The authored-ID artifacts are retained as **invalid blind evidence**, preserving the initial attempt and its flaw. They do not contribute to the primary opaque-ID score. The replay validates exact authored request equality through the ID mapping, frozen descriptions, both retained outputs, and their recorded hashes. No cases or labels were edited to improve a score.
