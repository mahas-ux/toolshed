# === Stage 40: Add plain text report export ===
# Project: ToolShed
def export_report(shed):
    """Export a plain-text report of the shed inventory."""
    lines = [f"ToolShed Report - {shed.name}\n"]
    for item in shed.items:
        lines.append(f"  - {item.name} ({item.category})")
    if shed.loans:
        lines.append(f"\nLoans:")
        for loan in shed.loans:
            lines.append(f"  - {loan.borrower} borrowed {loan.item_name} on {loan.date}")
    if shed.maintenance:
        lines.append(f"\nMaintenance:")
        for record in shed.maintenance:
            lines.append(f"  - {record.item_name}: {record.description} ({record.date})")
    if shed.locations:
        lines.append(f"\nLocations:")
        for loc in shed.locations:
            lines.append(f"  - {loc.name}: {loc.description}")
    return "\n".join(lines)
