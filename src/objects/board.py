from src.objects.cell import *

import random
from ursina import Entity


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[Cell(j, i, CellState.EMPTY,
                           Entity(model="quad", visible=False, scale=(0.5, 0.5, 0.5),
                                  position=((j - width // 2) * 0.5, -(i - height // 2) * 0.5)))
                      for j in range(width)] for i in range(height)]
        self.empty_cells = set()
        self.food = None
        for i in range(height):
            for j in range(width):
                self.empty_cells.add(self.grid[i][j])

    def get_cell(self, x, y):
        return self.grid[y % self.height][x % self.width]

    def set_state(self, cell, state: CellState):
        cell.state = state
        cell.entity.model = state.value[0]
        cell.entity.visible = state.value[1]
        cell.entity.color = state.value[2]
        if state is CellState.SNAKE:
            if self.empty_cells.__contains__(cell):
                self.empty_cells.remove(cell)
            if self.food is cell:
                self.food = None
        elif state is CellState.FOOD:
            if self.empty_cells.__contains__(cell):
                self.empty_cells.remove(cell)
            self.food = cell
        else:
            if self.food is cell:
                self.food = None
            self.empty_cells.add(cell)

    def get_empty_cell(self):
        empty_cells = random.sample(self.empty_cells, 1)
        if len(empty_cells) > 0:
            return empty_cells[0]
