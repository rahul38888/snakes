from src.objects.linked_list import LinkedList, Node
from src.objects.cell import *


class Snake:
    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list
        root = self.linked_list.head

    def move(self, cell: Cell):
        self.linked_list.add_head(cell)
        old_tail = self.linked_list.remove()
        return old_tail

    def check_collision(self, cell: Cell):
        return cell.state is CellState.SNAKE

    def get_head(self):
        return self.linked_list.head

    def get_tail(self):
        return self.linked_list.tail

    def add_cell(self, cell: Cell, tail):
        if tail:
            self.linked_list.add_tail(cell)
        else:
            self.linked_list.add_head(cell)