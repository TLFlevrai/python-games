# games/dino/core/entities/obstacle.py

import pygame
from ..configs import obstacle_config

class Obstacle:
    """
    Obstacle (cactus) pour Dino Runner.
    Défile de droite à gauche.
    """

    def __init__(self, screen_width, ground_y, speed):

        self.screen_width = screen_width
        self.ground_y = ground_y
        self.speed = speed

        # Obtenir un type aléatoire
        self.obstacle_type = obstacle_config.get_random_type()
        self.width = self.obstacle_type.width
        self.height = self.obstacle_type.height
        self.color = self.obstacle_type.color
        self.points = self.obstacle_type.points

        # Position
        self.x = screen_width
        self.y = ground_y - self.height + self.obstacle_type.y_offset

        # ---------- HITBOX ----------
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # ---------- UPDATE ----------
    def update(self):
        """Fait défiler l'obstacle vers la gauche"""
        self.x -= self.speed
        self.rect.x = self.x

    # ---------- UTILITY ----------
    def is_offscreen(self):
        """Vérifie si l'obstacle est sorti de l'écran"""
        return self.x + self.width < 0

    def get_rect(self):
        """Retourne la hitbox"""
        return self.rect

    # ---------- DRAW ----------
    def draw(self, surface):
        """Dessine l'obstacle (rectangle vert pour l'instant)"""
        pygame.draw.rect(surface, self.color, self.rect)