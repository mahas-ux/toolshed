# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ToolShed
from datetime import date, timedelta

# Demo: simulate a typical workflow
items = [
    {"id": "T001", "name": "Angle Grinder", "category": "Power"},
    {"id": "T002", "name": "Ladder", "category": "Access"},
    {"id": "T003", "name": "Wrench Set", "category": "Hand"},
]
for i, item in enumerate(items):
    item["last_maintenance"] = date.today() - timedelta(days=i * 30)

loans = [
    {"id": "L001", "item_id": "T001", "borrower": "Alice", "borrowed": date.today() - timedelta(days=5)},
    {"id": "L002", "item_id": "T002", "borrower": "Bob", "borrowed": date.today() - timedelta(days=12)},
]

locations = {"Garage": ["T001", "T002"], "Workshop": ["T003"]}

# Simulate a maintenance check
print("=== ToolShed Demo ===")
print(f"Tracked items: {len(items)}")
print(f"Active loans: {len(loans)}")
print(f"Locations: {list(locations.keys())}")
for loan in loans:
    print(f"  Loan {loan['id']}: {loan['item_id']} -> {loan['borrower']}")
