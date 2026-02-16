import pygame

from core.utilities.colors import Colors
from core.utilities.UI.Layout import Layout
from core.utilities.UI.ui_builder import UIBuilder
from core.utilities.UI.label.subtitle_manager import SubtitleManager  # ← NOUVEAU


class Menu:
    """Menu principal utilisant le système UIBuilder"""

    def __init__(self, surface, input_manager):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.input = input_manager

        self.layout = Layout(
        self.screen_width, 
        self.screen_height, 
        spacing=80,
        corner_padding=20,       # Distance horizontale
        corner_padding_y=15      # ← Distance verticale (petite valeur = collé en bas)
        )
        self.ui_builder = UIBuilder(self.layout, Layout.CENTER, self.input)
        self.version_ui = UIBuilder(self.layout, Layout.RIGHT_CORNER, self.input)

        # ---------- SUBTITLE MANAGER ← NOUVEAU ----------
        self.subtitle_manager = SubtitleManager()
        self.subtitle_manager.set_mode("random")  # Mode aléatoire
        self.subtitle_manager.enable_auto_change(5000)   # change tous les 5s

        # Ajouter le titre
        self.title_label = self.ui_builder.add_label("PYTHON GAMES", font_size=72, color=Colors.WHITE)
        
        # Ajouter le sous-titre avec le texte du manager ← MODIFIÉ
        self.subtitle_label = self.ui_builder.add_subtitle(self.subtitle_manager.get_current())

        # Ajouter les boutons
        self.pong_button = self.ui_builder.add_button("PONG", size=(250, 60))
        self.flappy_button = self.ui_builder.add_button("FLAPPY BIRD", size=(250, 60))
        self.settings_button = self.ui_builder.add_button("Settings", size=(250, 60))
        self.quit_button = self.ui_builder.add_button("Quit", size=(250, 60))

        # Ajouter la version
        self.version_label = self.version_ui.add_version("v.0.0.4.5 flappy_bird_integration")

        print("Menu initialisé avec UIBuilder")
        print(f"  - {len(self.ui_builder.elements)} éléments créés")
        print(f"  - Sous-titre actuel : '{self.subtitle_manager.get_current()}'")

    def update(self):
        """Met à jour le menu et retourne l'action sélectionnée"""

        # ---------- MISE À JOUR DU SUBTITLE MANAGER ← NOUVEAU ----------
        if self.subtitle_manager.update():
            # Si le sous-titre a changé automatiquement, mettre à jour l'affichage
            self.subtitle_label.set_text(self.subtitle_manager.get_current())

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
        self.version_ui.draw(surface)

    # ---------- MÉTHODE HELPER ← NOUVEAU (Optionnel) ----------
    
    def refresh_subtitle(self):
        """Change manuellement le sous-titre (utile lors du retour au menu)"""
        self.subtitle_manager.next_subtitle()
        self.subtitle_label.set_text(self.subtitle_manager.get_current())