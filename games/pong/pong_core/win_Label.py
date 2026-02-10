import pygame

class WinLabel:

    def __init__(self, screen):

        self.screen = screen
        self.font = pygame.font.SysFont(None, 72)

        self.visible = False
        self.text = ""
        self.color = (255, 255, 255)

    def show_left_win(self):
        self.visible = True
        self.text = "LEFT PLAYER WINS"
        self.color = (50, 100, 255) #bleu

    def show_right_win(self):
        self.visible = True
        self.text = "RIGHT PLAYER WINS"
        self.color = (255, 80, 80) #rouge

    def hide(self):
        self.visible = False

    def draw(self, surface):

        if not self.visible:
            return

        label = self.font.render(self.text, True, self.color)

        rect = label.get_rect(center=(
            surface.get_width() // 2,
            surface.get_height() // 2
        ))

        surface.blit(label, rect)