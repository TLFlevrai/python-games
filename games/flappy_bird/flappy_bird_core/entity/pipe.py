import pygame
import random
from games.flappy_bird.flappy_bird_core.flappy_bird_config import FlappyBirdConfig

class Pipe:

    def __init__(self, screen_width, screen_height, speed):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.width = FlappyBirdConfig.PIPE_WIDTH
        self.gap_size = FlappyBirdConfig.PIPE_GAP_SIZE

        self.speed = speed

        # position initiale
        self.x = screen_width

        # gap random
        self.gap_y = random.randint(FlappyBirdConfig.PIPE_MARGIN, screen_height - FlappyBirdConfig.PIPE_MARGIN)

        # flag score
        self.scored = False

    # ---------- UPDATE ----------

    def update(self):
        self.x -= self.speed

    # ---------- RECTANGLES ----------

    def get_rects(self):

        top_rect = pygame.Rect(
            self.x,
            0,
            self.width,
            self.gap_y - self.gap_size // 2
        )

        bottom_rect = pygame.Rect(
            self.x,
            self.gap_y + self.gap_size // 2,
            self.width,
            self.screen_height
        )

        return top_rect, bottom_rect

    # ---------- DRAW ----------

    def draw(self, surface):
        top_rect, bottom_rect = self.get_rects()
        pygame.draw.rect(surface, (0, 255, 0), top_rect)
        pygame.draw.rect(surface, (0, 255, 0), bottom_rect)

    # ---------- UTILITY ----------

    def is_offscreen(self):
        return self.x + self.width < 0

    # ---------- COLLISION ----------

    def collide(self, bird_rect):
        top_rect, bottom_rect = self.get_rects()
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
            return True
        return False

    # ---------- SCORE ----------

    def check_score(self, bird_rect):
        if not self.scored and bird_rect.x > self.x + self.width:
            self.scored = True
            return True
        return False