# games/dino/core/configs/dino_config.py
from dataclasses import dataclass
from typing import Tuple
from core.utilities.colors import Colors

@dataclass
class DinoConfig:
    x_position: int = 100
    width: int = 80       # ajusté pour correspondre aux sprites
    height: int = 100
    ducking_width: int = 110
    ducking_height: int = 60
    gravity: float = 2.0
    jump_strength: int = -25   # ajusté
    max_jumps: int = 1
    color: Tuple[int, int, int] = Colors.DINO_BODY
    debug_color: Tuple[int, int, int] = Colors.DINO_DEBUG

    # Sprites
    walk_sprites: list = None  # sera chargé dans le code
    duck_sprites: list = None

    def __post_init__(self):
        assert self.width > 0
        assert self.height > 0
        assert self.gravity > 0
        assert self.jump_strength < 0
        assert self.max_jumps >= 1

    @property
    def ground_collision_y(self) -> int:
        return self.height

    def __repr__(self) -> str:
        return f"DinoConfig(size={self.width}x{self.height}, gravity={self.gravity})"

dino_config = DinoConfig()