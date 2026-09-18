# === Stage 37: Add recommendations for the next useful action ===
# Project: ToolShed
import json
from datetime import datetime

def generate_recommendations(loan_records, maintenance_records):
    """Generate actionable recommendations based on loan and maintenance history.
    
    Args:
        loan_records (list[dict]): List of loan records with keys:
            'item_name', 'borrower', 'due_date', 'status'
        maintenance_records (list[dict]): List of maintenance records with keys:
            'item_name', 'last_maintenance', 'next_maintenance'
    
    Returns:
        list[dict]: List of recommendation dicts with keys:
            'action', 'priority', 'item_name', 'reason'
    """
    recommendations = []
    
    # Check for overdue loans
    today = datetime.now().date()
    for loan in loan_records:
        if loan['status'] == 'borrowed':
            due_date = datetime.strptime(loan['due_date'], '%Y-%m-%d').date()
            if today > due_date:
                days_overdue = (today - due_date).days
                if days_overdue > 30:
                    recommendations.append({
                        'action': 'URGENT_RECALL',
                        'priority': 'high',
                        'item_name': loan['item_name'],
                        'reason': f"Item borrowed for {days_overdue} days past due. Contact borrower immediately."
                    })
                elif days_overdue > 7:
                    recommendations.append({
                        'action': 'RECALL',
                        'priority': 'medium',
                        'item_name': loan['item_name'],
                        'reason': f"Item is {days_overdue} days overdue. Follow up with borrower."
                    })
    
    # Check for items needing maintenance
    for maint in maintenance_records:
        if maint['next_maintenance'] and maint['next_maintenance'].date() <= today:
            days_since = (today - datetime.strptime(maint['next_maintenance'], '%Y-%m-%d').date()).days
            if days_since > 0:
                recommendations.append({
                    'action': 'SCHEDULE_MAINTENANCE',
                    'priority': 'high' if days_since <= 7 else 'medium',
                    'item_name': maint['item_name'],
                    'reason': f"Item needs maintenance {days_since} days past scheduled date."
                })
    
    return recommendations
