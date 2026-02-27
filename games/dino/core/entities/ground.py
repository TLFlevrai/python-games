#games/dino/core/entities/ground.py

import pygame
from ..configs import game_config

class Ground:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.y = game_config.get_ground_y()
        self.image = None
        self._load_image()
        self.x = 0
        self.scroll_speed = game_config.ground_scroll_speed

    def _load_image(self):
        try:
            raw = pygame.image.load(game_config.ground_image_path).convert_alpha()
            self.image = pygame.transform.scale(raw, (self.screen_width, 20))
        except (pygame.error, FileNotFoundError) as e:
            print(f"⚠️ Sol non chargé, utilisation du rectangle: {e}")
            self.image = None

    def update(self):
        self.x -= self.scroll_speed
        if self.x <= -self.screen_width:
            self.x = 0

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, self.y))
            surface.blit(self.image, (self.x + self.screen_width, self.y))
        else:
            pygame.draw.line(surface, game_config.ground_color, (0, self.y),
                             (self.screen_width, self.y), game_config.ground_line_thickness)