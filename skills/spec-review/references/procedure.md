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

Default to diagnosis only: no fix suggestions, replacement snippets, or patches unless the user explicitly requests them. Do not modify source merely to confirm a finding. Run safe existing tests only when permitted; report unexecuted checks clearly. External review logging is project-specific and never required by this library.

## Acceptance defaults

- **Diagnosis-only handoff:** report the issue, location, trigger, effect, and violated rule without suggesting fixes unless the user explicitly requests them.
- **Design rules are acceptance criteria:** enforce the target guide’s named tokens, fonts, patterns, and signal-color rule. Report a documented violation even when the UI still functions; a personal style preference is not a rule.
- **No unsupported cosmetic findings:** omit low-severity cosmetic preferences without a cited project rule. Report genuine documented style violations, and do not suppress correctness or security findings to meet a report quota.

[Source and precise rule mapping](../PROVENANCE.md). A spec finding identifies the actual rule or section, but this library does not require a verbatim quotation where a precise reference is sufficient.
