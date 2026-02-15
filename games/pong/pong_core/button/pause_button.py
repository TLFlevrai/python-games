import pygame

class PauseButton:

    def __init__(self, screen_width, screen_height, input_manager):

        self.input = input_manager
        self.visible = True

        size = 40

        self.rect = pygame.Rect(0,0,size,size)
        self.rect.center = (screen_width//2, screen_height - 40)

    def update(self):

        if not self.visible:
            return False
        
        mouse_pos = self.input.get_mouse_pos()

        if self.rect.collidepoint(mouse_pos):

            if self.input.click():
                print("pause_button clicked")
                return True

        return False

    def draw(self, surface):

        if not self.visible:
            return

        # dessine symbole pause
        bar_width = 6
        gap = 6

        x, y = self.rect.center
        h = 20

        pygame.draw.rect(surface,(255,255,255),(x-gap-bar_width,y-h//2,bar_width,h))
        pygame.draw.rect(surface,(255,255,255),(x+gap,y-h//2,bar_width,h))