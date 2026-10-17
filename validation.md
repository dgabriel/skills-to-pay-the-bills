# Validation results

Executed 2026-10-17. Seven skills have structural checks, selection evaluations, and retained paired-task evidence. This report separates historical scores, current reruns, and fresh cases; no result was improved by changing a request after seeing its outcome.

## Selection history and current scores

| Dataset/run | Result | What changed before this run |
| --- | --- | --- |
| Historical v1 | 32/35 target decisions | Original descriptions and requests |
| Historical v2 | 35/35 | PRD description broadened to support immediate drafting; two issue positives revised to explicitly establish Beads context |
| Current existing set | 35/35 | Approved identifier renames and finalized descriptions; the exact 35 v2 request strings and IDs were reused unchanged |
| Fresh set | 28/28 (14 positive, 14 negative) | A separate author received only finalized descriptions, then wrote two positive and two negative cases for each of all seven skills |

The historical v1→v2 improvement was partly due to two fixture edits, not solely a better description. Both old and revised versions remain in [results](evaluations/results/). The raw pre-rename JSON digests are in [history.json](evaluations/history.json). Names/paths in historical artifacts were normalized as explained in the rename notes; historical request arrays were checked against the raw outside-checkout copies and remain identical.

Before fresh cases were written, final entry hashes/descriptions were saved in [final-descriptions.json](evaluations/final-descriptions.json). The fresh author did not see previous cases/results or skill bodies. Another evaluator received only descriptions and request IDs/text, with labels hidden, and evaluated the existing and fresh sets. [Fresh authored cases](evaluations/fresh-cases.json) and all actual routing outputs/answers are retained. No fresh prompt, expected label, description, or response was edited after scoring. Replay verifies the preserved evaluation fingerprints, documented editorial changes, and unchanged existing requests.

Scoring checks selection/omission of the intended target; another skill may legitimately match a target-negative request. These are model selection exercises, not native host discovery tests. Evaluator settings were inherited without model/reasoning overrides.

## Current paired rerun: outcome versus presentation

Two fresh, isolated evaluator sessions repeated the exact previous raw tasks for spec-review and regression-testing. Baseline had only the raw fixtures; assisted had the corresponding final skill package. They could not read each other's outputs or previous runs. No network, installs, Git/tracker mutations, or edits to application fixtures were permitted.

| Skill | Baseline | Skill-assisted | Did the result change? |
| --- | --- | --- | --- |
| [spec-review](evaluations/results/current-pair/with-skill/spec-review/output.md) | Static diagnosis of unauthorized cancellation; suggested restoring ordering and adding a regression | Same defect; diagnosis-only handoff without unsolicited fixes; added `verify_review.py`, whose assertion reproduced the state mutation (exit 1) | **Defect conclusion unchanged.** Response scope changed, not merely headings: unsolicited repair directions were withheld. Runnable evidence also differed, but one run cannot attribute that choice causally to the new default. |
| [regression-testing](evaluations/results/current-pair/with-skill/regression-testing/output.md) | 2 methods/30 subcases, 6 adjacency failures | 3 methods, 2 adjacency subtest failures, explicit boundary triplet and justified N/A entries for HTTP/state/external-oracle checks | **Defect conclusion unchanged.** Coverage organization and reporting changed; no stronger defect detection or quality gain demonstrated. |

Both versions left implementation unchanged and caught the known half-open-range bug. Test-method/subcase counts are not quality rankings. The added endpoint-contract and missing-external-oracle defaults are not exercised on a real API or scientific oracle by this pure-function task; their provenance and plausibility do not substitute for a behavioral proof of those paths.

[Current baseline outputs](evaluations/results/current-pair/baseline/) and [current assisted outputs](evaluations/results/current-pair/with-skill/) include exact reports, generated tests, and logs. Intentional exit-1 assertion failures prove these fixture defects were exposed; they do not mean an application passed verification.

## Earlier seven-task paired run

The historical paired run remains under [baseline](evaluations/results/baseline/) and [with-skill](evaluations/results/with-skill/). Each evaluator handled seven tasks in one session. Requirements/design produced usable drafts in both conditions; technical design followed FastAPI/Postgres author defaults with the skill versus Django without. Git and Beads plans respected policy in both conditions. Review found the same authorization defect in both. Historical regression tests ran 6 methods/42 assertion-subtest failures without and 12 tests/3 failures with the skill. Main demonstrated value was default alignment and repeatable structure, not better defect detection.

## Checks actually executed

- `python3 scripts/check_library.py`: seven packages, local links, metadata, contract copies, entry length for the new portable format, obsolete identifiers, and personal-path hygiene. Run before **each** of the five local commits.
- `python3 scripts/replay_evaluations.py`: scored all four retained routing sets, checked frozen entries and unchanged requests, reran historical/current saved test suites, replayed contrast calculations and the current review reproduction. Recorded assertion failures are intentional; collection/environment errors are rejected.
- Skill creator `quick_validate.py`: all seven final entry points passed frontmatter/name/scaffold validation.
- Historical independent package-copy check: seven complete standalone folders and their 28 package-local links resolved without the rest of the library. Current packages still use internal references and are checked again after this revision.
- Contract synchronization exercised on an isolated copy: clean check, intentional drift failure, synchronization, and repaired check passed.
- Privacy scan against excluded identifiers kept outside the checkout, plus tracked-text path checks: no excluded source identifiers or absolute personal paths introduced. No private inventory was restored.
- `git diff --check`: passed.

## Documentation verification and source-backed defaults

The [official Codex skill URL](https://learn.chatgpt.com/docs/build-skills) was opened successfully and returned **Build skills** content on 2026-10-17; it is retained because it was verified. Claude Code install/invoke documentation was checked in the prior pass. No native host install/discovery session was executed.

New opinionated rules are mapped to immutable source files/sections in [spec-review provenance](skills/spec-review/PROVENANCE.md) and [regression-testing provenance](skills/regression-testing/PROVENANCE.md). A source does not prescribe a report-wide numerical style quota or mandatory verbatim quotations, so neither is claimed as sourced. The spec review rule is **no unsupported cosmetic findings**, explicitly identified as a scope adaptation. Beads command/wrapper rules are mapped in [its provenance](skills/beads-workflow/PROVENANCE.md).

## Limits and replay

No native Claude Code/Codex discovery, real Beads mutation, real Git recovery, live stakeholder interview, UI integration/accessibility session, or repeated statistical trial ran. Source repositories and remote history were untouched. The five local commits await the owner's reviewer gate; no push or PR is authorized here.

Run the two scripts above to replay deterministic evidence without calling a model. See [evaluation instructions](evaluations/README.md) for regenerating agent runs and keeping author/evaluator roles separate.

## Editorial follow-up

Stale display titles were corrected, change-history/rationale text moved from runtime instructions into provenance, and the cosmetic-findings rule was named directly. Descriptions, selection requests, expected answers, and behavioral rules were not changed or re-evaluated. The evaluation-time entry hashes remain in final-descriptions.json; [editorial update fingerprints](evaluations/editorial-updates.json) document the two current entry-point changes. Replay verifies both the unchanged descriptions and the explicit old/current fingerprints rather than replacing the original freeze. The heading checker was observed failing on the four stale headings before they were corrected, then passing afterward.

## History-derived skills pass

Base selection: PR #1 was open, so the local `codex/history-skills` branch starts at the PR head `930407d209ab17f19ea2639baed70992b5d3d213`, not main. This pass adds four packages from the supplied reviewer paraphrases and author-stated prose rules. No session transcript directory or transcript export was searched, read, quoted, or copied. No personal/global settings were changed.

### Fresh selection, separate from all historical scores

The new pass scored **16/16**, comprising two positive and two negative cases for each of the four new skills. The four entry points/descriptions were finalized and hashed before a separate author received descriptions and wrote the cases. A fresh evaluator received only all eleven descriptions and the shuffled request IDs/text. Expected labels and skill bodies were hidden. No prompts, labels, descriptions, or outcomes were edited after scoring. Target negatives exercise raw patch review/concept explanation, feature implementation/non-repository planning, staging deployment/test-code-only requests, and original writing/code changes.

The earlier 32/35, prompt-edited 35/35, unchanged rerun 35/35, and previous fresh 28/28 remain separate historical results. No new score replaces them. [New evidence](evaluations/history-skills/README.md) contains all authored cases, frozen descriptions, actual decisions, fixtures, and paired outputs.

### Paired baseline versus skill

| New skill | Baseline | Assisted | Supported conclusion |
| --- | --- | --- | --- |
| review-findings-triage | Complete four-finding table, valid defect identified, same proposed dismissals, upstream draft, reviewer-quality assessment, gate unverified | Same decisions and unresolved state; more explicit run-local/fingerprint, approval, and application columns; two narrower upstream drafts | No improved finding classification or completed resolution demonstrated. The clearest difference is identity/state accounting and report detail. |
| prose-edit | Preserved the supplied facts and removed the unwanted wording in 51 words | Preserved the same facts and removed unwanted wording in 53 words | Both matched the requested editing direction. The skill did not produce a shorter result or demonstrate a quality gain. |

These were two actual agent sessions, each doing two fictional tasks with inherited settings and no overrides. Triage was static reasoning and command planning only. No review run, dismissal mutation, dashboard generation, upstream filing, Git action, external service, account seed, LAN server, or owner-device test was executed. Prose editing generated text; it did not commit or change a real site. The replay checks artifact integrity, all four finding labels, explicit unverified gate wording, preserved prose facts, word counts, and no em dashes. These checks do not grade every reasoning claim or prove native host routing.

One assisted triage report introduced two fictional personal labels. Only those labels were replaced with role placeholders in the retained copy; raw and retained digests and the redaction reason are preserved. No behavioral result was changed. There is no randomized repetition, independent quality score, or causal proof that the skill alone caused the report differences.

### Source, privacy, and execution checks

Eligible public source metadata and MIT declarations were verified before file retrieval/use. The public review-tool docs supplied fingerprint/dismissal and dashboard semantics. Public project session/run instructions supplied orientation, handoff, readiness, and branch-preservation procedures. Two other public source candidates had no verified license declaration and were not extracted in this pass. The prose skill uses no public source; its rules are author-stated and its three examples were written for the package.

The literal request for no hostnames or people's names anywhere in tracked files conflicts with required pinned public URLs, MIT attribution, and pre-existing fictional fixture labels. This pass retains required public references and notices, checks introduced text for operational endpoints/addresses, credentials and session-like identifiers, and manually reviews personal/source identifiers. New fictional personal labels in one response were removed as described above. It does not claim that a regex proves the absence of every possible personal name or that pre-existing evidence was scrubbed.

All four packages passed the skill validator. All eleven packages pass the library checker, including explicit new-skill exclusions, Pattern evidence sections, synced contracts, and an enforced no-em-dash check over the complete prose package. Complete standalone package copies were checked for internal reference resolution. The scripted replay verifies the preserved earlier evidence and new frozen descriptions/artifacts; only the earlier executable booking/contrast/review fixtures execute code.

Both required scripts are run from an isolated archive of each exact local commit, so later uncommitted files cannot make an earlier commit appear valid. Feature commits replay the existing evidence; new history-derived evidence and its replay checks arrive in the fifth, test-focused commit. Full per-commit outputs are retained outside the checkout for the reviewer handoff. No push, PR creation, remote-history mutation, or source-repository edit is part of this pass.
