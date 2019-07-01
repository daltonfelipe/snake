import pygame


class Cell(pygame.rect.Rect):

    def __init__(self, x: int, y: int, grid_size: int):
        self.size = [grid_size, grid_size]
        self.grid_size = grid_size
        self.left = x
        self.top = y
        self.color = (40, 228, 21)

