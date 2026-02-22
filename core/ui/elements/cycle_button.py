# core/ui/elements/cycle_button.py
import pygame
from core.utilities.colors import Colors
from ..styles import CycleButtonStyle
from .base import UIElement

class CycleButton(UIElement):
    def __init__(self, options, position, input_manager):
        super().__init__(input_manager)
        self.options = options
        self.current_index = 0

        self.font_btn = pygame.font.SysFont(None, CycleButtonStyle.FONT_BTN_SIZE)
        self.font_value = pygame.font.SysFont(CycleButtonStyle.FONT_VALUE_NAME,
                                              CycleButtonStyle.FONT_VALUE_SIZE)

        self.arrow_w = CycleButtonStyle.ARROW_SIZE
        self.arrow_h = CycleButtonStyle.ARROW_SIZE
        self.value_padding_x = CycleButtonStyle.VALUE_PADDING_X
        self.spacing = CycleButtonStyle.SPACING

        self._compute_value_rect()
        self.total_width = (self.arrow_w + self.spacing + self.value_rect_w +
                            self.spacing + self.arrow_w)
        self.height = self.arrow_h
        self.rect = pygame.Rect(0, 0, self.total_width, self.height)
        self.set_position(position)

    def _compute_value_rect(self):
        max_width = 0
        for opt in self.options:
            surf = self.font_value.render(str(opt), True, (0,0,0))
            max_width = max(max_width, surf.get_width())
        self.value_rect_w = max_width + self.value_padding_x * 2

    def set_position(self, pos):
        self.rect.center = pos
        x, y = self.rect.topleft
        self.left_arrow_rect = pygame.Rect(x, y, self.arrow_w, self.arrow_h)
        self.value_display_rect = pygame.Rect(x + self.arrow_w + self.spacing, y,
                                              self.value_rect_w, self.arrow_h)
        self.right_arrow_rect = pygame.Rect(x + self.arrow_w + self.spacing +
                                            self.value_rect_w + self.spacing, y,
                                            self.arrow_w, self.arrow_h)

    def get_current(self):
        return self.options[self.current_index]

    def set_index(self, index):
        if 0 <= index < len(self.options):
            self.current_index = index

    def update(self):
        mouse_pos = self.input.get_mouse_pos()
        if self.input.click():
            if self.left_arrow_rect.collidepoint(mouse_pos):
                self.current_index = (self.current_index - 1) % len(self.options)
                return True
            if self.right_arrow_rect.collidepoint(mouse_pos):
                self.current_index = (self.current_index + 1) % len(self.options)
                return True
        return False

    def _draw_arrow(self, surface, rect, symbol, mouse_pos):
        hovered = rect.collidepoint(mouse_pos)
        color = CycleButtonStyle.HOVER_COLOR if hovered else CycleButtonStyle.BG_COLOR
        border_color = CycleButtonStyle.BORDER_COLOR
        pygame.draw.rect(surface, color, rect, border_radius=8)
        pygame.draw.rect(surface, border_color, rect, width=1, border_radius=8)
        text_color = (CycleButtonStyle.TEXT_COLOR if hovered
                      else CycleButtonStyle.TEXT_SECONDARY)
        text = self.font_btn.render(symbol, True, text_color)
        text_rect = text.get_rect(center=rect.center)
        surface.blit(text, text_rect)

    def _draw_value(self, surface):
        rect = self.value_display_rect
        pygame.draw.rect(surface, CycleButtonStyle.VALUE_BG, rect, border_radius=8)
        pygame.draw.rect(surface, CycleButtonStyle.VALUE_BORDER, rect, width=1, border_radius=8)
        text = self.font_value.render(str(self.get_current()), True,
                                      CycleButtonStyle.TEXT_COLOR)
        text_rect = text.get_rect(center=rect.center)
        surface.blit(text, text_rect)

    def draw(self, surface):
        mouse_pos = self.input.get_mouse_pos()
        self._draw_arrow(surface, self.left_arrow_rect, "<-", mouse_pos)
        self._draw_value(surface)
        self._draw_arrow(surface, self.right_arrow_rect, "->", mouse_pos)