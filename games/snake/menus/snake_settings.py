import pygame
from core.utilities.colors import Colors
from core.ui import Layout, Zone, UIBuilder

class SnakeSettings:
    
    def __init__(self, surface, input_manager):
        
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()
        self.input = input_manager

        # Layout pour le titre
        self.layout = Layout(self.screen_width, self.screen_height)
        
        # Layout pour le bouton RETURN (coin bas gauche)
        self.layout_return = Layout(self.screen_width, self.screen_height, corner_padding_y=60)

        # UIBuilders
        self.ui_center = UIBuilder(self.layout, Zone.CENTER, self.input)
        self.ui_return = UIBuilder(self.layout_return, Zone.LEFT_CORNER, self.input)

        # Éléments
        self.title = self.ui_center.add_label("SNAKE SETTINGS", font_size=72, color=Colors.WHITE)
        self.return_button = self.ui_return.add_button("RETURN")

        print("SNAKE_Settings initialisé avec UIBuilder")
        print(f"  - {len(self.ui_center.elements)} éléments créés")
        print(f"  - {len(self.ui_return.elements)} éléments créés")

    def update(self):
        
        # Bouton RETURN
        clicked = self.ui_return.update()
        
        if clicked == self.return_button:
            return "RETURN"
        return None

    def draw(self, surface):
        
        self.ui_center.draw(surface)
        self.ui_return.draw(surface)