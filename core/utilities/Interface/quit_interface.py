import pygame
from core.utilities.colors import Colors


class QuitInterface:
    """Interface de confirmation pour quitter l'application"""

    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.font_title = pygame.font.SysFont(None, 72)
        self.font_button = pygame.font.SysFont(None, 48)

        # Dimensions des boutons
        button_width = 150
        button_height = 60
        spacing = 40

        # Position centrée
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2

        # Boutons côte à côte
        self.yes_button_rect = pygame.Rect(
            center_x - button_width - spacing // 2,
            center_y + 50,
            button_width,
            button_height
        )

        self.no_button_rect = pygame.Rect(
            center_x + spacing // 2,
            center_y + 50,
            button_width,
            button_height
        )

        self.last_click_time = 0
        self.cooldown = 500

    def update(self):
        """Gère les clics sur les boutons"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        current_time = pygame.time.get_ticks()

        if self.yes_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : YES (quit_interface.py)")
                return "YES"

        if self.no_button_rect.collidepoint(mouse_pos) and mouse_click:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                print("button_clicked : NO (quit_interface.py)")
                return "NO"

        return None

    def draw(self, surface):
        """Dessine l'interface de confirmation"""

        # Fond semi-transparent
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(200)  # Plus opaque pour masquer le contenu
        overlay.fill((30, 30, 30))
        surface.blit(overlay, (0, 0))

        # Titre
        title = self.font_title.render("Quit Game?", True, Colors.WHITE)
        title_rect = title.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 80))
        surface.blit(title, title_rect)

        # Obtenir position de la souris pour hover
        mouse_pos = pygame.mouse.get_pos()

        # Bouton YES
        yes_color = Colors.RED if self.yes_button_rect.collidepoint(mouse_pos) else (180, 50, 50)
        pygame.draw.rect(surface, yes_color, self.yes_button_rect, border_radius=10)
        pygame.draw.rect(surface, Colors.WHITE, self.yes_button_rect, width=2, border_radius=10)

        yes_text = self.font_button.render("YES", True, Colors.WHITE)
        yes_text_rect = yes_text.get_rect(center=self.yes_button_rect.center)
        surface.blit(yes_text, yes_text_rect)

        # Bouton NO
        no_color = Colors.BUTTON_HOVER if self.no_button_rect.collidepoint(mouse_pos) else Colors.BUTTON_BG
        pygame.draw.rect(surface, no_color, self.no_button_rect, border_radius=10)
        pygame.draw.rect(surface, Colors.WHITE, self.no_button_rect, width=2, border_radius=10)

        no_text = self.font_button.render("NO", True, Colors.WHITE)
        no_text_rect = no_text.get_rect(center=self.no_button_rect.center)
        surface.blit(no_text, no_text_rect)