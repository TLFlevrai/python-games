import pygame

class Board:
    """
    Grille de Tic Tac Toe 3x3 avec style moderne.
    Bords arrondis, hover effects, détection de victoire.
    """

    def __init__(self, screen_width, screen_height, input_manager):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.input = input_manager

        # ---------- DIMENSIONS ----------
        self.board_size = min(screen_width, screen_height) - 200  # Marge de 100px de chaque côté
        self.cell_size = self.board_size // 3
        self.cell_padding = 8  # Espace entre les cases

        # Position centrée
        self.board_x = (screen_width - self.board_size) // 2
        self.board_y = (screen_height - self.board_size) // 2

        # ---------- GRILLE 3x3 ----------
        self.grid = [[None for _ in range(3)] for _ in range(3)]  # None, "X", ou "O"

        # ---------- STYLE ----------
        self.border_radius = 12
        self.font_symbol = pygame.font.SysFont("Courier New", 80, bold=True)

        # Couleurs
        self.bg_cell = (35, 35, 38)
        self.bg_hover = (55, 55, 60)
        self.border_color = (60, 60, 65)

        self.color_x = (50, 120, 215)   # Bleu
        self.color_o = (215, 60, 50)    # Rouge

        # ---------- RECTS DES CASES ----------
        self.cell_rects = []
        for row in range(3):
            row_rects = []
            for col in range(3):
                x = self.board_x + col * self.cell_size + self.cell_padding
                y = self.board_y + row * self.cell_size + self.cell_padding
                w = self.cell_size - self.cell_padding * 2
                h = self.cell_size - self.cell_padding * 2
                rect = pygame.Rect(x, y, w, h)
                row_rects.append(rect)
            self.cell_rects.append(row_rects)

    # ---------- RESET ----------

    def reset(self):
        """Réinitialise la grille"""
        self.grid = [[None for _ in range(3)] for _ in range(3)]

    # ---------- CLICK ----------

    def click(self, player):
        """
        Gère le clic sur une case.
        
        Args:
            player (str): "X" ou "O"
        
        Returns:
            bool: True si un coup a été joué
        """
        if not self.input.click():
            return False

        mouse_pos = self.input.get_mouse_pos()

        for row in range(3):
            for col in range(3):
                rect = self.cell_rects[row][col]
                if rect.collidepoint(mouse_pos):
                    # Case vide ?
                    if self.grid[row][col] is None:
                        self.grid[row][col] = player
                        return True

        return False

    # ---------- VICTOIRE ----------

    def check_winner(self):
        """
        Vérifie s'il y a un gagnant.
        
        Returns:
            str: "X", "O", ou None
        """
        # Lignes
        for row in range(3):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] and self.grid[row][0] is not None:
                return self.grid[row][0]

        # Colonnes
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] is not None:
                return self.grid[0][col]

        # Diagonales
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
            return self.grid[0][0]

        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
            return self.grid[0][2]

        return None

    # ---------- MATCH NUL ----------

    def is_full(self):
        """Vérifie si la grille est pleine (match nul)"""
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] is None:
                    return False
        return True

    # ---------- DRAW ----------

    def draw(self, surface):
        """Affiche la grille"""

        mouse_pos = self.input.get_mouse_pos()

        for row in range(3):
            for col in range(3):

                rect = self.cell_rects[row][col]
                value = self.grid[row][col]

                # ---------- FOND DE LA CASE ----------
                is_hovered = rect.collidepoint(mouse_pos) and value is None
                bg = self.bg_hover if is_hovered else self.bg_cell

                pygame.draw.rect(surface, bg, rect, border_radius=self.border_radius)
                pygame.draw.rect(surface, self.border_color, rect, width=1, border_radius=self.border_radius)

                # ---------- SYMBOLE X ou O ----------
                if value:
                    color = self.color_x if value == "X" else self.color_o
                    text = self.font_symbol.render(value, True, color)
                    text_rect = text.get_rect(center=rect.center)
                    surface.blit(text, text_rect)