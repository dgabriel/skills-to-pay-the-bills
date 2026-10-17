# Local device testing handoff

## Keep the tested branch and data

Read the target run instructions and startup scripts, then confirm branch/revision. A script called “dev” may switch to an integration branch, apply migrations, rebuild dependencies, or reset data. If it switches branches, use a supported branch-preserving mode or a documented equivalent; do not run it blindly and then claim to be testing the feature. Record the actual running revision where possible.

Reuse project service names, ports, environment configuration, and test account conventions as overlays. Start required dependencies, wait for health/readiness, and start/update the app. Separate “process started,” “HTTP ready,” and “owner-device reachable.” Read logs when readiness fails; do not present a crash loop as a ready handoff. Prefer the existing stable Docker or equivalent runtime when repeated server crashes justify it, rather than replatforming without need. Update in place and preserve persistent data, account state, and unrelated services. Never delete volumes or reset the database as routine setup.

## LAN access is more than the bind flag

When phone/tablet access is requested, discover the actual local interface address, web port, and supported listen option. Bind appropriately for that local network, using the project’s option equivalent to `--host` where available. Do not publish a public tunnel or change staging/production as a substitute. Avoid a universal hard-coded port or address. Inspect client API base URLs, API binding, allowed hosts/CORS, auth cookies, and secure-context requirements so the frontend does not load while all API calls still target the desktop’s loopback interface.

Give the exact discovered URL in the handoff after readiness checks. A successful request from the development machine does not prove reachability from the owner’s device: ask for a device check or label that step unverified if no such device is available. If local secure-context/cookie/network restrictions block the feature, explain the concrete limitation and use a project-supported local solution within scope. Do not weaken auth or expose admin endpoints simply to clear a checklist.

## Persistent test identity and checklist

Reuse an existing dev account or idempotent dev-only seed so the owner need not recreate it after each change. Confirm the target is local development before sharing any dev-only credential in chat; never copy credentials into committed docs, tests, or issue text. Never share staging/production credentials. Use placeholders in maintained instructions, and keep actual values in the existing local mechanism. Do not reset unrelated account data, send real invitations/email, or seed production by accident. If privileged seeding is outside current authority, report the exact pending setup rather than invent credentials.

End with a short handoff: running branch/revision; exact local device URL; dev account access via the agreed local channel; readiness checks actually run; any unverified device/browser path; and a checklist the owner can answer pass/fail per item. Cover the changed journey, one important failure/edge path, and relevant mobile layout/input behavior without turning it into a broad QA campaign. State how the runtime stays available and how to update/stop it without losing data. Record owner feedback as follow-up work when authorized; owner testing does not automatically authorize merge.
