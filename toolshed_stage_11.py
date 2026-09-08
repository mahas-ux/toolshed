# === Stage 11: Add JSON export for the current application state ===
# Project: ToolShed
def export_state():
    """Export the current ToolShed state to a JSON file."""
    import json
    import os
    state = {
        "tools": tools,
        "loans": loans,
        "maintenance": maintenance,
        "locations": locations,
        "settings": settings,
    }
    filename = "toolshed_state.json"
    with open(filename, "w") as f:
        json.dump(state, f, indent=2)
    print(f"State exported to {filename}")
