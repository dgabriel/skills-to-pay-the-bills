# History-derived skill evaluation

Four descriptions and entry hashes were frozen before a separate author wrote two positive and two negative cases per skill. A fresh evaluator saw only the eleven available descriptions and sixteen shuffled requests, with labels hidden. No case or description was edited after scoring. `final-descriptions.json`, authored cases, evaluator inputs, answers, and actual outputs are retained here.

Two independent sessions completed identical fictional triage and prose fixtures. Baseline saw only raw inputs. Assisted saw the relevant packages and raw inputs. They did not see each other's outputs, earlier evaluations, or answer keys. Inherited model/settings were used without overrides. These were actual text-generation runs with static review, not live tool/device executions.

`paired-tasks.json` contains the common raw inputs. Retained reports and upstream drafts are under `results/`. No review CLI, dismissal write, dashboard renderer, tracker mutation, network call, or local server ran. No session transcripts were searched or read.

One assisted report introduced two fictional personal labels. The retained copy replaces only those labels with owner/caller role placeholders. `manifest.json` records the raw digest, the redaction reason, and retained artifact hashes; the exact raw output remains outside the checkout. No finding, proposed action, uncertainty, score, or source fact was improved during that privacy edit.

## Result and limits

Fresh routing scored 16/16 target decisions. Both triage outputs found the valid defect, recommended the same evidence-backed dismissals, and left the gate unverified. Assisted output made run-local/stable identities and approval/application states more explicit, but no better defect identification or resolution was demonstrated. Both prose outputs preserved the facts and removed unwanted wording; baseline was 51 words and assisted was 53. No quality improvement is established.

Provenance patterns are the work-order reviewer's paraphrases, not an independently audited transcript dataset. Public source visibility/license checks are recorded in `source-checks.json`. Required public reference URLs and unmodified MIT attribution are retained; no operational endpoint or credential is included.

Run `python3 scripts/replay_evaluations.py` from the library root for the original executable fixtures and this evidence's integrity/content checks. `scripts/replay_history_evaluations.py` checks this subset directly. Neither script regenerates agents or calls a review tool. See the root validation report for limitations and per-commit verification scope.
