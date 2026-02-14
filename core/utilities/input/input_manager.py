import pygame

class InputManager:

    def __init__(self):

        self.last_click = (0, 0)

        self.mouse_pressed = False
        self.mouse_just_pressed = False
        self.mouse_released = False

        self.last_click = 0
        self.cooldown = 150

    def update(self, events):

        now = pygame.time.get_ticks()

        self.mouse_just_pressed = False
        self.mouse_released = False

        self.mouse_pos = pygame.mouse.get_pos()

        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:

                if not self.mouse_pressed:

                    if now - self.last_click > self.cooldown:
                        self.mouse_just_pressed = True
                        self.last_click = now

                self.mouse_pressed = True

            elif event.type == pygame.MOUSEBUTTONUP:

                self.mouse_pressed = False
                self.mouse_released = True

    # ---------- API ----------

    def click(self):
        return self.mouse_just_pressed

    def pressed(self):
        return self.mouse_pressed

    def released(self):
        return self.mouse_released

    def get_mouse_pos(self):
        return self.mouse_pos