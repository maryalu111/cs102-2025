"""
Game of Life
"""

import pathlib
import random
import typing as tp
from typing import List, Optional, Tuple

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        """Defines the Game"""
        # Размер клеточного поля
        self.rows, self.cols = size
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)

    def create_grid(self, randomize: bool = False) -> Grid:
        """Creates a grid"""
        grid = []
        for _ in range(self.rows):
            if randomize:
                grid.append([random.randint(0, 1) for _ in range(self.cols)])
            else:
                grid.append([0 for _ in range(self.cols)])
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        """Finds neighbours of a cell"""
        i, j = cell
        neighbours = []
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x, y) != (i, j) and 0 <= x < self.rows and 0 <= y < self.cols:
                    neighbours.append(self.curr_generation[x][y])
        return neighbours

    def get_next_generation(self) -> Grid:
        """Finds next generation of cells"""
        new_grid = self.create_grid()
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = sum(self.get_neighbours((i, j)))
                if self.curr_generation[i][j] == 1:
                    if neighbours in [2, 3]:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
                else:
                    if neighbours == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
        return new_grid

    def step(self) -> None:
        """Выполнить один шаг игры."""
        """Changes the previous generation to next"""
        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        """Checks if max generations were exceeded"""
        return (
            self.max_generations is not None
            and self.generations >= self.max_generations
        )

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        """Checks that the cells are actually changing"""
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        """Load a grid from a text file and return a GameOfLife instance"""
        with open(filename, encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        grid = [[int(ch) for ch in line] for line in lines]

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        life = GameOfLife((rows, cols), randomize=False)
        life.curr_generation = grid
        life.prev_generation = life.create_grid()
        return life

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        """Save current grid to a file"""
        with open(filename, "w", encoding="utf-8") as f:
            for row in self.curr_generation:
                f.write("".join(str(cell) for cell in row) + "\n")
