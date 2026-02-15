import pygame

class RestartButton:

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
                print("restart_button clicked")
                return True

        return False

    def draw(self, surface):

        if not self.visible:
            return

        center = self.rect.center

        # cercle
        pygame.draw.circle(surface,(255,255,255),center,15,2)

        # flèche
        pygame.draw.polygon(surface,(255,255,255),[
            (center[0]+5, center[1]-12),
            (center[0]+12, center[1]-12),
            (center[0]+12, center[1]-5)
        ])