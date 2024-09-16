from typing import Optional
from dataclasses import dataclass, field


class Queue:

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, value) -> None:
        self.items.append(value)

    def dequeue(self) -> Optional[object]:
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self) -> Optional[object]:
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0


@dataclass
class Node:
    value: Optional[object]
    next: Optional["Node"] = field(compare=False, default=None)


class LinkedQueue:
    front_node: Optional[Node]
    rear_node: Optional[Node]

    def __init__(self) -> None:
        self.front_node = None
        self.rear_node = None

    def enqueue(self, value: object) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def dequeue(self) -> Optional[object]:
        if self.is_empty():
            return None
        node = self.front_node
        self.front_node = self.front_node.next
        if self.is_empty():
            self.rear_node = None
        return node.value

    def front(self) -> object:
        if self.is_empty():
            return None
        return self.front_node.value

    def is_empty(self) -> bool:
        return self.front_node is None

    def as_list(self) -> list[object]:
        l = []
        cur = self.front_node
        while cur:
            l.append(cur.value)
            cur = cur.next
        return l
