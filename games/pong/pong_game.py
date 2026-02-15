import pygame

#core integration
from games.pong.pong_core.ball import Ball
from games.pong.pong_core.paddle import Paddle

#label integration
from games.pong.pong_core.label.pong_score import Score
from games.pong.pong_core.label.pong_win_Label import WinLabel
from games.pong.pong_core.label.pause_label import PauseLabel

#button integration
from games.pong.pong_core.button.pause_button import PauseButton
from games.pong.pong_core.button.play_button import PlayButton
from games.pong.pong_core.button.restart_button import RestartButton
from games.pong.pong_core.button.return_button import ReturnButton

#utilities
from core.utilities.time.delay import Delay

class PongGame:

    def __init__(self, screen, input_manager, screen_width, screen_height):
        self.screen = screen
        self.input = input_manager

        self.screen_width = screen_width
        self.screen_height = screen_height
        paddle_width, paddle_height = 10, 100

        center_x = self.screen_width//2
        bottom_y = self.screen_height - 40

        #core integration
        self.ball = Ball()
        self.score = Score(self.screen_width)

        #label integration
        self.win_label = WinLabel(self.screen)
        self.pause_label = PauseLabel(self.screen)

        #button integration
        self.pause_button = PauseButton(self.screen_width, self.screen_height, self.input)
        self.play_button = PlayButton(self.screen_width, self.screen_height, self.input)
        self.restart_button = RestartButton(center_x+60, bottom_y, self.input)
        self.return_button = ReturnButton(center_x-60, bottom_y, self.input)

        self.game_over = False
        self.paused = False

        #player left
        self.paddle_left = Paddle(50, (self.screen_height - paddle_height)//2, paddle_width, paddle_height)

        #player right
        self.paddle_right = Paddle(self.screen_width - 50 - paddle_width, (self.screen_height - paddle_height)//2, paddle_width, paddle_height)

        self.transition_delay = Delay(250) #0.25 sec

    def reset(self):
        """Réinitialise le jeu pour une nouvelle partie"""
        self.game_over = False
        self.paused = False
        
        # Reset scores
        self.score.left_score = 0
        self.score.right_score = 0
        
        # Reset ball
        self.ball.reset()
        
        # Reset paddles positions
        paddle_height = 100
        self.paddle_left.y = (self.screen_height - paddle_height)//2
        self.paddle_right.y = (self.screen_height - paddle_height)//2
        
        # Reset UI
        self.win_label.hide()
        self.pause_button.visible = True
        self.play_button.visible = False
        self.pause_label.visible = False
        self.restart_button.visible = False
        self.return_button.visible = False
        
        print("🔄 Pong_Game reset!")

    def update(self):

        if self.pause_button.update():

            print("pause is true")

            self.paused = True

            self.pause_button.visible = False

            #Apply delay
            self.transition_delay.start()

        if self.paused and not self.transition_delay.is_running():

            self.play_button.visible = True
            self.restart_button.visible = True
            self.pause_label.visible = True
            self.return_button.visible = True

        if self.play_button.update():

            print("play is true")

            self.paused = False

            self.pause_button.visible = True
            self.play_button.visible = False
            self.pause_label.visible = False
            self.return_button.visible = False

        if self.restart_button.update():
            self.reset()

        if self.return_button.update():
            self.reset()
            return "RETURN"
        
        if self.game_over : #game over UI

            self.pause_button.visible = False
            self.play_button.visible = False

            self.restart_button.visible = True
            self.return_button.visible = True


        keys = pygame.key.get_pressed()

        if not self.game_over and not self.paused:
            #joueur gauche
            if keys[pygame.K_w]:
                self.paddle_left.move_up()
            if keys[pygame.K_s]:
                self.paddle_left.move_down(self.screen_height)

            #joueur droit
            if keys[pygame.K_UP]:
                self.paddle_right.move_up()
            if keys[pygame.K_DOWN]:
                self.paddle_right.move_down(self.screen_height)

        if not self.game_over and not self.paused:

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

        #load game element
        self.ball.draw(surface)
        self.paddle_left.draw(surface)
        self.paddle_right.draw(surface)

        #load game label
        self.score.draw(surface)
        self.win_label.draw(surface)
        self.pause_label.draw(surface)

        #load game button
        self.pause_button.draw(surface)
        self.play_button.draw(surface)
        self.restart_button.draw(surface)
        self.return_button.draw(surface)