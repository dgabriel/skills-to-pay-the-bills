# Provenance: Review Findings Triage

## Public sources

- [docs/dismissals.md](https://github.com/flaught/core/blob/6622fe772e0dcd4d0af74c7dc86111f73795cbd8/docs/dismissals.md) at `6622fe772e0dcd4d0af74c7dc86111f73795cbd8`. Relevant sections: How matching works; Workflow; CLI reference. Repository visibility verified public and license verified MIT before reading; its license file was also fetched at this revision.
- [docs/dashboard.md](https://github.com/flaught/core/blob/6622fe772e0dcd4d0af74c7dc86111f73795cbd8/docs/dashboard.md) at `6622fe772e0dcd4d0af74c7dc86111f73795cbd8`. Relevant sections: Command; Empty or invalid input. Repository visibility verified public and license verified MIT before reading; its license file was also fetched at this revision.
- [docs/findings-schema.md](https://github.com/flaught/core/blob/6622fe772e0dcd4d0af74c7dc86111f73795cbd8/docs/findings-schema.md) at `6622fe772e0dcd4d0af74c7dc86111f73795cbd8`. Relevant sections: ID prefixes; Source types; Analysis completeness. Repository visibility verified public and license verified MIT before reading; its license file was also fetched at this revision.
- [.advreview.yml](https://github.com/dgabriel/MysteryMixClub/blob/3b406c4630e9c857495ebfdfdae76b5b79a70b71/.advreview.yml) at `3b406c4630e9c857495ebfdfdae76b5b79a70b71`. Relevant sections: Test inversion; Severity gate; Dismissals. Repository visibility verified public and license verified MIT before reading; its license file was also fetched at this revision.

## Pattern evidence

Attribution: **author session history, paraphrased by reviewer, 2026-10-17**. No session transcripts were searched, read, quoted, or copied.

Reviewer estimate: about 20 sessions across at least four projects. The repeated pattern is a full finding table before action, owner-led decisions (often one row at a time), specific tracked dismissals, no merging past unresolved valid findings, and a regenerated report. Recurring false positives, reworded dismissal recurrence, docs-only noise, and base/head test-inversion noise become an upstream issue draft, filed only when requested. Plain explanations and a reviewer-quality/coverage assessment are recurring outputs.

## Adaptation and boundaries

Pattern evidence supplies the owner-led decision sequence and blocking unresolved-findings policy. Public dismissal/schema docs supply run-local versus stable identity, expiry, source-type distinctions, and reporting mechanics; the public project config corroborates explicit gate/dismissal and docs-only inversion controls. Provider settings, thresholds, actor identities, project paths, and any credentials from examples are not copied. The current public review-tool repository passed the license/visibility check; no local-only source was needed.

The package retains the author’s [MIT notice](LICENSE). Pattern counts are reviewer estimates, not an independently verified transcript audit.
