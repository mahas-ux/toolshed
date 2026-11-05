# === Stage 57: Add structured result objects for command handlers ===
# Project: ToolShed
class ShedResult:
    def __init__(self, success=True, data=None, error=None, message=None):
        self.success = success
        self.data = data
        self.error = error
        self.message = message

    def serialize(self):
        out = {"success": self.success}
        if self.data is not None:
            out["data"] = self.data
        if self.error is not None:
            out["error"] = self.error
        if self.message is not None:
            out["message"] = self.message
        return out


def ok(data=None, message=None):
    return ShedResult(success=True, data=data, message=message)


def fail(error=None, message=None):
    return ShedResult(success=False, error=error, message=message)


def find_one(collection, query):
    for item in collection:
        if all(item.get(k) == v for k, v in query.items()):
            return ShedResult(success=True, data=item)
    return ShedResult(success=False, error="not_found", message="No matching record found.")


def find_all(collection):
    return ShedResult(success=True, data=list(collection))
