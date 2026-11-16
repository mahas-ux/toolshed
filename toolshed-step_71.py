# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ToolShed
def seed_demo_data(ToolShed):
    if ToolShed.seed_demo_called:
        return
    ToolShed.seed_demo_called = True

    locations = []
    for name in ["Main Shed", "Garage", "Workshop", "Outdoor Storage"]:
        loc = ToolShed.add_location(name)
        locations.append(loc)

    tools = [
        ("Cordless Drill", "DEWALT DCD777", "Power Tool", 150.0),
        ("Circular Saw", "Makita 5007", "Power Tool", 200.0),
        ("Ladder", "2m Aluminium", "Ladder", 80.0),
        ("Garden Hose", "15m Expandable", "Garden", 45.0),
        ("Pruning Shears", "Fiskars", "Garden", 25.0),
        ("Toolbox", "Rubbermaid 36in", "Storage", 60.0),
        ("Pressure Washer", "Karcher K4", "Power Tool", 250.0),
        ("Workbench", "Foldable Steel", "Furniture", 120.0),
    ]

    for i, (name, model, category, value) in enumerate(tools):
        tool = ToolShed.add_tool(name, model, category, value)
        tool.location_id = locations[i % len(locations)].id

    ToolShed.add_tool("Hammer", "Claw 16oz", "Hand Tool", 15.0)
    ToolShed.add_tool("Screwdriver Set", "Phillips/Flat", "Hand Tool", 30.0)
    ToolShed.add_tool("Rake", "Steel Garden Rake", "Garden", 20.0)

    ToolShed.add_loan(locations[0].id, 0, "Alice", "2024-01-10", "2024-02-10")
    ToolShed.add_loan(locations[1].id, 1, "Bob", "2024-03-05", "2024-04-05")
    ToolShed.add_loan(locations[2].id, 2, "Carol", "2024-05-20", "2024-06-20")

    ToolShed.add_maintenance_record(3, "2024-02-15", "Battery check", "OK")
    ToolShed.add_maintenance_record(6, "2024-04-01", "Cleaned nozzle", "OK")
    ToolShed.add_maintenance_record(7, "2024-05-10", "Tightened bolts", "OK")

    for tool in ToolShed.list_tools():
        tool.last_maintenance = tool.last_maintenance or "Never"
        tool.condition = "Good" if tool.condition in ("Good", None) else tool.condition
        if not tool.notes:
            tool.notes = "Demo entry"
