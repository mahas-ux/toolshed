# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ToolShed
import pytest
from toolshed.models.item import Item
from toolshed.models.location import Location
from toolshed.models.maintenance import MaintenanceRecord
from toolshed.services.search import SearchService


@pytest.fixture
def search_svc():
    return SearchService()


@pytest.mark.parametrize("query,expected", [
    ("hammer", True),
    ("drill", True),
    ("phone", False),
    ("", True),
])
def test_search_items_by_name(search_svc, query, expected):
    items = [
        Item(name="Hammer", status="active"),
        Item(name="Drill", status="active"),
        Item(name="Phone", status="active"),
    ]
    results = search_svc.search_items(items, query)
    assert len(results) == (1 if query else 3)
    if query:
        assert results[0].name == "Hammer" if query == "hammer" else "Drill"


@pytest.mark.parametrize("status,expected", [
    ("active", 2),
    ("broken", 1),
    ("active", 2),
])
def test_search_items_by_status(search_svc, status, expected):
    items = [
        Item(name="Hammer", status="active"),
        Item(name="Drill", status="broken"),
        Item(name="Phone", status="active"),
    ]
    results = search_svc.search_items(items, status=status)
    assert len(results) == expected
