from core.utilities.colors import Colors
from core.ui.layout import Layout
from core.ui.builder import UIBuilder
from core.ui import Zone

class DinoMenu:
    def __init__(self, surface, input_manager):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()
        self.input = input_manager

        # initialisation du layout
        self.layout = Layout(self.screen_width, self.screen_height, spacing=80)
        self.ui_builder = UIBuilder(self.layout, Zone.CENTER, self.input)

        # ajout des éléments
        self.title_Label = self.ui_builder.add_label("DINO", font_size=72, color=Colors.WHITE)
        self.play_button = self.ui_builder.add_button("PLAY", size=(250, 60))
        self.settings_button = self.ui_builder.add_button("Settings", size=(250, 60))
        self.return_button = self.ui_builder.add_button("Return", size=(250, 60))
        self.quit_button = self.ui_builder.add_button("Quit", size=(250, 60))

        print("DINO_Menu initialisé avec UIBuilder")
        print(f"  - {len(self.ui_builder.elements)} éléments créés")

    def update(self):
        clicked_element = self.ui_builder.update()
        if clicked_element:
            if clicked_element == self.play_button:
                print("→ Dino_Menu: Bouton PLAY cliqué")
                return "PLAY"
            if clicked_element == self.settings_button:
                print("→ Dino_Menu: Bouton SETTINGS cliqué")
                return "SETTINGS"
            if clicked_element == self.return_button:
                print("→ Dino_Menu: Bouton RETURN cliqué")
                return "RETURN"
            if clicked_element == self.quit_button:
                print("→ Dino_Menu: Bouton QUIT cliqué")
                return "QUIT"
        return None

    def draw(self, surface):
        self.ui_builder.draw(surface)