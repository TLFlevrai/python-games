import pygame
from .core.entities.dino import Dino
from .core.entities.ground import Ground
from .core.managers.obstacle_manager import ObstacleManager
from .core.managers.score_manager import ScoreManager          # ← Ajout
from .core.interfaces.pause_interface import PauseInterface
from .core.interfaces.game_over_interface import GameOverInterface
from .core.configs import game_config                          # ← Ajout


class DinoGame:
    def __init__(self, screen, input_manager):
        self.surface = screen
        self.input = input_manager

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # Création du sol
        self.ground = Ground(self.screen_height)

        # ---------- STATE MACHINE ----------
        self.state = "playing"  # playing / paused / game_over

        # ---------- DINO ----------
        self.dino = Dino(self.ground.get_y())

        # ---------- OBSTACLES ----------
        self.obstacle_manager = ObstacleManager(self.screen_width, self.ground.get_y())

        # ---------- SCORE (via ScoreManager) ----------
        self.score_manager = ScoreManager()

        # ---------- INTERFACES ----------
        self.pause_interface = PauseInterface(self.surface, self.input)
        self.game_over_interface = GameOverInterface(self.surface, self.input)

        # ---------- VISUALS ----------
        self.font_score = pygame.font.SysFont("Courier New", 20)

    # RESET
    def reset(self):
        """Réinitialise le jeu"""
        self.state = "playing"
        self.dino.reset(self.ground.get_y())
        self.obstacle_manager.reset()
        self.score_manager.reset()          # ← Important
        print("🔄 Dino Runner reset")

    # UPDATE
    def update(self):
        # ---------- PLAYING ----------
        if self.state == "playing":
            # Input saut
            if self.input.space_pressed() or self.input.click():
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

            # Score temporel
            self.score_manager.increase_time_score()   # ← Nouveau

            # Bonus pour obstacles passés (optionnel, à implémenter plus tard)
            # for obstacle in self.obstacle_manager.obstacles:
            #     if obstacle.get_rect().right < self.dino.get_rect().left:
            #         self.score_manager.register_obstacle_pass(id(obstacle))

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
            # Passage du score courant ET du high score
            result = self.game_over_interface.update(
                self.score_manager.current_score,
                self.score_manager.high_score
            )
            if result == "RESTART":
                self.reset()
            elif result == "MENU":
                return "MENU"

    # ==================================================
    # DRAW
    # ==================================================

    def draw(self, surface):
        # ---------- SOL (avec game_config) ----------
        self.ground.draw(surface)

        # ---------- JEU ----------
        self.dino.draw(surface)
        self.obstacle_manager.draw(surface)

        # ---------- SCORE ----------
        if self.state == "playing":
            self._draw_scores(surface)

        # ---------- OVERLAYS ----------
        if self.state == "paused":
            self.pause_interface.draw(surface)
        elif self.state == "game_over":
            self.game_over_interface.draw(
                surface,
                self.score_manager.current_score,
                self.score_manager.high_score
            )

    # HELPERS
    def _draw_scores(self, surface):
        """Affiche le score courant et le high score"""
        # Score courant formaté
        score_text = self.font_score.render(
            f"Score: {self.score_manager.get_formatted_score()}",
            True, game_config.ground_color
        )
        surface.blit(score_text, (self.screen_width - 200, 30))

        # High score
        high_score_text = self.font_score.render(
            f"HI: {self.score_manager.get_formatted_high_score()}",
            True, (100, 100, 100)
        )
        surface.blit(high_score_text, (self.screen_width - 200, 55))

        # Indicateur de nouveau record
        if (self.score_manager.current_score >= self.score_manager.high_score
                and self.score_manager.current_score > 0):
            record_font = pygame.font.SysFont("Courier New", 16)
            record_text = record_font.render("NEW RECORD!", True, (255, 200, 50))
            surface.blit(record_text, (self.screen_width - 200, 75))