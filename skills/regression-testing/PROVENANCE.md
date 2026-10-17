# Provenance: Testing

## Sources

- [.claude/agents/tester.md](https://github.com/dgabriel/claude-code-project-template/blob/59616904f514d6351b8d8de1d6e16ae708057dc3/.claude/agents/tester.md) — `59616904f514d6351b8d8de1d6e16ae708057dc3`.
- [.claude/agents/tester.md](https://github.com/dgabriel/MysteryMixClub/blob/3b406c4630e9c857495ebfdfdae76b5b79a70b71/.claude/agents/tester.md) — `3b406c4630e9c857495ebfdfdae76b5b79a70b71`.

- [.claude/agents/tester.md](https://github.com/dgabriel/cosmic-jev/blob/4039f03cc1da92e5e1cca40a260eef4dfb3f5d31/.claude/agents/tester.md) — `4039f03cc1da92e5e1cca40a260eef4dfb3f5d31` (external-oracle and threshold procedure).

Retrieved 2026-10-17 from public repositories owned by the library author.

## Adaptation

Merged happy/edge/error coverage, pytest/API-client defaults, behavior-oriented frontend assertions, exact failure reports, and the shared-Postgres serialization rule. Extended reference-based oracles and threshold checks as general testing procedure; domain-specific scientific values and project test cases remain in their source repositories. Removed mandatory tester/developer delegation and fixed frontend runner assumptions.

The bundled [MIT notice](LICENSE) retains copyright (c) 2026 Dawn Gabriel. No private repository contents, local infrastructure identities, or machine-specific inventory data are included.

## Opinionated rule mapping

| New default | Exact source and section | Source support / adaptation |
| --- | --- | --- |
| Per-changed-operation validation/shape/status/error checklist | Template `.claude/agents/tester.md`, **Stack → Backend tests**, pinned above | Explicitly lists request validation, response shape, status codes, and error handling. Adapted into a per-changed-operation default with justified N/A entries. |
| Citation next to externally defined expected values; stop affected assertions when oracle unavailable | Cosmic JEV `.claude/agents/tester.md`, **Non-negotiable rules for expected values**, pinned above | Requires a real reference and citation comment, and says to stop/report when unavailable rather than compute expected values from the implementation. Generalized beyond astronomy only for externally defined values. |
| Below/on/above threshold cases | Cosmic JEV tester, **Stack → Tests**, pinned above | Boundary routing and wraparound tests. This behavior existed in the previous library and is not counted as a new opinion. |

The Cosmic JEV file is an author-owned public source with no separate repository license found during discovery. Its procedure is adapted under the owner’s explicit extraction request; the source file is not copied. The library package retains its author’s MIT notice. No claim is made that every source repository declares MIT.
