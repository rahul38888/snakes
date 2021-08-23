from src.objects.cell import *
from src.game.keymap import Keymap


@DeprecationWarning
class HomeBrewed:

    def __init__(self):
        pass

    def display(self):

        screen = "=" * (self.board.width + 4)
        for i in range(self.board.height):
            line = ""
            for j in range(self.board.width):
                cell = self.board.get_cell(j, i)
                if cell.state is CellState.EMPTY:
                    line += " "
                elif cell.state is CellState.SNAKE:
                    if cell is self.snake.get_head():
                        line += "0"
                    else:
                        line += "\u2588"
                else:
                    line += "@"
            screen += "\n||" + line + "||"

        screen += "\n" + "=" * (self.board.width + 4)
        print(screen, end="\r")

    def render(self):
        movement_keys = {Keymap.UP.value, Keymap.DOWN.value, Keymap.RIGHT.value, Keymap.LEFT.value}
        try:
            while True:
                self.display()
                command = input()
                if movement_keys.__contains__(command):
                    self.change_direction(Keymap(command))
                else:
                    pass

                if not self.move_snake():
                    break
        except KeyboardInterrupt:
            pass
        finally:
            print("Your score is: " + str(self.score))
