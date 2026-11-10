# === Stage 60: Add saved views for frequently used filters ===
# Project: ToolShed
SAVED_VIEWS = {}

def save_view(name, predicate):
    SAVED_VIEWS[name] = predicate

def load_view(name):
    return SAVED_VIEWS.get(name)

def has_view(name):
    return name in SAVED_VIEWS

def list_views():
    return list(SAVED_VIEWS.keys())

def tools_matching(view_name):
    predicate = load_view(view_name)
    if predicate is None:
        return []
    return [t for t in TOOLS if predicate(t)]

save_view("recently_loaned", lambda t: t["loaned_out"] is not None)
save_view("needs_service", lambda t: t["last_maintenance"] is None or (t["calibration_days"] or 0) >= t.get("service_interval", 365))
save_view("at_home", lambda t: t["location"] == "shed")
save_view("drills", lambda t: t["category"] == "drills")
