from typing import Optional
from dataclasses import dataclass, field


@dataclass
class Node:
    next: Optional["Node"] = field(compare=False)
    value: object

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


@dataclass
class LinkedList:
    head: Optional[Node]

    def __init__(self, nodes: list = []) -> None:
        self.head = None
        if nodes:
            self.head = Node(nodes[0])
            temp = self.head
            for value in nodes[1:]:
                temp.next = Node(value)
                temp = temp.next

    def __find_node_at_position(self, position: int) -> Optional[Node]:
        i = 0
        found = self.head
        while found and i <= position:
            i += 1
            found = found.next
        return found

    def insert_begin(self, data: object) -> None:
        # Cria o novo nó
        node = Node(data)

        # Aponta o novo nó para a cabeça da lista
        node.next = self.head

        # Substituiu a cabeça da lista pelo novo nó
        self.head = node

    def insert_end(self, value) -> None:
        # Cria o novo nó
        node = Node(value)

        # Se a lista está vazia, adiciona o item na cabeça
        if self.head is None:
            self.head = node
            return

        # Percorre até o último item e adiciona o novo nó como next
        end = self.head
        while end.next:
            end = end.next
        end.next = Node(value)

    def insert_position(self, position, value) -> None:
        # Find the node right before the position we want
        found = self.__find_node_at_position(position - 1)
        if found is not None:
            node = Node(value)
            node.next = found.next
            found.next = node

    def remove_begin(self) -> None:
        if self.head:
            self.head = self.head.next

    def remove_end(self) -> None:
        if self.head is None:
            return
        found = self.head
        while found and found.next and found.next.next:
            found = found.next
        found.next = None

    def remove_position(self, position) -> None:
        # Find the node right before the position we want
        found = self.__find_node_at_position(position - 1)
        if found:
            found.next = (found.next or Node(-1)).next

    def middle(self) -> Optional[Node]:
        mid, tail = self.head, self.head
        while mid and tail and tail.next:
            mid = mid.next
            tail = tail.next.next
        return mid

    def reverse(self) -> None:
        if self.head is None:
            return

        prev = None
        cur = self.head

        while cur:
            # save reference to the next element
            temp = cur.next

            # change element direction, pointing to previous
            cur.next = prev

            # next iteration previous should be cur
            prev = cur

            # next iteration cur should be next
            cur = temp

        # update head reference
        self.head = prev

    def as_list(self) -> list[object]:
        res = []
        node = self.head
        while node is not None:
            res.append(node.value)
            node = node.next
        return res
