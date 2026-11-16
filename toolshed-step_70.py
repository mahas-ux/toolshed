# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ToolShed
RESET_CONFIRMED = False


def clear_all():
    global RESET_CONFIRMED
    if not RESET_CONFIRMED:
        print("⚠ Aborting! Type 'clear_all' again to confirm.")
        return
    if tools:
        tools.clear()
    if loans:
        loans.clear()
    if maintenance:
        maintenance.clear()
    if locations:
        locations.clear()
    print("All data cleared.")


def clear_all():
    global RESET_CONFIRMED
    RESET_CONFIRMED = True
    clear_all()
    RESET_CONFIRMED = False
