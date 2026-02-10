import pygame
from screen import Screen

class Game:

    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = Screen()

    def run(self):

        while self.running :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.update()
            self.screen.draw()

            pygame.display.flip()
            self.clock.tick(60)