# === Stage 66: Add export of a short status dashboard ===
# Project: ToolShed
def export_status_dashboard(tools, loans, maintenance, locations):
    total = len(tools)
    borrowed = len(loans)
    on_hand = total - borrowed
    needs_service = sum(1 for t in tools if t.get('last_service') and
                        (now := __import__('time').time() - t['last_service']) > 365)
    print("TOOLSHED STATUS DASHBOARD")
    print("Total tools:", total)
    print("On hand:", on_hand, "| Borrowed:", borrowed)
    print("Needs service:", needs_service)
    for loc in sorted(locations, key=lambda x: x['name']):
        count = sum(1 for t in tools if t.get('location') == loc['name'])
        print(f"  {loc['name']}: {count}")
    print("  (365-day service window)")
