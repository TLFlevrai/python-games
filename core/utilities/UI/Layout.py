class Layout:

    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"

    def __init__(self, screen_width, screen_height, spacing=20):

        self.width = screen_width
        self.height = screen_height
        self.spacing = spacing

    def compute_positions(self, count, zone):

        positions = []

        if count == 0:
            return positions

        # distribution verticale
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
