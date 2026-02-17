import pygame
from core.utilities.colors import Colors
from core.utilities.UI.Layout import Layout
from core.utilities.UI.ui_builder import UIBuilder

class PongSettings:

    BALL_SKINS = ["White", "Blue", "Red"]

    def __init__(self, surface, input_manager, current_ball="White"):

        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()
        self.input = input_manager

        # ---------- LAYOUTS ----------
        block_offset = 40

        self.layout = Layout(self.screen_width, self.screen_height - block_offset)
        self.layout_return = Layout(self.screen_width, self.screen_height, corner_padding_y=60)
        self.layout_row = Layout(
            self.screen_width,
            self.screen_height,
            horizontal_spacing=20,
            row_y=self.screen_height // 2 + block_offset
        )

        # ---------- UI ----------
        self.ui_center = UIBuilder(self.layout, Layout.CENTER, self.input)
        self.ui_return = UIBuilder(self.layout_return, Layout.LEFT_CORNER, self.input)
        self.ui_row = UIBuilder(self.layout_row, Layout.HORIZONTAL_CENTER, self.input)

        # ---------- ÉLÉMENTS ----------
        self.title = self.ui_center.add_label("PONG SETTINGS", font_size=72, color=Colors.WHITE)
        self.return_button = self.ui_return.add_button("RETURN")

        # Ligne Ball Skin
        self.ball_label = self.ui_row.add_label("Ball", font_size=30, color=Colors.GRAY)
        self.ball_cycle = self.ui_row.add_cycle_button(self.BALL_SKINS)

        # Initialiser au bon skin
        if current_ball in self.BALL_SKINS:
            self.ball_cycle.set_index(self.BALL_SKINS.index(current_ball))

        print("PONG_Settings initialisé avec UIBuilder")

    def update(self):

        # ---------- RETURN ----------
        clicked = self.ui_return.update()
        if clicked == self.return_button:
            return "RETURN"

        # ---------- BALL SKIN ----------
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