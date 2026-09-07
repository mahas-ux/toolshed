# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ToolShed
def filter_items(items, filters=None):
    """Filter shed items by status, category, owner, or tag."""
    if filters is None:
        return items
    result = items
    for key, value in filters.items():
        if value is not None:
            result = [item for item in result if item.get(key) == value]
    return result
