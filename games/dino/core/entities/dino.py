# games/dino/core/entities/dino.py

import pygame
import os
from ..configs import dino_config
from core.engine.animation import Animation

class Dino:
    def __init__(self, ground_y):
        self.x = dino_config.x_position
        self.ground_y = ground_y
        self.width = dino_config.width
        self.height = dino_config.height
        self.ducking_width = dino_config.ducking_width
        self.ducking_height = dino_config.ducking_height

        self.gravity = dino_config.gravity
        self.jump_strength = dino_config.jump_strength
        self.velocity_y = 0

        self.is_jumping = False
        self.is_alive = True
        self.ducking = False

        # Position et hitbox : on utilise rect pour tout
        self.rect = pygame.Rect(self.x, self.ground_y - self.height, self.width, self.height)

        self.running_animation = None
        self.ducking_animation = None
        self.jump_image = None
        self.current_image = None
        self._load_sprites()

    def _load_sprites(self):
        base_path = os.path.join("assets", "dino", "entity", "dino")
        try:
            run1 = pygame.image.load(os.path.join(base_path, "walk", "dino_walk1.png")).convert_alpha()
            run2 = pygame.image.load(os.path.join(base_path, "walk", "dino_walk2.png")).convert_alpha()
            run1 = pygame.transform.scale(run1, (self.width, self.height))
            run2 = pygame.transform.scale(run2, (self.width, self.height))
            self.running_animation = Animation([run1, run2], frame_duration=200)

            duck1 = pygame.image.load(os.path.join(base_path, "ducking", "dino_duck1.png")).convert_alpha()
            duck2 = pygame.image.load(os.path.join(base_path, "ducking", "dino_duck2.png")).convert_alpha()
            duck1 = pygame.transform.scale(duck1, (self.ducking_width, self.ducking_height))
            duck2 = pygame.transform.scale(duck2, (self.ducking_width, self.ducking_height))
            self.ducking_animation = Animation([duck1, duck2], frame_duration=200)

            jump = pygame.image.load(os.path.join(base_path, "jump", "dino_jump.png")).convert_alpha()
            self.jump_image = pygame.transform.scale(jump, (self.width, self.height))

            self.current_image = run1
            print("✅ Sprites Dino chargés")
        except Exception as e:
            print(f"⚠️ Erreur chargement sprites Dino: {e}")
            self.color = dino_config.color

    def jump(self):
        if not self.is_jumping and self.is_alive and not self.ducking:
            self.velocity_y = self.jump_strength
            self.is_jumping = True

    def duck(self):
        if not self.is_jumping and self.is_alive:
            self.ducking = True
            # Ajuster la hitbox
            self.rect.width = self.ducking_width
            self.rect.height = self.ducking_height
            self.rect.bottom = self.ground_y  # le bas reste au sol

    def unduck(self):
        if self.ducking:
            self.ducking = False
            self.rect.width = self.width
            self.rect.height = self.height
            self.rect.bottom = self.ground_y

    def update(self):
        if not self.is_alive:
            return

        # Physique (on utilise rect.y)
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.velocity_y = 0
            self.is_jumping = False

        # Animation
        if self.is_jumping and self.jump_image:
            self.current_image = self.jump_image
            
        elif self.ducking and self.ducking_animation:
            self.ducking_animation.update()
            self.current_image = self.ducking_animation.get_frame()
        elif self.running_animation and not self.is_jumping:
            self.running_animation.update()
            self.current_image = self.running_animation.get_frame()

    def draw(self, surface):
        if self.current_image:
            surface.blit(self.current_image, self.rect.topleft)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

    def get_rect(self):
        return self.rect

    def die(self):
        self.is_alive = False

    def reset(self, ground_y):
        self.ground_y = ground_y
        self.rect.topleft = (self.x, ground_y - self.height)
        self.rect.width = self.width
        self.rect.height = self.height
        self.velocity_y = 0
        self.is_jumping = False
        self.is_alive = True
        self.ducking = False
        
        if self.running_animation:
            self.running_animation.current_frame = 0
            self.running_animation.last_update = pygame.time.get_ticks()
            self.current_image = self.running_animation.get_frame()