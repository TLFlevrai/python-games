import pygame
from core.utilities.colors import Colors
from core.ui import Layout, Zone, UIBuilder
from core.ui.managers import SubtitleManager  # ← chemin corrigé


class Menu:
    """Menu principal utilisant le système UIBuilder"""

    def __init__(self, surface, input_manager):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()
        self.input = input_manager

        # Layout principal (centre)
        self.layout = Layout(
            self.screen_width, self.screen_height,
            spacing=80, corner_padding=20, corner_padding_y=15
        )
        self.ui_builder = UIBuilder(self.layout, Zone.CENTER, self.input)

        # Layout pour la version (coin bas droit)
        self.version_ui = UIBuilder(self.layout, Zone.RIGHT_CORNER, self.input)

        # Gestionnaire de sous-titres
        self.subtitle_manager = SubtitleManager()
        self.subtitle_manager.set_mode("random")
        self.subtitle_manager.enable_auto_change(5000)

        # Éléments
        self.title_label = self.ui_builder.add_label(
            "PYTHON GAMES", font_size=72, color=Colors.WHITE
        )
        self.subtitle_label = self.ui_builder.add_subtitle(
            self.subtitle_manager.get_current()
        )
        self.play_button = self.ui_builder.add_button("PLAY", size=(250, 60))
        self.settings_button = self.ui_builder.add_button("Settings", size=(250, 60))
        self.quit_button = self.ui_builder.add_button("Quit", size=(250, 60))
        self.version_label = self.version_ui.add_version("v.0.0.6.2 snake_integration")

        print("Menu initialisé avec UIBuilder")
        print(f"  - {len(self.ui_builder.elements)} éléments créés")
        print(f"  - Sous-titre actuel : '{self.subtitle_manager.get_current()}'")

    def update(self):
        """Met à jour le menu et retourne l'action sélectionnée"""
        # Mise à jour automatique du sous-titre
        if self.subtitle_manager.update():
            self.subtitle_label.set_text(self.subtitle_manager.get_current())

        # Détection des clics
        clicked_element = self.ui_builder.update()

        if clicked_element:
            if clicked_element == self.play_button:
                print("→ Menu: Bouton PLAY cliqué")
                return "PLAY"
            elif clicked_element == self.settings_button:
                print("→ Menu: Bouton Settings cliqué")
                return "SETTINGS"
            elif clicked_element == self.quit_button:
                print("→ Menu: Bouton Quit cliqué")
                return "QUIT"

        return None

    def draw(self, surface):
        """Dessine le menu"""
        self.ui_builder.draw(surface)
        self.version_ui.draw(surface)

    def refresh_subtitle(self):
        """Change manuellement le sous-titre"""
        self.subtitle_manager.next_subtitle()
        self.subtitle_label.set_text(self.subtitle_manager.get_current())