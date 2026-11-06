# === Stage 58: Add bulk update behavior for selected records ===
# Project: ToolShed
def bulk_update_records(records, field, values, selected_ids):
    """Apply a single field change across a set of selected records."""
    for record in records:
        if record.get("id") in selected_ids:
            record[field] = values
    return records

def bulk_update_multiple(records, updates, selected_ids):
    """Apply several field changes at once for the selected records."""
    for record in records:
        if record.get("id") in selected_ids:
            for field, value in updates.items():
                record[field] = value
    return records

def bulk_set_status(records, status, selected_ids):
    """Mark selected records with a given status."""
    for record in records:
        if record.get("id") in selected_ids:
            record["status"] = status
    return records

def bulk_add_maintenance(records, note, selected_ids):
    """Append a maintenance entry for each selected record."""
    for record in records:
        if record.get("id") in selected_ids:
            record.setdefault("maintenance", []).append(note)
    return records

def bulk_increment_hours(records, hours, selected_ids):
    """Add usage hours to selected records that already track hours."""
    for record in records:
        if record.get("id") in selected_ids:
            record.setdefault("hours_used", 0)
            record["hours_used"] += hours
    return records
