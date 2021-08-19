from enum import Enum
from src.game.keymap import Keymap

class Direction(Enum):
    UP = {"x":0, "y":-1}
    DOWN = {"x":0, "y":1}
    RIGHT = {"x":1, "y":0}
    LEFT = {"x":-1, "y":0}

turns = {Direction.UP: {Keymap.RIGHT: Direction.RIGHT, Keymap.LEFT: Direction.LEFT},
         Direction.DOWN: {Keymap.RIGHT: Direction.RIGHT, Keymap.LEFT: Direction.LEFT},
         Direction.RIGHT: {Keymap.UP: Direction.UP, Keymap.DOWN: Direction.DOWN},
         Direction.LEFT: {Keymap.UP: Direction.UP, Keymap.DOWN: Direction.DOWN}}
