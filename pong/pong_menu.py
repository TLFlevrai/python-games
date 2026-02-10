import pygame
from core.colors import Colors
from core.UI.create_buton import Button

class PongMenu:

    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.SysFont(None, 48)
        self.play_button_rect = pygame.Rect(100, 200, 200, 50)
        self.settings_button_rect = pygame.Rect(100, 300, 250, 50)
        self.return_button_rect = pygame.Rect(100, 400, 200, 50)
        self.quit_button_rect = pygame.Rect(100, 500, 200, 50)

        self.last_click_time = 0
        self.cooldown = 1000

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        current_time = pygame.time.get_ticks()

        if self.play_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : PLAY (pong_menu.py)")
                return "PLAY"

        if self.return_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : SETTINGS (pong_menu.py)")
                return "SETTINGS"

        if self.return_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : RETURN (pong_menu.py)")
                return "RETURN"

        return None

    def draw(self, surface):
        title = self.font.render("PONG", True, Colors.WHITE)
        surface.blit(title, (100, 100))

        #button play
        pygame.draw.rect(surface, Colors.BUTTON, self.play_button_rect)
        play_text = self.font.render("Play", True, Colors.WHITE)
        surface.blit(play_text, (self.play_button_rect.x + 60, self.play_button_rect.y + 10))

        #button settings
        pygame.draw.rect(surface, Colors.BUTTON, self.settings_button_rect)
        settings_text = self.font.render("Settings", True, Colors.WHITE)
        surface.blit(settings_text, (self.settings_button_rect.x + 50, self.settings_button_rect.y + 10))

        #button return
        pygame.draw.rect(surface, Colors.BUTTON, self.return_button_rect)
        return_text = self.font.render("return", True, Colors.WHITE)
        surface.blit(return_text, (self.return_button_rect.x + 50, self.return_button_rect.y + 10))

        #button quit