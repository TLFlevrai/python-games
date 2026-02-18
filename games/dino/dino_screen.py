import pygame

from games.dino.dino_interface.dino_menu import DinoMenu
from games.dino.dino_interface.dino_settings import DinoSettings
from games.dino.dino_game import DinoRunnerGame
from core.utilities.Interface.quit_interface import QuitInterface
from core.utilities.time.delay import Delay

class DinoScreen:

    def __init__(self, surface, input_manager):
        self.surface = surface

        self.input = input_manager

        self.state = "menu"
        self.next_state = None

        self.menu = DinoMenu(self.surface, self.input)
        self.game = DinoRunnerGame(self.surface, self.input)
        self.settings = DinoSettings(self.surface, self.input)
        self.quit = QuitInterface(self.surface)

        self.transition_delay = Delay(500)  # 0.5 secondes

    def update(self):

        if self.state == "menu":

            result = self.menu.update()

            if result == "PLAY":
                self.next_state = "play"
                self.state = "transition"
                self.transition_delay.start()

            if result == "SETTINGS":
                self.next_state = "settings"
                self.state = "transition"
                self.transition_delay.start()

            if result == "RETURN":
                return "RETURN"

            if result == "QUIT":
                self.next_state = "quit"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "play":
            result_game = self.game.update()

            if result_game == "MENU":
                self.next_state = "menu"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "settings":

            settings_result = self.settings.update()

            if settings_result == "RETURN":
                self.next_state = "menu"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "quit":
            
            quit_result = self.quit.update()

            if quit_result == "YES":
                pygame.quit()
            if quit_result == "NO":
                self.next_state = "menu"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "transition":

            if not self.transition_delay.is_running():
                self.state = self.next_state
                self.next_state = None

    def draw(self, surface):

        self.surface.fill((30, 30, 30))

        if self.state == "menu" and not self.transition_delay.is_running():
            self.menu.draw(surface)

        if self.state == "play" and not self.transition_delay.is_running():
            self.game.draw(surface)

        if self.state == "settings" and not self.transition_delay.is_running():
            self.settings.draw(surface)