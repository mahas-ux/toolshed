# === Stage 24: Add grouped summaries by category or status ===
# Project: ToolShed
def grouped_summary(items):
    """Return a compact grouped summary of items by category or status."""
    groups = {}
    for item in items:
        key = item.get('category', item.get('status', 'unknown'))
        if key not in groups:
            groups[key] = 0
        groups[key] += 1
    return groups
