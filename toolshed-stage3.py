# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ToolShed
def validate_id(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("ID must be a positive integer")

def validate_short_text(value, max_len=100):
    if not isinstance(value, str) or len(value) > max_len:
        raise ValueError(f"Text must be a string of at most {max_len} characters")

def validate_email(value):
    if not isinstance(value, str) or "@" not in value or "." not in value:
        raise ValueError("Invalid email format")

def validate_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise ValueError("Date must be in YYYY-MM-DD format")

def validate_bool(value):
    if value not in (True, False):
        raise ValueError("Must be a boolean")
