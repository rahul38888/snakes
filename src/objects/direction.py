from enum import Enum

class Direction(Enum):
    UP = {"x":-1, "y":0}
    DOWN = {"x":1, "y":0}
    RIGHT ={"x":0, "y":1}
    LEFT = {"x":0, "y":-1}
