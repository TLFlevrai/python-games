import pygame

class Menu:

    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.SysFont(None, 48)
        self.pong_button_rect = pygame.Rect(300, 200, 200, 50)
        self.settings_button_rect = pygame.Rect(275, 300, 250, 50)
        self.quit_button_rect = pygame.Rect(300, 400, 200, 50)

        self.last_click_time = 0
        self.cooldown = 1000

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        current_time = pygame.time.get_ticks()

        if self.pong_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : PONG (menu.py)")
                return "PONG"

        if self.settings_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : SETTINGS (menu.py)")
                return "SETTINGS"

        if self.quit_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : QUIT (menu.py)")
                return "QUIT"

    def draw(self, surface):
        title = self.font.render("MENU", True, (255, 255, 255))
        surface.blit(title, (350, 100))

        #pong
        pygame.draw.rect(surface, (100, 100, 255), self.pong_button_rect)
        pong_text = self.font.render("PONG", True, (255, 255, 255))
        surface.blit(pong_text, (self.pong_button_rect.x + 50, self.pong_button_rect.y + 10))

        #settings
        pygame.draw.rect(surface, (100, 100, 255), self.settings_button_rect)
        settings_text = self.font.render("SETTINGS", True, (255, 255, 255))
        surface.blit(settings_text, (self.settings_button_rect.x + 40, self.settings_button_rect.y + 10))

        #quit
        pygame.draw.rect(surface, (100, 100, 255), self.quit_button_rect)
        quit_text = self.font.render("QUIT", True, (255, 255, 255))
        surface.blit(quit_text, (self.quit_button_rect.x + 50, self.quit_button_rect.y + 10))