# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ToolShed
import random
from datetime import date, timedelta

ITEMS = [
    {"id": 1, "name": "Circular Saw", "category": "power", "status": "available"},
    {"id": 2, "name": "Ladder", "category": "manual", "status": "borrowed"},
    {"id": 3, "name": "Drill Set", "category": "power", "status": "maintenance"},
    {"id": 4, "name": "Hammer", "category": "manual", "status": "available"},
    {"id": 5, "name": "Pressure Washer", "category": "power", "status": "available"},
]

LOCATIONS = ["Garage", "Basement", "Patio", "Workshop", "Storage Room"]
MAINTENANCE_LOG = [
    {"item_id": 3, "date": date(2023, 5, 15), "notes": "Replaced bit, cleaned chuck"},
    {"item_id": 1, "date": date(2024, 1, 10), "notes": "Sharpened blade, oiled motor"},
]
