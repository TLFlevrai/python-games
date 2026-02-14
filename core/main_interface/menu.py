import pygame

from core.utilities.colors import Colors
from core.utilities.UI.Layout import Layout
from core.utilities.UI.ui_builder import UIBuilder


class Menu:
    """Menu principal utilisant le système UIBuilder"""

    def __init__(self, surface, input_manager):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.input = input_manager

        self.layout = Layout(self.screen_width, self.screen_height, spacing=80)
        self.ui_builder = UIBuilder(self.layout, Layout.CENTER, self.input)

        #ajouter le titre
        self.title_label = self.ui_builder.add_label("PYTHON GAMES", font_size=72, color=Colors.WHITE)

        # Ajouter les boutons
        self.pong_button = self.ui_builder.add_button("PONG", size=(250, 60))
        self.flappy_button = self.ui_builder.add_button("FLAPPY BIRD", size=(250, 60))
        self.settings_button = self.ui_builder.add_button("Settings", size=(250, 60))
        self.quit_button = self.ui_builder.add_button("Quit", size=(250, 60))

        print("Menu initialisé avec UIBuilder")
        print(f"  - {len(self.ui_builder.elements)} éléments créés")

    def update(self):
        """Met à jour le menu et retourne l'action sélectionnée"""

        # Appeler update() du UIBuilder pour détecter les clics
        clicked_element = self.ui_builder.update()

        # Vérifier quel bouton a été cliqué
        if clicked_element:
            if clicked_element == self.pong_button:
                print("→ Menu: Bouton PONG cliqué")
                return "PONG"

            elif clicked_element == self.flappy_button:
                print("→ Menu: Bouton FLAPPY BIRD cliqué")
                return "FLAPPY_BIRD"

            elif clicked_element == self.settings_button:
                print("→ Menu: Bouton Settings cliqué")
                return "SETTINGS"

            elif clicked_element == self.quit_button:
                print("→ Menu: Bouton Quit cliqué")
                return "QUIT"

        return None

    def draw(self, surface):
        """Dessine le menu"""

        # Dessiner tous les éléments via UIBuilder
        self.ui_builder.draw(surface)

        # Optionnel: Ajouter une version en bas à droite
        font_small = pygame.font.SysFont(None, 24)
        version_text = font_small.render("v0.0.0.3.5 - UI_Integration", True, Colors.GRAY)
        surface.blit(version_text, (self.screen_width - 200, self.screen_height - 30))