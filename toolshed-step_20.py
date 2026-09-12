# === Stage 20: Add duplicate detection for newly created records ===
# Project: ToolShed
def check_duplicates(self, record: dict) -> str:
        """Return a unique suffix for a record whose primary key already exists."""
        base = f"{record['name']}-{record['location']}-{record['owner']}"
        seen = {r['id']: r for r in self.records}
        for i in range(1, 1000):
            candidate = f"{base}-{i}"
            if candidate not in seen.values():
                return candidate
        return f"{base}-{len(self.records)+1}"
