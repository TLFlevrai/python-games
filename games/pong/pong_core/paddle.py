import pygame

class Paddle:

    SKINS = {
        "Blue": "assets/pong/paddle/Blue_Paddle.png",
        "Red":  "assets/pong/paddle/Red_Paddle.png",
    }

    def __init__(self, x, y, width=8, height=64, speed=10, skin="Blue"):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.set_skin(skin)

    def set_skin(self, skin):
        """Change le skin du paddle"""
        if skin in self.SKINS:
            try:
                self.image = pygame.image.load(self.SKINS[skin]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.skin = skin
            except (pygame.error, FileNotFoundError) as e:
                print(f"⚠️ Paddle skin '{skin}' not found: {e}")
                self.image = None
                self.skin = skin

    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0

    def move_down(self, screen_height):
        self.y += self.speed
        if self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def draw(self, surface):

        if self.image:
            surface.blit(self.image, (self.x, self.y))
        else:
            # Fallback rectangle blanc
            pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height))