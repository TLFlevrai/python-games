import pygame
import random

class Ball:

    def __init__(self, screen_width=800, screen_height=600, radius=10, speed=5):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = radius
        self.speed = speed

        self.reset()

    def reset(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2

        self.vx = self.speed if random.choice([True, False]) else -self.speed
        self.vy = random.choice([-self.speed, self.speed])

    def update(self, paddle_left, paddle_right):

        self.x += self.vx
        self.y += self.vy

        # rebond murs haut/bas
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.vy = -self.vy

        # collisions paddles
        rect_ball = pygame.Rect(self.x - self.radius,
                                self.y - self.radius,
                                self.radius * 2,
                                self.radius * 2)

        rect_left = pygame.Rect(paddle_left.x,
                                paddle_left.y,
                                paddle_left.width,
                                paddle_left.height)
        rect_right = pygame.Rect(paddle_right.x,
                                 paddle_right.y,
                                 paddle_right.width,
                                 paddle_right.height)

        if rect_ball.colliderect(rect_left) or rect_ball.colliderect(rect_right):
            self.vx = -self.vx

        # score
        if self.x < 0:
            self.reset()
            return "RIGHT_SCORE"
        elif self.x > self.screen_width:
            self.reset()
            return "LEFT_SCORE"

        return None

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)