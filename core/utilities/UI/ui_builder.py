from core.utilities.UI.create_buton import Button
from core.utilities.UI.create_label import Label

class UIBuilder:

    def __init__(self, layout, zone, input_manager):

        self.layout = layout
        self.zone = zone
        self.input = input_manager

        self.elements = []

    # ---------- ADD ----------

    def add_button(self, text, size=(200, 50)):
        button = Button(text, (0, 0), self.input, size=size)
        self.elements.append(button)

        self.refresh_layout()

        return button

    def add_label(self, text, font_size=36, color=(255, 255, 255)):
        label = Label(text, (0, 0), font_size=font_size, color=color)
        self.elements.append(label)

        self.refresh_layout()

        return label
    
    def add_version(self, text, font_size=36, color=(255, 255, 255)):
        Label = Label(text, (0, 0))

    # ---------- REMOVE ----------

    def remove(self, element):
        """Retire un élément et met à jour le layout"""
        if element in self.elements:
            self.elements.remove(element)
            self.refresh_layout()

    def clear(self):
        """Retire tous les éléments"""
        self.elements.clear()

    # ---------- LAYOUT UPDATE ----------

    def refresh_layout(self):
        """Recalcule et applique les positions de tous les éléments"""
        positions = self.layout.compute_positions(
            len(self.elements),
            self.zone
        )

        for element, pos in zip(self.elements, positions):
            element.set_position(pos)

    # ---------- UPDATE ----------

    def update(self):
        for element in self.elements:

            if hasattr(element, 'update'):
                result = element.update()

                if result:  # Si l'élément a été cliqué
                    return element
        return None

    # ---------- DRAW ----------

    def draw(self, surface):
        """Dessine tous les éléments"""
        for element in self.elements:
            element.draw(surface)

    # ---------- UTILITY ----------

    def get_button_by_text(self, text):
        """Trouve un bouton par son texte"""
        for element in self.elements:
            if isinstance(element, Button) and element.text == text:
                return element
        return None

    def get_label_by_text(self, text):
        """Trouve un label par son texte"""
        for element in self.elements:
            if isinstance(element, Label) and element.text == text:
                return element
        return None