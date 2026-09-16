# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ToolShed
def parse_date(s):
    """Parse a date string into a datetime.date object.
    Accepts formats: YYYY-MM-DD, DD/MM/YYYY, DD.MM.YYYY, or ISO 8601.
    Raises ValueError with a clear message on failure.
    """
    if not isinstance(s, str) or not s.strip():
        raise ValueError("Empty or non-string date input")
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d.%m.%Y", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Cannot parse date: '{s}'. Expected YYYY-MM-DD, DD/MM/YYYY, DD.MM.YYYY, or ISO 8601.")
