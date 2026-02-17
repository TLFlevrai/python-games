class Layout:

    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"

    RIGHT_CORNER = "right_corner"
    LEFT_CORNER = "left_corner"

    TOP_LEFT_CORNER = "top_left_corner"   # ← NOUVEAU
    TOP_RIGHT_CORNER = "top_right_corner" # ← NOUVEAU

    HORIZONTAL_CENTER = "horizontal_center"  # ← NOUVEAU

    def __init__(self, screen_width, screen_height, spacing=20, corner_padding=20, corner_padding_y=15, horizontal_spacing=30, row_y=None):

        self.width = screen_width
        self.height = screen_height
        self.spacing = spacing
        self.corner_padding = corner_padding          # Distance horizontale depuis le bord
        self.corner_padding_y = corner_padding_y      # ← NOUVEAU : Distance verticale depuis le bas
        self.horizontal_spacing = horizontal_spacing
        self.row_y = row_y if row_y is not None else screen_height // 2

    def compute_positions(self, count, zone, elements=None):

        positions = []

        if count == 0:
            return positions
        
        # ---------- CORNERS (SPECIAL CASE) ----------

        if zone == Layout.RIGHT_CORNER:

            for i in range(count):

                # Calculer x en fonction de la largeur de l'élément
                if elements and i < len(elements):
                    element = elements[i]
                    # Obtenir la largeur réelle du texte rendu
                    if hasattr(element, 'rect'):
                        element_width = element.rect.width
                        x = self.width - element_width // 2 - self.corner_padding
                    else:
                        x = self.width - 100  # fallback
                else:
                    x = self.width - 100  # fallback si pas d'éléments

                # ← MODIFIÉ : Utiliser corner_padding_y au lieu de 50
                y = self.height - self.corner_padding_y - (count - 1 - i) * self.spacing

                positions.append((int(x), int(y)))

            return positions

        if zone == Layout.LEFT_CORNER:

            for i in range(count):

                # Calculer x en fonction de la largeur de l'élément
                if elements and i < len(elements):
                    element = elements[i]
                    if hasattr(element, 'rect'):
                        element_width = element.rect.width
                        x = element_width // 2 + self.corner_padding
                    else:
                        x = 100  # fallback
                else:
                    x = 100  # fallback

                # ← MODIFIÉ : Utiliser corner_padding_y au lieu de 50
                y = self.height - self.corner_padding_y - (count - 1 - i) * self.spacing

                positions.append((int(x), int(y)))

            return positions
        
        # ← NOUVEAU
        if zone == Layout.TOP_LEFT_CORNER:

            for i in range(count):

                if elements and i < len(elements):
                    element = elements[i]
                    if hasattr(element, 'rect'):
                        element_width = element.rect.width
                        x = element_width // 2 + self.corner_padding
                    else:
                        x = 100
                else:
                    x = 100

                y = self.corner_padding_y + i * self.spacing
                positions.append((int(x), int(y)))

            return positions

        # ← NOUVEAU
        if zone == Layout.TOP_RIGHT_CORNER:

            for i in range(count):

                if elements and i < len(elements):
                    element = elements[i]
                    if hasattr(element, 'rect'):
                        element_width = element.rect.width
                        x = self.width - element_width // 2 - self.corner_padding
                    else:
                        x = self.width - 100
                else:
                    x = self.width - 100

                y = self.corner_padding_y + i * self.spacing
                positions.append((int(x), int(y)))

            return positions
        
        # ---------- HORIZONTAL CENTER ← NOUVEAU ----------

        if zone == Layout.HORIZONTAL_CENTER:

            total_width = 0
            widths = []

            for i in range(count):
                if elements and i < len(elements):
                    element = elements[i]
                    if hasattr(element, 'rect'):
                        w = element.rect.width
                    else:
                        w = 100
                else:
                    w = 100
                widths.append(w)
                total_width += w

            total_width += self.horizontal_spacing * (count - 1)

            start_x = self.width // 2 - total_width // 2

            y = self.row_y  # ← Utilise row_y au lieu de height // 2

            current_x = start_x
            for i, w in enumerate(widths):
                x = current_x + w // 2
                positions.append((int(x), int(y)))
                current_x += w + self.horizontal_spacing

            return positions

        # ---------- DISTRIBUTION VERTICALE (RESTE IDENTIQUE) ----------

        total_height = (count - 1) * self.spacing

        start_y = (self.height // 2) - (total_height // 2)

        for i in range(count):

            y = start_y + i * self.spacing

            if zone == Layout.CENTER:
                x = self.width // 2

            elif zone == Layout.LEFT:
                x = self.width * 0.2

            elif zone == Layout.RIGHT:
                x = self.width * 0.8

            elif zone == Layout.TOP:
                x = self.width // 2
                y = 80 + i * self.spacing

            elif zone == Layout.BOTTOM:
                x = self.width // 2
                y = self.height - 80 - (count-1-i)*self.spacing

            positions.append((int(x), int(y)))

        return positions