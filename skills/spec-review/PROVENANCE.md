# Provenance: Spec Review

## Sources

- [.claude/agents/reviewer.md](https://github.com/dgabriel/claude-code-project-template/blob/59616904f514d6351b8d8de1d6e16ae708057dc3/.claude/agents/reviewer.md) — `59616904f514d6351b8d8de1d6e16ae708057dc3`.
- [.claude/agents/reviewer.md](https://github.com/dgabriel/MysteryMixClub/blob/3b406c4630e9c857495ebfdfdae76b5b79a70b71/.claude/agents/reviewer.md) — `3b406c4630e9c857495ebfdfdae76b5b79a70b71`.

Retrieved 2026-10-17 from public repositories owned by the library author.

## Adaptation

Merged the repeated read-only reviewer role, logic/security/style checks, and structured verdict format. Added explicit state-effect tracing and an INCOMPLETE verdict to avoid passing uninspected behavior. Left project palette, domain constraints, mandatory agent role separation, and review instrumentation at the source. Other public reviewers corroborated the pattern but their domain-specific text was not copied.

The bundled [MIT notice](LICENSE) retains copyright (c) 2026 Dawn Gabriel. No private repository contents, local infrastructure identities, or machine-specific inventory data are included.

## Opinionated rule mapping

| New default | Exact source and section | Source support / adaptation |
| --- | --- | --- |
| Diagnosis only; no unsolicited fix direction | Template `.claude/agents/reviewer.md`, **How to report**, pinned above | “Do not suggest fixes.” Restored directly; replaces the previous skill’s permission to suggest a correction. |
| Treat off-token colors/fonts/patterns as acceptance findings | Same file, **Style guide compliance** | “Enforce … exactly” and no new colors/fonts/patterns outside the guide. Target guide supplies actual values. |
| No unsupported cosmetic findings | Same file, **Code quality** and **Style guide compliance** | Derived from no speculative changes beyond issue scope and enforcing the actual guide. Excluding unsupported cosmetic findings is an explicit scope adaptation; the source does not prescribe an arbitrary report-wide count. |

The exact immutable source link is listed under Sources; all three defaults come from that reviewer file. No universal quote requirement or arbitrary numerical limit on legitimate findings was invented.

## Maintenance notes

The diagnosis-only rule restores the source reviewer’s separation of diagnosis from implementation and replaces the previous library default permitting unsolicited correction directions. That history and its source rationale belong here rather than in runtime instructions. The cosmetic-findings rule is named “no unsupported cosmetic findings”; it is not a numerical finding limit. References to a signal-color cap concern only the target project’s design system.
