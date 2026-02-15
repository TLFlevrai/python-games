import pygame

from core.main_interface.menu import Menu
from core.main_interface.settings import Settings
from games.pong.pong_screen import PongScreen
from games.flappy_bird.flappy_bird_screen import FlappyBirdScreen
from core.utilities.Interface.quit_interface import QuitInterface
from core.utilities.time.delay import Delay

class Screen:

    def __init__(self, input_manager):
        self.width = 800
        self.height = 600

        self.input = input_manager

        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Python Games")

        try :
            icon = pygame.image.load("assets/LOGO_PYTHON_GAMES.png")
            pygame.display.set_icon(icon)
        except (pygame.error, FileNotFoundError) as e:
            print(f"⚠️ Warning: Could not load icon - {e}")

        self.transition_delay = Delay(500)  # 0.5 seconde

        self.state = "main_menu"
        
        self.next_state = None
        self.menu = Menu(self.surface, self.input)
        self.pong = PongScreen(self.surface, self.input, self.width, self.height)
        self.flappy_bird = FlappyBirdScreen()
        self.settings = Settings(self.surface, self.input)
        self.quit = QuitInterface(self.surface)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def update(self):

        if self.state == "main_menu":

            result_menu = self.menu.update()

            if result_menu == "PONG":
                self.next_state = "pong"
                self.state = "transition"
                self.transition_delay.start()

            elif result_menu == "SETTINGS":
                self.state = "settings"
                self.transition_delay.start()

            elif result_menu == "QUIT":
                self.state = "quit"
                self.transition_delay.start()

        elif self.state == "pong":

            result_pong = self.pong.update()

            if result_pong == "RETURN":
                self.state = "main_menu"
                self.transition_delay.start()

        elif self.state == "settings":

            result2 = self.settings.update()

            if result2 == "RETURN":
                self.state = "main_menu"
                self.transition_delay.start()

        elif self.state == "quit":

            result_quit = self.quit.update()

            if result_quit == "YES":
                print("good bye !")
                pygame.quit()
            if result_quit == "NO":
                self.state = "main_menu"
                self.transition_delay.start()

        elif self.state == "transition":

            if not self.transition_delay.is_running():
                self.state = self.next_state
                self.next_state = None

    def draw(self):

        self.surface.fill((30, 30, 30))

        if self.state == "main_menu":
            self.menu.draw(self.surface)

        if self.state == "pong":
            self.pong.draw(self.surface)

        if self.state == "settings":
            self.settings.draw(self.surface)

        if self.state == "quit":
            self.quit.draw(self.surface)

        if self.state == "transition":
            pass