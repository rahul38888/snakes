from src.objects.board import Board
from src.objects.snake import Snake
from src.objects.direction import *
from src.objects.linked_list import LinkedList
from src.objects.cell import *
from src.engine.render_engine import RenderEngine

from enum import Enum
from ursina import Text, destroy


class Game:
    def __init__(self, size, init_pos, init_size, init_dir):
        self.board = Board(size[0], size[1])
        self.direction = init_dir
        self.score = 0
        self.state = GameState.RUNNING

        self.score_board = Text(text="Score: " + str(self.score),
                                origin=(-self.board.width // 2, self.board.height // 2 + 1),
                                background=True, size=1)
        self.end_board = Text(text="", origin=(0, -2), background=True, size=1, visible=False, z=-1)

        def update():
            self.move_snake()

        def input(key):
            if self.state is not GameState.RUNNING:
                return
            print(key)
            if key == "w up" or key == "s up" or key == "d up" or key == "a up":
                self.change_direction(Keymap(key[0]))
            elif key == "escape up":
                self.state = GameState.TERMINATED

            if not self.move_snake():
                self.state = GameState.LOST

            if self.state is not GameState.RUNNING:
                self.end_board.text = self.state.value + " Score is " + str(self.score)
                self.end_board.visible = True

        self.render_engine = RenderEngine(input, update)

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
            destroy(self.score_board)
            self.score_board = Text(text="Score: " + str(self.score),
                                    origin=(-self.board.width // 2, self.board.height // 2 + 1),
                                    background=True, size=1)
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
        self.render_engine.run()


class GameState(Enum):
    LOST = "You lost!"
    RUNNING = "Running"
    TERMINATED = "Ended!"
