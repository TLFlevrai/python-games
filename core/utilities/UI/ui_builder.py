from core.utilities.UI.create_buton import Button
from core.utilities.UI.create_label import Label

class UIBuilder:

    def __init__(self, layout, zone):

        self.layout = layout
        self.zone = zone

        self.elements = []

    # ---------- ADD ----------

    def add_button(self, text):

        button = Button(text, (0,0))  # position temporaire
        self.elements.append(button)

        self.refresh_layout()

        return button

    def add_label(self, text):

        label = Label(text, (0,0))
        self.elements.append(label)

        self.refresh_layout()

        return label

    # ---------- REMOVE ----------

    def remove(self, element):

        if element in self.elements:
            self.elements.remove(element)
            self.refresh_layout()

    # ---------- LAYOUT UPDATE ----------

    def refresh_layout(self):

        positions = self.layout.compute_positions(
            len(self.elements),
            self.zone
        )

        for element, pos in zip(self.elements, positions):
            element.set_position(pos)

    # ---------- DRAW ----------

    def draw(self, surface):

        for element in self.elements:
            element.draw(surface)