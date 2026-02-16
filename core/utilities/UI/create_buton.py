import pygame
from core.utilities.colors import Colors

class Button:

    def __init__(self, text, center_pos, input_manager, size=(200, 50), color=None):

        self.input = input_manager
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, *size)
        self.rect.center = center_pos

        self.text = text

        # ---------- STYLE MODERNE ----------
        self.border_radius = 10  # Coins arrondis Windows 11 style
        self.border_width = 2    # Bordure subtile
        
        # Couleurs personnalisables
        if color:
            # Si une couleur d'accent est fournie
            self.bg_color = color
            self.hover_color = self._lighten_color(color, 20)
            self.pressed_color = self._darken_color(color, 20)
        else:
            # Couleurs par défaut (gris sobre)
            self.bg_color = Colors.BUTTON_BG
            self.hover_color = Colors.BUTTON_HOVER
            self.pressed_color = Colors.BUTTON_PRESSED
        
        self.text_color = Colors.BUTTON_TEXT
        self.border_color = Colors.BUTTON_BORDER
        
        # États
        self.is_hovered = False
        self.is_pressed = False

    # ---------- UTILITAIRES COULEUR ----------
    
    def _lighten_color(self, color, amount):
        """Éclaircit une couleur"""
        return tuple(min(255, c + amount) for c in color)
    
    def _darken_color(self, color, amount):
        """Assombrit une couleur"""
        return tuple(max(0, c - amount) for c in color)

    # ---------- MÉTHODE PUBLIQUE ----------
    
    def set_color(self, color):
        """Permet de changer la couleur du bouton après création"""
        self.bg_color = color
        self.hover_color = self._lighten_color(color, 20)
        self.pressed_color = self._darken_color(color, 20)

    # ---------- UPDATE ----------

    def update(self):

        mouse_pos = self.input.get_mouse_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
        # Détection du clic
        if self.is_hovered:
            
            # État pressed pendant le clic
            if self.input.pressed():
                self.is_pressed = True
            else:
                self.is_pressed = False
            
            # Action au relâchement
            if self.input.click():
                return True

        return False

    # ---------- DRAW ----------

    def draw(self, surface):

        # Sélection de la couleur selon l'état
        if self.is_pressed:
            current_color = self.pressed_color
        elif self.is_hovered:
            current_color = self.hover_color
        else:
            current_color = self.bg_color

        # ---------- FOND ARRONDI ----------
        pygame.draw.rect(
            surface,
            current_color,
            self.rect,
            border_radius=self.border_radius
        )

        # ---------- BORDURE ARRONDIE ----------
        pygame.draw.rect(
            surface,
            self.border_color,
            self.rect,
            width=self.border_width,
            border_radius=self.border_radius
        )

        # ---------- TEXTE CENTRÉ ----------
        label = self.font.render(self.text, True, self.text_color)
        label_rect = label.get_rect(center=self.rect.center)
        surface.blit(label, label_rect)

    # ---------- POSITION ----------

    def set_position(self, pos):
        self.rect.center = pos