import enum


class CellState(enum.Enum):
    EMPTY = 0
    SNAKE = 1
    FOOD = 2


class Cell:
    def __init__(self, x, y, state: CellState):
        self.x = x
        self.y = y
        self.state = state
