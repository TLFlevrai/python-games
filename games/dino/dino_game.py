import pygame

from games.dino.dino_core.dino import Dino
from games.dino.dino_core.obstacle_manager import ObstacleManager
from games.dino.dino_interface.pause_interface import PauseInterface
from games.dino.dino_interface.game_over_interface import GameOverInterface

class DinoRunnerGame:
    """
    Jeu Dino Runner - Évite les obstacles en sautant.
    Score basé sur le temps de survie.
    """

    def __init__(self, screen, input_manager):

        self.surface = screen
        self.input = input_manager

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # ---------- STATE MACHINE ----------
        self.state = "playing"  # playing / paused / game_over

        # ---------- DINO ----------
        self.dino = Dino(self.screen_height - 80)

        # ---------- OBSTACLES ----------
        self.obstacle_manager = ObstacleManager(self.screen_width, self.screen_height)

        # ---------- SCORE ----------
        self.score = 0
        self.score_increment = 1  # Points par frame

        # ---------- INTERFACES ----------
        self.pause_interface = PauseInterface(self.surface, self.input)
        self.game_over_interface = GameOverInterface(self.surface, self.input)

        # ---------- VISUALS ----------
        self.font_score = pygame.font.SysFont("Courier New", 20)
        self.ground_y = self.screen_height - 80

    # ==================================================
    # RESET
    # ==================================================

    def reset(self):
        """Réinitialise le jeu"""

        self.state = "playing"
        self.score = 0

        self.dino.reset(self.screen_height - 80)
        self.obstacle_manager.reset()

        print("🔄 Dino Runner reset")

    # ==================================================
    # UPDATE
    # ==================================================

    def update(self):

        # ---------- PLAYING ----------
        if self.state == "playing":

            # Input saut
            if self.input.space_pressed():
                self.dino.jump()

            # Input pause
            if self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "paused"
                return

            # Mise à jour dino
            self.dino.update()

            # Mise à jour obstacles + collision
            collision = self.obstacle_manager.update(self.dino.get_rect())

            if collision:
                self.state = "game_over"
                return

            # Score augmente avec le temps
            self.score += self.score_increment

        # ---------- PAUSED ----------
        elif self.state == "paused":

            result = self.pause_interface.update()

            if result == "RESUME" or self.input.key_just_pressed(pygame.K_ESCAPE):
                self.state = "playing"

            elif result == "RESTART":
                self.reset()

            elif result == "MENU":
                return "MENU"

        # ---------- GAME OVER ----------
        elif self.state == "game_over":

            result = self.game_over_interface.update(self.score)

            if result == "RESTART":
                self.reset()

            elif result == "MENU":
                return "MENU"

    # ==================================================
    # DRAW
    # ==================================================

    def draw(self, surface):

        # ---------- SOL ----------
        self._draw_ground(surface)

        # ---------- JEU ----------
        self.dino.draw(surface)
        self.obstacle_manager.draw(surface)

        # ---------- SCORE ----------
        if self.state == "playing":
            self._draw_score(surface)

        # ---------- OVERLAYS ----------
        if self.state == "paused":
            self.pause_interface.draw(surface)

        elif self.state == "game_over":
            self.game_over_interface.draw(surface, self.score)

    # ==================================================
    # HELPERS
    # ==================================================

    def _draw_ground(self, surface):
        """Dessine la ligne de sol"""
        pygame.draw.line(
            surface,
            (83, 83, 83),  # Gris
            (0, self.ground_y),
            (self.screen_width, self.ground_y),
            3
        )

    def _draw_score(self, surface):
        """Affiche le score en haut à droite"""
        score_text = self.font_score.render(f"Score: {self.score}", True, (83, 83, 83))
        surface.blit(score_text, (self.screen_width - 150, 30))