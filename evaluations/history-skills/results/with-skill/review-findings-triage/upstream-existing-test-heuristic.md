# Draft: base/head pass heuristic flags an existing regression test

Tool: Flaught; version not supplied. Observed check source_type: deterministic. Finding F-4, fingerprint `base-head-test`, reports “Existing ownership regression passes on base and head” at confidence 1.0.

Minimal supplied case: an existing test covers unchanged ownership behavior, passes on base and head, and is flagged solely for those two passes. The project requirements explicitly allow useful existing regressions to pass on both revisions. The test source, raw runner output and exact check implementation are not supplied, so the observed behavior is artifact-backed but not independently reproduced. There is no prior dismissal for this finding.

Expected: distinguish an existing regression from a newly introduced test intended to demonstrate a changed behavior. Passing on both revisions alone is insufficient evidence that an existing test is invalid. Actual: this criterion generates a finding against the existing test. Impact: misleading test-quality feedback and unnecessary owner triage at the blocking gate.

Please reproduce with a minimal repository containing a pre-existing ownership test and an unrelated change; inspect whether configuration limits this check to newly added regression tests. Verify that the heuristic accepts valid existing tests while still evaluating whether new tests exercise the intended change. Separately assess whether this particular test covers state preservation on rejected cancellation; the available evidence does not establish that coverage. This draft is not filed, and F-4 remains unresolved pending current owner disposition and verification.
