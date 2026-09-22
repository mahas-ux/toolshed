# === Stage 44: Add backup creation for the data file ===
# Project: ToolShed
def create_backup(db_path):
    """Create a timestamped backup of the SQLite database."""
    import shutil
    import os
    backup_dir = os.path.join(os.path.dirname(db_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"toolshed_{timestamp}.db")
    shutil.copy2(db_path, backup_path)
    return backup_path
