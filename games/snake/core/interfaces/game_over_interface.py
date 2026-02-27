import pygame
from core.utilities.colors import Colors

class GameOverInterface:
    """
    Overlay Game Over pour Snake.
    Affiche le score final et le high score.
    """

    def __init__(self, surface, input_manager):
        self.surface = surface
        self.input = input_manager

        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.font_title = pygame.font.SysFont("Courier New", 18)
        self.font_score = pygame.font.SysFont("Courier New", 14)
        self.font_button = pygame.font.SysFont(None, 28)

        self.panel_width = 340
        self.panel_height = 160  # assez grand pour deux lignes de score
        self.panel_x = self.screen_width // 2 - self.panel_width // 2
        self.panel_y = self.screen_height - self.panel_height - 20

        # Boutons
        btn_w, btn_h = 120, 40
        btn_y = self.panel_y + self.panel_height - btn_h - 15
        self.restart_rect = pygame.Rect(
            self.screen_width // 2 - btn_w - 10,
            btn_y,
            btn_w, btn_h
        )
        self.menu_rect = pygame.Rect(
            self.screen_width // 2 + 10,
            btn_y,
            btn_w, btn_h
        )

        self.overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

    def update(self, current_score, high_score):
        mouse_pos = self.input.get_mouse_pos()
        if self.input.click():
            if self.restart_rect.collidepoint(mouse_pos):
                return "RESTART"
            if self.menu_rect.collidepoint(mouse_pos):
                return "MENU"
        return None

    def draw(self, surface, current_score, high_score):
        # Overlay sombre
        self.overlay.fill((0, 0, 0, 130))
        surface.blit(self.overlay, (0, 0))

        # Panneau
        panel_surf = pygame.Surface((self.panel_width, self.panel_height), pygame.SRCALPHA)
        pygame.draw.rect(
            panel_surf,
            (20, 20, 22, 220),
            pygame.Rect(0, 0, self.panel_width, self.panel_height),
            border_radius=16
        )
        pygame.draw.rect(
            panel_surf,
            (180, 50, 40, 200),  # Bordure rouge (game over)
            pygame.Rect(0, 0, self.panel_width, self.panel_height),
            width=1,
            border_radius=16
        )
        surface.blit(panel_surf, (self.panel_x, self.panel_y))

        # Titre
        title = self.font_title.render("game_over", True, (180, 70, 60))
        surface.blit(title, (self.panel_x + 16, self.panel_y + 14))

        # Score actuel
        score_text = self.font_score.render(f"score: {current_score:05d}", True, (140, 140, 145))
        surface.blit(score_text, (self.panel_x + 16, self.panel_y + 38))

        # High score
        high_score_text = self.font_score.render(f"high score: {high_score:05d}", True, (140, 140, 145))
        surface.blit(high_score_text, (self.panel_x + 16, self.panel_y + 58))

        # Boutons
        mouse_pos = self.input.get_mouse_pos()
        self._draw_button(surface, self.restart_rect, "RESTART", mouse_pos)
        self._draw_button(surface, self.menu_rect, "MENU", mouse_pos, accent=True)

    def _draw_button(self, surface, rect, text, mouse_pos, accent=False):
        hovered = rect.collidepoint(mouse_pos)
        if accent:
            color = (50, 30, 28) if hovered else (35, 20, 20)
            border_color = (160, 60, 50) if hovered else (120, 45, 38)
        else:
            color = (55, 55, 60) if hovered else (35, 35, 38)
            border_color = (90, 90, 95) if hovered else (60, 60, 65)

        pygame.draw.rect(surface, color, rect, border_radius=10)
        pygame.draw.rect(surface, border_color, rect, width=1, border_radius=10)

        label = self.font_button.render(text, True, (230, 230, 230))
        label_rect = label.get_rect(center=rect.center)
        surface.blit(label, label_rect)