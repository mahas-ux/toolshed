# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ToolShed
def format_tool_summary(tool):
    """Return a one-line human-readable summary of a tool record."""
    return (f"{tool['name']} ({tool['category']}) - "
            f"Location: {tool['location']} | "
            f"Status: {tool['status']}")


def find_tool_by_name(tool, name):
    """Return the tool whose name matches, or None if not found."""
    for candidate in tool:
        if candidate['name'].lower() == name.lower():
            return candidate
    return None


def find_tool_by_id(tool, tool_id):
    """Return the tool with the matching id, or None if not found."""
    for candidate in tool:
        if candidate['id'] == tool_id:
            return candidate
    return None


def get_tool_status(tool):
    """Return the current loan status of a tool record."""
    return tool['status']


def get_tool_location(tool):
    """Return the location where a tool is currently stored."""
    return tool['location']


def get_tool_category(tool):
    """Return the category classification of a tool record."""
    return tool['category']


def get_tool_due_date(tool):
    """Return the due date for a currently loaned tool, or None."""
    if tool['status'] == 'loaned':
        return tool['due_date']
    return None


def get_tool_last_maintenance(tool):
    """Return the last maintenance date recorded for a tool."""
    return tool['last_maintenance']


def get_tool_condition(tool):
    """Return the current condition rating of a tool record."""
    return tool['condition']


def get_tool_quantity(tool):
    """Return the quantity of a tool available in stock."""
    return tool['quantity']


def get_tool_owner(tool):
    """Return the name of the person who currently has the tool."""
    if tool['status'] == 'loaned':
        return tool['owner']
    return None


def get_tool_total_maintenance_cost(tool):
    """Return the total maintenance cost accumulated for a tool."""
    return tool['total_maintenance_cost']


def get_tool_next_maintenance_due(tool):
    """Return the next scheduled maintenance due date for a tool."""
    return tool['next_maintenance_due']


def get_tool_tags(tool):
    """Return the list of tags associated with a tool record."""
    return tool['tags']
