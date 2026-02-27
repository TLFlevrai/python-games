import pygame
import os
from .base import Obstacle
from ...configs import obstacle_config

class Cactus(Obstacle):
    def __init__(self, screen_width, ground_y, speed, width, height, color, points, image_paths, y_offset=0):
        # Charger la première image de la liste
        image = None
        if image_paths and len(image_paths) > 0:
            full_path = os.path.join(obstacle_config.base_path, image_paths[0])
            try:
                raw = pygame.image.load(full_path).convert_alpha()
                image = pygame.transform.scale(raw, (width, height))
                print(f"✅ Chargé: {full_path}")
            except (pygame.error, FileNotFoundError) as e:
                print(f"⚠️ Impossible de charger {full_path}: {e}")

        super().__init__(screen_width, ground_y, speed, width, height, color, points, image, y_offset)
        # La classe de base positionne déjà correctement l'obstacle, pas besoin de réajuster ici