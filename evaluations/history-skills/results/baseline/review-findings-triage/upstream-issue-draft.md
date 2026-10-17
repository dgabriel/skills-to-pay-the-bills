# Draft: Repeated dismissed comment finding and false scope/test findings

Tool: Flaught. Reviewed revision: `fictional-feature-head` (fictional fixture). This draft has not been filed.

The current review includes three findings that contradict supplied context or requirements:

- F-3 (`reworded-comment-warning`) reports an unchanged comment as a potential ownership bypass. The prior artifact had an owner-approved dismissal under `old-comment-warning`, titled “Comment looks like an auth override,” because the comment describes the existing check and has no runtime effect. Context confirms the same comment text in both revisions. The current title/fingerprint differ, and the current artifact reports the finding active. Expected: preserve or surface semantically matching dismissal history for owner review, without silently treating an old approval as a new-artifact dismissal.
- F-2 (`decision-record-scope`) calls the accompanying implementation decision record scope creep, although requirements explicitly include it. Expected: ground scope findings in the task's declared boundaries.
- F-4 (`base-head-test`) deterministically flags an existing ownership regression solely because it passes on base and head. Expected: distinguish unchanged regression coverage from a newly added test intended to demonstrate a new failure; passing both revisions is not sufficient evidence of a defective existing test.

The review also correctly identifies F-1: status is assigned before ownership validation. This valid finding should remain actionable.

Analysis metadata reports `partial`, with `neighborhood` dropped. Gate status is `unverified`. No current dismissal write or rerun has happened. No raw prompts, renderer output, complete surrounding callers, or exact tool build are available. The artifacts establish the reported symptoms, not a root cause or confirmed reproduction in a real installation.

Suggested investigation: inspect semantic finding identity and prior-dismissal matching, requirement grounding, and the deterministic base/head test rule; investigate the dropped analysis context separately. Validate corrections with fixtures for unchanged comments with renamed findings, explicitly in-scope decision records, useful existing regressions passing both revisions, and a real mutation-before-authorization defect.

Before filing, attach sanitized current/prior artifacts and relevant requirement excerpts through the owner's normal issue process, and supply tool version and reproduction steps if available. Preserve current gate policy while investigating.
