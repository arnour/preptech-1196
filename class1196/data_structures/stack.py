from typing import Optional

class Stack:

    def __init__(self) -> None:
        self.items = []

    def push(self, value: object) -> None:
        self.items.append(value)

    def pop(self) -> Optional[object]:
        if not self.is_empty():
            return self.items.pop()
        return None

    def top(self) -> Optional[object]:
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self) -> int:
        return len(self.items) == 0
