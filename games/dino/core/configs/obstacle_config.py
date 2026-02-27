# games/dino/core/configs/obstacle_config.py
from dataclasses import dataclass, field
from typing import List
import random
import os
from core.utilities.colors import Colors

@dataclass
class ObstacleType:
    name: str
    class_name: str
    width: int
    height: int
    points: int = 100
    color: tuple = Colors.CACTUS_GREEN
    y_offset: int = 0
    spawn_weight: int = 1
    image_paths: List[str] = field(default_factory=list)

@dataclass
class ObstacleConfig:
    types: List[ObstacleType] = field(default_factory=list)
    base_path: str = os.path.join("assets", "dino", "entity", "obstacle")

    def __post_init__(self):
        if not self.types:
            self.types = [
                ObstacleType("cactus_1", "cactus", 100, 100, 100, Colors.CACTUS_GREEN, 5, 4,
                             [os.path.join("cactus", "cactus1.png")]),
                ObstacleType("cactus_2", "cactus", 100, 100, 150, Colors.CACTUS_GREEN, 5, 3,
                             [os.path.join("cactus", "cactus2.png")]),
                ObstacleType("cactus_3", "cactus", 100, 100, 200, Colors.CACTUS_GREEN, 5, 2,
                             [os.path.join("cactus", "cactus3.png")]),
                ObstacleType("cactus_4", "cactus", 100, 100, 250, Colors.CACTUS_GREEN, 5, 1,
                             [os.path.join("cactus", "cactus4.png")]),
                ObstacleType("cactus_5", "cactus", 100, 100, 200, Colors.CACTUS_GREEN, 5, 2,
                             [os.path.join("cactus", "cactus5.png")]),
                ObstacleType("cactus_6", "cactus", 100, 100, 120, Colors.CACTUS_GREEN, 5, 3,
                             [os.path.join("cactus", "cactus6.png")]),
                # Bird : y_offset plus négatif pour être plus haut
                ObstacleType("bird", "bird", 84, 62, 300, Colors.BIRD_BROWN, -80, 1,
                             [os.path.join("flying", "Ptero1.png"), os.path.join("flying", "Ptero2.png")]),
            ]

    def get_random_type(self) -> ObstacleType:
        weights = [t.spawn_weight for t in self.types]
        return random.choices(self.types, weights=weights)[0]

    def get_type_by_name(self, name: str) -> ObstacleType:
        for t in self.types:
            if t.name == name:
                return t
        raise ValueError(f"Type d'obstacle inconnu: {name}")

    def add_type(self, obstacle_type: ObstacleType):
        self.types.append(obstacle_type)

    def __repr__(self) -> str:
        return f"ObstacleConfig({len(self.types)} types disponibles)"

obstacle_config = ObstacleConfig()