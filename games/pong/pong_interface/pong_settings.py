from core.utilities.colors import Colors
from core.utilities.UI.Layout import Layout
from core.utilities.UI.ui_builder import UIBuilder

class PongSettings:

    def __init__(self, surface, input_manager):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.input = input_manager

        self.layout = Layout(self.screen_width, self.screen_height)

        self.ui_center = UIBuilder(self.layout, Layout.CENTER, self.input)
        self.ui_return = UIBuilder(self.layout, Layout.LEFT_CORNER, self.input)

        self.title = self.ui_center.add_label("PONG SETTINGS", font_size=72, color=Colors.WHITE)
        self.return_button = self.ui_return.add_button("RETURN")

        print("PONG_Settings initialisé avec UIBuilder")
        print(f"  - {len(self.ui_center.elements)} éléments créés")
        print(f"  - {len(self.ui_return.elements)} éléments créés")

    def update(self):
        clicked_element = self.ui_return.update()

        if clicked_element :
            if clicked_element == self.return_button:
                print("→ Pong_Settings: Bouton RETURN cliqué")
                return "RETURN"
                
        return None

    def draw(self, surface):
        self.ui_center.draw(surface)
        self.ui_return.draw(surface)