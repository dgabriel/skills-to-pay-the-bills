# Rename notes

- spec-review: renamed from `code-review` to avoid a host command collision.
- regression-testing: renamed from `testing` to narrow discovery to regression work.
- beads-workflow: renamed from `issue-workflow` to make the tracker dependency explicit.

Historical evaluation artifacts retain the same prompts, expected decisions, outputs, and scores. Only skill identifiers, titles, and artifact directory references were normalized to current names; no behavioral response or request was improved retroactively. Exact pre-normalization artifacts are retained outside this checkout. Original historical JSON digests are recorded in evaluations/history.json.

An obsolete-identifier check must match names and paths, not the substring “testing”: the current name contains that word, and ordinary prose still uses it. The old identifiers above are intentional rename notes.
