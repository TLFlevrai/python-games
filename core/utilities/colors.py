# core/utilities/colors.py
from typing import Tuple
import random

Color = Tuple[int, int, int]


class Colors:
    """Palette de couleurs centralisée pour toute l'application."""

    # ===== COULEURS DE BASE =====
    WHITE: Color = (255, 255, 255)
    BLACK: Color = (0, 0, 0)
    RED: Color = (255, 0, 0)
    GREEN: Color = (0, 255, 0)
    BLUE: Color = (0, 0, 255)
    YELLOW: Color = (255, 255, 0)
    CYAN: Color = (0, 255, 255)
    MAGENTA: Color = (255, 0, 255)
    GRAY: Color = (128, 128, 128)
    DARK_GRAY: Color = (64, 64, 64)
    LIGHT_GRAY: Color = (192, 192, 192)

    # ===== COULEURS SPÉCIFIQUES AU JEU =====
    # Interface générale
    BACKGROUND: Color = (30, 30, 30)
    TEXT_PRIMARY: Color = (255, 255, 255)
    TEXT_SECONDARY: Color = (150, 150, 150)

    # Boutons standard (Windows 11 style)
    BUTTON_BG: Color = (45, 45, 48)
    BUTTON_HOVER: Color = (60, 60, 65)
    BUTTON_PRESSED: Color = (35, 35, 38)
    BUTTON_TEXT: Color = (240, 240, 240)
    BUTTON_BORDER: Color = (70, 70, 75)

    # Couleurs d'accent (pour différents jeux ou actions)
    ACCENT_BLUE: Color = (0, 120, 215)
    ACCENT_BLUE_HOVER: Color = (16, 137, 232)
    ACCENT_GREEN: Color = (16, 124, 16)
    ACCENT_GREEN_HOVER: Color = (24, 140, 24)
    ACCENT_RED: Color = (196, 43, 28)
    ACCENT_RED_HOVER: Color = (232, 50, 33)
    ACCENT_PURPLE: Color = (135, 100, 184)
    ACCENT_PURPLE_HOVER: Color = (150, 115, 199)

    # ===== COULEURS POUR ÉLÉMENTS UI SPÉCIFIQUES =====
    # Panneaux et fonds
    PANEL_BG: Color = (20, 20, 22)          # Fond de panneau (ex: valeur cycle)
    PANEL_BORDER: Color = (70, 70, 75)      # Bordure de panneau

    # Boutons de jeu (GameButton)
    GAME_BUTTON_BG_NORMAL: Color = (35, 35, 38)
    GAME_BUTTON_BG_HOVER: Color = (55, 55, 60)
    GAME_BUTTON_BG_PRESSED: Color = (25, 25, 28)
    GAME_BUTTON_BORDER_NORMAL: Color = (60, 60, 65)
    GAME_BUTTON_BORDER_HOVER: Color = (100, 100, 110)
    GAME_BUTTON_BORDER_PRESSED: Color = (80, 80, 85)
    GAME_BUTTON_TEXT_NORMAL: Color = (160, 160, 165)
    GAME_BUTTON_TEXT_HOVER: Color = (220, 220, 220)
    GAME_BUTTON_FALLBACK: Color = (70, 70, 75)

    # ===== COULEURS SPÉCIFIQUES AUX JEUX =====
    # Dino
    DINO_BODY: Color = (80, 80, 85)
    DINO_DEBUG: Color = RED

    # Obstacles
    CACTUS_GREEN: Color = (83, 124, 66)
    BIRD_BROWN: Color = (150, 75, 0)
    ROCK_GRAY: Color = (100, 100, 100)

    # Pong
    PONG_PADDLE: Color = (255, 255, 255)
    PONG_BALL: Color = (255, 255, 255)

    # Flappy Bird
    FLAPPY_BIRD: Color = (255, 255, 0)
    PIPE_GREEN: Color = (0, 150, 0)

    # Tic Tac Toe
    TIC_TAC_TOE_X: Color = (255, 100, 100)
    TIC_TAC_TOE_O: Color = (100, 100, 255)

    # ===== MÉTHODES UTILITAIRES =====

    @staticmethod
    def lighten(color: Color, amount: int = 30) -> Color:
        return tuple(min(255, c + amount) for c in color)

    @staticmethod
    def darken(color: Color, amount: int = 30) -> Color:
        return tuple(max(0, c - amount) for c in color)

    @staticmethod
    def blend(color1: Color, color2: Color, ratio: float = 0.5) -> Color:
        return tuple(int(c1 * (1 - ratio) + c2 * ratio) for c1, c2 in zip(color1, color2))

    @staticmethod
    def random() -> Color:
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    @staticmethod
    def from_hex(hex_code: str) -> Color:
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def to_hex(color: Color) -> str:
        return '#{:02x}{:02x}{:02x}'.format(*color)


# ===== CONSTANTES DE THÈME (optionnel) =====
class DarkTheme:
    BACKGROUND = Colors.BACKGROUND
    TEXT = Colors.TEXT_PRIMARY
    BUTTON = Colors.BUTTON_BG
    BUTTON_HOVER = Colors.BUTTON_HOVER


class LightTheme:
    BACKGROUND = (240, 240, 240)
    TEXT = Colors.BLACK
    BUTTON = (200, 200, 200)
    BUTTON_HOVER = (180, 180, 180)