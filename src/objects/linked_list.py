from src.objects.cell import Cell


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def add_head(self, cell: Cell):
        node = Node()
        node.data = cell
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def add_tail(self, cell: Cell):
        node = Node()
        node.data = cell
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self):
        if self.size == 0:
            return None
        old_tail = self.tail
        self.tail = old_tail.prev
        self.tail.next = None
        old_tail.prev = None
        self.size -= 1
        return old_tail.data


class Node:
    def __init__(self):
        self.data: Cell = None
        self.next: Node = None
        self.prev: Node = None
