# core/ui/elements/version_label.py
from ..styles import VersionStyle
from .label import Label

class VersionLabel(Label):
    def __init__(self, text, position):
        super().__init__(text, position, font_size=VersionStyle.FONT_SIZE,
                         color=VersionStyle.COLOR, center=True)