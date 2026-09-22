# === Stage 46: Add a schema version field and migration helper ===
# Project: ToolShed
SCHEMA_VERSION = 2

def migrate_to_v2(db):
    """Upgrade the in-memory ToolShed database to schema version 2."""
    if db.get("_schema_version") != SCHEMA_VERSION:
        # Ensure every tool has a `maintenance` field (added in v2).
        for tool in db.get("tools", []):
            tool.setdefault("maintenance", {"notes": "", "last_service": ""})
        db["_schema_version"] = SCHEMA_VERSION
