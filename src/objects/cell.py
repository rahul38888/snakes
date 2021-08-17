from cell_state import CellState


class Cell:
    def __init__(self, x, y, state: CellState):
        self.x = x
        self.y = y
        self.state = CellState.EMPTY
