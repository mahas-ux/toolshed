# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ToolShed
def delete_tool(tool_id: int, confirm: bool = False) -> bool:
    """Delete a tool by ID with optional confirmation flag.
    
    Args:
        tool_id: The ID of the tool to delete.
        confirm: If True, the user must confirm the deletion.
    
    Returns:
        True if the tool was successfully deleted, False otherwise.
    
    Raises:
        ValueError: If the tool does not exist.
        RuntimeError: If confirmation is required but not provided.
    """
    if not confirm:
        confirm = input("Are you sure you want to delete this tool? (y/n): ").strip().lower()
    if confirm != 'y':
        raise RuntimeError("Deletion cancelled by user.")
    for tool in tools:
        if tool['id'] == tool_id:
            tools.remove(tool)
            print(f"Tool '{tool['name']}' has been deleted.")
            return True
    raise ValueError(f"No tool found with ID {tool_id}.")
