"""
Configuration du système de score
"""
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class ScoringConfig:
    """Paramètres de scoring"""
    
    # Score de base
    base_score_increment: int = 1  # Points par frame
    
    # Multiplicateurs
    combo_multiplier: float = 1.0  # Pour plus tard
    distance_multiplier: float = 1.0  # Score basé sur distance
    
    # Bonus
    obstacle_pass_bonus: int = 50  # Points pour avoir passé un obstacle
    perfect_timing_bonus: int = 100  # Pour plus tard
    
    # High score
    high_score_file: str = "dino_highscore.txt"
    
    # Formatage
    score_digits: int = 5  # Nombre de chiffres (ex: 00042)
    
    # Seuils de difficulté (pour info)
    difficulty_thresholds: Dict[str, int] = None
    
    def __post_init__(self):
        if self.difficulty_thresholds is None:
            self.difficulty_thresholds = {
                "easy": 0,
                "medium": 500,
                "hard": 1500,
                "expert": 3000
            }
    
    def get_formatted_score(self, score: int) -> str:
        """Formate le score avec des zéros"""
        return f"{score:0{self.score_digits}d}"
    
    def get_difficulty_level(self, score: int) -> str:
        """Retourne le niveau de difficulté basé sur le score"""
        for level, threshold in sorted(
            self.difficulty_thresholds.items(), 
            key=lambda x: x[1], 
            reverse=True
        ):
            if score >= threshold:
                return level
        return "easy"
    
    def __repr__(self) -> str:
        return f"ScoringConfig(increment={self.base_score_increment})"


# Instance unique
scoring_config = ScoringConfig()