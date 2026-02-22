# core/ui/elements/label.py
import pygame
from ..styles import LabelStyle
from .base import UIElement

class Label(UIElement):
    def __init__(self, text, position, font_size=None, color=None, center=True):
        super().__init__(input_manager=None)  # Pas besoin d'input
        if font_size is None:
            font_size = LabelStyle.DEFAULT_FONT_SIZE
        if color is None:
            color = LabelStyle.DEFAULT_COLOR
        self.text = text
        self.position = position
        self.color = color
        self.center = center
        self.font = pygame.font.SysFont(LabelStyle.FONT_NAME, font_size)
        self.render_text()

    def render_text(self):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        if self.center:
            self.rect.center = self.position
        else:
            self.rect.topleft = self.position

    def set_text(self, new_text):
        self.text = new_text
        self.render_text()

    def set_color(self, new_color):
        self.color = new_color
        self.render_text()

    def set_position(self, pos):
        self.position = pos
        self.rect.center = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)