# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ToolShed
# ── Dry-run mode (append to existing CLI entry point) ──────────────────────
import sys, argparse

def _dry_run_wrapper(func):
    """Run *func* under a dry-run flag; if enabled, print an echo and exit 0."""
    def wrapper(args):
        if getattr(args, "dry_run", False):
            print(f"[DRY RUN] Would execute: {func.__name__}({', '.join(repr(v) for v in args.arguments or ())})")
            return 0
        return func(args)
    wrapper.__name__ = func.__name__
    return wrapper
