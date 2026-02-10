import pygame

from pong.pong_menu import PongMenu
from pong.pong_game import PongGame
from pong.pong_settings import PongSettings

class PongScreen:

    def __init__(self, screen):

        self.surface = screen

        self.state = "menu"

        self.menu = PongMenu(self.surface)
        self.game = PongGame(self.surface)
        self.settings = PongSettings(self.surface)

    def update(self):

        if self.state == "menu":

            result = self.menu.update()

            if result == "PLAY":
                self.state = "game"

        elif self.state == "game":

            self.game.update()

    def draw(self, surface):

        self.surface.fill((30, 30, 30))

        if self.state == "menu":
            self.menu.draw(surface)

        if self.state == "game":
            self.game.draw(surface)
