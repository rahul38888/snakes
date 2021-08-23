from random import randint
from asciimatics.screen import Screen

width = 10
height = 15

x, j = 0, 0


def render_boundaries(screen):
    width = screen.width // 2
    height = screen.height

    screen.print_at(" " * width, width // 2, 0, bg=Screen.COLOUR_RED)
    screen.print_at(" " * width, width // 2, height - 1, bg=Screen.COLOUR_RED)
    for i in range(0, height):
        screen.print_at('  ', width // 2, i, bg=Screen.COLOUR_RED)
    for i in range(0, height):
        screen.print_at('  ', 3 * width // 2, i, bg=Screen.COLOUR_RED)


def demo(screen):
    global width, height, x, j
    while True:
        screen.print_at('  ', x, j, bg=0)

        render_boundaries(screen)

        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        if ev in (ord('s'), ord('S')):
            j = (j + 1) % screen.height

        x = (x + 2) % screen.width
        screen.print_at('  ', 0, 0, bg=(x + j) % screen.colours)

        screen.refresh()


Screen.wrapper(demo)
