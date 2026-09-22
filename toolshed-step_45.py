# === Stage 45: Add restore from backup with validation ===
# Project: ToolShed
import sqlite3

def restore_from_backup(db_path: str, backup_path: str, validate: bool = True) -> bool:
    """Restore the database from a backup file.

    Args:
        db_path: Path to the current database file.
        backup_path: Path to the backup SQLite file.
        validate: If True, verify the backup integrity before restoring.

    Returns:
        True if the restore was successful, False otherwise.
    """
    try:
        if validate:
            conn = sqlite3.connect(backup_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            if not tables:
                print("Backup file is empty or corrupted. Restore failed.")
                conn.close()
                return False
            conn.close()
            print("Backup validation passed.")
        conn = sqlite3.connect(db_path)
        conn.backup(backup_path)
        conn.close()
        print("Restore completed successfully.")
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False
