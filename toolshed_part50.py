# === Stage 50: Add unit tests for import and export behavior ===
# Project: ToolShed
import json
from pathlib import Path


def test_import_export_roundtrip(tmp_path: Path) -> None:
    from toolshed.models import Tool, ToolState

    tool = Tool(
        name="Drill",
        state=ToolState.LOANED,
        location="Garage",
        loanee="Alice",
        loan_date="2026-01-10",
        maintenance_history=[
            {"date": "2025-06", "note": "replaced battery", "status": "ok"},
        ],
    )

    data = tool.to_dict()
    restored = Tool.from_dict(data)

    assert restored.name == tool.name
    assert restored.state == tool.state
    assert restored.location == tool.location
    assert restored.loanee == tool.loanee
    assert restored.loan_date == tool.loan_date
    assert restored.maintenance_history == tool.maintenance_history

    json_str = json.dumps(data)
    parsed = json.loads(json_str)
    assert parsed["name"] == "Drill"
    assert parsed["state"] == "LOANED"
