import pygame

class PauseButton:
    """
    Petit bouton pause discret positionné en haut à droite.
    Affiche ▐▐ quand en jeu et ▶ quand en pause.
    """

    def __init__(self, screen_width, input_manager):

        self.input = input_manager

        # ---------- DIMENSIONS ----------
        self.size = 36
        self.margin = 15

        self.rect = pygame.Rect(
            screen_width - self.size - self.margin,
            self.margin,
            self.size,
            self.size
        )

        # ---------- FONTS ----------
        self.font = pygame.font.SysFont("Courier New", 14)

        # ---------- SURFACE ----------
        self.hovered = False

    # ---------- UPDATE ----------

    def update(self, state):

        mouse_pos = self.input.get_mouse_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)

        if self.hovered and self.input.click():

            if state == "playing":
                return "PAUSE"

            elif state == "paused":
                return "RESUME"

        return None

    # ---------- DRAW ----------

    def draw(self, surface, state):

        # ---------- FOND ----------
        color = (55, 55, 60) if self.hovered else (30, 30, 33)
        border_color = (90, 90, 95) if self.hovered else (55, 55, 60)

        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, border_color, self.rect, width=1, border_radius=8)

        # ---------- ICONE ----------
        icon = "▶" if state == "paused" else "▐▐"
        icon_color = (200, 200, 200) if self.hovered else (150, 150, 155)

        icon_surf = self.font.render(icon, True, icon_color)
        icon_rect = icon_surf.get_rect(center=self.rect.center)
        surface.blit(icon_surf, icon_rect)