from .layout import Layout, Zone
from .builder import UIBuilder
from .elements import Button, CycleButton, GameButton, Label, SubtitleLabel, VersionLabel
from .managers import SubtitleManager   # ← ajout

__all__ = [
    'Layout', 'Zone',
    'UIBuilder',
    'Button', 'CycleButton', 'GameButton',
    'Label', 'SubtitleLabel', 'VersionLabel',
    'SubtitleManager',                   # ← ajout
]