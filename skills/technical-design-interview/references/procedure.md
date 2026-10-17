# Technical design procedure

## Defaults and overrides

The author's starting stack for a new web MVP is FastAPI routers, async SQLAlchemy on Postgres, Alembic migrations, pydantic-settings, env-driven feature flags, and React/TypeScript frontend. Prefer request/response, polling, and simple scheduled work before introducing queues or websockets. These are actual starting choices, not a menu left undecided. Preserve an existing Django/Hono/etc. project or a user-chosen stack; state the override. A requirement such as offline-only operation may justify another storage/runtime choice.

## Propose then confirm

Read the PRD/core journey and current technical design. If requirements are absent, clarify the core journey and constraints instead of inventing architecture. No installed PRD skill is required.

1. Data: propose entities, relationships, key fields, uniqueness, ownership, state transitions, and retention/deletion needs. Distinguish user data from derived data. Explain how transactional invariants will hold under concurrent requests.
2. Access: propose the simplest suitable sign-in method; identify roles, public surfaces, ownership boundaries, and enforcement points.
3. Interfaces: map MVP features to resources/operations and existing API conventions. Separate load-bearing integrations from optional enhancements and describe absent-service/error fallbacks. Justify asynchronous processing with a named requirement.
4. Operations: deployment constraints, honest scale, backup/data-loss tolerance, downtime expectations, and the first likely limit at 10× scale. Keep unresolved provider choice explicit; a small MVP does not imply enterprise infrastructure.

## Deliver

Default destination `docs/technical/technical-design.md`; preserve existing structure. Cover overview, architecture, data/invariants, APIs, auth, configuration, operations, testing, decisions with rejected alternatives, simplifications, limits, and questions. Describe needed config keys without values/secrets. For the default stack, plan Alembic migration verification (upgrade → downgrade → upgrade where reversibility is supported); for other stacks use their actual migration tooling. Design changes alone do not run migrations or alter the environment.

Name acceptance checks for the core journey and invariants, and link components to requirements. Review consistency across data ownership, interfaces, failures, tests, and budget. A draft makes proposed choices clear without claiming acceptance. Handoff includes design/requirements paths, accepted versus proposed decisions, gaps, and implementation prerequisites. In chat-only use, output inline.
