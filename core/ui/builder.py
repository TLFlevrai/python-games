from core.ui.layout import Layout, Zone
from core.ui.elements import Button, Label, SubtitleLabel, VersionLabel, CycleButton, GameButton
from core.utilities.input.input_manager import InputManager

class UIBuilder:

    def __init__(self, layout, zone, input_manager):

        self.layout = layout
        self.zone = zone
        self.input = input_manager

        self.elements = []

    # ---------- ADD ----------

    def add_button(self, text, size=(200, 50), color=None):
        button = Button(text, (0, 0), self.input, size=size, color=color)
        self.elements.append(button)
        self.refresh_layout()
        return button

    def add_label(self, text, font_size=36, color=(255, 255, 255)):
        label = Label(text, (0, 0), font_size=font_size, color=color)
        self.elements.append(label)
        self.refresh_layout()
        return label

    def add_subtitle(self, text):
        subtitle = SubtitleLabel(text, (0, 0))
        self.elements.append(subtitle)
        self.refresh_layout()
        return subtitle

    def add_version(self, text):
        version = VersionLabel(text, (0, 0))
        self.elements.append(version)
        self.refresh_layout()
        return version

    def add_cycle_button(self, options):  # ← NOUVEAU
        """Ajoute un bouton défilant avec plusieurs options"""
        cycle = CycleButton(options, (0, 0), self.input)
        self.elements.append(cycle)
        self.refresh_layout()
        return cycle
    
    def add_game_button(self, text, logo_path):  # ← NOUVEAU
        """Ajoute un bouton de jeu avec logo"""
        btn = GameButton(text, logo_path, (0, 0), self.input)
        self.elements.append(btn)
        self.refresh_layout()
        return btn

    # ---------- REMOVE ----------

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
            self.refresh_layout()

    def clear(self):
        self.elements.clear()

    # ---------- LAYOUT UPDATE ----------

    def refresh_layout(self):
        positions = self.layout.compute_positions(
            len(self.elements),
            self.zone,
            elements=self.elements
        )
        for element, pos in zip(self.elements, positions):
            element.set_position(pos)

    # ---------- UPDATE ----------

    def update(self):
        for element in self.elements:
            if hasattr(element, 'update'):
                result = element.update()
                if result:
                    return element
        return None

    # ---------- DRAW ----------

    def draw(self, surface):
        for element in self.elements:
            element.draw(surface)

    # ---------- UTILITY ----------

    def get_button_by_text(self, text):
        for element in self.elements:
            if isinstance(element, Button) and element.text == text:
                return element
        return None

    def get_label_by_text(self, text):
        for element in self.elements:
            if isinstance(element, Label) and element.text == text:
                return element
        return None