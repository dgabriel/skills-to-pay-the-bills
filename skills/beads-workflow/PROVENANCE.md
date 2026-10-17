# Provenance: Issue Workflow

## Sources

- [.agents/skills/beads/SKILL.md](https://github.com/dgabriel/MysteryMixClub/blob/3b406c4630e9c857495ebfdfdae76b5b79a70b71/.agents/skills/beads/SKILL.md) — `3b406c4630e9c857495ebfdfdae76b5b79a70b71`.
- [.agents/skills/mmc-issue-management/SKILL.md](https://github.com/dgabriel/MysteryMixClub/blob/3b406c4630e9c857495ebfdfdae76b5b79a70b71/.agents/skills/mmc-issue-management/SKILL.md) — `3b406c4630e9c857495ebfdfdae76b5b79a70b71`.

- [.agents/skills/mmc-git-hygiene/SKILL.md](https://github.com/dgabriel/MysteryMixClub/blob/3b406c4630e9c857495ebfdfdae76b5b79a70b71/.agents/skills/mmc-git-hygiene/SKILL.md) — `3b406c4630e9c857495ebfdfdae76b5b79a70b71` (canonical wrapper/policy precedence).

Retrieved 2026-10-17 from public repositories owned by the library author.

## Adaptation

Consolidated the already reusable Beads entry point with legacy-ID resolution, durable task boundaries, numeric priorities, and handoff/sync lessons from the project issue skill. Added explicit wrapper precedence to prevent duplicate claims. Removed historical issue counts, retired-system specifics, fixed branches, personal memory paths, and unconditional sync/merge actions. The same Beads entry point was corroborated byte-for-byte in two other public repositories; the MIT-licensed MysteryMixClub copy is the canonical extraction source.

The bundled [MIT notice](LICENSE) retains copyright (c) 2026 Dawn Gabriel. No private repository contents, local infrastructure identities, or machine-specific inventory data are included.

## Concrete rule mapping

The default preference for the `bd` CLI, noninteractive updates instead of `bd edit`, atomic claims, and JSON parsing comes from the pinned generic Beads source above. Legacy-ID lookup through `external_ref`, numeric priorities, and distinguishing issue state from code branches come from **The migration**, **Non-negotiables**, and **Git/sync authority** in the pinned project issue skill. Target-required wrapper precedence is a library adaptation that follows the newer canonical Git router rather than duplicating an older manual-claim sequence.
