# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ToolShed
try:
    while True:
        command = input("toolshed> ").strip()
        if not command:
            continue
        if command.lower() in ("exit", "quit"):
            print("Goodbye.")
            break
        handle_command(command)
except (KeyboardInterrupt, EOFError):
    print()
    print("Goodbye.")
