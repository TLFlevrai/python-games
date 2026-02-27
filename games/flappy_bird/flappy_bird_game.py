import pygame

# core
from games.flappy_bird.flappy_bird_core.entity.bird import Bird
from games.flappy_bird.flappy_bird_core.entity.pipe_manager import PipeManager
from games.flappy_bird.flappy_bird_core.UI.label.flappy_bird_score import Score

# interfaces
from games.flappy_bird.flappy_bird_core.interface.pause_interface import PauseInterface
from games.flappy_bird.flappy_bird_core.interface.game_over_interface import GameOverInterface
from games.flappy_bird.flappy_bird_core.UI.button.pause_button import PauseButton


class FlappyBirdGame:

    def __init__(self, screen, input_manager):

        self.surface = screen
        self.input = input_manager

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # ---------- STATE MACHINE ----------
        self.state = "playing"  # playing / paused / game_over

        # ---------- PLAYER ----------
        self.bird = Bird(200, self.screen_height // 2)

        # ---------- PIPES ----------
        self.pipe_manager = PipeManager(self.screen_width, self.screen_height)

        # ---------- SCORE ----------
        self.score_manager = Score(self.screen_width, self.screen_height)

        # ---------- INTERFACES ----------
        self.pause_button = PauseButton(self.screen_width, self.input)
        self.pause_interface = PauseInterface(self.surface, self.input)
        self.game_over_interface = GameOverInterface(self.surface, self.input)

    # ==================================================
    # RESET
    # ==================================================

    def reset(self):

        self.state = "playing"

        self.bird.reset(200, self.screen_height // 2)
        self.pipe_manager.reset()
        self.score_manager.reset()

        print("🔄 Flappy Bird reset")

    # ==================================================
    # UPDATE
    # ==================================================

    def update(self):

        # ---------- PLAYING ----------
        if self.state == "playing":

            if self.input.click() or self.input.space_pressed():
                self.bird.flap()

            result_btn = self.pause_button.update(self.state)
            if result_btn == "PAUSE" or self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "paused"
                return

            self.bird.update()

            collision, scored = self.pipe_manager.update(self.bird.get_rect())

            if collision:
                self.state = "game_over"
                self.bird.alive = False

            if scored:
                self.score_manager.add_point()

            if self.bird.y < 0 or self.bird.y > self.screen_height:
                self.state = "game_over"
                self.bird.alive = False

        # ---------- PAUSED ----------
        elif self.state == "paused":

            # Bouton play cliqué ou ESC
            result_btn = self.pause_button.update(self.state)
            if result_btn == "RESUME" or self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "playing"
                return

            result = self.pause_interface.update()

            if result == "RESUME":
                self.state = "playing"

            elif result == "RESTART":
                self.reset()

            elif result == "MENU":
                self.reset()
                return "MENU"

        # ---------- GAME OVER ----------
        elif self.state == "game_over":

            result = self.game_over_interface.update(self.score_manager.get_score())

            if result == "RESTART":
                self.reset()

            elif result == "MENU":
                self.reset()
                return "MENU"

    # ==================================================
    # DRAW
    # ==================================================

    def draw(self, surface):

        # ---------- JEU ----------
        self.pipe_manager.draw(surface)
        self.bird.draw(surface)
        self.score_manager.draw(surface)

        # ---------- BOUTON PAUSE (toujours visible sauf game over) ----------
        if self.state != "game_over":
            self.pause_button.draw(surface, self.state)

        # ---------- OVERLAYS ----------
        if self.state == "paused":
            self.pause_interface.draw(surface)

        elif self.state == "game_over":
            self.game_over_interface.draw(surface, self.score_manager.get_score())