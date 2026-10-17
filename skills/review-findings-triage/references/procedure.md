# Review finding procedure

## Inventory before action

Establish the current reviewed revision, artifact freshness, gate config, tool version, and dismissal mechanism. Flaught is the default integration, not a dependency for another reviewer’s findings. If the CLI is absent, work from supplied artifacts and label commands as planned; do not install or initialize tools implicitly.

Create one row per finding with run-local ID, fingerprint or equivalent stable key, source/source_type, severity, confidence, description in plain language, supporting code/spec evidence, proposed fix/dismiss/upstream-bug action, owner decision, and application/verification state. Include harmless and informational findings so none disappear. Explain a confusing finding as concrete input, actual effect, expected effect, and impact before asking for a decision. Confidence is not proof, and an ID prefix is not a substitute for source_type.

## Owner-led disposition

Default to the owner selecting one row at a time; batch only when requested. A proposal is not an approval. “Code owner understands the risk” is a valid dismissal rationale for design tradeoffs and accepted risks. For a verified defect, state that it is a confirmed defect and ask whether to fix it or record an explicit owner override for that specific finding. Fix and verify it unless the owner explicitly overrides; if overridden, dismiss it through the tool’s tracked mechanism with the specific override and the owner’s rationale recorded. For a harmless or false-positive finding, record why the cited code is safe or the check is inapplicable, what evidence was examined, and the authorized dismissal decision. Never apply blanket dismissals or silently merge past an unresolved finding.

Use the tool’s tracked dismissal mechanism, not deletion of a row or editing a status field in a generated report. For current Flaught, inspect the installed help and project config before applying `flaught dismiss <finding-id> --artifact <artifact-path> --reason <specific-rationale>`; the run-local ID must come from that exact artifact. Respect any expiry policy and actual actor attribution; never invent either. Verify the resulting store entry and matching active fingerprint. Expired, missing, or mismatched dismissals remain unresolved until handled. Store modifications and code fixes follow current task authorization.

## Rerun and reporting

After authorized fixes/dismissals, rerun the project’s actual review command for the current revision. Inspect findings, dismissal status, tool failures, and reported analysis completeness; an exit code alone does not prove broad coverage. Keep the existing gate policy. Do not add a new LLM release gate or suppress categories to bypass a result. A plan-only or missing-tool task ends with pending commands and a gate status of unverified, not clean.

Regenerate the project review report and, for Flaught trend artifacts, use `flaught dashboard --input <artifact-directory> --output <report-path>`. Keep runs in separate artifact directories so a report does not accidentally reuse stale evidence. A zero-finding valid artifact differs from missing/invalid input. Say whether review and dashboard commands actually ran and whether any LLM/tool pass was incomplete.

Finding IDs are run-local. Fingerprints support durable dismissal matching, but LLM title changes can create a new fingerprint for the same concern. Compare code context and prior rationale rather than copying a dismissal by ID or assuming an old decision matched. If a previously dismissed concern recurs under new wording, retain both records, verify the context, and get the proper current disposition. A repeated unchanged result with no new evidence is a blocker to report, not a reason for an endless loop.

## Upstream feedback and reviewer quality

For recurring false positives, docs-only noise, or inversion checks that treat an existing regression test passing on both base/head as inherently invalid, draft a concise tool issue: observed check and version, minimal redacted example, expected versus actual behavior, prior dismissal/context, impact, and reproduction/verification limits. Passing on both revisions alone does not establish that a test is useless. Distinguish tool defect from configuration issue and genuine application bug. File the issue only when requested; draft text is not a filed issue or a resolved finding.

Close with the complete dispositions, remaining gate blockers, refreshed artifact/report paths, checks actually executed, and a short reviewer-quality assessment: useful detections, false positives, blind spots, missing context, and what evidence would test those gaps.
