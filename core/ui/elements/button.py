# core/ui/elements/button.py
import pygame
from core.utilities.colors import Colors
from ..styles import ButtonStyle
from .base import UIElement

class Button(UIElement):
    def __init__(self, text, center_pos, input_manager, size=None, color=None):
        super().__init__(input_manager)
        if size is None:
            size = ButtonStyle.DEFAULT_SIZE
        self.font = pygame.font.SysFont(ButtonStyle.FONT_NAME, ButtonStyle.FONT_SIZE)
        self.rect = pygame.Rect(0, 0, *size)
        self.rect.center = center_pos
        self.text = text
        self.border_radius = ButtonStyle.BORDER_RADIUS
        self.border_width = ButtonStyle.BORDER_WIDTH

        if color:
            self.bg_color = color
            self.hover_color = self._lighten_color(color, 20)
            self.pressed_color = self._darken_color(color, 20)
        else:
            self.bg_color = ButtonStyle.BG_COLOR
            self.hover_color = ButtonStyle.HOVER_COLOR
            self.pressed_color = ButtonStyle.PRESSED_COLOR

        self.text_color = ButtonStyle.TEXT_COLOR
        self.border_color = ButtonStyle.BORDER_COLOR
        self.is_hovered = False
        self.is_pressed = False

    def _lighten_color(self, color, amount):
        return tuple(min(255, c + amount) for c in color)

    def _darken_color(self, color, amount):
        return tuple(max(0, c - amount) for c in color)

    def set_color(self, color):
        self.bg_color = color
        self.hover_color = self._lighten_color(color, 20)
        self.pressed_color = self._darken_color(color, 20)

    def update(self):
        mouse_pos = self.input.get_mouse_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        if self.is_hovered:
            self.is_pressed = self.input.pressed()
            if self.input.click():
                return True
        else:
            self.is_pressed = False
        return False

    def draw(self, surface):
        if self.is_pressed:
            current_color = self.pressed_color
        elif self.is_hovered:
            current_color = self.hover_color
        else:
            current_color = self.bg_color

        pygame.draw.rect(surface, current_color, self.rect,
                         border_radius=self.border_radius)
        pygame.draw.rect(surface, self.border_color, self.rect,
                         width=self.border_width, border_radius=self.border_radius)

        label = self.font.render(self.text, True, self.text_color)
        label_rect = label.get_rect(center=self.rect.center)
        surface.blit(label, label_rect)