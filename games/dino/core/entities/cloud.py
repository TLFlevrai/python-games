#games/dino/core/entities/cloud.py

import pygame
import random
from ..configs import game_config

class Cloud:
    def __init__(self, screen_width, y_pos):
        self.screen_width = screen_width
        self.image = None
        self._load_image()
        self.x = screen_width
        self.y = y_pos
        self.speed = 1  # vitesse fixe ou basée sur game_speed? On utilise une vitesse constante
        if self.image:
            self.rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.rect = pygame.Rect(self.x, self.y, 200, 80)  # fallback

    def _load_image(self):
        try:
            raw = pygame.image.load(game_config.cloud_image_path).convert_alpha()
            self.image = pygame.transform.scale(raw, (200, 80))
        except (pygame.error, FileNotFoundError) as e:
            print(f"⚠️ Nuage non chargé: {e}")
            self.image = None

    def update(self):
        self.x -= self.speed
        if self.image:
            self.rect.centerx = self.x
        else:
            self.rect.x = self.x

    def is_offscreen(self):
        return self.x + (self.rect.width if self.image else 200) < 0

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, self.y - (self.rect.height//2 if self.image else 0)))
        else:
            pygame.draw.rect(surface, (200,200,200), self.rect)