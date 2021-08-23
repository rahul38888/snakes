from src.game.game import Game
from src.objects.cell import *
from src.objects.direction import *
from src.game.keymap import Keymap

from asciimatics.screen import Screen, ResizeScreenError
from time import time


class AsciimaticsEngine:
    def __init__(self):
        self.cell_height = 1
        self.cell_width = self.cell_height * 2
        self.boundary_color = Screen.COLOUR_RED

        screen = Screen.open()
        self.screen_dimensions = (self.cell_width * ((screen.width // 2) // self.cell_width), screen.height - 2)
        self.origin = (screen.width // 2 - self.screen_dimensions[0] // 2, 1)

        game_dimensions = (self.screen_dimensions[0] // self.cell_width, self.screen_dimensions[1])
        self.game = Game(game_dimensions, (game_dimensions[0] // 2, game_dimensions[1] - 5), 3, Direction.UP, 3)

        self.colors = {CellState.SNAKE: Screen.COLOUR_YELLOW,
                       CellState.FOOD: Screen.COLOUR_GREEN, CellState.EMPTY: Screen.COLOUR_DEFAULT}

        restore = True
        try:
            try:
                self.render(screen)
            except ResizeScreenError:
                restore = False
                raise
        finally:
            screen.close(restore)

    def render(self, screen):
        self.render_boundaries(screen)

        t1 = time()
        t2 = time()
        while True:
            ev = screen.get_key()
            if ev in (ord('q'), ord('Q')):
                return
            elif ev in (ord('a'), ord('d'), ord('w'), ord('s')):
                self.game.change_direction(Keymap(chr(ev).lower()))

            if t2 - t1 >= 1 / self.game.speed:
                if not self.game.move_snake():
                    return
                self.update_render(screen)

                screen.refresh()
                t1, t2 = t2, time()
            else:
                t2 = time()

    def update_render(self, screen):
        x, y = self.origin[0], self.origin[1]
        for arr in self.game.board.grid:
            for cell in arr:
                for i in range(self.cell_height):
                    screen.print_at(" " * self.cell_width, x, y + i, bg=self.colors[cell.state])
                x += self.cell_width
            y += self.cell_height
            x = self.origin[0]

    def render_boundaries(self, screen):

        screen.print_at(" " * self.screen_dimensions[0], self.origin[0], self.origin[1]-1, bg=self.boundary_color)
        screen.print_at(" " * self.screen_dimensions[0], self.origin[0], self.origin[1]+self.screen_dimensions[1],
                        bg=self.boundary_color)
        for i in range(0, self.screen_dimensions[0]+2):
            screen.print_at('  ', self.origin[0]-self.cell_width, i, bg=self.boundary_color)
        for i in range(0, self.screen_dimensions[0]+2):
            screen.print_at('  ', self.origin[0]+self.screen_dimensions[0], i, bg=self.boundary_color)
