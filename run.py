from src.game.game import *
from src.game.keymap import Keymap

if __name__ == '__main__':
    game = Game((11, 15), (5, 11), 3, Direction.UP)
    game.run()

