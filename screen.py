import pygame

from menu import Menu
from settings import Settings
from pong.pong_screen import PongScreen

class Screen:

    def __init__(self):
        self.surface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Python Games")

        self.state = "main_menu"

        self.settings = Settings(self.surface)
        self.menu = Menu(self.surface)
        self.pong = PongScreen(self.surface)


    def update(self):

        if self.state == "main_menu":

            result1 = self.menu.update()

            if result1 == "PONG":
                self.state = "pong"

            elif result1 == "SETTINGS":
                self.state = "settings"

        elif self.state == "settings":

            result2 = self.settings.update()

            if result2 == "RETURN":
                self.state = "main_menu"


        elif self.state == "pong":

            self.pong.update()

    def draw(self):

        self.surface.fill((30, 30, 30))

        if self.state == "main_menu":
            self.menu.draw(self.surface)

        if self.state == "settings":
            self.settings.draw(self.surface)

        if self.state == "pong":
            self.pong.draw(self.surface)