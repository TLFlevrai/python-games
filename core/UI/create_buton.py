import pygame
from core.colors import Colors

class Button:

    def __init__(self, text, center_pos, size=(200,50), cooldown=300):

        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0,*size)
        self.rect.center = center_pos

        self.text = text

        self.last_click = 0
        self.cooldown = cooldown

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        now = pygame.time.get_ticks()

        if self.rect.collidepoint(mouse_pos):

            if mouse_click and now - self.last_click > self.cooldown:

                self.last_click = now
                return True

        return False

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()

        # hover color
        color = Colors.BUTTON_HOVER if self.rect.collidepoint(mouse_pos) else Colors.BUTTON

        pygame.draw.rect(surface, color, self.rect)

        label = self.font.render(self.text, True, Colors.WHITE)
        label_rect = label.get_rect(center=self.rect.center)

        surface.blit(label, label_rect)
