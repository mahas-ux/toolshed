# === Stage 31: Add compact table rendering for long lists ===
# Project: ToolShed
class CompactTable:
    """Compact table renderer for long lists."""

    def __init__(self, columns, width=80):
        self.columns = columns
        self.width = width

    def render(self, data):
        """Render data as a compact table."""
        if not data:
            return ""

        # Calculate column widths
        col_widths = [len(str(col)) for col in self.columns]
        for row in data:
            for i, val in enumerate(row):
                if len(str(val)) > col_widths[i]:
                    col_widths[i] = len(str(val))

        # Render table
        lines = []
        # Header
        header = " | ".join(str(col).ljust(col_widths[i]) for i, col in enumerate(self.columns))
        lines.append(header)
        lines.append("-" * len(header))

        # Data rows
        for row in data:
            line = " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row))
            lines.append(line)

        return "\n".join(lines)
