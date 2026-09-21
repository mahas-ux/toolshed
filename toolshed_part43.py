# === Stage 43: Add CSV import for the primary record type ===
# Project: ToolShed
def import_tools_from_csv(filepath):
    """Import Tool records from a CSV file.
    
    CSV must have columns: name, category, location, condition, last_maintenance, notes
    Returns list of imported Tool dicts.
    """
    import csv
    tools = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tool = {
                'name': row['name'].strip(),
                'category': row.get('category', 'Other').strip(),
                'location': row.get('location', '').strip(),
                'condition': row.get('condition', 'good').strip(),
                'last_maintenance': row.get('last_maintenance', '').strip(),
                'notes': row.get('notes', '').strip(),
            }
            if tool['name']:
                tools.append(tool)
    return tools
