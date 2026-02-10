import pygame
from core.utilities.UI.Layout import Layout
from core.utilities.UI.create_buton import Button
from core.utilities.UI.create_label import Label

class Menu:

    def __init__(self, screen):
        self.screen = screen

        w = screen.get_width() #800
        h = screen.get_height() #600

        self.title = Label(text="Menu", position=Layout.CENTER, font_size=48)

        self.pong_button = Button("PONG", (w//2, h//2 - 100))
        self.settings_button = Button("SETTINGS", (w//2, h//2 - 25))
        self.quit_button = Button("QUIT", (w//2, h//2 + 50))

        self.last_click_time = 0
        self.cooldown = 1000

    def update(self):

        if self.pong_button.update():
            print("button_clicked : PONG (menu.py)")
            return "PONG"

        if self.settings_button.update():
            print("button_clicked : SETTINGS (menu.py)")
            return "SETTINGS"

        if self.quit_button.update():
            print("button_clicked : QUIT (menu.py)")
            return "QUIT"

    def draw(self, surface):
        self.title.draw(surface)

        #pong
        self.pong_button.draw(surface)

        #settings
        self.settings_button.draw(surface)

        #quit
        self.quit_button.draw(surface)