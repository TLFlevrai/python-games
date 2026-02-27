import pygame
import random
from ..configs import game_config

class Food:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = game_config.cell_size
        self.position = (0, 0)
        self.respawn()

    def respawn(self, snake_body=None):
        if snake_body is None:
            snake_body = []
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break

    def get_position(self):
        return self.position

    def draw(self, surface, offset_x=0, offset_y=0):
        x, y = self.position
        rect = pygame.Rect(offset_x + x * self.cell_size, offset_y + y * self.cell_size,
                           self.cell_size, self.cell_size)
        pygame.draw.rect(surface, game_config.food_color, rect)
        pygame.draw.rect(surface, game_config.grid_line_color, rect, 1)