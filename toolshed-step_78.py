# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ToolShed
def split_tool_id(raw):
    parts = str(raw).strip().split()
    if not parts:
        return "", ""
    return parts[0], " ".join(parts[1:])


def parse_due_date(text):
    if not text:
        return None
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


def is_overdue(due_date, today=None):
    if due_date is None:
        return False
    return due_date < (today or date.today())


def summarize_tool(tool, loans=None):
    loans = loans or []
    active = sum(1 for loan in loans if not loan["returned"])
    total_time = sum(loan["days"] for loan in loans)
    return {
        "id": tool["id"],
        "name": tool["name"],
        "location": tool["location"],
        "active_loans": active,
        "total_borrowed_days": total_time,
    }
