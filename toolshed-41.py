# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ToolShed
def import_lines(filepath):
    """Read a plain text file line by line and return a list of stripped strings."""
    with open(filepath, 'r', encoding='utf-8') as fh:
        return [line.strip() for line in fh if line.strip()]
