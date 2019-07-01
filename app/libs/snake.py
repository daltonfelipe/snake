from app.libs.cell import Cell
import pygame, random


class Snake:

    def __init__(self, cells_num: int, grid_size: int):
        self.cells = []
        self.grid_size = grid_size
        self.score = 0
        self.dead = False
        self.direction = None
        for i in range(cells_num + 2, 2, -1):
            self.add_cell(Cell(i*grid_size, grid_size, grid_size))

    def add_cell(self, cell: Cell):
        """
        Add a new cell to Snake object.
        :param cell: Cell
        :return: None
        """
        self.cells.insert(0, cell)

    def self_collide(self):
        """
        Check if snake object eat self
        :return: bool
        """
        for i in range(len(self.cells)):
            if i < len(self.cells) - 1:
                if self.cells[-1].colliderect(self.cells[i]):
                    return True

    def draw_cells(self, surface):
        """
        Draw all cells on a specific surface.
        :param surface: pygame.Surface
        :return: None
        """
        for cell in self.cells:
            pygame.draw.rect(surface, cell.color, cell, 2)

    def override_edges(self):
        """
        Check if snake across trougth the edges
        :return: bool
        """
        if self.cells[-1].top > 600 - self.grid_size \
            or self.cells[-1].top < 0 \
            or self.cells[-1].left > 800 - self.grid_size \
            or self.cells[-1].left < 0:
            return True
        return False

    def move(self, direction):
        """
        Move snake cells on a specific direction.
        :param direction: int
        :return: None
        """
        if not self.dead:
            cells = self.cells

            if direction == 0:
                self.direction = 0
                for i in range(len(cells) - 1):
                    cells[i].top = cells[i+1].top
                    cells[i].left = cells[i+1].left
                cells[-1].top -= cells[-1].grid_size

            if direction == 1:
                self.direction = 1
                for i in range(len(cells) - 1):
                    cells[i].top = cells[i+1].top
                    cells[i].left = cells[i+1].left
                cells[-1].left += cells[-1].grid_size

            if direction == 2:
                self.direction = 2
                for i in range(len(cells) - 1):
                    cells[i].top = cells[i+1].top
                    cells[i].left = cells[i+1].left
                cells[-1].top += cells[-1].grid_size

            if direction == 3:
                self.direction = 3
                for i in range(len(cells) - 1):
                    cells[i].top = cells[i+1].top
                    cells[i].left = cells[i+1].left
                cells[-1].left -= cells[-1].grid_size

    def eat(self, apple):
        """
        Test if snake head collides with apple.
        :return: bool
        """
        if self.cells[-1].colliderect(apple):
            self.add_cell(
                Cell(
                    x = self.cells[0].left,
                    y = self.cells[0].top,
                    grid_size = self.grid_size
                )
            )
            return True
    
    def kill(self):
        self.dead = True
    