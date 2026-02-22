import pygame

#import interface
from games.flappy_bird.flappy_bird_game import FlappyBirdGame
from games.flappy_bird.flappy_bird_core.interface.flappy_bird_menu import FlappyBirdMenu
from games.flappy_bird.flappy_bird_core.interface.flappy_bird_settings import FlappyBirdSettings
from core.Interface.quit_interface import QuitInterface

#import utilities
from core.utilities.time.delay import Delay

class FlappyBirdScreen :

    def __init__(self, surface, input_manager):
        
        self.surface = surface
        self.input = input_manager

        #init state
        self.state = "menu"
        self.next_state = None

        self.menu = FlappyBirdMenu(self.surface, self.input)
        self.game = FlappyBirdGame(self.surface, self.input)
        self.settings = FlappyBirdSettings(self.surface, self.input)
        self.quit = QuitInterface(self.surface, self.input)

        self.transition_delay = Delay(500)  # 0.5 secondes

    def update(self):
        
        if self.state == "menu":

            result_menu = self.menu.update()

            if result_menu == "PLAY":
                self.next_state = "play"
                self.state = "transition"
                self.transition_delay.start()

            if result_menu == "SETTINGS":
                self.next_state = "settings"
                self.state = "transition"
                self.transition_delay.start()

            if result_menu == "RETURN":
                self.state = "menu"
                return "RETURN"
            
            if result_menu == "QUIT":
                self.next_state = "quit"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "play":
            result_game = self.game.update()  # ← Récupère le retour du jeu

            # Si le jeu demande de retourner au menu
            if result_game == "MENU":
                self.game.reset()
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

        if self.state == "play" and not self.transition_delay.is_running():
            self.game.draw(surface)

        if self.state == "settings" and not self.transition_delay.is_running():
            self.settings.draw(surface)

        if self.state == "quit" and not self.transition_delay.is_running():
            self.quit.draw(surface)

        if self.state == "transition" :
            pass