# === Stage 13: Add file save support using a configurable path ===
# Project: ToolShed
def save_tools(path="tools.json"):
    if not tools:
        print("No tools to save.")
        return
    with open(path, "w") as f:
        json.dump(tools, f, indent=2)
    print(f"Saved {len(tools)} tool(s) to {path}")

def load_tools(path="tools.json"):
    if not os.path.exists(path):
        print(f"No file found at {path}. Starting fresh.")
        return
    with open(path, "r") as f:
        global tools
        tools = json.load(f)
    print(f"Loaded {len(tools)} tool(s) from {path}")
