# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ToolShed
from dataclasses import dataclass
from datetime import date, timedelta
from enum import Enum


class ToolCategory(Enum):
    HAND = "hand"
    POWER = "power"
    OUTDOOR = "outdoor"
    ELECTRICAL = "electrical"


@dataclass
class Location:
    name: str
    latitude: float
    longitude: float

    def __str__(self) -> str:
        return self.name


@dataclass
class Tool:
    name: str
    category: ToolCategory
    location: Location
    last_maintenance: date
    notes: str

    def is_due_for_maintenance(self, interval: timedelta) -> bool:
        return (date.today() - self.last_maintenance) >= interval


@dataclass
class Loan:
    tool: Tool
    borrower: str
    due_date: date
    notes: str

    def is_overdue(self) -> bool:
        return date.today() > self.due_date
