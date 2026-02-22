# games/dino/core/configs/game_config.py

from dataclasses import dataclass
from core.utilities.colors import Colors

@dataclass
class GameConfig:
    screen_width: int = 800
    screen_height: int = 600
    ground_level: int = 80
    initial_speed: int = 6
    speed_increment: float = 0.002
    max_speed: int = 20
    initial_spawn_interval: int = 90
    min_spawn_interval: int = 40
    ground_color: tuple = Colors.GRAY
    ground_line_thickness: int = 3

    def get_ground_y(self) -> int:
        return self.screen_height - self.ground_level

game_config = GameConfig()