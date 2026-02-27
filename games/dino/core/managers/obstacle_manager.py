# games/dino/core/managers/obstacle_manager.py

import pygame
import random
from ..configs import game_config, obstacle_config
from ..entities.obstacles import Cactus, Bird

class ObstacleManager:
    def __init__(self, screen_width, ground_y):
        self.screen_width = screen_width
        self.ground_y = ground_y
        self.obstacles = []
        self.spawn_timer = 0
        self.spawn_interval = game_config.initial_spawn_interval
        self.min_spawn_interval = game_config.min_spawn_interval
        self.initial_speed = game_config.initial_speed
        self.speed = self.initial_speed
        self.speed_increment = game_config.speed_increment

    def update(self, dino_rect):
        collision = False
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_obstacle()
            self.spawn_timer = 0

        for obstacle in self.obstacles[:]:
            obstacle.update()
            if obstacle.get_rect().colliderect(dino_rect):
                collision = True
            if obstacle.is_offscreen():
                self.obstacles.remove(obstacle)

        self.speed += self.speed_increment
        return collision

    def spawn_obstacle(self):
        # Reproduction de la logique du main.py
        r = random.randint(1, 50)
        if 1 <= r <= 6:
            # cactus
            name = f"cactus_{r}"
            obs_type = obstacle_config.get_type_by_name(name)
            obs = Cactus(
                self.screen_width,
                self.ground_y,
                self.speed,
                obs_type.width,
                obs_type.height,
                obs_type.color,
                obs_type.points,
                obs_type.image_paths,
                obs_type.y_offset
            )
            self.obstacles.append(obs)
        elif 7 <= r <= 9:
            # bird
            obs_type = obstacle_config.get_type_by_name("bird")
            obs = Bird(
                self.screen_width,
                self.ground_y,
                self.speed,
                obs_type.width,
                obs_type.height,
                obs_type.color,
                obs_type.points,
                obs_type.y_offset,
                obs_type.image_paths
            )
            self.obstacles.append(obs)
        # sinon pas d'obstacle

    def draw(self, surface):
        for obstacle in self.obstacles:
            obstacle.draw(surface)

    def reset(self):
        self.obstacles.clear()
        self.spawn_timer = 0
        self.speed = self.initial_speed

    def increase_difficulty(self):
        if self.spawn_interval > self.min_spawn_interval:
            self.spawn_interval -= 5