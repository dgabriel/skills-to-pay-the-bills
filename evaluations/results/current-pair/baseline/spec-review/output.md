# Cancellation patch review

## [P1] Reject unauthorized cancellation before mutating the booking

**Location:** `after.py:4` (authorization check at lines 5–6).

The requirements say only the owner may cancel and rejected cancellations must not mutate state (`requirements.md:1`). The patch assigns `booking.status = "cancelled"` at line 4 before checking ownership at line 5. For a booking owned by `owner`, initially `status = "confirmed"`, a call with actor `someone-else` returns `"forbidden"` at line 6 but leaves status `"cancelled"`. This is an unauthorized state change even though the response looks correct.

`before.py:4–6` rejects a non-owner before the mutation at line 6. Restore that ordering so authorization succeeds before changing status.

The existing test (`test_cancel.py:2`) checks only the returned status and therefore misses this regression. Add a test that snapshots a non-owner booking's state, invokes cancellation, asserts `"forbidden"`, and verifies state is unchanged. Also retain owner-success and missing-booking cases.

## Verification and limits

Static review of requirements.md, before.py, after.py, and test_cancel.py only; no behavioral test was executed for this review. The missing-booking branch remains before mutation (`after.py:2–3`), and an authorized owner still receives `"ok"` after status is set (`after.py:4–7`). No code was edited.
