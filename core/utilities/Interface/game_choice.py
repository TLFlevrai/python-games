import pygame

from core.utilities.colors import Colors
from core.utilities.UI.Layout import Layout
from core.utilities.UI.ui_builder import UIBuilder

class GameChoice :

    def __init__(self, surface, input_manager):
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        self.input = input_manager

        block_offset = 120

        self.layout = Layout(self.screen_width, self.screen_height - block_offset)
        self.version_layout = Layout(self.screen_width, self.screen_height)
        self.layout_return = Layout(self.screen_width, self.screen_height, corner_padding_y=60)

        # Layout horizontal pour les game buttons
        self.layout_games = Layout(self.screen_width,self.screen_height,horizontal_spacing=40, row_y=self.screen_height // 2 + 60)

        self.ui_builder = UIBuilder(self.layout, Layout.CENTER, self.input)
        self.ui_games = UIBuilder(self.layout_games, Layout.HORIZONTAL_CENTER, self.input)
        self.return_ui = UIBuilder(self.layout_return, Layout.LEFT_CORNER, self.input)
        self.version_ui = UIBuilder(self.version_layout, Layout.RIGHT_CORNER, self.input)

        #add title
        self.title_label = self.ui_builder.add_label("GAMES", font_size=72, color=Colors.WHITE)

        #add game_button
        self.pong_button = self.ui_games.add_game_button(
            "Pong",
            "assets/pong/pong_logo.png"
        )

        self.flappy_bird_button = self.ui_games.add_game_button(
            "Flappy Bird",
            "assets/flappy_bird/flappy_bird_logo.png"
        )

        self.dino_button = self.ui_games.add_game_button(
            "Dino",
            "assets/dino/dino_logo.png"
        )

        self.tic_tac_toe_button = self.ui_games.add_game_button(
            "Tic Tac Toe",
            "assets/tic_tac_toe/tic_tac_toe_logo.png"
        )

        #bottom
        #add return button
        self.return_button = self.return_ui.add_button("RETURN")

        # Ajouter la version
        self.version_label = self.version_ui.add_version("v.0.0.5 general_improvements")


    def update(self):
        
        clicked_element = self.ui_games.update()

        if clicked_element:
            if clicked_element == self.pong_button:
                print("→ game_choice: Bouton PONG cliqué")
                return "PONG"

            elif clicked_element == self.flappy_bird_button:
                print("→ game_choice: Bouton Flappy Bird cliqué")
                return "FLAPPY_BIRD"
            
            elif clicked_element == self.dino_button:
                print("→ game_choice: Bouton DINO cliqué")
                return "Dino"

            elif clicked_element == self.tic_tac_toe_button:
                print("→ game_choice: Bouton Tic Tac Toe cliqué")
                return "Tic_Tac_Toe"

        clicked_return = self.return_ui.update()

        if clicked_return == self.return_button:
            print("→ game_choice: RETURN cliqué")
            return "RETURN"

        return None

    def draw(self, surface):
        self.ui_builder.draw(surface)
        self.ui_games.draw(surface)
        self.return_ui.draw(surface)
        self.version_ui.draw(surface)