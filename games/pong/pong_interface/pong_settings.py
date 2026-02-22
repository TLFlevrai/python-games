import pygame
from core.utilities.colors import Colors
from core.ui.layout import Layout
from core.ui.builder import UIBuilder
from core.ui import Zone

class PongSettings:
    BALL_SKINS = ["White", "Blue", "Red"]

    def __init__(self, surface, input_manager, current_ball="White"):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()
        self.input = input_manager

        block_offset = 40

        # Layout pour le titre (centre, mais décalé verticalement)
        self.layout = Layout(self.screen_width, self.screen_height - block_offset)
        # Layout pour le bouton RETURN (coin bas gauche)
        self.layout_return = Layout(self.screen_width, self.screen_height, corner_padding_y=60)
        # Layout horizontal pour la ligne Ball Skin
        self.layout_row = Layout(
            self.screen_width,
            self.screen_height,
            horizontal_spacing=20,
            row_y=self.screen_height // 2 + block_offset
        )

        # UIBuilders avec les zones correspondantes
        self.ui_center = UIBuilder(self.layout, Zone.CENTER, self.input)
        self.ui_return = UIBuilder(self.layout_return, Zone.LEFT_CORNER, self.input)
        self.ui_row = UIBuilder(self.layout_row, Zone.HORIZONTAL_CENTER, self.input)

        # Éléments
        self.title = self.ui_center.add_label("PONG SETTINGS", font_size=72, color=Colors.WHITE)
        self.return_button = self.ui_return.add_button("RETURN")

        # Ligne Ball Skin
        self.ball_label = self.ui_row.add_label("Ball", font_size=30, color=Colors.GRAY)
        self.ball_cycle = self.ui_row.add_cycle_button(self.BALL_SKINS)

        # Initialiser au bon skin
        if current_ball in self.BALL_SKINS:
            self.ball_cycle.set_index(self.BALL_SKINS.index(current_ball))

        print("Pong_Settings initialisé avec UIBuilder")
        print(f"  - {len(self.ui_center.elements)} éléments créés")
        print(f"  - {len(self.ui_return.elements)} éléments créés")

    def update(self):
        # Bouton RETURN
        clicked = self.ui_return.update()
        if clicked == self.return_button:
            return "RETURN"

        # Changement de ball skin
        changed = self.ui_row.update()
        if changed == self.ball_cycle:
            selected = self.ball_cycle.get_current()
            print(f"→ Pong_Settings: Ball skin changé → {selected}")
            return f"BALL_SKIN:{selected}"

        return None

    def draw(self, surface):
        self.ui_center.draw(surface)
        self.ui_return.draw(surface)
        self.ui_row.draw(surface)