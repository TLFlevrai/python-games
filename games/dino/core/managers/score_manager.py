# games/dino/core/managers/score_manager.py

from ..configs import scoring_config
from core.config.managers.high_score_manager import HighScoreManager

class ScoreManager:
    """Gestionnaire de score et high score pour Dino Runner"""

    def __init__(self):
        self.current_score = 0
        self.high_score_manager = HighScoreManager()
        self.game_id = "dino"
        self.high_score = self.high_score_manager.get_high_score(self.game_id)
        self.increment = scoring_config.base_score_increment
        self.combo = 0
        self.last_obstacle_passed = None

    # ------------------------------------------------------------------
    # Gestion du score courant
    # ------------------------------------------------------------------

    def increase_time_score(self):
        """Incrément automatique basé sur le temps (appelé chaque frame)"""
        self.current_score += self.increment
        self._check_high_score()

    def add_bonus(self, bonus_type: str):
        """Ajoute un bonus selon le type défini dans scoring_config"""
        if bonus_type == "obstacle_pass":
            self.current_score += scoring_config.obstacle_pass_bonus
        elif bonus_type == "perfect_timing":
            self.current_score += scoring_config.perfect_timing_bonus
        self._check_high_score()

    def _check_high_score(self):
        """Vérifie si le high score est battu et met à jour via le gestionnaire central"""
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.high_score_manager.set_high_score(self.game_id, self.high_score)

    def reset(self):
        """Réinitialise le score courant (mais pas le high score)"""
        self.current_score = 0
        self.combo = 0
        self.last_obstacle_passed = None

    # ------------------------------------------------------------------
    # Formatage pour affichage
    # ------------------------------------------------------------------

    def get_formatted_score(self) -> str:
        return f"{self.current_score:0{scoring_config.score_digits}d}"

    def get_formatted_high_score(self) -> str:
        return f"{self.high_score:0{scoring_config.score_digits}d}"

    # ------------------------------------------------------------------
    # Gestion des obstacles passés (bonus)
    # ------------------------------------------------------------------

    def register_obstacle_pass(self, obstacle_id):
        """
        Enregistre le passage d'un obstacle pour éviter de compter deux fois
        le même obstacle et donner le bonus.
        """
        if obstacle_id != self.last_obstacle_passed:
            self.add_bonus("obstacle_pass")
            self.last_obstacle_passed = obstacle_id
            self.combo += 1  # Pour futur combo