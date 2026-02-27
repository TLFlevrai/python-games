# core/engine/animation.py
import pygame

class Animation:
    def __init__(self, frames, frame_duration=100):
        self.frames = frames  # liste de surfaces
        self.frame_duration = frame_duration  # durée en ms par frame
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now

    def get_frame(self):
        return self.frames[self.current_frame]