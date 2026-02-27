import pygame

class Obstacle:
    """Classe de base pour tous les obstacles."""

    def __init__(self, screen_width, ground_y, speed, width, height, color, points, image=None, y_offset=0):
        self.screen_width = screen_width
        self.ground_y = ground_y
        self.speed = speed
        self.width = width
        self.height = height
        self.color = color
        self.points = points
        self.image = image
        self.y_offset = y_offset

        self.x = screen_width
        self.y = ground_y - self.height + self.y_offset  # sera ajusté par les sous-classes
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def is_offscreen(self):
        return self.x + self.width < 0

    def get_rect(self):
        return self.rect

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(surface, self.color, self.rect)