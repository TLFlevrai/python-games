import pygame
from core.utilities.UI.create_buton import Button

class Settings:

    def __init__(self, screen):
        self.screen = screen

        w = screen.get_width()  # 800
        h = screen.get_height()  # 600

        self.font = pygame.font.SysFont(None, 48)

        self.return_button = Button("RETURN", (100, 400))

        self.last_click_time = 0
        self.cooldown = 1000

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        current_time = pygame.time.get_ticks()

        if self.button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : RETURN (settings.py)")
                return "RETURN"

    def draw(self, surface):
        title = self.font.render("SETTINGS", True, (255, 255, 255))
        surface.blit(title, (340, 50))

        pygame.draw.rect(surface, (100, 100, 255), self.button_rect)
        text = self.font.render("RETURN", True, (255, 255, 255))
        surface.blit(text, (self.button_rect.x + 30, self.button_rect.y + 10))
