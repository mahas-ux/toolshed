# === Stage 64: Add validation for relationship references ===
# Project: ToolShed
def validate_references(model, record, data):
    if isinstance(data, dict):
        for field, value in data.items():
            if field in model._VALIDATORS and model._VALIDATORS[field]:
                model._VALIDATORS[field](record, value)
            elif field in ("location", "borrower"):
                if value is not None and value not in model._ALL:
                    raise ValueError(f"{field} '{value}' not found")
            elif field in ("maintenance_log",) and isinstance(value, list):
                for entry in value:
                    if entry.get("tool") is not None and entry["tool"] not in model._ALL:
                        raise ValueError(f"maintenance_log references unknown tool")
    return True
