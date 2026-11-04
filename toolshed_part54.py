# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ToolShed
def colorize(text, color):
    codes = {
        'red': (31, 39), 'green': (32, 39), 'yellow': (33, 39),
        'blue': (34, 39), 'magenta': (35, 39), 'cyan': (36, 39),
        'white': (37, 39), 'bold': (1, 22),
    }
    if color not in codes:
        return text
    fg, reset = codes[color]
    return f"\033[{fg}m{text}\033[{reset}m"

def color_enabled():
    return os.environ.get('NO_COLOR') is None and sys.stdout.isatty()

class Colorizer:
    def __init__(self, enabled=True):
        self.enabled = enabled
    def __getattr__(self, name):
        if name in ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bold'):
            return lambda text: text if not self.enabled else colorize(text, name)
        raise AttributeError(name)

def make_ansi():
    if color_enabled():
        return Colorizer(True)
    return Colorizer(False)

ANSI = make_ansi()
