# === Stage 42: Add CSV export without external dependencies ===
# Project: ToolShed
import csv
from datetime import datetime

def export_tools_csv(tools, filename="tools_export.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Location", "Loan Date", "Due Date", "Condition", "Last Maintenance", "Notes"])
        for tool in tools:
            writer.writerow([
                tool["name"],
                tool.get("location", ""),
                tool.get("loan_date", ""),
                tool.get("due_date", ""),
                tool.get("condition", ""),
                tool.get("last_maintenance", ""),
                tool.get("notes", ""),
            ])
        print(f"Exported {len(tools)} tools to {filename}")
