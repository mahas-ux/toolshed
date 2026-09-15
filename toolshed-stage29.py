# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ToolShed
def upcoming_items(items, days_ahead=7):
    """Return items whose next_due is within `days_ahead` days from today."""
    from datetime import datetime, timedelta
    today = datetime.now().date()
    cutoff = today + timedelta(days=days_ahead)
    return [
        it for it in items
        if it.get("next_due") and it["next_due"] <= cutoff
    ]

def overdue_items(items):
    """Return items whose next_due is before today."""
    from datetime import datetime
    today = datetime.now().date()
    return [
        it for it in items
        if it.get("next_due") and it["next_due"] < today
    ]

def next_reminders(items, days_ahead=7):
    """Return sorted list of next_due dates for items due within `days_ahead` days."""
    from datetime import datetime, timedelta
    today = datetime.now().date()
    cutoff = today + timedelta(days=days_ahead)
    dates = []
    for it in items:
        nd = it.get("next_due")
        if nd and nd <= cutoff:
            dates.append((nd, it["name"]))
    dates.sort(key=lambda x: x[0])
    return dates
