from dataclasses import dataclass

@dataclass
class ScoringConfig:
    points_per_food: int = 10
    score_digits: int = 5  # pour formatage
    high_score_file: str = "snake_highscore.txt"

scoring_config = ScoringConfig()