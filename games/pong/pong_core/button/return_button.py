import pygame

class ReturnButton:

    def __init__(self, x, y, input_manager):

        self.input = input_manager
        self.visible = False

        size = 40
        self.rect = pygame.Rect(0,0,size,size)
        self.rect.center = (x,y)

    def update(self):

        if not self.visible:
            return False

        mouse_pos = self.input.get_mouse_pos()

        if self.rect.collidepoint(mouse_pos):
            if self.input.click():
                return True

        return False

    def draw(self, surface):

        if not self.visible:
            return

        x,y = self.rect.center

        pygame.draw.polygon(surface,(255,255,255),[
            (x-10,y),
            (x+5,y-10),
            (x+5,y+10)
        ])