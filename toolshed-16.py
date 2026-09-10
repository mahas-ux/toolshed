# === Stage 16: Add argparse support for the most common commands ===
# Project: ToolShed
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="ToolShed - Home tool and equipment tracker")
    sub = parser.add_subparsers(dest="command")

    # add
    p_add = sub.add_parser("add", help="Add a new tool")
    p_add.add_argument("name", help="Tool name")
    p_add.add_argument("--category", default="Tools", help="Category (default: Tools)")
    p_add.add_argument("--location", default="Shed", help="Location (default: Shed)")
    p_add.add_argument("--owner", default="None", help="Owner (default: None)")
    p_add.set_defaults(func=add_tool)

    # view
    p_view = sub.add_parser("view", help="View all tools")
    p_view.set_defaults(func=view_tools)

    # loan
    p_loan = sub.add_parser("loan", help="Loan a tool")
    p_loan.add_argument("tool_name", help="Tool to loan")
    p_loan.add_argument("--to", required=True, help="Borrower name")
    p_loan.add_argument("--due", default=None, help="Due date (YYYY-MM-DD)")
    p_loan.set_defaults(func=loan_tool)

    # return
    p_ret = sub.add_parser("return", help="Return a loaned tool")
    p_ret.add_argument("tool_name", help="Tool to return")
    p_ret.set_defaults(func=return_tool)

    # maintenance
    p_maint = sub.add_parser("maintenance", help="Log maintenance")
    p_maint.add_argument("tool_name", help="Tool being maintained")
    p_maint.add_argument("--note", required=True, help="Maintenance note")
    p_maint.add_argument("--date", default=None, help="Date (YYYY-MM-DD)")
    p_maint.set_defaults(func=log_maintenance)

    # location
    p_loc = sub.add_parser("location", help="Change tool location")
    p_loc.add_argument("tool_name", help="Tool to move")
    p_loc.add_argument("--to", required=True, help="New location")
    p_loc.set_defaults(func=change_location)

    return parser
