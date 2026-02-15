import pygame

from games.pong.pong_interface.pong_menu import PongMenu
from games.pong.pong_game import PongGame
from games.pong.pong_interface.pong_settings import PongSettings
from core.utilities.Interface.quit_interface import QuitInterface
from core.utilities.time.delay import Delay

class PongScreen:

    def __init__(self, screen, input_manager, screen_width, screen_height):

        self.surface = screen

        self.input = input_manager

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.transition_delay = Delay(1000)  # 1 seconde

        self.state = "menu"

        self.next_state = None
        self.menu = PongMenu(self.surface, self.input)
        self.game = PongGame(self.surface, self.input, self.screen_width, self.screen_height)
        self.settings = PongSettings(self.surface, self.input)
        self.quit = QuitInterface(self.surface)

    def update(self):

        if self.state == "menu":

            result = self.menu.update()

            if result == "PLAY":
                self.state = "game"
                self.transition_delay.start()

            if result == "SETTINGS" :
                self.state = "settings"
                self.transition_delay.start()

            if result == "RETURN":
                self.state = "menu"
                self.transition_delay.start()
                return "RETURN"
            
            if result == "QUIT":
                self.state = "quit"
                self.transition_delay.start()

        elif self.state == "game":

            result_game = self.game.update()

            if result_game == "RETURN":
                self.state = "menu"
                self.transition_delay.start()


        elif self.state == "settings":

            result_settings = self.settings.update()

            if result_settings == "RETURN":
                self.state = "menu"
                self.transition_delay.start()

        elif self.state == "quit":

            result_quit = self.quit.update()

            if result_quit == "YES":
                print("good bye !")
                pygame.quit()
            if result_quit == "NO":
                self.state = "menu"

    def draw(self, surface):

        self.surface.fill((30, 30, 30))

        if self.state == "menu" and not self.transition_delay.is_running():
            self.menu.draw(surface)

        if self.state == "game":
            self.game.draw(surface)

        if self.state == "settings":
            self.settings.draw(surface)

        if self.state == "quit":
            self.quit.draw(surface)