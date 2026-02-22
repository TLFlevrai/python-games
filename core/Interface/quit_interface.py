import pygame
from core.ui import UIBuilder, Layout, Zone
from core.utilities.colors import Colors
from core.utilities import InputManager

class QuitInterface:
    """Interface de confirmation pour quitter l'application (utilise UIBuilder)"""

    def __init__(self, screen, input_manager: InputManager):
        self.screen = screen
        self.input = input_manager
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # Créer un layout centré pour le titre et les boutons
        self.layout = Layout(self.screen_width, self.screen_height, spacing=60)
        self.builder = UIBuilder(self.layout, Zone.CENTER, self.input)

        # Ajouter les éléments
        self.title_label = self.builder.add_label("Quit Game?", font_size=72, color=Colors.WHITE)
        self.yes_button = self.builder.add_button("YES", size=(150, 60), color=Colors.ACCENT_RED)
        self.no_button = self.builder.add_button("NO", size=(150, 60))

        # Pour stocker le résultat
        self.result = None

    def update(self) -> str | None:
        """Met à jour l'interface et retourne 'YES' ou 'NO' si un bouton est cliqué."""
        clicked = self.builder.update()
        if clicked == self.yes_button:
            print("button_clicked : YES (quit_interface.py)")
            return "YES"
        elif clicked == self.no_button:
            print("button_clicked : NO (quit_interface.py)")
            return "NO"
        return None

    def draw(self, surface):
        """Dessine l'interface avec un overlay sombre."""
        # Overlay semi-transparent
        overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))  # Noir avec alpha 200
        surface.blit(overlay, (0, 0))

        # Dessiner les éléments via le builder
        self.builder.draw(surface)