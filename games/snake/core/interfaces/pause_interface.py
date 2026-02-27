import pygame
from core.utilities.colors import Colors

class PauseInterface:
    """
    Overlay Pause pour Snake.
    HUD discret en bas de l'écran.
    """

    def __init__(self, surface, input_manager):
        self.surface = surface
        self.input = input_manager

        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.font_title = pygame.font.SysFont("Courier New", 18)
        self.font_button = pygame.font.SysFont(None, 28)

        # Panneau
        self.panel_width = 360
        self.panel_height = 110
        self.panel_x = self.screen_width // 2 - self.panel_width // 2
        self.panel_y = self.screen_height - self.panel_height - 20

        # Boutons
        btn_w, btn_h = 100, 40
        btn_y = self.panel_y + self.panel_height - btn_h - 15
        spacing = 10

        self.resume_rect = pygame.Rect(
            self.screen_width // 2 - (btn_w * 1.5 + spacing),
            btn_y,
            btn_w, btn_h
        )
        self.restart_rect = pygame.Rect(
            self.screen_width // 2 - btn_w // 2,
            btn_y,
            btn_w, btn_h
        )
        self.menu_rect = pygame.Rect(
            self.screen_width // 2 + (btn_w // 2 + spacing),
            btn_y,
            btn_w, btn_h
        )

        #overlay
        self.overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

    def update(self):
        mouse_pos = self.input.get_mouse_pos()
        if self.input.click():
            if self.resume_rect.collidepoint(mouse_pos):
                return "RESUME"
            if self.restart_rect.collidepoint(mouse_pos):
                return "RESTART"
            if self.menu_rect.collidepoint(mouse_pos):
                return "MENU"
        return None

    def draw(self, surface):
        # Overlay sombre
        self.overlay.fill((0, 0, 0, 100))
        surface.blit(self.overlay, (0, 0))

        # Panneau
        panel_surf = pygame.Surface((self.panel_width, self.panel_height), pygame.SRCALPHA)
        pygame.draw.rect(
            panel_surf,
            (20, 20, 22, 210),
            pygame.Rect(0, 0, self.panel_width, self.panel_height),
            border_radius=16
        )
        pygame.draw.rect(
            panel_surf,
            (70, 70, 75, 180),
            pygame.Rect(0, 0, self.panel_width, self.panel_height),
            width=1,
            border_radius=16
        )
        surface.blit(panel_surf, (self.panel_x, self.panel_y))

        # Titre
        title = self.font_title.render("game_paused", True, (120, 120, 125))
        surface.blit(title, (self.panel_x + 16, self.panel_y + 14))

        # Boutons
        mouse_pos = self.input.get_mouse_pos()
        self._draw_button(surface, self.resume_rect, "RESUME", mouse_pos)
        self._draw_button(surface, self.restart_rect, "RESTART", mouse_pos)
        self._draw_button(surface, self.menu_rect, "MENU", mouse_pos)

    def _draw_button(self, surface, rect, text, mouse_pos):
        hovered = rect.collidepoint(mouse_pos)
        color = (55, 55, 60) if hovered else (35, 35, 38)
        border_color = (90, 90, 95) if hovered else (60, 60, 65)

        pygame.draw.rect(surface, color, rect, border_radius=10)
        pygame.draw.rect(surface, border_color, rect, width=1, border_radius=10)

        label = self.font_button.render(text, True, (230, 230, 230))
        label_rect = label.get_rect(center=rect.center)
        surface.blit(label, label_rect)