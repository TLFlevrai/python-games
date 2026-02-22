"""
Core package pour Dino Runner
Exporte les classes principales
"""
from .entities import Dino, Obstacle
from .managers import ObstacleManager
from .configs import dino_config, obstacle_config, game_config, scoring_config

__all__ = [
    'Dino',
    'Obstacle',
    'ObstacleManager',
    'dino_config',
    'obstacle_config',
    'game_config',
    'scoring_config',
]