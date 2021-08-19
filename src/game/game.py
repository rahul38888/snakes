from src.objects.board import Board
from src.objects.snake import Snake
from src.objects.direction import *
from src.objects.linked_list import LinkedList
from src.objects.cell import *

from enum import Enum


class Game:
    def __init__(self, size, init_pos, init_size, init_dir):
        self.board = Board(size[0], size[1])
        self.direction = init_dir
        self.score = 0

        snake_length = LinkedList()
        for i in range(init_size):
            cell = self.board.get_cell(init_pos[0] - i * init_dir.value["x"], init_pos[1] - i * init_dir.value["y"])
            self.board.set_state(cell, CellState.SNAKE)
            snake_length.add_tail(cell)

        self.snake = Snake(snake_length)
        self.init_food()

    def move_snake(self):
        head = self.snake.get_head().data
        new_head = self.board.get_cell(head.x + self.direction.value["x"], head.y + self.direction.value["y"])
        if new_head.state is CellState.SNAKE:
            return False
        elif new_head.state is CellState.FOOD:
            self.snake.add_cell(new_head, False)
            self.board.set_state(new_head, CellState.SNAKE)
            self.score += 1
            self.init_food()
        else:
            self.board.set_state(new_head, CellState.SNAKE)
            old_tail = self.snake.move(new_head)
            self.board.set_state(old_tail, CellState.EMPTY)
        return True

    def init_food(self):
        cell = self.board.get_empty_cell()
        self.board.set_state(cell, CellState.FOOD)

    def change_direction(self, keymap):
        turn_map = turns[self.direction]
        if turn_map.__contains__(keymap):
            self.direction = turn_map[keymap]

    def render(self):
        print("=" * (self.board.width + 4))
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
                        line += "O"
                else:
                    line += "@"
            print("||" + line + "||")

        print("=" * (self.board.width + 4))

    def run(self):
        movement_keys = {Keymap.UP.value, Keymap.DOWN.value, Keymap.RIGHT.value, Keymap.LEFT.value}
        try:
            while True:
                self.render()
                command = input()
                print("\033[2J")
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


class GameState(Enum):
    LOST = 0
    RUNNING = 1
    TERMINATED = 2
