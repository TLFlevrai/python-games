import pygame
from games.flappy_bird.flappy_bird_core.flappy_bird_config import FlappyBirdConfig

class Score:

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        # ---------- SCORE ----------
        self.score = 0
        self.high_score = 0

        # ---------- VISUAL ----------
        self.font = pygame.font.SysFont(None, FlappyBirdConfig.SCORE_FONT_SIZE)
        self.color = FlappyBirdConfig.SCORE_COLOR

        # Position (centré en haut)
        self.x = screen_width // 2
        self.y = FlappyBirdConfig.SCORE_Y_POSITION

    # ---------- UPDATE ----------

    def add_point(self):
        """Ajoute 1 point au score"""
        self.score += 1

        # Mise à jour du meilleur score
        if self.score > self.high_score:
            self.high_score = self.score

    def get_score(self):
        """Retourne le score actuel"""
        return self.score

    def get_high_score(self):
        """Retourne le meilleur score"""
        return self.high_score

    # ---------- DRAW ----------

    def draw(self, surface):
        """Affiche le score à l'écran"""

        # Rendu du texte
        score_text = self.font.render(str(self.score), True, self.color)

        # Centrer le texte
        text_rect = score_text.get_rect(center=(self.x, self.y))

        # Affichage
        surface.blit(score_text, text_rect)

    # ---------- RESET ----------

    def reset(self):
        """Remet le score à 0"""
        self.score = 0