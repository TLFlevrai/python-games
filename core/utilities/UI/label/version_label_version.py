import pygame
from core.utilities.UI.label.create_label import Label
from core.utilities.colors import Colors

class VersionLabel(Label):

    def __init__(self, text, position):

        super().__init__(
            text,
            position,
            font_size=24,        # taille fixe
            color=Colors.GRAY,   # couleur version
            center=True
        )
