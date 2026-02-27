import pygame
import os
from .base import Obstacle
from ...configs import obstacle_config
from core.engine.animation import Animation

class Bird(Obstacle):
    def __init__(self, screen_width, ground_y, speed, width, height, color, points, y_offset, image_paths):
        self.animation = None
        image = None
        if image_paths:
            frames = []
            for path in image_paths:
                full_path = os.path.join(obstacle_config.base_path, path)
                try:
                    raw = pygame.image.load(full_path).convert_alpha()
                    frame = pygame.transform.scale(raw, (width, height))
                    frames.append(frame)
                except (pygame.error, FileNotFoundError) as e:
                    print(f"⚠️ Impossible de charger {full_path}: {e}")
            if frames:
                self.animation = Animation(frames, frame_duration=100)
                image = frames[0]

        super().__init__(screen_width, ground_y, speed, width, height, color, points, image, y_offset)

    def update(self):
        super().update()
        if self.animation:
            self.animation.update()
            self.image = self.animation.get_frame()