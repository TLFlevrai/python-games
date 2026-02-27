import pygame
from ..configs import game_config

class Snake:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = game_config.cell_size

        # Position initiale : au centre
        start_x = grid_width // 2
        start_y = grid_height // 2
        self.body = [(start_x, start_y), (start_x-1, start_y), (start_x-2, start_y)]
        self.direction = (1, 0)  # droite
        self.next_direction = (1, 0)
        self.grow = False

    def change_direction(self, new_dir):
        # Empêcher le demi-tour
        if (new_dir[0] != -self.direction[0] or new_dir[1] != -self.direction[1]):
            self.next_direction = new_dir

    def move(self):
        # Appliquer la nouvelle direction
        self.direction = self.next_direction
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        # Vérifier les limites de la grille (sera utilisé par le collision manager)
        # On insère la nouvelle tête
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def set_grow(self):
        self.grow = True

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body

    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def check_wall_collision(self):
        x, y = self.body[0]
        return x < 0 or x >= self.grid_width or y < 0 or y >= self.grid_height

    def draw(self, surface, offset_x=0, offset_y=0):
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(offset_x + x * self.cell_size, offset_y + y * self.cell_size, self.cell_size, self.cell_size)
            color = game_config.snake_head_color if i == 0 else game_config.snake_body_color
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, game_config.grid_line_color, rect, 1)  # bordure