# Evaluation cases and evidence

[cases.json](cases.json) contains seven raw task fixtures plus three selection-positive and two selection-negative requests per skill. [results](results/) retains actual outputs, routing decisions, generated test code/logs, and the assisted design calculator. Inputs use a fictional tool-sharing product; no personal source inventory is included.

## Behavioral runs

To reproduce a baseline, create an isolated directory per task, write its `artifacts` to their relative paths, and give a fresh agent the `request` only. Do not expose skill text or expected results. For the assisted run, create the identical raw fixture and give another agent the selected skill’s complete package. Preserve output.md, any requested test code, executed commands, exit codes, and exact errors. Use the same model/settings, isolate baseline from assisted outputs, and restrict execution to local fixtures without network or external mutations.

For selection, give an evaluator only skill names/descriptions and the requests, with stable case IDs. Require zero or more selected skill names and rationale. Keep expected positives/negatives hidden until scoring. Each negative is a negative for its target skill; it may legitimately match another skill. Retain failed or ambiguous cases as well as reruns.

The completed paired run used one evaluator session for seven baseline tasks and a separate session for seven assisted tasks, with inherited session settings and no overrides. The two routing rounds each used a fresh evaluator. This design prevents baseline access to skill content, but has no repetition or per-task randomization. See [validation.md](../validation.md) for results and limitations.

## Review criteria

| Task | Observable criteria |
| --- | --- |
| Requirements | Draft rather than interview when requested; core journey, scoped MVP, budget, non-goals, signals, and explicit unknowns |
| Technical design | Concrete stack with rationale, budget uncertainty, ownership, concurrent non-overlap, tests and unresolved choices; assisted run should use author defaults absent an override |
| Design | Concrete semantic tokens, actual text/muted/status contrast calculations, guide-only boundary, states and later integration checks |
| Git | Canonical main-only policy overrides old issue guide; preserve published history and unrelated notes; explicit PR gate and unverified refs |
| Issues | Exact native-ID lookup, no duplicate manual claim around wrapper, correct completion gate, no invented sync authorization |
| Review | Find unauthorized mutation and inadequate assertion, with location/evidence; remain read-only |
| Testing | Derive half-open adjacency from spec, run standard-library tests, expose intentional bug, retain failures, leave implementation untouched |

These criteria were used for manual comparison of actual outputs; they are not a claim that a separate blinded judge assigned numerical quality scores.

## Deterministic replay

From the library root:

```sh
python3 scripts/check_library.py
python3 scripts/replay_evaluations.py
```

Replay creates temporary fixtures, reruns the two saved test suites and assisted contrast calculator, verifies the known review defect, and scores stored routing decisions. It **does not** call a model or regenerate an agent response. Expected test failures are distinguished from collection/environment errors. Initial routing evidence is retained because the first round revealed a description gap and two underspecified positive requests.

## Current revision and fresh cases

Final descriptions/entry hashes were frozen in [final-descriptions.json](final-descriptions.json) before a separate author wrote [28 new cases](fresh-cases.json). They were evaluated with hidden labels after the descriptions were final. Existing v2 request IDs and texts were reused verbatim for the 35-case rerun. Current inputs, answers, and actual model outputs use `current-existing` and `fresh` suffixes under results. No prompt was edited after seeing either score.

Historical artifacts received identifier/path normalization only. [history.json](history.json) retains pre-normalization raw JSON digests and request-equality checks; the exact originals remain outside the checkout. Historical behavior and original scores were not replaced.

The new paired run is under `results/current-pair/`, with two raw fixture tasks per evaluator and separate baseline/assisted sessions. It supplements rather than overwrites the earlier seven-task run. Replay checks both generations. The current spec conclusion did not change; assisted review withheld unsolicited fixes and included executable evidence. Regression defect detection did not change; report and test organization did. See the root report for limits.
