# games/dino/core/managers/obstacle_manager.py

import pygame
from ..configs import game_config
from ..entities import Obstacle

class ObstacleManager:
    """
    Gestionnaire d'obstacles pour Dino Runner.
    Spawn automatique, vitesse progressive.
    """

    def __init__(self, screen_width, ground_y):

        self.screen_width = screen_width
        self.ground_y = ground_y

        self.obstacles = []

        # ---------- SPAWN TIMING ----------
        self.spawn_timer = 0
        self.spawn_interval = game_config.initial_spawn_interval
        self.min_spawn_interval = game_config.min_spawn_interval

        # ---------- VITESSE ----------
        self.initial_speed = game_config.initial_speed
        self.speed = self.initial_speed
        self.speed_increment = game_config.speed_increment  # Augmentation progressive

    # ---------- UPDATE ----------

    def update(self, dino_rect):
        """
        Met à jour tous les obstacles.
        
        Returns:
            bool: True si collision détectée
        """

        collision = False

        # Timer de spawn
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_obstacle()
            self.spawn_timer = 0

        # Mise à jour de chaque obstacle
        for obstacle in self.obstacles[:]:

            obstacle.update()

            # Collision avec le dino
            if obstacle.get_rect().colliderect(dino_rect):
                collision = True

            # Suppression hors écran
            if obstacle.is_offscreen():
                self.obstacles.remove(obstacle)

        # Augmentation progressive de la vitesse
        self.speed += self.speed_increment

        return collision

    # ---------- SPAWN ----------

    def spawn_obstacle(self):
        """Crée un nouvel obstacle"""
        obstacle = Obstacle(self.screen_width, self.ground_y, self.speed)
        self.obstacles.append(obstacle)

    # ---------- DRAW ----------

    def draw(self, surface):
        """Dessine tous les obstacles"""
        for obstacle in self.obstacles:
            obstacle.draw(surface)

    # ---------- RESET ----------

    def reset(self):
        """Réinitialise le gestionnaire"""
        self.obstacles.clear()
        self.spawn_timer = 0
        self.speed = self.initial_speed

    # ---------- DIFFICULTY ----------

    def increase_difficulty(self):
        """Réduit l'intervalle de spawn (plus difficile)"""
        if self.spawn_interval > self.min_spawn_interval:
            self.spawn_interval -= 5