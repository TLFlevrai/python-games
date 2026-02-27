#games/dino/core/managers/sound_manager.py

import pygame
from ..configs import game_config

class SoundManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.jump_sound = None
        self.death_sound = None
        self.point_sound = None
        self._load_sounds()

    def _load_sounds(self):
        try:
            self.jump_sound = pygame.mixer.Sound(game_config.jump_sound_path)
            self.death_sound = pygame.mixer.Sound(game_config.death_sound_path)
            self.point_sound = pygame.mixer.Sound(game_config.point_sound_path)
            print("✅ Sons chargés")
        except (pygame.error, FileNotFoundError) as e:
            print(f"⚠️ Sons non chargés: {e}")

    def play_jump(self):
        if self.jump_sound:
            self.jump_sound.play()

    def play_death(self):
        if self.death_sound:
            self.death_sound.play()

    def play_point(self):
        if self.point_sound:
            self.point_sound.play()