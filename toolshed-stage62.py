# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ToolShed
def recommend_next_maintenance(tools, maintenance_log, due_days=30):
    candidates = []
    for tool in tools:
        if tool.get('maintenance_due') is None:
            continue
        days_left = tool['maintenance_due'] - datetime.now().date()
        if days_left <= due_days:
            priority = 1 if days_left <= 0 else 2
            candidates.append((priority, days_left, tool['name']))
    candidates.sort()
    return [name for _, _, name in candidates[:5]]
