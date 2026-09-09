# === Stage 14: Add file load support with fallback demo data ===
# Project: ToolShed
def load_demo_data():
    return {
        "tools": [
            {"id": 1, "name": "Hammer", "category": "hand tools", "condition": "good", "last_maintenance": "2024-01-15", "location": "shed"},
            {"id": 2, "name": "Drill", "category": "power tools", "condition": "fair", "last_maintenance": "2024-03-10", "location": "garage"},
            {"id": 3, "name": "Ladder", "category": "safety", "condition": "excellent", "last_maintenance": None, "location": "shed"}
        ],
        "loans": [
            {"id": 1, "tool_id": 1, "borrower": "Alice", "borrow_date": "2024-05-01", "due_date": "2024-05-15", "status": "active"},
            {"id": 2, "tool_id": 3, "borrower": "Bob", "borrow_date": "2024-04-20", "due_date": "2024-05-20", "status": "active"}
        ],
        "maintenance": [
            {"id": 1, "tool_id": 2, "date": "2024-03-10", "description": "Cleaned and oiled", "cost": 5.0},
            {"id": 2, "tool_id": 1, "date": "2024-01-15", "description": "Replaced handle grip", "cost": 3.5}
        ],
        "locations": [
            {"id": 1, "name": "Shed", "description": "Main outdoor storage", "capacity": 50},
            {"id": 2, "name": "Garage", "description": "Indoor workshop", "capacity": 30}
        ]
    }
