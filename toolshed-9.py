# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ToolShed
import operator

def sort_items(items, key=None, reverse=False):
    """Sort a list of dict-like items by a chosen key.
    Supported keys: 'title', 'date', 'priority', 'last_update'.
    """
    if key is None:
        key = 'title'

    def _key_func(item):
        v = item.get(key, '')
        if key in ('priority',):
            return (0 if v == 'high' else 1, 0 if v == 'medium' else 1, 0 if v == 'low' else 2)
        if key in ('date', 'last_update'):
            return (0, v or '')
        return (0, v or '')

    return sorted(items, key=_key_func, reverse=reverse)
