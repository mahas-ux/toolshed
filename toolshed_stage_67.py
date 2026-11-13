# === Stage 67: Add a function that returns key project metrics ===
# Project: ToolShed
def get_project_metrics(tools, loans, maintenance_records, locations):
    total_tools = len(tools)
    active_loans = sum(1 for loan in loans if loan['status'] == 'borrowed')
    completed_maintenance = sum(1 for record in maintenance_records if record['completed'])
    overdue_loans = sum(1 for loan in loans if loan['status'] == 'borrowed' and loan['due_date'] < str(datetime.date.today()))
    locations_count = len(locations)
    return {'total_tools': total_tools, 'active_loans': active_loans, 'completed_maintenance': completed_maintenance, 'overdue_loans': overdue_loans, 'locations_count': locations_count}
