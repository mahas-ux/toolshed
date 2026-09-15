# === Stage 27: Add monthly summary calculations ===
# Project: ToolShed
def monthly_summary(data):
    """Compute monthly summaries: loan counts, maintenance counts, unique locations per month."""
    monthly = {}
    for record in data:
        month = record.get("date", "")[:7]  # "YYYY-MM"
        if month not in monthly:
            monthly[month] = {
                "loan_count": 0,
                "maintenance_count": 0,
                "locations": set(),
            }
        if record.get("status") == "loaned_out":
            monthly[month]["loan_count"] += 1
        if record.get("type") == "maintenance":
            monthly[month]["maintenance_count"] += 1
        loc = record.get("location")
        if loc:
            monthly[month]["locations"].add(loc)
    return {k: v for k, v in sorted(monthly.items())}
