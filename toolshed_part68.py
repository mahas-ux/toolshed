# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ToolShed
def generate_changelog(activity_log, max_entries=10):
    """
    ToolShed: compact changelog generated from the activity log.
    Collapses consecutive entries sharing the same action type into
    a single line with a count, preserving chronological order.
    """
    if not activity_log:
        return "No activity recorded."

    entries = []
    current = None
    count = 0

    for record in activity_log:
        action = record.get("action", "unknown")
        if action == current:
            count += 1
        else:
            if current is not None:
                entries.append((current, count))
            current = action
            count = 1

    if current is not None:
        entries.append((current, count))

    lines = []
    for action, count in entries[:max_entries]:
        verb = "Recorded" if count == 1 else "Recorded {} times".format(count)
        lines.append("{}: {}".format(verb, action))

    if len(entries) > max_entries:
        lines.append("... and {} more actions".format(len(entries) - max_entries))

    return "\n".join(lines)
