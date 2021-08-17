from linked_list import LinkedList, Node
from cell import Cell
from direction import Direction
from cell_state import CellState

class Snake:
    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list
        root = self.linked_list.head
        while root is not None:
            root.data.state = CellState.SNAKE

    def move(self, cell: Cell):
        self.linked_list.add(cell)
        cell.state = CellState.SNAKE
        old_cell = self.linked_list.remove()
        old_cell.state = CellState.EMPTY

    def check_collision(self, cell: Cell):
        return cell.state is CellState.SNAKE