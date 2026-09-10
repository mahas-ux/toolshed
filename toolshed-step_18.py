# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ToolShed
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, item_name=None, user=None, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now()
        entry = {
            "timestamp": timestamp,
            "action": action,
            "item_name": item_name,
            "user": user,
        }
        self.entries.append(entry)
        return entry

    def get_last(self, n=1):
        return self.entries[-n:] if self.entries else []

    def get_by_action(self, action):
        return [e for e in self.entries if e["action"] == action]

    def get_by_user(self, user):
        return [e for e in self.entries if e["user"] == user]

    def __len__(self):
        return len(self.entries)
