# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ToolShed
def generate_validation_report(items, loans, maintenance, locations):
    warnings = []
    errors = []

    for item in items:
        if not item.get('name'):
            errors.append(f"Item missing name: {item}")
        if not item.get('category'):
            warnings.append(f"Item has no category: {item.get('name')}")
        if item.get('location') not in locations:
            warnings.append(f"Item '{item.get('name')}' at unknown location: {item.get('location')}")
        if item.get('quantity', 0) < 0:
            errors.append(f"Item '{item.get('name')}' has negative quantity: {item.get('quantity')}")

    for loan in loans:
        if not loan.get('item_id'):
            errors.append(f"Loan missing item_id: {loan}")
        if loan.get('due_date') and loan['due_date'] < loan.get('loan_date', ''):
            errors.append(f"Loan for item {loan.get('item_id')} has past due date")
        if loan.get('status') not in ('active', 'returned'):
            warnings.append(f"Loan for item {loan.get('item_id')} has unknown status: {loan.get('status')}")

    for record in maintenance:
        if not record.get('item_id'):
            errors.append(f"Maintenance record missing item_id: {record}")
        if record.get('cost') is not None and record['cost'] < 0:
            errors.append(f"Maintenance for item {record.get('item_id')} has negative cost")

    return warnings, errors
