# === Stage 36: Add templates for quickly creating common records ===
# Project: ToolShed
def quick_create_record(db_path, record_type, record_data):
    """Create a common record quickly without writing full SQL."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (record_type,))
    if not cursor.fetchone():
        raise ValueError(f"Table '{record_type}' does not exist.")
    cursor.execute(f"PRAGMA table_info({record_type})")
    columns = [col[1] for col in cursor.fetchall()]
    placeholders = ", ".join(["?"] * len(columns))
    col_names = ", ".join(columns)
    values = tuple(record_data.get(col, None) for col in columns)
    cursor.execute(f"INSERT INTO {record_type} ({col_names}) VALUES ({placeholders})", values)
    conn.commit()
    conn.close()
    return cursor.lastrowid
