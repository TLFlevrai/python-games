import pygame

from core.utilities.colors import Colors
from core.utilities.UI.Layout import Layout
from core.utilities.UI.ui_builder import UIBuilder

class Settings:

    # Résolutions supportées
    RESOLUTIONS = [
        "Fullscreen",
        "1280x720",
        "800x600"
    ]

    def __init__(self, surface, input_manager, current_resolution="Fullscreen"):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.input = input_manager

        # ---------- LAYOUTS ----------
        block_offset = 40  # La moitié de l'espace entre titre et row (80 // 2)

        # Layout titre → remonté de block_offset
        self.layout = Layout(self.screen_width, self.screen_height - block_offset)
        self.layout_return = Layout(self.screen_width, self.screen_height, corner_padding_y=60)

        # Layout horizontal pour la ligne Resolution (avec spacing entre éléments)
        self.layout_row = Layout(
            self.screen_width,
            self.screen_height,
            horizontal_spacing=20,
            row_y=self.screen_height // 2 + block_offset
        )

        # ---------- UI VERTICALE ----------
        self.ui_center = UIBuilder(self.layout, Layout.CENTER, self.input)
        self.ui_return = UIBuilder(self.layout_return, Layout.LEFT_CORNER, self.input)

        # ---------- UI HORIZONTALE ----------
        self.ui_row = UIBuilder(self.layout_row, Layout.HORIZONTAL_CENTER, self.input)

        # ---------- ÉLÉMENTS ----------
        self.title = self.ui_center.add_label("SETTINGS", font_size=72, color=Colors.WHITE)
        self.return_button = self.ui_return.add_button("RETURN")

        # Ligne Resolution : Label → CycleButton
        self.resolution_label = self.ui_row.add_label(
            "Resolution",
            font_size=30,
            color=Colors.GRAY
        )

        self.resolution_cycle = self.ui_row.add_cycle_button(self.RESOLUTIONS)

        if current_resolution in self.RESOLUTIONS:
            self.resolution_cycle.set_index(self.RESOLUTIONS.index(current_resolution))

        print("Settings initialisé avec UIBuilder")

    def update(self):

        # ---------- RETURN ----------
        clicked = self.ui_return.update()
        if clicked == self.return_button:
            print("→ Settings: Bouton RETURN cliqué")
            return "RETURN"

        # ---------- RESOLUTION ----------
        changed = self.ui_row.update()
        if changed == self.resolution_cycle:
            selected = self.resolution_cycle.get_current()
            print(f"→ Settings: Résolution changée → {selected}")
            return f"RESOLUTION:{selected}"  # ← Screen.py interceptera ça

        return None

    def draw(self, surface):
        self.ui_center.draw(surface)
        self.ui_return.draw(surface)
        self.ui_row.draw(surface)