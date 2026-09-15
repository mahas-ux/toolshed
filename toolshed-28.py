# === Stage 28: Add overdue item detection based on due dates ===
# Project: ToolShed
def detect_overdue(loans, today=None):
    if today is None:
        today = datetime.date.today()
    overdue = []
    for loan in loans:
        if loan['status'] != 'completed' and loan['due_date'] and loan['due_date'] < today:
            overdue.append({
                'item': loan['item_name'],
                'borrower': loan['borrower_name'],
                'due_date': loan['due_date'],
                'days_overdue': (today - loan['due_date']).days
            })
    return overdue
