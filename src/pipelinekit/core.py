from collections.abc import Iterable, Mapping

def summarize(steps: Iterable[Mapping[str, object]]) -> dict[str, int]:
    """Count pipeline steps by status."""
    result: dict[str, int] = {}
    for step in steps:
        status = str(step.get("status", "unknown")).strip().lower() or "unknown"
        result[status] = result.get(status, 0) + 1
    return dict(sorted(result.items()))
