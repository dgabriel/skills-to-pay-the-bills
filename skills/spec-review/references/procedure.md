# Review procedure

## Evidence before verdict

Default posture: skeptical, evidence-based, read-only. Start with changed behavior and stated acceptance criteria. Read relevant callers, consumers, tests, and architecture/style rules, not only the PR description. For each suspected defect, identify the triggering input/state, actual behavior, expected behavior, and practical impact. Distinguish confirmed defects from unanswered questions.

Check logic/invariants, boundary/error paths, ownership and auth, data validation, secret/log exposure, scope creep, and meaningful test coverage. Inspect ordering: a request can return forbidden after already mutating state. A test that asserts only an error string does not prove an unauthorized action had no side effects.

Use target-specific domain checks from its specs. Independent expected values matter for scientific/business calculations; flag expectations derived from the same implementation. For visual changes, consult current named tokens, typography, component states, and any signal-color rule. Do not invent a universal palette, font pair, or signal cap.

## Reporting

Default format:

- Verdict: PASS (no actionable defect found in inspected scope), FAIL (blocking defect), or INCOMPLETE (material context/check unavailable).
- Findings ranked high/medium/low with `file:line`, concrete trigger, expected versus actual effect, evidence, and impact.
- Spec/style violations identify the exact project rule.
- Checks actually run, coverage limitations, and unresolved questions.

Use precise changed-line locations when available, with a narrow range if needed. If code is provided without stable line metadata, identify the function and snippet rather than invent line numbers. Do not fabricate findings to sound adversarial or bury a real blocker under stylistic nits. A clean report should say what was inspected, not imply a guarantee.

Default to diagnosis only: no fix suggestions, replacement snippets, or patches unless the user explicitly requests them. The source reviewer separates diagnosis from the developer’s repair work. This changes the previous library default that permitted unsolicited correction directions. Do not modify source merely to confirm a finding. Run safe existing tests only when permitted; report unexecuted checks clearly. External review logging is project-specific and never required by this library.

## Opinionated acceptance defaults and source basis

- **Diagnosis-only handoff:** the template reviewer’s “How to report” says to flag the issue/location without suggesting fixes. Apply this even when the repair seems obvious; explicit user requests can override it.
- **Design rules are acceptance criteria:** its “Style guide compliance” requires exact enforcement of named tokens, fonts, patterns, and any signal cap. Report a documented violation even when the UI still functions; a personal style preference is not a rule.
- **Zero unsupported cosmetic nits:** derived from “No speculative changes beyond the scope of the issue” and the documented-style-guide checks. The cap is zero for low-severity cosmetic findings without a cited project rule, not zero for genuine documented style violations. This is a scope adaptation, not a numerical finding limit quoted from the source. Do not suppress correctness/security findings to meet a report quota.

[Source and precise rule mapping](../PROVENANCE.md). A spec finding identifies the actual rule or section, but this library does not require a verbatim quotation where a precise reference is sufficient.
