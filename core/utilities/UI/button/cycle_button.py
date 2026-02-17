import pygame
from core.utilities.colors import Colors

class CycleButton:
    """
    Bouton qui défile entre plusieurs options.
    Affiche : [ ◄ ]  option  [ ► ]
    """

    def __init__(self, options, position, input_manager):

        self.options = options
        self.input = input_manager
        self.current_index = 0

        # ---------- FONTS ----------
        self.font_btn = pygame.font.SysFont(None, 32)
        self.font_value = pygame.font.SysFont("Courier New", 20)

        # ---------- DIMENSIONS ----------
        self.arrow_w = 36
        self.arrow_h = 36
        self.value_padding_x = 20
        self.value_padding_y = 8
        self.spacing = 8  # espace entre flèche et valeur

        # Calcul de la largeur de la valeur affichée
        self._compute_value_rect()

        # Largeur totale = flèche + valeur + flèche
        self.total_width = self.arrow_w + self.spacing + self.value_rect_w + self.spacing + self.arrow_w
        self.height = self.arrow_h

        # ---------- POSITION ----------
        self.rect = pygame.Rect(0, 0, self.total_width, self.height)
        self.set_position(position)

    def _compute_value_rect(self):
        """Calcule la largeur du cadre valeur selon l'option la plus longue"""
        max_width = 0
        for option in self.options:
            text_surf = self.font_value.render(str(option), True, (255, 255, 255))
            max_width = max(max_width, text_surf.get_width())
        self.value_rect_w = max_width + self.value_padding_x * 2

    def set_position(self, pos):
        """Centre le composant sur la position donnée"""
        self.rect.center = pos

        # Recalculer les rects des flèches et de la valeur
        x = self.rect.left
        y = self.rect.top

        self.left_arrow_rect = pygame.Rect(x, y, self.arrow_w, self.arrow_h)

        self.value_display_rect = pygame.Rect(
            x + self.arrow_w + self.spacing,
            y,
            self.value_rect_w,
            self.arrow_h
        )

        self.right_arrow_rect = pygame.Rect(
            x + self.arrow_w + self.spacing + self.value_rect_w + self.spacing,
            y,
            self.arrow_w,
            self.arrow_h
        )

    def get_current(self):
        """Retourne l'option actuellement sélectionnée"""
        return self.options[self.current_index]

    def set_index(self, index):
        """Définit l'index courant"""
        if 0 <= index < len(self.options):
            self.current_index = index

    # ---------- UPDATE ----------

    def update(self):
        """Retourne True si la valeur a changé"""
        mouse_pos = self.input.get_mouse_pos()

        if self.input.click():

            # Flèche gauche → précédent
            if self.left_arrow_rect.collidepoint(mouse_pos):
                self.current_index = (self.current_index - 1) % len(self.options)
                return True

            # Flèche droite → suivant
            if self.right_arrow_rect.collidepoint(mouse_pos):
                self.current_index = (self.current_index + 1) % len(self.options)
                return True

        return False

    # ---------- DRAW ----------

    def draw(self, surface):

        mouse_pos = self.input.get_mouse_pos()

        # ---------- FLÈCHE GAUCHE ----------
        self._draw_arrow(surface, self.left_arrow_rect, "<-", mouse_pos)

        # ---------- VALEUR AFFICHÉE ----------
        self._draw_value(surface)

        # ---------- FLÈCHE DROITE ----------
        self._draw_arrow(surface, self.right_arrow_rect, "->", mouse_pos)

    def _draw_arrow(self, surface, rect, symbol, mouse_pos):
        """Dessine un bouton flèche"""
        hovered = rect.collidepoint(mouse_pos)
        color = (55, 55, 60) if hovered else (35, 35, 38)
        border_color = (90, 90, 95) if hovered else (60, 60, 65)

        pygame.draw.rect(surface, color, rect, border_radius=8)
        pygame.draw.rect(surface, border_color, rect, width=1, border_radius=8)

        text = self.font_btn.render(symbol, True, (200, 200, 200) if hovered else (140, 140, 145))
        text_rect = text.get_rect(center=rect.center)
        surface.blit(text, text_rect)

    def _draw_value(self, surface):
        """Dessine la valeur actuelle avec un fond stylisé"""
        rect = self.value_display_rect

        # Fond
        pygame.draw.rect(surface, (20, 20, 22), rect, border_radius=8)
        pygame.draw.rect(surface, (70, 70, 75), rect, width=1, border_radius=8)

        # Texte
        value_text = self.font_value.render(str(self.get_current()), True, (220, 220, 220))
        text_rect = value_text.get_rect(center=rect.center)
        surface.blit(value_text, text_rect)