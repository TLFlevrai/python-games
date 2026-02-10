import pygame
from core.colors import Colors

class QuitInterface:

    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.SysFont(None, 48)
        self.yes_button_rect = pygame.Rect(300, 200, 100, 20)
        self.no_button_rect = pygame.Rect(300, 300, 100, 20)

        self.last_click_time = 0
        self.cooldown = 1000

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        current_time = pygame.time.get_ticks()

        if self.yes_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : PONG (quit_interface.py)")
                return "YES"

        if self.no_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : NO (quit_interface.py)")
                return "NO"

    def draw(self):
        pass