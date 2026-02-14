import pygame
from game import Game
from core.utilities.input.input_manager import InputManager

pygame.init()

Game = Game()
Game.run()

pygame.quit()