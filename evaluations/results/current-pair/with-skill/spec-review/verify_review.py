from types import SimpleNamespace
import after
import before

for module in (before, after):
    booking = SimpleNamespace(owner_id="owner", status="confirmed")
    result = module.cancel(booking, "someone-else")
    print(f"{module.__name__}: unauthorized result={result!r}, status={booking.status!r}")
    assert result == "forbidden"
    owner_booking = SimpleNamespace(owner_id="owner", status="confirmed")
    assert module.cancel(owner_booking, "owner") == "ok"
    assert owner_booking.status == "cancelled"
    assert module.cancel(None, "owner") == "not_found"
assert booking.status == "confirmed", "Rejected cancellation mutated booking status"
