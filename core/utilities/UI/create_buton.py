import pygame
from core.utilities.colors import Colors
from core.utilities.input.input_manager import InputManager

class Button:

    def __init__(self, text, center_pos, input_manager, size=(200,50)):

        self.input = input_manager
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0,*size)
        self.rect.center = center_pos

        self.text = text

    def update(self):

        mouse_pos = self.input.get_mouse_pos()

        if self.rect.collidepoint(mouse_pos):

            if self.input.click() :

                return True

        return False

    def draw(self, surface):

        mouse_pos = self.input.get_mouse_pos()

        # hover color
        color = Colors.BUTTON_HOVER if self.rect.collidepoint(mouse_pos) else Colors.BUTTON

        pygame.draw.rect(surface, color, self.rect)

        label = self.font.render(self.text, True, Colors.WHITE)
        label_rect = label.get_rect(center=self.rect.center)

        surface.blit(label, label_rect)

    def set_position(self, pos):
        self.rect.center = pos