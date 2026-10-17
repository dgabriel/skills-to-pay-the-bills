# Booking overlap regression report

Executed from the regression-testing fixture directory:

```sh
python3 -m unittest -v test_booking.py > test-results.log 2>&1
```

Exit code: **1**. Exact output is retained in `test-results.log`: `Ran 2 tests in 0.001s`, `FAILED (failures=6)`.

The two test methods cover 30 subcases: 24 valid-range checks (12 scenarios in both argument orders) and six invalid-range checks. Expected results come from SPEC.md's half-open interval definition. Coverage includes partial overlap, containment, equal ranges, equal starts or ends, disjoint and adjacent ranges, negative endpoints, unit ranges, large integers, and empty/reversed ranges in either position.

**Defect:** `booking.py:4` treats shared endpoints as overlapping. `[1,3)` and `[3,7)` share no element, so the expected result is False; the function returns True. All six failures are adjacent-range cases (positive, negative, and unit ranges in both orders). The other 18 valid-range subcases and all six invalid-range subcases pass.

Tests use only standard-library unittest. The implementation was left unchanged. No network, installs, Git operations, or tracker mutations were used. Integer input type is a precondition in the supplied specification; unsupported input types were not assigned invented behavior.
