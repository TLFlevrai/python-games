import pygame

from screen import Screen
from core.utilities.input.input_manager import InputManager

class Game:

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()

        self.input = InputManager()
        self.screen = Screen(self.input)

    def run(self):

        while self.running :

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            #input manager
            self.input.update(events)

            screen_result = self.screen.update()

            if screen_result == "QUIT":
                print("good bye !")
                pygame.quit()

            self.screen.draw()

            pygame.display.flip()
            self.clock.tick(60)