# Provenance: Local Test Handoff

## Public sources

- [.agents/skills/run-mysterymixclub/SKILL.md](https://github.com/dgabriel/MysteryMixClub/blob/3b406c4630e9c857495ebfdfdae76b5b79a70b71/.agents/skills/run-mysterymixclub/SKILL.md) at `3b406c4630e9c857495ebfdfdae76b5b79a70b71`. Relevant sections: Setup + Build; Run; Gotchas; Troubleshooting. Repository visibility verified public and license verified MIT before reading; its license file was also fetched at this revision.

## Pattern evidence

Attribution: **author session history, paraphrased by reviewer, 2026-10-17**. No session transcripts were searched, read, quoted, or copied.

Reviewer estimate: about 12 sessions across three projects. Completed features are made runnable locally from the feature branch before merge. Phone/tablet testing needs LAN binding and the exact reachable URL. A persistent dev test account avoids repeated recreation; dev-only local access may be shared in chat, but staging/production credentials must never be shared. Repeated server crashes favor a stable runtime, in-place updates, and preserved data. Handoffs finish with short device pass/fail checklists.

## Adaptation and boundaries

The public run skill supplies branch-switch hazards, dependency/readiness checks, branch-preserving startup, and persistent-volume/migration troubleshooting. Pattern evidence adds the device/LAN handoff, persistent dev account, and stable-runtime preferences. Fixed service names, hostnames, ports, account values, machine-specific browser driver, and any “verified this session” claims are not copied. No local server or owner device is started merely by creating this package.

The package retains the author’s [MIT notice](LICENSE). Pattern counts are reviewer estimates, not an independently verified transcript audit.
