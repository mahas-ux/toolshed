# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ToolShed
def search(self, query: str):
        query = query.strip().lower()
        if not query:
            return self._items
        results = []
        for item in self._items:
            fields = [
                item.get("name", "").lower(),
                item.get("category", "").lower(),
                item.get("location", "").lower(),
                item.get("tags", "").lower(),
                str(item.get("last_used", "")).lower(),
                str(item.get("notes", "")).lower(),
            ]
            if any(query in f for f in fields):
                results.append(item)
        return results
