# core/engine/game.py
import pygame
from .scene_manager import SceneManager

class Game:
    def __init__(self, screen, input_manager):
        self.screen = screen
        self.input = input_manager
        self.scene_manager = SceneManager()

    def update(self):
        self.scene_manager.update()

    def draw(self):
        self.scene_manager.draw(self.screen)

    def handle_event(self, event):
        self.scene_manager.handle_event(event)