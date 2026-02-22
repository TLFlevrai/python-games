# core/ui/styles.py
from dataclasses import dataclass
from core.utilities.colors import Colors

@dataclass
class ButtonStyle:
    """Style pour les boutons simples."""
    DEFAULT_SIZE = (200, 50)
    BORDER_RADIUS = 10
    BORDER_WIDTH = 2
    FONT_SIZE = 48
    FONT_NAME = None
    BG_COLOR = Colors.BUTTON_BG
    HOVER_COLOR = Colors.BUTTON_HOVER
    PRESSED_COLOR = Colors.BUTTON_PRESSED
    TEXT_COLOR = Colors.BUTTON_TEXT
    BORDER_COLOR = Colors.BUTTON_BORDER

@dataclass
class CycleButtonStyle:
    """Style pour le bouton cyclique."""
    ARROW_SIZE = 36
    VALUE_PADDING_X = 20
    VALUE_PADDING_Y = 8
    SPACING = 8
    FONT_BTN_SIZE = 32
    FONT_VALUE_SIZE = 20
    FONT_VALUE_NAME = "Courier New"
    BG_COLOR = Colors.BUTTON_BG
    HOVER_COLOR = Colors.BUTTON_HOVER
    BORDER_COLOR = Colors.BUTTON_BORDER
    VALUE_BG = Colors.PANEL_BG
    VALUE_BORDER = Colors.PANEL_BORDER
    TEXT_COLOR = Colors.BUTTON_TEXT
    TEXT_SECONDARY = Colors.TEXT_SECONDARY

@dataclass
class GameButtonStyle:
    """Style pour les boutons de jeu avec logo."""
    WIDTH = 130
    HEIGHT = 160
    BORDER_RADIUS = 14
    LOGO_SIZE = 50
    FONT_SIZE = 16
    FONT_NAME = "Courier New"
    BG_NORMAL = Colors.GAME_BUTTON_BG_NORMAL
    BG_HOVER = Colors.GAME_BUTTON_BG_HOVER
    BG_PRESSED = Colors.GAME_BUTTON_BG_PRESSED
    BORDER_NORMAL = Colors.GAME_BUTTON_BORDER_NORMAL
    BORDER_HOVER = Colors.GAME_BUTTON_BORDER_HOVER
    BORDER_PRESSED = Colors.GAME_BUTTON_BORDER_PRESSED
    TEXT_NORMAL = Colors.GAME_BUTTON_TEXT_NORMAL
    TEXT_HOVER = Colors.GAME_BUTTON_TEXT_HOVER
    FALLBACK_COLOR = Colors.GAME_BUTTON_FALLBACK

@dataclass
class LabelStyle:
    """Style pour les labels simples."""
    DEFAULT_FONT_SIZE = 36
    FONT_NAME = None
    DEFAULT_COLOR = Colors.WHITE

@dataclass
class SubtitleStyle:
    """Style pour les sous-titres."""
    FONT_SIZE = 28
    ITALIC = True
    COLOR = Colors.GRAY
    MIN_ALPHA = 150
    MAX_ALPHA = 255
    FADE_SPEED = 2

@dataclass
class VersionStyle:
    """Style pour les labels de version."""
    FONT_SIZE = 24
    COLOR = Colors.GRAY