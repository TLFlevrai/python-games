# games/dino/core/__init__.py

"""
Core package pour Dino Runner
Exporte les classes principales
"""

from .entities import Dino, Ground, Cloud, Obstacle, Cactus, Bird
from .managers import ObstacleManager, ScoreManager, SoundManager
from .interfaces import PauseInterface, GameOverInterface
from .configs import dino_config, obstacle_config, game_config, scoring_config

__all__ = [
    'Dino',
    'Ground',
    'Cloud',
    'Obstacle',
    'Cactus',
    'Bird',
    'ObstacleManager',
    'ScoreManager',
    'SoundManager',
    'PauseInterface',
    'GameOverInterface',
    'dino_config',
    'obstacle_config',
    'game_config',
    'scoring_config',
]