from src.game.game import *
from src.objects.cell import *
from src.objects.direction import *
from src.game.keymap import Keymap

from asciimatics.screen import Screen, ResizeScreenError
from asciimatics.effects import Stars, Cycle, Print, Snow
from asciimatics.renderers import FigletText, StaticRenderer, Fire
from asciimatics.scene import Scene
from time import time
from random import choice


class AsciimaticsEngine:
    def __init__(self):
        self.cell_height = 1
        self.cell_width = self.cell_height * 2
        self.boundary_color = [Screen.COLOUR_CYAN, Screen.COLOUR_BLUE]

        self.screen = Screen.open()
        self.screen_dimensions = (
            self.cell_width * ((self.screen.width // 2) // self.cell_width), self.screen.height - 2)
        self.origin = (self.screen.width // 2 - self.screen_dimensions[0] // 2, 1)

        game_dimensions = (self.screen_dimensions[0] // self.cell_width, self.screen_dimensions[1])
        self.game = Game(game_dimensions, (game_dimensions[0] // 2, game_dimensions[1] - 5), 3, Direction.UP, 3)

        self.colors = {CellState.SNAKE: Screen.COLOUR_YELLOW,
                       CellState.FOOD: Screen.COLOUR_GREEN, CellState.EMPTY: 0}

    def run(self):
        restore = True
        try:
            try:
                self.render(self.screen)
            except ResizeScreenError:
                restore = False
                raise
        finally:
            self.screen.close(restore)

    def render(self, screen):
        self.render_starting(screen)
        self.render_boundaries(screen)
        t1 = time()
        t2 = time()
        try:
            while True:

                ev = screen.get_key()
                if self.game.state == GameState.LOST:
                    break
                elif self.game.state == GameState.PAUSED:
                    if ev is ord(' '):
                        self.game.state = GameState.RUNNING
                    else:
                        continue

                if ev in (ord('q'), ord('Q')):
                    return
                elif ev in (ord('a'), ord('d'), ord('w'), ord('s')):
                    self.game.change_direction(Keymap(chr(ev).lower()))
                elif ev is ord(' '):
                    self.game.state = GameState.PAUSED

                if t2 - t1 >= 1 / self.game.speed:
                    if not self.game.move_snake():
                        self.game.state = GameState.LOST
                    self.render_boundaries(screen)
                    self.render_game(screen)
                    self.render_score(screen)

                    screen.refresh()
                    t1, t2 = t2, time()
                else:
                    t2 = time()
        except KeyboardInterrupt:
            pass
        finally:
            self.render_final(screen)

    def render_final(self, screen):
        effects = [
            Cycle(screen, FigletText("Your score is  " + str(self.game.score)), int(screen.height / 2 - 8)),
            Print(screen,
                  StaticRenderer(images=["Thanks for playing. Space to exit ..."]),
                  screen.height - 1),
            Snow(screen)
            # Print(screen,
            #       Fire(screen.height, screen.width, "*" * 70, 0.4, 40, screen.colours),
            #       0,
            #       speed=1,
            #       transparent=False),
        ]

        screen.play([Scene(effects, 0)], stop_on_resize=True, repeat=False)

    def render_starting(self, screen):
        effects = [
            Cycle(screen, FigletText("SNAKES", font='big'), int(screen.height / 2 - 8)),
            Cycle(screen, FigletText("The classic one", font='small'), int(screen.height / 2 + 1)),
            Print(screen,
                  StaticRenderer(images=["Space to play ..."]),
                  screen.height - 1),
            Stars(screen, 50)
        ]

        screen.play([Scene(effects, 0)], stop_on_resize=True, repeat=False)

    def render_score(self, screen):
        score = " Score : " + str(self.game.score) + " "
        screen.print_at(" " * len(score),
                        self.origin[0] + self.screen_dimensions[0] + 4, screen.height // 2 - 1, bg=Screen.COLOUR_WHITE,
                        colour=Screen.COLOUR_BLACK)
        screen.print_at(score,
                        self.origin[0] + self.screen_dimensions[0] + 4, screen.height // 2, bg=Screen.COLOUR_WHITE,
                        colour=Screen.COLOUR_BLACK, attr=Screen.A_BOLD)
        screen.print_at(" " * len(score),
                        self.origin[0] + self.screen_dimensions[0] + 4, screen.height // 2 + 1, bg=Screen.COLOUR_WHITE,
                        colour=Screen.COLOUR_BLACK)

    def render_game(self, screen):
        x, y = self.origin[0], self.origin[1]
        for arr in self.game.board.grid:
            for cell in arr:
                for i in range(self.cell_height):
                    screen.print_at(" " * self.cell_width, x, y + i, bg=self.colors[cell.state])
                x += self.cell_width
            y += self.cell_height
            x = self.origin[0]

    def render_boundaries(self, screen):

        color = choice(self.boundary_color)
        screen.print_at(" " * self.screen_dimensions[0], self.origin[0], self.origin[1] - 1, bg=color)
        screen.print_at(" " * self.screen_dimensions[0], self.origin[0], self.origin[1] + self.screen_dimensions[1],
                        bg=color)
        for i in range(0, self.screen_dimensions[0] + 2):
            screen.print_at('  ', self.origin[0] - self.cell_width, i, bg=color)
        for i in range(0, self.screen_dimensions[0] + 2):
            screen.print_at('  ', self.origin[0] + self.screen_dimensions[0], i, bg=color)
