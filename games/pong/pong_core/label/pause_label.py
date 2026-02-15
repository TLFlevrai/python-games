import pygame

class PauseLabel:

    def __init__(self, surface):

        self.visible = False

        self.font = pygame.font.SysFont(None,60)

        self.surface = surface

    def draw(self, surface):

        if not self.visible:
            return

        text = self.font.render("GAME PAUSED",True,(255,255,255))

        rect = text.get_rect(center=(400,300))

        surface.blit(text,rect)