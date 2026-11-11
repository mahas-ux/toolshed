# === Stage 63: Add relationships between records where useful ===
# Project: ToolShed
def link_records(tools, loans, maintenance, locations):
    for tool in tools:
        if 'location_id' not in tool:
            tool['location_id'] = next((loc['id'] for loc in locations if loc['name'] == tool.get('location_name')), None)
        if 'loaned_to_id' not in tool:
            tool['loaned_to_id'] = next((loan['user_id'] for loan in loans if loan['tool_id'] == tool['id']), None)
        if 'last_maintenance_id' not in tool:
            tool['last_maintenance_id'] = next((maint['id'] for maint in maintenance if maint['tool_id'] == tool['id']), None)
        for loan in loans:
            if loan['tool_id'] == tool['id'] and 'location_id' not in loan:
                loan['location_id'] = tool.get('location_id')
        for maint in maintenance:
            if maint['tool_id'] == tool['id'] and 'location_id' not in maint:
                maint['location_id'] = tool.get('location_id')
        for location in locations:
            if location['id'] == tool.get('location_id') and 'related_tool_ids' not in location:
                location['related_tool_ids'] = [tid for tid in [t['id'] for t in tools] if t.get('location_id') == location['id']]
