import pygame

from games.tic_tac_toe.tic_tac_toe_core.board import Board
from games.tic_tac_toe.tic_tac_toe_interface.game_over_interface import GameOverInterface

class TicTacToeGame:
    """
    Jeu de Tic Tac Toe pour 2 joueurs.
    Alternance X (bleu) et O (rouge).
    """

    def __init__(self, screen, input_manager):

        self.surface = screen
        self.input = input_manager

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # ---------- STATE ----------
        self.state = "playing"  # playing / game_over

        # ---------- JOUEURS ----------
        self.current_player = "X"  # X commence toujours
        self.winner = None

        # ---------- BOARD ----------
        self.board = Board(self.screen_width, self.screen_height, self.input)

        # ---------- INTERFACE ----------
        self.game_over_interface = GameOverInterface(self.surface, self.input)

        # ---------- FONTS ----------
        self.font_turn = pygame.font.SysFont("Courier New", 28)

    # ==================================================
    # RESET
    # ==================================================

    def reset(self):
        """Réinitialise le jeu"""

        self.state = "playing"
        self.current_player = "X"
        self.winner = None
        self.board.reset()

        print("🔄 Tic Tac Toe reset")

    # ==================================================
    # UPDATE
    # ==================================================

    def update(self):

        # ---------- PLAYING ----------
        if self.state == "playing":

            # Joueur clique sur une case
            if self.board.click(self.current_player):

                # Vérifier victoire
                winner = self.board.check_winner()
                if winner:
                    self.state = "game_over"
                    self.winner = winner
                    return

                # Vérifier match nul
                if self.board.is_full():
                    self.state = "game_over"
                    self.winner = "DRAW"
                    return

                # Changer de joueur
                self.current_player = "O" if self.current_player == "X" else "X"

        # ---------- GAME OVER ----------
        elif self.state == "game_over":

            result = self.game_over_interface.update(self.winner)

            if result == "RESTART":
                self.reset()

            elif result == "MENU":
                return "MENU"

    # ==================================================
    # DRAW
    # ==================================================

    def draw(self, surface):

        # ---------- GRILLE ----------
        self.board.draw(surface)

        # ---------- INDICATEUR DE TOUR ----------
        if self.state == "playing":
            self._draw_turn_indicator(surface)

        # ---------- GAME OVER OVERLAY ----------
        elif self.state == "game_over":
            self.game_over_interface.draw(surface, self.winner)

    # ==================================================
    # HELPERS
    # ==================================================

    def _draw_turn_indicator(self, surface):
        """Affiche quel joueur doit jouer"""

        color_x = (50, 120, 215)
        color_o = (215, 60, 50)

        player_color = color_x if self.current_player == "X" else color_o
        text = f"Player {self.current_player} turn"

        label = self.font_turn.render(text, True, player_color)
        rect = label.get_rect(center=(self.screen_width // 2, 60))

        surface.blit(label, rect)