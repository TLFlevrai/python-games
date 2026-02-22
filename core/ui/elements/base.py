# core/ui/elements/base.py
import pygame

class UIElement:
    """Classe de base pour tous les éléments d'interface."""

    def __init__(self, input_manager=None):
        self.input = input_manager
        self.rect = pygame.Rect(0, 0, 0, 0)

    def set_position(self, pos):
        """Définit la position centrale de l'élément."""
        self.rect.center = pos

    def update(self):
        """Met à jour l'élément (retourne True si activé). À surcharger."""
        return False

    def draw(self, surface):
        """Dessine l'élément. À surcharger."""
        pass