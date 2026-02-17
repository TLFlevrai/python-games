"""
Configuration centralisée pour Flappy Bird
Extrait les constantes hardcodées du code existant
"""

class FlappyBirdConfig:
    """Configuration du jeu Flappy Bird"""

    # ==================== BIRD ====================
    
    # Dimensions
    BIRD_WIDTH = 40
    BIRD_HEIGHT = 30
    
    # Physique
    BIRD_GRAVITY = 0.5
    BIRD_JUMP_STRENGTH = -8
    
    # Visuel (rotation)
    BIRD_ROTATION_UP = -25
    
    
    # ==================== PIPES ====================
    
    # Dimensions
    PIPE_WIDTH = 60
    PIPE_GAP_SIZE = 160
    
    # Marges
    PIPE_MARGIN = 80  # Marge haut et bas
    
    # Gameplay
    PIPE_SPEED = 3
    PIPE_SPAWN_INTERVAL = 90  # frames
    
    
    # ==================== SCORE ====================
    
    # Affichage
    SCORE_FONT_SIZE = 72
    SCORE_COLOR = (255, 255, 255)
    SCORE_Y_POSITION = 80