# === Stage 55: Add a setting to disable colorized output ===
# Project: ToolShed
def color_enabled():
    return os.environ.get("TOOLSHED_COLOR", "1") != "0"

def disable_colorized_output():
    """Disable colorized output when TOOLSHED_COLOR=0."""
    os.environ["TOOLSHED_COLOR"] = "0"

def colorize(text, color):
    if not color_enabled():
        return text
    codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m",
    }
    return f"{codes.get(color, '')}{text}{codes['reset']}"

def styled(message, color="white"):
    return colorize(message, color)
