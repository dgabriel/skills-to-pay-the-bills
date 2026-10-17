# Review

[P1] Unauthorized cancellation mutates the booking — after.py:4–6.

Line 4 sets status to `cancelled` before line 5 checks ownership. For a booking owned by Alice with status `accepted`, calling `cancel(booking, "Bob")` returns `forbidden` at line 6 but leaves status `cancelled`. This violates both the owner-only cancellation rule and the explicit requirement that rejected cancellations preserve state (requirements.md:1). The previous ordering checked ownership before mutation (before.py:4–6).

Move the mutation after successful ownership validation. Extend the unauthorized-caller regression test to assert that the entire booking remains unchanged, in addition to the returned status. The supplied test (test_cancel.py:1–2) checks only the return value and misses this regression.

The missing-booking path still returns `not_found` before mutation (after.py:2–3). Authorized cancellation still returns `ok` with cancelled status. This was a static review; no code was edited and no tests were executed.
