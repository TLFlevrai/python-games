import pygame

class Delay:

    def __init__(self, duration_ms):
        """
        duration_ms : durée du delay en millisecondes
        """
        self.duration = duration_ms
        self.start_time = None
        self.active = False

    def start(self):
        """Active le delay"""
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def is_running(self):
        """Retourne True si le delay est encore actif"""
        if not self.active:
            return False

        current = pygame.time.get_ticks()

        if current - self.start_time >= self.duration:
            self.active = False
            return False

        return True
    
    def is_finished(self):
        if not self.active:
            return True