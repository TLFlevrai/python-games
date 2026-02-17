import pygame

from games.pong.pong_core.ball import Ball
from games.pong.pong_core.paddle import Paddle
from games.pong.pong_core.label.pong_score import Score
from games.pong.pong_interface.pong_pause_interface import PongPauseInterface
from games.pong.pong_interface.pong_game_over_interface import PongGameOverInterface

class PongGame:

    def __init__(self, surface, input_manager):

        self.screen = surface
        self.input = input_manager

        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        paddle_width, paddle_height = 10, 100

        # ---------- STATE ----------
        self.state = "playing"  # playing / paused / game_over

        # ---------- CORE ----------
        self.ball = Ball()
        self.score = Score(self.screen_width)

        self.paddle_left = Paddle(
            50,
            (self.screen_height - paddle_height) // 2,
            paddle_width, paddle_height
        )
        self.paddle_right = Paddle(
            self.screen_width - 50 - paddle_width,
            (self.screen_height - paddle_height) // 2,
            paddle_width, paddle_height
        )

        # ---------- INTERFACES ----------
        self.pause_interface = PongPauseInterface(self.screen, self.input)
        self.game_over_interface = PongGameOverInterface(self.screen, self.input)

    # ---------- RESET ----------

    def reset(self):

        self.state = "playing"

        self.score.left_score = 0
        self.score.right_score = 0

        self.ball.reset()

        paddle_height = 100
        self.paddle_left.y = (self.screen_height - paddle_height) // 2
        self.paddle_right.y = (self.screen_height - paddle_height) // 2

        print("🔄 Pong reset!")

    # ---------- UPDATE ----------

    def update(self):

        # ---------- PLAYING ----------
        if self.state == "playing":

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.paddle_left.move_up()
            if keys[pygame.K_s]:
                self.paddle_left.move_down(self.screen_height)
            if keys[pygame.K_UP]:
                self.paddle_right.move_up()
            if keys[pygame.K_DOWN]:
                self.paddle_right.move_down(self.screen_height)

            # Pause via ESC
            if self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "paused"
                return

            event = self.ball.update(self.paddle_left, self.paddle_right)

            if event == "LEFT_SCORE":
                self.score.add_left()
            elif event == "RIGHT_SCORE":
                self.score.add_right()

            # WIN CONDITION
            if self.score.left_score > 4:
                self.state = "game_over"
                self.game_over_interface.set_winner("left")

            elif self.score.right_score > 4:
                self.state = "game_over"
                self.game_over_interface.set_winner("right")

        # ---------- PAUSED ----------
        elif self.state == "paused":

            result = self.pause_interface.update()

            if result == "RESUME" or self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "playing"

            elif result == "RESTART":
                self.reset()

        # ---------- GAME OVER ----------
        elif self.state == "game_over":

            result = self.game_over_interface.update()

            if result == "RESTART":
                self.reset()

            elif result == "MENU":
                self.reset()
                return "RETURN"

    # ---------- DRAW ----------

    def draw(self, surface):

        # ---------- CORE ----------
        self.ball.draw(surface)
        self.paddle_left.draw(surface)
        self.paddle_right.draw(surface)
        self.score.draw(surface)

        # ---------- OVERLAYS ----------
        if self.state == "paused":
            self.pause_interface.draw(surface)

        elif self.state == "game_over":
            self.game_over_interface.draw(surface)