# === Stage 53: Add command help text and usage examples ===
# Project: ToolShed
HELP = {
    "toolshed": "ToolShed - Home tool and equipment shed tracker",
    "commands": ["add", "list", "borrow", "return", "maintain", "locate", "status"],
    "examples": [
        "python toolshed.py add --name 'Cordless Drill' --type power --location garage",
        "python toolshed.py add --name 'Hammer' --type hand --location shed",
        "python toolshed.py list",
        "python toolshed.py borrow --name 'Cordless Drill' --user Alice",
        "python toolshed.py return --name 'Cordless Drill' --user Alice",
        "python toolshed.py maintain --name 'Hammer' --note 'Replaced handle' --due 2025-08-01",
        "python toolshed.py locate --tool 'Cordless Drill'",
        "python toolshed.py status",
    ],
}

USAGE = """
ToolShed - Track tools, equipment, loans, maintenance, and locations.

Usage:
  python toolshed.py <command> [options]

Commands:
  add      Add a new tool to the shed
  list     List all tools with their current status
  borrow   Borrow a tool (records a loan)
  return   Return a borrowed tool
  maintain Record maintenance and a due date
  locate   Show which location a tool is stored in
  status   Show overall tool counts and shed summary

Examples:
  python toolshed.py add --name 'Cordless Drill' --type power --location garage
  python toolshed.py borrow --name 'Cordless Drill' --user Alice
  python toolshed.py return --name 'Cordless Drill' --user Alice
  python toolshed.py maintain --name 'Hammer' --note 'Replaced handle' --due 2025-08-01
  python toolshed.py locate --tool 'Cordless Drill'
  python toolshed.py status
Run 'python toolshed.py help' to see all commands and examples.
"""

def show_help():
    print(USAGE)

def show_commands():
    print("ToolShed commands:", ", ".join(HELP["commands"]))
    print("Examples:")
    for example in HELP["examples"]:
        print("  " + example)
