import enum
from ursina import Entity, color


class CellState(enum.Enum):
    EMPTY = ("quad", False, None)
    SNAKE = ("sphere", True, color.green)
    FOOD = ("sphere", True, color.orange)


class Cell:
    def __init__(self, x, y, state: CellState, entity: Entity):
        self.x = x
        self.y = y
        self.state = state
        self.entity: Entity = entity

