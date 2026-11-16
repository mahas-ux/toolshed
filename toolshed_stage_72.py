# === Stage 72: Add Markdown report export ===
# Project: ToolShed
def export_markdown(tools, loans, maintenance, locations):
    lines = ["# ToolShed Report", ""]
    lines.append("## Locations")
    for loc in locations:
        lines.append(f"- {loc['name']} ({loc['address']})")
    lines.append("")
    lines.append("## Tools")
    for t in tools:
        lines.append(f"- {t['name']} - {t['category']}")
    lines.append("")
    lines.append("## Active Loans")
    for l in loans:
        lines.append(f"- {l['tool']} -> {l['borrower']} (due {l['due_date']})")
    lines.append("")
    lines.append("## Maintenance Log")
    for m in maintenance:
        lines.append(f"- {m['tool']} - {m['task']} ({m['date']})")
    with open("toolshed_report.md", "w") as f:
        f.write("\n".join(lines) + "\n")
