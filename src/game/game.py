from src.objects.board import Board
from src.objects.snake import Snake
from src.objects.direction import *
from src.objects.linked_list import LinkedList
from src.objects.cell import *

from enum import Enum


class Game:
    def __init__(self, size, init_pos, init_size=3, init_dir=Direction.UP, speed=3, acceleration=0.1):
        self.board = Board(size[0], size[1])
        self.direction = init_dir
        self.score = 0
        self.state = GameState.RUNNING

        self.speed = speed
        self.acceleration = acceleration

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
            self.increase_speed(self.acceleration)
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

    def increase_speed(self, delta):
        self.speed += delta


class GameState(Enum):
    LOST = "You lost!"
    RUNNING = "Running"
    TERMINATED = "Ended!"
    PAUSED = "Paused ..."
