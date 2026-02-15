import pygame

class Label:

    def __init__(self, text, position, font_size=36, color=(255,255,255), center=True):

        self.text = text
        self.position = position
        self.color = color
        self.center = center

        self.font = pygame.font.SysFont(None, font_size)

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

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_position(self, pos):
        self.rect.center = pos
