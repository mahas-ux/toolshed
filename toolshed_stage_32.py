# === Stage 32: Add pagination helpers for long console output ===
# Project: ToolShed
def paginate(items, page_size=20):
    """Yield slices of items for console pagination."""
    total = len(items)
    if total == 0:
        return
    start = 0
    while start < total:
        end = min(start + page_size, total)
        print(f"--- Page {start // page_size + 1} / {total // page_size + (1 if total % page_size else 0) } ---")
        for idx, item in enumerate(items[start:end], start=0):
            print(f"  [{start + idx}] {item}")
        print()
        start = end
