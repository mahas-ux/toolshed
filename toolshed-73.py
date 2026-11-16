# === Stage 73: Add a lightweight HTML report export ===
# Project: ToolShed
def export_html_report(tools, loans, maintenance, locations, filename="toolshed_report.html"):
    items = list(tools.values())
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><head><title>ToolShed Report</title>")
        f.write("<style>body{font-family:sans-serif}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px}</style></head><body>")
        f.write("<h1>ToolShed Report</h1>")
        f.write("<h2>Tools</h2><table><tr><th>ID</th><th>Name</th><th>Location</th><th>Condition</th></tr>")
        for t in items:
            f.write("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (t["id"], t["name"], t.get("location", "-"), t.get("condition", "-")))
        f.write("</table>")
        f.write("<h2>Loans</h2><table><tr><th>Tool</th><th>Borrower</th><th>Due</th></tr>")
        for l in loans:
            f.write("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (l.get("tool", "-"), l.get("borrower", "-"), l.get("due", "-")))
        f.write("</table>")
        f.write("<h2>Maintenance</h2><table><tr><th>Tool</th><th>Task</th><th>Date</th></tr>")
        for m in maintenance:
            f.write("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (m.get("tool", "-"), m.get("task", "-"), m.get("date", "-")))
        f.write("</table>")
        f.write("<h2>Locations</h2><table><tr><th>Name</th><th>Notes</th></tr>")
        for loc in locations:
            f.write("<tr><td>%s</td><td>%s</td></tr>" % (loc["name"], loc.get("notes", "-")))
        f.write("</table></body></html>")
    return filename
