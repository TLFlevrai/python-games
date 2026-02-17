import pygame
import random

class Ball:

    SKINS = {
        "White": "assets/pong/ball/White_ball.png",
        "Blue":  "assets/pong/ball/Blue_ball.png",
        "Red":   "assets/pong/ball/Red_ball.png",
    }

    def __init__(self, screen_width=800, screen_height=600, speed=5, skin="White"):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed

        # ---------- ASSET ----------
        self.size = 32  # Taille fixe des assets
        self.radius = self.size // 2

        self.set_skin(skin)
        self.reset()

    def set_skin(self, skin):
        """Change le skin de la balle"""
        if skin in self.SKINS:
            try:
                self.image = pygame.image.load(self.SKINS[skin]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.size, self.size))
                self.skin = skin
            except (pygame.error, FileNotFoundError) as e:
                print(f"⚠️ Ball skin '{skin}' not found: {e}")
                self.image = None
                self.skin = "White"

    def reset(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2

        self.vx = self.speed if random.choice([True, False]) else -self.speed
        self.vy = random.choice([-self.speed, self.speed])

    def update(self, paddle_left, paddle_right):

        self.x += self.vx
        self.y += self.vy

        # Rebond murs haut/bas
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.vy = -self.vy

        # Collisions paddles
        rect_ball = pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.size,
            self.size
        )

        rect_left = pygame.Rect(paddle_left.x, paddle_left.y, paddle_left.width, paddle_left.height)
        rect_right = pygame.Rect(paddle_right.x, paddle_right.y, paddle_right.width, paddle_right.height)

        if rect_ball.colliderect(rect_left) or rect_ball.colliderect(rect_right):
            self.vx = -self.vx

        # Score
        if self.x < 0:
            self.reset()
            return "RIGHT_SCORE"
        elif self.x > self.screen_width:
            self.reset()
            return "LEFT_SCORE"

        return None

    def draw(self, surface):

        if self.image:
            surface.blit(self.image, (self.x - self.radius, self.y - self.radius))
        else:
            # Fallback cercle blanc
            pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)