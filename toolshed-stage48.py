# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ToolShed
import pytest
from datetime import date

def test_create_item():
    from toolshed.models.item import Item
    item = Item(name="Hammer", category="hand_tools", owner="Alice", location="Shed A")
    assert item.name == "Hammer"
    assert item.owner == "Alice"
    assert item.location == "Shed A"
    assert item.status == "available"

def test_item_validation():
    from toolshed.models.item import Item
    with pytest.raises(ValueError):
        Item(name="", category="hand_tools", owner="Bob", location="Shed B")

def test_validate_date():
    from toolshed.utils.validation import validate_date
    valid = date(2024, 1, 15)
    assert validate_date(valid) is True
    invalid = date(2024, 2, 30)
    assert validate_date(invalid) is False
