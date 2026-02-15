import pygame

class PlayButton:

    def __init__(self, screen_width, screen_height, input_manager):

        self.input = input_manager
        self.visible = False

        size = 40

        self.rect = pygame.Rect(0,0,size,size)
        self.rect.center = (screen_width//2, screen_height - 40)

    def update(self):

        if not self.visible:
            return False
        
        mouse_pos = self.input.get_mouse_pos()

        if self.rect.collidepoint(mouse_pos):

            if self.input.click():
                print("play button clicked")
                return True

        return False

    def draw(self, surface):

        if not self.visible:
            return

        x,y = self.rect.center

        points = [
            (x-10,y-12),
            (x-10,y+12),
            (x+12,y)
        ]

        pygame.draw.polygon(surface,(255,255,255),points)