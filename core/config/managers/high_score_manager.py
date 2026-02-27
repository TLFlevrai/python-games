# core/config/managers/high_score_manager.py

import json
import os

class HighScoreManager:
    _instance = None
    # Chemin vers core/config/score/highscores.json
    _file_path = os.path.join(os.path.dirname(__file__), '..', 'score', 'highscores.json')
    _file_path = os.path.abspath(_file_path)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self):
        # Crée le dossier si nécessaire
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        if os.path.exists(self._file_path):
            try:
                with open(self._file_path, 'r') as f:
                    self._data = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._data = {}
        else:
            self._data = {}

    def _save(self):
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        try:
            with open(self._file_path, 'w') as f:
                json.dump(self._data, f, indent=4)
        except IOError as e:
            print(f"⚠️ Erreur sauvegarde high scores: {e}")

    def get_high_score(self, game_key: str, default=0) -> int:
        return self._data.get(game_key, default)

    def set_high_score(self, game_key: str, score: int):
        if score > self.get_high_score(game_key):
            self._data[game_key] = score
            self._save()
            return True
        return False

    def reset_high_score(self, game_key: str):
        if game_key in self._data:
            del self._data[game_key]
            self._save()