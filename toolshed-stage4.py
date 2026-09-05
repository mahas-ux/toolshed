# === Stage 4: Implement create operations for the primary records ===
# Project: ToolShed
def create_tool(tool_id, name, category, condition, location_id, notes=""):
    """Create a new tool record."""
    return {
        "id": tool_id,
        "name": name,
        "category": category,
        "condition": condition,
        "location_id": location_id,
        "notes": notes,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

def create_location(location_id, name, address, notes=""):
    """Create a new location record."""
    return {
        "id": location_id,
        "name": name,
        "address": address,
        "notes": notes,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

def create_loan(tool_id, borrower_name, borrower_email, loan_date, due_date, notes=""):
    """Create a new loan record."""
    return {
        "id": None,
        "tool_id": tool_id,
        "borrower_name": borrower_name,
        "borrower_email": borrower_email,
        "loan_date": loan_date,
        "due_date": due_date,
        "notes": notes,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

def create_maintenance(tool_id, date, description, cost, notes=""):
    """Create a new maintenance record."""
    return {
        "id": None,
        "tool_id": tool_id,
        "date": date,
        "description": description,
        "cost": cost,
        "notes": notes,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
