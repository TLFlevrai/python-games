import pygame

class Score:

    def __init__(self, screen_width):
        self.left_score = 0
        self.right_score = 0

        self.screen_width = screen_width

        self.font = pygame.font.SysFont(None, 60)

    def add_left(self):
        self.left_score += 1

    def add_right(self):
        self.right_score += 1

    def draw(self, surface):
        text = f"{self.left_score} {self.right_score}"

        label = self.font.render(text, True, (255, 255, 255))
        rect = label.get_rect(center=(self.screen_width//2, 50))

        surface.blit(label, rect)