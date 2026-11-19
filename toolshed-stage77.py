# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ToolShed
def load_tools(path):
    tools = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            tools.append(ToolShedItem(*parts))
    return tools


def load_locations(path):
    locations = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            locations[parts[0]] = parts[1:]
    return locations


def load_maintenance(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            records.append(MaintenanceRecord(*parts))
    return records


def load_loans(path):
    loans = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            loans.append(LoanRecord(*parts))
    return loans
