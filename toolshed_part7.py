# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ToolShed
def format_shed(s: dict) -> str:
    """Return a one-line formatted summary of a shed."""
    return (
        f"[{s['id']}] {s['name']} "
        f"({s['location']}, {s['status']}) "
        f"tools: {s['tools']} "
        f"maint: {s['maintenance']}"
    )

def format_shed_detail(s: dict) -> str:
    """Return a multi-line detailed view of a shed."""
    lines = [format_shed(s)]
    if s['tools']:
        lines.append("  Tools:")
        for t in s['tools']:
            lines.append(f"    - {t['name']} ({t['status']})")
    if s['maintenance']:
        lines.append("  Maintenance:")
        for m in s['maintenance']:
            lines.append(f"    - {m['date']} : {m['action']}")
    return "\n".join(lines)
