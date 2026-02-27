# games/snake/core/managers/score_manager.py

from ..configs import scoring_config
from core.config.managers.high_score_manager import HighScoreManager

class ScoreManager:
    def __init__(self):
        self.current_score = 0
        self.high_score_manager = HighScoreManager()
        self.game_id = "snake"
        self.high_score = self.high_score_manager.get_high_score(self.game_id)
        self.points_per_food = scoring_config.points_per_food

    def add_food_score(self):
        self.current_score += self.points_per_food
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.high_score_manager.set_high_score(self.game_id, self.high_score)

    def reset(self):
        self.current_score = 0

    def get_formatted_score(self) -> str:
        return f"{self.current_score:0{scoring_config.score_digits}d}"

    def get_formatted_high_score(self) -> str:
        return f"{self.high_score:0{scoring_config.score_digits}d}"