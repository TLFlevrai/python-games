#games/dino/configs/dino_config.py

"""
Configuration spécifique au dinosaure
"""

from dataclasses import dataclass
from typing import Tuple
from core.utilities.colors import Colors

@dataclass
class DinoConfig:
    """Paramètres physiques et visuels du dino"""
    
    # Position
    x_position: int = 100  # Position fixe à gauche
    
    # Dimensions
    width: int = 40
    height: int = 50
    
    # Physique
    gravity: float = 0.8  # Accélération vers le bas
    jump_strength: int = -15  # Force initiale du saut (négatif = vers haut)
    
    # États possibles
    max_jumps: int = 1  # Pour l'instant 1, mais on pourra faire double saut plus tard
    
    # Visuel
    color: Tuple[int, int, int] = Colors.DINO_BODY  # Gris foncé
    debug_color: Tuple[int, int, int] = Colors.DINO_DEBUG  # Rouge pour hitbox debug
    
    def __post_init__(self):
        """Validation des valeurs"""
        assert self.width > 0, "La largeur du dino doit être positive"
        assert self.height > 0, "La hauteur du dino doit être positive"
        assert self.gravity > 0, "La gravité doit être positive"
        assert self.jump_strength < 0, "La force de saut doit être négative"
        assert self.max_jumps >= 1, "Le nombre de sauts doit être ≥ 1"
    
    @property
    def ground_collision_y(self) -> int:
        """Position Y où le dino touche le sol"""
        return self.height
    
    def __repr__(self) -> str:
        return f"DinoConfig(size={self.width}x{self.height}, gravity={self.gravity})"


# Instance unique pour tout le jeu
dino_config = DinoConfig()