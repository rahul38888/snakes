import enum


class CellState(enum.Enum):
    EMPTY = enum.auto()
    SNAKE = enum.auto()
    FOOD = enum.auto()


class Cell:
    def __init__(self, x, y, state: CellState):
        self.x = x
        self.y = y
        self.state = state

