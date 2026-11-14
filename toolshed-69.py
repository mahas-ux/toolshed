# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ToolShed
def reset_demo_data():
    tools = [
        {"id": 1, "name": "Cordless Drill", "category": "power", "condition": "good", "location": "garage"},
        {"id": 2, "name": "Ladder", "category": "safety", "condition": "fair", "location": "shed"},
        {"id": 3, "name": "Pressure Washer", "category": "cleaning", "condition": "new", "location": "garage"},
    ]
    locations = [
        {"id": 1, "name": "garage", "address": "123 Main St"},
        {"id": 2, "name": "shed", "address": "123 Main St"},
    ]
    loans = [
        {"id": 1, "tool_id": 1, "borrower": "Alice", "borrow_date": "2024-01-01", "due_date": "2024-01-15"},
    ]
    maintenance = [
        {"id": 1, "tool_id": 1, "date": "2024-01-01", "description": "Battery replacement"},
    ]
    return tools, locations, loans, maintenance
