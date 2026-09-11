# === Stage 19: Add undo support for the last simple mutation ===
# Project: ToolShed
import copy
import collections

class UndoStack:
    def __init__(self, max_size=100):
        self._stack = collections.deque(maxlen=max_size)
        self._counter = 0

    def push(self, state):
        self._counter += 1
        self._stack.append(copy.deepcopy(state))

    def pop(self):
        if self._stack:
            return self._stack.pop()
        return None

    def is_empty(self):
        return len(self._stack) == 0

    def get_last(self):
        if self._stack:
            return self._stack[-1]
        return None
