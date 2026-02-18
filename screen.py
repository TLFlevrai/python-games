import pygame

from core.main_interface.menu import Menu
from core.main_interface.settings import Settings
from core.utilities.Interface.game_choice import GameChoice
from games.pong.pong_screen import PongScreen
from games.flappy_bird.flappy_bird_screen import FlappyBirdScreen
from games.tic_tac_toe.tic_tac_toe_screen import TicTacToeScreen
from games.dino.dino_screen import DinoScreen
from core.utilities.Interface.quit_interface import QuitInterface
from core.utilities.time.delay import Delay

class Screen:

    def __init__(self, input_manager):
        self.current_resolution = "Fullscreen"  # ← Corriger la typo "FullScreen" → "Fullscreen"

        self.input = input_manager

        # ← Démarrer directement en fullscreen
        self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Récupérer les vraies dimensions
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        
        self.current_resolution = "FullScreen"

        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Python Games")

        try :
            icon = pygame.image.load("assets/LOGO_PYTHON_GAMES.png")
            pygame.display.set_icon(icon)
        except (pygame.error, FileNotFoundError) as e:
            print(f"⚠️ Warning: Could not load icon - {e}")

        self.transition_delay = Delay(500)  # 0.5 secondes

        self.state = "main_menu"
        
        self.next_state = None
        self.menu = Menu(self.surface, self.input)
        self.game_choice = GameChoice(self.surface, self.input)
        self.settings = Settings(self.surface, self.input, self.current_resolution)
        self.pong = PongScreen(self.surface, self.input)
        self.flappy_bird = FlappyBirdScreen(self.surface, self.input)
        self.tic_tac_toe = TicTacToeScreen(self.surface, self.input)
        self.dino = DinoScreen(self.surface, self.input)
        self.quit = QuitInterface(self.surface)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def update(self):

        if self.state == "main_menu":

            result_menu = self.menu.update()

            if result_menu == "PLAY":
                self.next_state = "play"
                self.state = "transition"
                self.transition_delay.start()

            elif result_menu == "SETTINGS":
                self.next_state = "settings"
                self.state = "transition"
                self.transition_delay.start()

            elif result_menu == "QUIT":
                self.next_state = "quit"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "play":

            result_game_choice = self.game_choice.update()

            if result_game_choice == "FLAPPY_BIRD":
                self.next_state = "flappy_bird"
                self.state = "transition"
                self.transition_delay.start()

            elif result_game_choice == "PONG":
                self.next_state = "pong"
                self.state = "transition"
                self.transition_delay.start()

            elif result_game_choice == "Tic_Tac_Toe":
                self.next_state = "tic_tac_toe"
                self.state = "transition"
                self.transition_delay.start()

            elif result_game_choice == "Dino":
                self.next_state = "dino"
                self.state = "transition"
                self.transition_delay.start()

            elif result_game_choice == "RETURN":
                self.next_state = "main_menu"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "pong":

            result_pong = self.pong.update()

            if result_pong == "RETURN":
                self.next_state = "play"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "flappy_bird":

            result_flappy_bird = self.flappy_bird.update()

            if result_flappy_bird == "RETURN":
                self.next_state = "play"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "tic_tac_toe":
            result_tic_tac_toe = self.tic_tac_toe.update()

            if result_tic_tac_toe == "RETURN":
                self.next_state = "play"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "dino":

            result_dino = self.dino.update()

            if result_dino == "RETURN":
                self.next_state = "play"
                self.state = "transition"
                self.transition_delay.start()

        elif self.state == "settings":

            result2 = self.settings.update()

            if result2 == "RETURN":
                self.state = "main_menu"
                self.transition_delay.start()

            elif result2 and result2.startswith("RESOLUTION:"):
                selected = result2.split(":")[1]
                self._apply_resolution(selected)

        elif self.state == "quit":

            result_quit = self.quit.update()

            if result_quit == "YES":
                return "QUIT"
            if result_quit == "NO":
                self.state = "main_menu"
                self.transition_delay.start()

        elif self.state == "transition":

            if not self.transition_delay.is_running():
                self.state = self.next_state
                self.next_state = None

    def draw(self):

        self.surface.fill((30, 30, 30))

        if self.state == "main_menu" and not self.transition_delay.is_running():
            self.menu.draw(self.surface)

        if self.state == "play" and not self.transition_delay.is_running():
            self.game_choice.draw(self.surface)

        if self.state == "pong" and not self.transition_delay.is_running():
            self.pong.draw(self.surface)

        if self.state == "flappy_bird" and not self.transition_delay.is_running():
            self.flappy_bird.draw(self.surface)

        if self.state == "tic_tac_toe" and not self.transition_delay.is_running():
            self.tic_tac_toe.draw(self.surface)

        if self.state == "dino" and not self.transition_delay.is_running():
            self.dino.draw(self.surface)

        if self.state == "settings" and not self.transition_delay.is_running():
            self.settings.draw(self.surface)

        if self.state == "quit" and not self.transition_delay.is_running():
            self.quit.draw(self.surface)

        if self.state == "transition":
            pass

    def _apply_resolution(self, resolution):
        """Applique la résolution sélectionnée et reconstruit tous les écrans"""

        if resolution == "Fullscreen":
            self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif resolution == "800x600":
            self.surface = pygame.display.set_mode((800, 600))
        elif resolution == "1280x720":
            self.surface = pygame.display.set_mode((1280, 720))

        # Mettre à jour les dimensions
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        self.current_resolution = resolution

        print(f"🖥️ Résolution appliquée : {self.width}x{self.height}")

        # Reconstruire tous les écrans avec les nouvelles dimensions
        self._rebuild()

    def _rebuild(self):
        """Recrée tous les écrans avec les dimensions actuelles"""

        self.menu = Menu(self.surface, self.input)
        self.pong = PongScreen(self.surface, self.input)
        self.flappy_bird = FlappyBirdScreen(self.surface, self.input)
        self.settings = Settings(self.surface, self.input, self.current_resolution)
        self.quit = QuitInterface(self.surface)

        self.state = "settings"  # ← Reste sur settings après rebuild ✅

        print("🔄 Tous les écrans reconstruits")