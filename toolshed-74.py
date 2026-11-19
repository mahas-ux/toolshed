# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ToolShed
def compare_snapshots(before, after, keys):
    before_map = {item['id']: item for item in before}
    after_map = {item['id']: item for item in after}
    changes = []
    for item_id in keys:
        old = before_map.get(item_id)
        new = after_map.get(item_id)
        if old is None and new is not None:
            changes.append({'id': item_id, 'status': 'added', 'value': new})
        elif old is not None and new is None:
            changes.append({'id': item_id, 'status': 'removed', 'value': old})
        else:
            diff = {key: old[key] for key in keys if old[key] != new[key]}
            if diff:
                changes.append({'id': item_id, 'status': 'changed', 'old': old, 'new': new, 'diff': diff})
    return changes
