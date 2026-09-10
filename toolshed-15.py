# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ToolShed
def handle_command(text, state):
    """Dispatch a user text command and return (new_state, response)."""
    text = text.strip().lower()
    if not text:
        return state, "Please type a command."

    commands = {
        "add item": lambda t: (state, "Add item: " + t),
        "list items": lambda t: (state, "Items: " + ", ".join(state.get("items", []))),
        "borrow": lambda t: (state, "Borrow: " + t),
        "return": lambda t: (state, "Return: " + t),
        "maintain": lambda t: (state, "Maintain: " + t),
        "locate": lambda t: (state, "Locate: " + t),
    }

    for cmd, handler in commands.items():
        if text.startswith(cmd):
            return handler(text[len(cmd):])

    return state, "Unknown command. Try: add item, list items, borrow, return, maintain, locate."
