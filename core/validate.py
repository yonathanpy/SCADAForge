LIMITS = {
    "temperature": (0, 1200),
    "pressure": (0, 500),
    "flow": (0, 10000)
}

def check(record):
    issues = []
    for k, (low, high) in LIMITS.items():
        v = record.get(k)
        if v is None:
            continue
        if not (low <= v <= high):
            issues.append(f"{k}:{v}")
    return issues
