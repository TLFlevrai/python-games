import pygame
from core.utilities.colors import Colors
from core.ui import Layout, Zone, UIBuilder


class Settings:
    # Résolutions supportées
    RESOLUTIONS = ["Fullscreen", "1280x720", "800x600"]

    def __init__(self, surface, input_manager, current_resolution="Fullscreen"):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()
        self.input = input_manager

        block_offset = 40  # La moitié de l'espace entre titre et row

        # Layout pour le titre (remonté)
        self.layout = Layout(self.screen_width, self.screen_height - block_offset)
        # Layout pour le bouton RETURN (coin bas gauche)
        self.layout_return = Layout(
            self.screen_width, self.screen_height, corner_padding_y=60
        )
        # Layout horizontal pour la ligne Resolution
        self.layout_row = Layout(
            self.screen_width,
            self.screen_height,
            horizontal_spacing=20,
            row_y=self.screen_height // 2 + block_offset
        )

        # UIBuilders
        self.ui_center = UIBuilder(self.layout, Zone.CENTER, self.input)
        self.ui_return = UIBuilder(self.layout_return, Zone.LEFT_CORNER, self.input)
        self.ui_row = UIBuilder(self.layout_row, Zone.HORIZONTAL_CENTER, self.input)

        # Éléments
        self.title = self.ui_center.add_label("SETTINGS", font_size=72, color=Colors.WHITE)
        self.return_button = self.ui_return.add_button("RETURN")

        self.resolution_label = self.ui_row.add_label(
            "Resolution", font_size=30, color=Colors.GRAY
        )
        self.resolution_cycle = self.ui_row.add_cycle_button(self.RESOLUTIONS)

        if current_resolution in self.RESOLUTIONS:
            self.resolution_cycle.set_index(self.RESOLUTIONS.index(current_resolution))

        print("Settings initialisé avec UIBuilder")

    def update(self):
        # Bouton RETURN
        clicked = self.ui_return.update()
        if clicked == self.return_button:
            print("→ Settings: Bouton RETURN cliqué")
            return "RETURN"

        # Changement de résolution
        changed = self.ui_row.update()
        if changed == self.resolution_cycle:
            selected = self.resolution_cycle.get_current()
            print(f"→ Settings: Résolution changée → {selected}")
            return f"RESOLUTION:{selected}"

        return None

    def draw(self, surface):
        self.ui_center.draw(surface)
        self.ui_return.draw(surface)
        self.ui_row.draw(surface)