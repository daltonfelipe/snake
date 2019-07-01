import pygame, random


class Apple(pygame.rect.Rect):

    def __init__(self, x: int = 0, y: int = 0, grid_size: int = 0):
        self.size = [grid_size, grid_size]
        self.grid_size = grid_size
        self.left = x
        self.top = y

    def show(self, surface: pygame.Surface):
        """
        Draw apple on a specific surface.
        :param surface: pygame.Surface
        :return: None
        """
        self.surface = surface
        pygame.draw.rect(surface, self.color, self)

    def new_position(self):
        """
        Generates new position to apple object
        :return: self
        """
        self.left = random.randint(0, 800 - self.grid_size)//self.grid_size*self.grid_size
        self.top = random.randint(0, 600 - self.grid_size)//self.grid_size*self.grid_size
        return self