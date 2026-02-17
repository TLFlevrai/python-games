import pygame
from games.flappy_bird.flappy_bird_core.flappy_bird_config import FlappyBirdConfig

class Bird:

    def __init__(self, x, y):

        # position
        self.x = x
        self.y = y

        # taille
        self.width = FlappyBirdConfig.BIRD_WIDTH
        self.height = FlappyBirdConfig.BIRD_HEIGHT

        # physique
        self.gravity = FlappyBirdConfig.BIRD_GRAVITY
        self.jump_strength = FlappyBirdConfig.BIRD_JUMP_STRENGTH
        self.velocity_y = 0

        # rotation (visuelle)
        self.rotation = 0

        # état
        self.alive = True

        # hitbox
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # ---------- INPUT ----------

    def flap(self):

        if self.alive:
            self.velocity_y = self.jump_strength

    # ---------- UPDATE ----------

    def update(self):

        if not self.alive:
            return

        # appliquer gravité
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # rotation (visuel)
        if self.velocity_y < 0:
            self.rotation = -FlappyBirdConfig.BIRD_ROTATION_UP
        else:
            self.rotation = min(90, self.rotation + 3)

        # update rect
        self.rect.topleft = (self.x, self.y)

    # ---------- COLLISION ----------

    def get_rect(self):
        return self.rect

    # ---------- DRAW ----------

    def draw(self, surface):

        # dessin simple (rectangle jaune)
        pygame.draw.rect(surface, (255,255,0), self.rect)

    # ---------- RESET ----------

    def reset(self, x, y):

        self.x = x
        self.y = y

        self.velocity_y = 0
        self.rotation = 0
        self.alive = True

        self.rect.topleft = (self.x, self.y)