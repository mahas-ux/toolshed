# === Stage 61: Add performance timing for core list and search operations ===
# Project: ToolShed
import time

def time_operation(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed

def timed_search(tools, query, field='name'):
    start = time.perf_counter()
    matches = [t for t in tools if query.lower() in str(getattr(t, field, '')).lower()]
    elapsed = time.perf_counter() - start
    return matches, elapsed

def timed_list(tools):
    start = time.perf_counter()
    result = list(tools)
    elapsed = time.perf_counter() - start
    return result, elapsed
