# === Stage 26: Add weekly summary calculations ===
# Project: ToolShed
def weekly_summary(records):
    """Compute a one-line weekly summary of loans and maintenance."""
    from collections import defaultdict
    weekly = defaultdict(int)
    for rec in records:
        week = rec.get("week", "unknown")
        weekly[week] += 1
    return dict(sorted(weekly.items()))
