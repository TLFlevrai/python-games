import pygame

from pong.ball import Ball
from pong.paddle import Paddle
from pong.score import Score
from pong.win_Label import WinLabel

class PongGame:

    def __init__(self, screen):
        self.screen = screen
        self.ball = Ball()
        self.score = Score(800)
        self.win_label = WinLabel(self.screen)

        self.game_over = False

        screen_width, screen_height = 800, 600
        paddle_width, paddle_height = 10, 100

        #player left
        self.paddle_left = Paddle(50, (screen_height - paddle_height)//2, paddle_width, paddle_height)

        #player right
        self.paddle_right = Paddle(screen_width - 50 - paddle_width, (screen_height - paddle_height)//2, paddle_width, paddle_height)

        #score


    def update(self):

        keys = pygame.key.get_pressed()

        #joueur gauche
        if keys[pygame.K_w]:
            self.paddle_left.move_up()
        if keys[pygame.K_s]:
            self.paddle_left.move_down(600)

        #joueur droit
        if keys[pygame.K_UP]:
            self.paddle_right.move_up()
        if keys[pygame.K_DOWN]:
            self.paddle_right.move_down(600)

        if not self.game_over:

            event = self.ball.update(self.paddle_left, self.paddle_right)

            if event == "LEFT_SCORE":
                self.score.add_left()

            elif event == "RIGHT_SCORE":
                self.score.add_right()

            # WIN CONDITION
            if self.score.left_score > 4:
                self.game_over = True
                self.win_label.show_left_win()

            elif self.score.right_score > 4:
                self.game_over = True
                self.win_label.show_right_win()

    def draw(self, surface):
        self.ball.draw(surface)
        self.paddle_left.draw(surface)
        self.paddle_right.draw(surface)
        self.score.draw(surface)
        self.win_label.draw(surface)