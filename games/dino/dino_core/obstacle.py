import pygame
import random

class Obstacle:
    """
    Obstacle (cactus) pour Dino Runner.
    Défile de droite à gauche.
    """

    # Types de cactus (hauteur différente)
    TYPES = {
        "small":  {"width": 17, "height": 35},
        "medium": {"width": 25, "height": 50},
        "tall":   {"width": 25, "height": 50},
    }

    def __init__(self, screen_width, screen_height, speed):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed

        # ---------- TYPE ALÉATOIRE ----------
        self.type = random.choice(list(self.TYPES.keys()))
        self.width = self.TYPES[self.type]["width"]
        self.height = self.TYPES[self.type]["height"]

        # ---------- POSITION ----------
        self.x = screen_width  # Commence hors écran à droite
        self.y = screen_height - 80 - self.height  # Sur le sol

        # ---------- HITBOX ----------
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # ---------- VISUEL ----------
        self.color = (83, 124, 66)  # Vert cactus

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