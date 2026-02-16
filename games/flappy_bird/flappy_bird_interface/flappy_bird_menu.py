import pygame

from core.utilities.colors import Colors
from core.utilities.UI.Layout import Layout
from core.utilities.UI.ui_builder import UIBuilder

class FlappyBirdMenu:

    def __init__ (self, surface, input_manager):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.input = input_manager

        self.layout = Layout(self.screen_width, self.screen_height, spacing=80)
        self.menu_ui = UIBuilder(self.layout, Layout.CENTER, self.input)

        #add label
        self.title_label = self.menu_ui.add_label("FLAPPY BIRD", font_size=72, color=Colors.WHITE)

        #add button
        self.play_button = self.menu_ui.add_button("PLAY", size=(250, 60))
        self.settings_button = self.menu_ui.add_button("Settings", size=(250, 60))
        self.return_button = self.menu_ui.add_button("Return", size=(250, 60))
        self.quit_button = self.menu_ui.add_button("Quit", size=(250, 60))

        print("Flappy_Bird_Menu initialisé avec UIBuilder")
        print(f"  - {len(self.menu_ui.elements)} éléments créés")

    def update(self):
        
        clicked_element = self.menu_ui.update()

        if clicked_element :
                if clicked_element == self.play_button:
                    print("→ Flappy_Bird_Menu: Bouton PLAY cliqué")
                    return "PLAY"
                if clicked_element == self.settings_button:
                    print("→ Flappy_Bird_Menu: Bouton SETTINGS cliqué")
                    return "SETTINGS"
                if clicked_element == self.return_button:
                    print("→ Flappy_Bird_Menu: Bouton RETURN cliqué")
                    return "RETURN"
                if clicked_element == self.quit_button:
                    print("→ Flappy_Bird_Menu: Bouton QUIT cliqué")
                    return "QUIT"
                
        return None

    def draw(self, surface):
        self.menu_ui.draw(surface)