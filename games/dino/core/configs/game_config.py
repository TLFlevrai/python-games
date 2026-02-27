# games/dino/core/configs/game_config.py
from dataclasses import dataclass
from core.utilities.colors import Colors

@dataclass
class GameConfig:
    screen_width: int = 800
    screen_height: int = 600
    ground_level: int = 80
    ground_image_path: str = "assets/dino/entity/ground/ground.png"
    ground_scroll_speed: int = 12  # vitesse de défilement du sol
    cloud_spawn_interval: int = 3000  # ms
    cloud_image_path: str = "assets/dino/entity/cloud/cloud.png"
    initial_speed: int = 12
    speed_increment: float = 0.006
    max_speed: int = 30
    initial_spawn_interval: int = 90
    min_spawn_interval: int = 40
    ground_color: tuple = Colors.GRAY  # fallback si image absente
    ground_line_thickness: int = 3

    # Sons
    jump_sound_path: str = "assets/dino/audio/jump.mp3"
    death_sound_path: str = "assets/dino/audio/lose.mp3"
    point_sound_path: str = "assets/dino/audio/100points.mp3"

    def get_ground_y(self) -> int:
        return self.screen_height - self.ground_level

game_config = GameConfig()