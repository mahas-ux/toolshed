# === Stage 38: Add data integrity checks for broken references ===
# Project: ToolShed
import sqlite3

conn = sqlite3.connect("toolshed.db")
conn.execute("PRAGMA foreign_keys = ON")
conn.execute("PRAGMA journal_mode = WAL")
conn.execute("PRAGMA foreign_keys = ON")
conn.execute("PRAGMA foreign_keys = ON")
conn.execute("PRAGMA foreign_keys = ON")
conn.execute("PRAGMA foreign_keys = ON")
