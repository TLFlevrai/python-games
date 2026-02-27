# games/dino/dino_game.py

import pygame
import random
from .core import (
    Dino, Ground, Cloud,
    ObstacleManager, ScoreManager, SoundManager,
    PauseInterface, GameOverInterface,
    game_config
)

class DinoGame:
    def __init__(self, screen, input_manager):
        self.surface = screen
        self.input = input_manager
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.ground = Ground(self.screen_width, self.screen_height)

        self.state = "playing"
        self.dino = Dino(self.ground.y)
        self.obstacle_manager = ObstacleManager(self.screen_width, self.ground.y)
        self.score_manager = ScoreManager()
        self.sound_manager = SoundManager()

        self.clouds = []
        self.cloud_timer = 0
        self.cloud_spawn_interval = game_config.cloud_spawn_interval

        self.pause_interface = PauseInterface(self.surface, self.input)
        self.game_over_interface = GameOverInterface(self.surface, self.input)

        self.font_score = pygame.font.SysFont("Courier New", 20)
        self.last_point_sound_score = 0

    def reset(self):
        self.state = "playing"
        self.dino.reset(self.ground.y)
        self.obstacle_manager.reset()
        self.score_manager.reset()
        self.clouds.clear()
        self.cloud_timer = 0
        self.last_point_sound_score = 0
        print("🔄 Dino Game reset")

    def update(self):
        if self.state == "playing":
            # Input
            if self.input.space_pressed() or self.input.click():
                self.dino.jump()
                self.sound_manager.play_jump()

            # Gestion du canard (touche bas)
            if self.input.key_is_pressed(pygame.K_DOWN):
                self.dino.duck()
            else:
                self.dino.unduck()

            if self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "paused"
                return

            # Mise à jour des entités
            self.dino.update()
            self.ground.update()

            # Nuages
            now = pygame.time.get_ticks()
            if now - self.cloud_timer >= self.cloud_spawn_interval:
                y = random.randint(50, 300)
                self.clouds.append(Cloud(self.screen_width, y))
                self.cloud_timer = now

            for cloud in self.clouds[:]:
                cloud.update()
                if cloud.is_offscreen():
                    self.clouds.remove(cloud)

            # Obstacles
            collision = self.obstacle_manager.update(self.dino.get_rect())
            if collision:
                self.sound_manager.play_death()
                self.state = "game_over"
                return

            # Score
            self.score_manager.increase_time_score()
            # Son tous les 100 points (arrondi à l'entier)
            current_int = int(self.score_manager.current_score)
            if current_int // 100 > self.last_point_sound_score:
                self.sound_manager.play_point()
                self.last_point_sound_score = current_int // 100

        elif self.state == "paused":
            result = self.pause_interface.update()
            if result == "RESUME" or self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "playing"
            elif result == "RESTART":
                self.reset()
            elif result == "MENU":
                return "MENU"

        elif self.state == "game_over":
            result = self.game_over_interface.update(
                self.score_manager.current_score,
                self.score_manager.high_score
            )
            if result == "RESTART":
                self.reset()
            elif result == "MENU":
                return "MENU"

    def draw(self, surface):
        surface.fill((255, 255, 255))

        for cloud in self.clouds:
            cloud.draw(surface)

        self.ground.draw(surface)
        self.dino.draw(surface)
        self.obstacle_manager.draw(surface)

        if self.state == "playing":
            self._draw_scores(surface)

        if self.state == "paused":
            self.pause_interface.draw(surface)
        elif self.state == "game_over":
            self.game_over_interface.draw(
                surface,
                self.score_manager.current_score,
                self.score_manager.high_score
            )

    def _draw_scores(self, surface):
        score_text = self.font_score.render(
            f"Score: {self.score_manager.get_formatted_score()}",
            True, (83,83,83)
        )
        surface.blit(score_text, (self.screen_width - 200, 30))

        high_score_text = self.font_score.render(
            f"HI: {self.score_manager.get_formatted_high_score()}",
            True, (100,100,100)
        )
        surface.blit(high_score_text, (self.screen_width - 200, 55))

        if (self.score_manager.current_score >= self.score_manager.high_score
                and self.score_manager.current_score > 0):
            record_font = pygame.font.SysFont("Courier New", 16)
            record_text = record_font.render("NEW RECORD!", True, (255,200,50))
            surface.blit(record_text, (self.screen_width - 200, 75))