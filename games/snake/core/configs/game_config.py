from dataclasses import dataclass
from core.utilities.colors import Colors

@dataclass
class GameConfig:
    # Dimensions de la grille (en nombre de cases)
    grid_width: int = 20
    grid_height: int = 15
    cell_size: int = 30  # taille d'une case en pixels

    # Vitesse initiale (en frames par déplacement)
    initial_speed: int = 10  # plus petit = plus rapide
    speed_increment: int = 1  # réduction de l'intervalle par palier
    min_speed: int = 5  # vitesse maximale (intervalle minimum)

    # Couleurs
    background_color: tuple = Colors.BLACK
    grid_line_color: tuple = Colors.DARK_GRAY
    snake_head_color: tuple = Colors.GREEN
    snake_body_color: tuple = (0, 200, 0)
    food_color: tuple = Colors.RED

    # Fichier high score
    high_score_file: str = "snake_highscore.txt"

    # Position du score
    score_x_offset: int = 200
    score_y: int = 30

game_config = GameConfig()