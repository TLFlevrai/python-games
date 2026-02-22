# core/ui/elements/subtitle_label.py
import pygame
from core.utilities.colors import Colors
from ..styles import SubtitleStyle
from .label import Label

class SubtitleLabel(Label):
    def __init__(self, text, position):
        # Initialiser les attributs d'animation AVANT l'appel à super()
        self.alpha = SubtitleStyle.MAX_ALPHA
        self.fade_direction = -1
        self.fade_speed = SubtitleStyle.FADE_SPEED
        self.min_alpha = SubtitleStyle.MIN_ALPHA
        self.max_alpha = SubtitleStyle.MAX_ALPHA
        self.italic_font = pygame.font.SysFont(None, SubtitleStyle.FONT_SIZE,
                                                italic=SubtitleStyle.ITALIC)
        # Appeler le parent (qui appelle render_text())
        super().__init__(text, position, font_size=SubtitleStyle.FONT_SIZE,
                         color=SubtitleStyle.COLOR, center=True)

    def render_text(self):
        self.image = self.italic_font.render(self.text, True, self.color)
        self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect()
        if self.center:
            self.rect.center = self.position
        else:
            self.rect.topleft = self.position

    def set_position(self, pos):
        self.position = pos
        self.rect.center = pos

    def update(self):
        self.alpha += self.fade_direction * self.fade_speed
        if self.alpha <= self.min_alpha:
            self.alpha = self.min_alpha
            self.fade_direction = 1
        elif self.alpha >= self.max_alpha:
            self.alpha = self.max_alpha
            self.fade_direction = -1
        self.image.set_alpha(self.alpha)
        return False

    def set_text(self, new_text):
        self.text = new_text
        self.render_text()
        if hasattr(self, 'position'):
            self.rect.center = self.position