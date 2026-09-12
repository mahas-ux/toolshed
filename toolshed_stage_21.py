# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ToolShed
def archive_complete_records(db_path, days_old=365):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, updated_at FROM records WHERE status = 'completed'")
    rows = cur.fetchall()
    archived = []
    for rid, updated_at in rows:
        if updated_at:
            age_days = (datetime.now().timestamp() - datetime.fromisoformat(updated_at).timestamp()).days
            if age_days > days_old:
                archived.append(rid)
    if archived:
        cur.execute("UPDATE records SET status = 'archived' WHERE id IN ({})".format(','.join('?' * len(archived))), archived)
        conn.commit()
    return len(archived)
