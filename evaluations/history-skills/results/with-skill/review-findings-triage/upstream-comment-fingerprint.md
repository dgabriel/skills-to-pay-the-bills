# Draft: unchanged comment concern resurfaces under a new fingerprint

Tool: Flaught; version not supplied. Observed check source_type: llm. Reviewed revision: `fictional-feature-head`.

The supplied fictional artifact reports F-3, `reworded-comment-warning`, active with title “Comment may weaken ownership validation.” Context states that the comment text is identical in the previous and current code. A prior artifact approved dismissal of `old-comment-warning`, titled “Comment looks like an auth override,” because the comment describes the existing owner check and has no runtime effect.

Minimal supplied sequence: dismiss a comment-only concern on one artifact; review unchanged comment context again; observe a changed title/fingerprint and an active concern. Exact comment text, full diffs, raw prompts, version and executable reproduction are unavailable, so this is a candidate tool issue, not a reproduced fingerprint defect. Configuration and matcher behavior need inspection too.

Expected: evaluate runtime evidence before reporting an authorization bypass; provide stable matching or candidate prior-disposition context when wording changes. Actual: supplied context reports the unchanged concern active under a different fingerprint. Impact: repeat owner triage and an unresolved current finding despite a prior decision. Do not automatically carry a dismissal into changed security context.

Please inspect fingerprint construction and prior-context matching using controlled repeated runs with identical code/comments, then contrast with a real authorization change. A separate mutation-before-validation defect in the same function is valid and must remain visible. No current dismissal or rerun has occurred. This draft is not filed and does not resolve F-3.
