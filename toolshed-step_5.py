# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ToolShed
def update_record(self, record_id, **kwargs):
    """Update an existing record by id; raise ValueError if not found."""
    record = self._get(record_id)
    if record is None:
        raise ValueError(f"Record {record_id} not found")
    for field, value in kwargs.items():
        if field not in record:
            raise ValueError(f"Unknown field {field}")
        record[field] = value
    self._save(record)
    return record

def remove_record(self, record_id):
    """Remove a record by id; raise ValueError if not found."""
    record = self._get(record_id)
    if record is None:
        raise ValueError(f"Record {record_id} not found")
    self._remove(record)
    return record
