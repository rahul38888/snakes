from random import randint
from asciimatics.screen import Screen

width = 10
height = 15

x, j = 0, 0


def demo(screen):
    global width, height, x, j
    while True:
        screen.print_at('  ', x, j, bg=0)

        for i in range(0, screen.height):
            screen.print_at('  ', screen.width // 4, i, bg=screen.colours // 2)
        for i in range(0, screen.height):
            screen.print_at('  ', 3*screen.width // 4, i, bg=screen.colours // 2)
        # screen.print_at('Hello world!',
        #                 randint(0, screen.width), randint(0, screen.height),
        #                 colour=randint(0, screen.colours - 1),
        #                 bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        if ev in (ord('s'), ord('S')):
            j = (j+1) % screen.height

        x = (x+2) % screen.width
        screen.print_at(str(x)+' ', x, j, bg=(x+j) % screen.colours)

        screen.refresh()


Screen.wrapper(demo)
