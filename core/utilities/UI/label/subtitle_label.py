import pygame
from core.utilities.UI.label.create_label import Label
from core.utilities.colors import Colors

class SubtitleLabel(Label):
    """
    Sous-titre stylisé avec effet visuel subtil.
    Design simple et amusant pour accompagner un titre principal.
    """

    def __init__(self, text, position):

        # ---------- CRÉER LES ATTRIBUTS AVANT LE SUPER() ----------
        self.italic_font = pygame.font.SysFont(None, 28, italic=True)
        
        # Animation subtile
        self.alpha = 255
        self.fade_direction = -1
        self.fade_speed = 2
        self.min_alpha = 150
        self.max_alpha = 255

        # ---------- APPELER LE PARENT APRÈS ----------
        super().__init__(
            text,
            position,
            font_size=28,              # Plus petit que le titre
            color=Colors.GRAY,         # Couleur sobre
            center=True
        )

    def render_text(self):
        """Rendu avec style italique"""
        self.image = self.italic_font.render(self.text, True, self.color)
        
        # Appliquer la transparence
        self.image.set_alpha(self.alpha)
        
        self.rect = self.image.get_rect()

        if self.center:
            self.rect.center = self.position
        else:
            self.rect.topleft = self.position

    def set_position(self, pos):
        """Override pour sauvegarder la position"""
        self.position = pos  # ← SAUVEGARDER LA POSITION
        self.rect.center = pos

    def update(self):
        """Animation de fade subtile"""
        
        # Faire osciller la transparence légèrement
        self.alpha += self.fade_direction * self.fade_speed
        
        # Inverser la direction aux limites
        if self.alpha <= self.min_alpha:
            self.alpha = self.min_alpha
            self.fade_direction = 1
        elif self.alpha >= self.max_alpha:
            self.alpha = self.max_alpha
            self.fade_direction = -1
        
        # ← SEULEMENT mettre à jour l'alpha, PAS tout re-render
        self.image.set_alpha(self.alpha)

    def set_text(self, new_text):
        """Override pour mettre à jour le texte correctement"""
        self.text = new_text
        self.render_text()
        # Repositionner après le render
        if hasattr(self, 'position'):
            self.rect.center = self.position

    def draw(self, surface):
        """Affichage du sous-titre"""
        surface.blit(self.image, self.rect)