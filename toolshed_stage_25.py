# === Stage 25: Add daily summary calculations ===
# Project: ToolShed
def daily_summary(schedules):
    """Compact daily summary for ToolShed schedules."""
    today = datetime.date.today()
    today_str = today.strftime('%A %Y-%m-%d')
    lines = [f'\n=== {today_str} ===']
    for sched in schedules:
        if sched['start'] <= today <= sched['end']:
            active = True
        else:
            active = False
        lines.append(f'  [{sched["name"]}] {"Active" if active else "Inactive"}  {sched["start"]} -> {sched["end"]}')
    return '\n'.join(lines)
