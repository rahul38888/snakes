from cell import Cell
from cell_state import CellState


class Board:
    def __init__(self, size):
        self.grid = [[Cell(i, j, CellState.EMPTY) for j in range(size)] for i in range(size)]

    def get_cell(self, x, y):
        return self.grid[x][y]