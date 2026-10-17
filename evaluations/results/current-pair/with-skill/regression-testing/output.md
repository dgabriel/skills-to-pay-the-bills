# Result: FAIL

Authored `test_booking.py` using only standard-library `unittest`, with literal expectations independently derived from `SPEC.md:1`. No implementation changes were made.

Command, from this directory: `python3 -m unittest -v test_booking.py > test-results.log 2>&1`. Exit code: 1. Runner emitted **3 tests**, with **2 failing subtests**, both in `OverlapTests.test_half_open_boundary_below_on_above` at `test_booking.py:28`.

- `overlaps(0, 3, 3, 6)`: expected `False`, actual `True`.
- `overlaps(3, 6, 0, 3)`: expected `False`, actual `True`.

Both raise `AssertionError: True is not False`. `booking.py:4` treats shared endpoints as overlap, violating the explicit rule that adjacent half-open ranges do not overlap. Full failure evidence is preserved in `test-results.log`; these are assertion failures, not environment or collection failures.

Coverage includes containment, identical ranges, partial overlap in both orders, negative integers, disjoint ranges, below/on/above the end boundary in both orders, equal endpoints, reversed endpoints in either range, and both ranges invalid. The ordinary overlap/disjoint method and invalid-range method passed. Successful results are checked as actual booleans; invalid ranges must raise `ValueError`.

Request validation is represented by start/end ordering checks. HTTP response shape and status codes are inapplicable: this fixture exposes a pure Python function, with no endpoint or HTTP layer. Error handling is checked through `ValueError`. Rejected-mutation state assertions are inapplicable because the function accepts immutable integer arguments and has no supplied mutable state. Non-integer behavior is unspecified and was not invented. No external domain oracle is needed because the supplied definition determines these outcomes.

No wider suite/configuration was supplied; broader integration checks were not run. No network, installations, or Git/tracker operations were used. Handoff: implementation owner receives the reproducible adjacent-range failures; retain these expectations for subsequent validation. No unresolved spec decision is needed for these failures.
