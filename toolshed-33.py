# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ToolShed
SETTINGS = {
    "default_loan_days": 14,
    "maintenance_interval_days": 365,
    "currency": "USD",
    "language": "en",
    "theme": "light",
    "notifications": True,
}

def get_setting(key, default=None):
    return SETTINGS.get(key, default)

def set_setting(key, value):
    if key in SETTINGS:
        SETTINGS[key] = value
    else:
        raise KeyError(f"Unknown setting: {key}")

def reset_settings():
    SETTINGS.update({
        "default_loan_days": 14,
        "maintenance_interval_days": 365,
        "currency": "USD",
        "language": "en",
        "theme": "light",
        "notifications": True,
    })
