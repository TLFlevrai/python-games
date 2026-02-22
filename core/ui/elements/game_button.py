# core/ui/elements/game_button.py
import pygame
from ..styles import GameButtonStyle
from .base import UIElement

class GameButton(UIElement):
    def __init__(self, text, logo_path, position, input_manager):
        super().__init__(input_manager)
        self.text = text
        self.width = GameButtonStyle.WIDTH
        self.height = GameButtonStyle.HEIGHT
        self.border_radius = GameButtonStyle.BORDER_RADIUS
        self.logo_size = GameButtonStyle.LOGO_SIZE
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = position
        self.font = pygame.font.SysFont(GameButtonStyle.FONT_NAME, GameButtonStyle.FONT_SIZE)

        try:
            raw = pygame.image.load(logo_path).convert_alpha()
            self.logo = pygame.transform.scale(raw, (self.logo_size, self.logo_size))
        except (pygame.error, FileNotFoundError) as e:
            print(f"⚠️ Logo '{logo_path}' not found: {e}")
            self.logo = None

        self.is_hovered = False
        self.is_pressed = False

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
            bg_color = GameButtonStyle.BG_PRESSED
            border_color = GameButtonStyle.BORDER_PRESSED
            text_color = GameButtonStyle.TEXT_NORMAL  # ou légèrement différent
        elif self.is_hovered:
            bg_color = GameButtonStyle.BG_HOVER
            border_color = GameButtonStyle.BORDER_HOVER
            text_color = GameButtonStyle.TEXT_HOVER
        else:
            bg_color = GameButtonStyle.BG_NORMAL
            border_color = GameButtonStyle.BORDER_NORMAL
            text_color = GameButtonStyle.TEXT_NORMAL

        pygame.draw.rect(surface, bg_color, self.rect,
                         border_radius=self.border_radius)
        pygame.draw.rect(surface, border_color, self.rect,
                         width=1, border_radius=self.border_radius)

        if self.logo:
            logo_x = self.rect.centerx - self.logo_size // 2
            logo_y = self.rect.top + 30
            surface.blit(self.logo, (logo_x, logo_y))
        else:
            fallback = pygame.Rect(self.rect.centerx - 25, self.rect.top + 30, 50, 50)
            pygame.draw.rect(surface, GameButtonStyle.FALLBACK_COLOR,
                             fallback, border_radius=8)

        label = self.font.render(self.text.upper(), True, text_color)
        label_rect = label.get_rect(center=(self.rect.centerx, self.rect.bottom - 25))
        surface.blit(label, label_rect)