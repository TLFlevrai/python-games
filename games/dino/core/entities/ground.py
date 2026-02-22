# games/dino/core/entities/ground.py

import pygame
from ..configs import game_config


class Ground:
    """Représente le sol du jeu Dino Runner."""

    def __init__(self, screen_height: int):
        """
        Args:
            screen_height: Hauteur de l'écran en pixels.
        """
        self.screen_height = screen_height
        self.level = game_config.ground_level
        self.color = game_config.ground_color
        self.thickness = game_config.ground_line_thickness
        self.y = screen_height - self.level

    def get_y(self) -> int:
        """Retourne la position verticale du sol (ligne)."""
        return self.y

    def draw(self, surface: pygame.Surface) -> None:
        """Dessine la ligne de sol sur la surface donnée."""
        pygame.draw.line(
            surface,
            self.color,
            (0, self.y),
            (surface.get_width(), self.y),
            self.thickness
        )