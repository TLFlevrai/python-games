import pygame

#import interface
from games.pong.pong_interface.pong_menu import PongMenu
from games.pong.pong_game import PongGame
from games.pong.pong_interface.pong_settings import PongSettings
from core.utilities.Interface.quit_interface import QuitInterface

#import utilities
from core.utilities.time.delay import Delay

class PongScreen:

    def __init__(self, surface, input_manager):

        self.surface = surface
        self.input = input_manager

        self.transition_delay = Delay(500)  # 0.5 secondes

        #init state
        self.state = "menu"
        self.next_state = None

        self.menu = PongMenu(self.surface, self.input)
        self.game = PongGame(self.surface, self.input)
        self.settings = PongSettings(self.surface, self.input)
        self.quit = QuitInterface(self.surface)

    def update(self):

        if self.state == "menu":

            result = self.menu.update()

            if result == "PLAY":
                self.next_state = "game"
                self.state = "transition"
                self.transition_delay.start()

            if result == "SETTINGS" :
                self.next_state = "settings"
                self.state = "transition"
                self.transition_delay.start()

            if result == "RETURN":
                self.state = "menu"
                return "RETURN"
            
            if result == "QUIT":
                self.next_state = "quit"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "game":

            result_game = self.game.update()

            if result_game == "RETURN":
                self.next_state = "menu"
                self.state = "transition"
                self.transition_delay.start()


        elif self.state == "settings":

            result_settings = self.settings.update()

            if result_settings == "RETURN":
                self.next_state = "menu"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "quit":

            result_quit = self.quit.update()

            if result_quit == "YES":
                print("good bye !")
                pygame.quit()
            if result_quit == "NO":
                self.next_state = "menu"
                self.state = "transition"

        elif self.state == "transition":

            if not self.transition_delay.is_running():
                self.state = self.next_state
                self.next_state = None

    def draw(self, surface):

        self.surface.fill((30, 30, 30))

        if self.state == "menu" and not self.transition_delay.is_running():
            self.menu.draw(surface)

        if self.state == "game" and not self.transition_delay.is_running():
            self.game.draw(surface)

        if self.state == "settings" and not self.transition_delay.is_running():
            self.settings.draw(surface)

        if self.state == "quit" and not self.transition_delay.is_running():
            self.quit.draw(surface)

        if self.state == "transition":
            pass