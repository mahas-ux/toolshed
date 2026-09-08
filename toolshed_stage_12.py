# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ToolShed
import json
from typing import Any, Dict

def load_json_friendly(path: str, default: Any = None) -> Any:
    """Load JSON from file with friendly error handling for malformed data."""
    if default is None:
        default = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ToolShed] File not found: {path}, using default.")
        return default
    except json.JSONDecodeError as e:
        print(f"[ToolShed] Malformed JSON in {path}: {e}")
        print("[ToolShed] Using default data instead.")
        return default
    except PermissionError:
        print(f"[ToolShed] Permission denied: {path}")
        return default
    except Exception as e:
        print(f"[ToolShed] Unexpected error reading {path}: {e}")
        return default
