import pygame

class GameOverInterface:
    """
    Overlay Game Over pour Tic Tac Toe.
    Style moderne HUD en bas de l'écran.
    """

    def __init__(self, surface, input_manager):

        self.surface = surface
        self.input = input_manager

        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        # ---------- FONTS ----------
        self.font_title = pygame.font.SysFont("Courier New", 18)
        self.font_winner = pygame.font.SysFont("Courier New", 24, bold=True)
        self.font_button = pygame.font.SysFont(None, 28)

        # ---------- HUD PANEL ----------
        self.panel_width = 360
        self.panel_height = 140
        self.panel_x = self.screen_width // 2 - self.panel_width // 2
        self.panel_y = self.screen_height - self.panel_height - 20
        self.panel_rect = pygame.Rect(self.panel_x, self.panel_y, self.panel_width, self.panel_height)

        # ---------- BOUTONS ----------
        btn_w, btn_h = 140, 40
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

        # ---------- OVERLAY ----------
        self.overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

    # ---------- UPDATE ----------

    def update(self, winner):

        mouse_pos = self.input.get_mouse_pos()

        if self.input.click():

            if self.restart_rect.collidepoint(mouse_pos):
                return "RESTART"

            if self.menu_rect.collidepoint(mouse_pos):
                return "MENU"

        return None

    # ---------- DRAW ----------

    def draw(self, surface, winner):

        # Overlay sombre
        self.overlay.fill((0, 0, 0, 130))
        surface.blit(self.overlay, (0, 0))

        # ---------- PANEL FOND ----------
        panel_surf = pygame.Surface((self.panel_width, self.panel_height), pygame.SRCALPHA)
        panel_surf.fill((0, 0, 0, 0))

        # Couleur bordure selon résultat
        if winner == "DRAW":
            border_color = (140, 140, 145, 200)
        elif winner == "X":
            border_color = (50, 120, 215, 200)  # Bleu
        else:  # O
            border_color = (215, 60, 50, 200)   # Rouge

        pygame.draw.rect(
            panel_surf,
            (20, 20, 22, 220),
            pygame.Rect(0, 0, self.panel_width, self.panel_height),
            border_radius=16
        )
        pygame.draw.rect(
            panel_surf,
            border_color,
            pygame.Rect(0, 0, self.panel_width, self.panel_height),
            width=2,
            border_radius=16
        )

        surface.blit(panel_surf, (self.panel_x, self.panel_y))

        # ---------- TEXTE STYLE CODE ----------
        title_text = self.font_title.render("game_over", True, (140, 140, 145))
        surface.blit(title_text, (self.panel_x + 16, self.panel_y + 14))

        # ---------- RÉSULTAT ----------
        if winner == "DRAW":
            result_text = "Draw!"
            result_color = (160, 160, 165)
        elif winner == "X":
            result_text = "Player X wins!"
            result_color = (80, 150, 255)  # Bleu clair
        else:  # O
            result_text = "Player O wins!"
            result_color = (255, 100, 90)  # Rouge clair

        winner_surf = self.font_winner.render(result_text, True, result_color)
        surface.blit(winner_surf, (self.panel_x + 16, self.panel_y + 42))

        # ---------- BOUTONS ----------
        mouse_pos = self.input.get_mouse_pos()
        self._draw_button(surface, self.restart_rect, "RESTART", mouse_pos)
        self._draw_button(surface, self.menu_rect, "MENU", mouse_pos, accent=True)

    def _draw_button(self, surface, rect, text, mouse_pos, accent=False):

        hovered = rect.collidepoint(mouse_pos)

        if accent:
            color = (50, 30, 28) if hovered else (35, 20, 20)
            border_color = (200, 80, 70) if hovered else (140, 60, 50)
        else:
            color = (55, 55, 60) if hovered else (35, 35, 38)
            border_color = (90, 90, 95) if hovered else (60, 60, 65)

        pygame.draw.rect(surface, color, rect, border_radius=10)
        pygame.draw.rect(surface, border_color, rect, width=1, border_radius=10)

        label = self.font_button.render(text, True, (230, 230, 230))
        label_rect = label.get_rect(center=rect.center)
        surface.blit(label, label_rect)