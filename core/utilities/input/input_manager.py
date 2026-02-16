import pygame

class InputManager:

    def __init__(self):

        self.last_click = (0, 0)

        self.mouse_pressed = False
        self.mouse_just_pressed = False
        self.mouse_released = False

        self.last_click = 0
        self.cooldown = 150

        # ---------- KEYBOARD ----------
        self.keys_just_pressed = {}  # Dictionnaire pour tracker les touches
        self.keys_pressed = {}
        self.last_key_press = {}  # Cooldown par touche
        self.key_cooldown = 150  # ms

    def update(self, events):

        now = pygame.time.get_ticks()

        # Reset flags
        self.mouse_just_pressed = False
        self.mouse_released = False
        self.keys_just_pressed.clear()

        self.mouse_pos = pygame.mouse.get_pos()

        for event in events:

            # ---------- MOUSE ----------
            if event.type == pygame.MOUSEBUTTONDOWN:

                if not self.mouse_pressed:

                    if now - self.last_click > self.cooldown:
                        self.mouse_just_pressed = True
                        self.last_click = now

                self.mouse_pressed = True

            elif event.type == pygame.MOUSEBUTTONUP:

                self.mouse_pressed = False
                self.mouse_released = True

            # ---------- KEYBOARD ----------
            elif event.type == pygame.KEYDOWN:

                key = event.key

                # Vérifier le cooldown pour cette touche
                last_press = self.last_key_press.get(key, 0)

                if now - last_press > self.key_cooldown:
                    self.keys_just_pressed[key] = True
                    self.last_key_press[key] = now

                self.keys_pressed[key] = True

            elif event.type == pygame.KEYUP:

                key = event.key
                if key in self.keys_pressed:
                    del self.keys_pressed[key]

    # ---------- MOUSE API ----------

    def click(self):
        return self.mouse_just_pressed

    def pressed(self):
        return self.mouse_pressed

    def released(self):
        return self.mouse_released

    def get_mouse_pos(self):
        return self.mouse_pos

    # ---------- KEYBOARD API ----------

    def key_just_pressed(self, key):
        """Vérifie si une touche vient d'être pressée (avec cooldown)"""
        return self.keys_just_pressed.get(key, False)

    def key_is_pressed(self, key):
        """Vérifie si une touche est actuellement maintenue"""
        return self.keys_pressed.get(key, False)

    def space_pressed(self):
        """Raccourci pour la touche Espace"""
        return self.key_just_pressed(pygame.K_SPACE)