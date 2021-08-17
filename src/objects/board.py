from cell import Cell
from cell_state import CellState


class Board:
    def __init__(self, size):
        self.grip = [[Cell(i, j, CellState.EMPTY) for j in range(size)] for i in range(size)]
