# === Stage 35: Add active user switching and user-specific records ===
# Project: ToolShed
from datetime import date, timedelta
from typing import Dict, List, Optional, Tuple

class ToolShed:
    def __init__(self):
        self.users: Dict[str, 'User'] = {}
        self.tools: Dict[str, 'Tool'] = {}
        self.loans: Dict[str, 'Loan'] = {}
        self.maintenance: Dict[str, 'Maintenance'] = {}
        self.locations: Dict[str, 'Location'] = {}

    def add_user(self, name: str) -> 'User':
        user = User(name)
        self.users[name] = user
        return user

    def add_tool(self, name: str, maintenance_interval: int) -> 'Tool':
        tool = Tool(name, maintenance_interval)
        self.tools[name] = tool
        return tool

    def add_location(self, name: str) -> 'Location':
        location = Location(name)
        self.locations[name] = location
        return location

    def add_loan(self, user: User, tool: Tool, location: Location) -> 'Loan':
        loan = Loan(user, tool, location)
        self.loans[str(loan)] = loan
        return loan

    def add_maintenance(self, user: User, tool: Tool, location: Location) -> 'Maintenance':
        maintenance = Maintenance(user, tool, location)
        self.maintenance[str(maintenance)] = maintenance
        return maintenance

    def get_active_user(self) -> Optional[User]:
        today = date.today()
        for user in self.users.values():
            if user.last_active is None or user.last_active >= today - timedelta(days=30):
                return user
        return None

    def get_user_records(self, user: User) -> Tuple[List[Loan], List[Maintenance], List[Location]]:
        user_loans = [loan for loan in self.loans.values() if loan.user == user]
        user_maintenance = [maint for maint in self.maintenance.values() if maint.user == user]
        user_locations = [loc for loc in self.locations.values() if loc.last_used_by == user]
        return user_loans, user_maintenance, user_locations

    def get_all_active_tools(self) -> List[Tool]:
        return [tool for tool in self.tools.values() if tool.is_active]
