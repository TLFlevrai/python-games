import pygame

class Paddle:

    def __init__(self, x, y, width=10, height=100, speed=10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0

    def move_down(self, screen_height):
        self.y += self.speed
        if self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255,), (self.x, self.y, self.width, self.height))