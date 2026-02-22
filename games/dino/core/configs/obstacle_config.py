"""
Configuration des obstacles
"""
from dataclasses import dataclass, field
from typing import List
import random
from core.utilities.colors import Colors


@dataclass
class ObstacleType:
    """Définition d'un type d'obstacle"""
    name: str
    width: int
    height: int
    points: int = 100
    color: tuple = Colors.CACTUS_GREEN  # Vert cactus
    y_offset: int = 0  # Décalage vertical (pour oiseaux volants)
    spawn_weight: int = 1  # Poids pour spawn aléatoire (plus = plus fréquent)


@dataclass
class ObstacleConfig:
    """Configuration de tous les obstacles"""
    # Définition des types d'obstacles
    types: List[ObstacleType] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.types:
            self.types = [
                ObstacleType("small_cactus", 17, 35, 100, Colors.CACTUS_GREEN, 0, 4),
                ObstacleType("medium_cactus", 25, 50, 150, Colors.CACTUS_GREEN, 0, 3),
                ObstacleType("tall_cactus", 25, 65, 200, Colors.CACTUS_GREEN, 0, 2),
                ObstacleType("double_cactus", 40, 50, 250, Colors.CACTUS_GREEN, 0, 1),
                ObstacleType("bird", 40, 25, 300, Colors.BIRD_BROWN, -50, 1),
            ]
    
    def get_random_type(self) -> ObstacleType:
        """Retourne un type d'obstacle aléatoire (pondéré)"""
        weights = [t.spawn_weight for t in self.types]
        return random.choices(self.types, weights=weights)[0]
    
    def get_type_by_name(self, name: str) -> ObstacleType:
        """Retourne un type par son nom"""
        for t in self.types:
            if t.name == name:
                return t
        raise ValueError(f"Type d'obstacle inconnu: {name}")
    
    def add_type(self, obstacle_type: ObstacleType):
        """Ajoute un nouveau type d'obstacle"""
        self.types.append(obstacle_type)
    
    def __repr__(self) -> str:
        return f"ObstacleConfig({len(self.types)} types disponibles)"


# Instance unique
obstacle_config = ObstacleConfig()