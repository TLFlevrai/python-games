# core/ui/layout.py
from enum import Enum
from typing import List, Optional, Any

class Zone(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    RIGHT_CORNER = "right_corner"
    LEFT_CORNER = "left_corner"
    TOP_LEFT_CORNER = "top_left_corner"
    TOP_RIGHT_CORNER = "top_right_corner"
    HORIZONTAL_CENTER = "horizontal_center"

class Layout:
    def __init__(self, screen_width, screen_height, spacing=20, corner_padding=20,
                 corner_padding_y=15, horizontal_spacing=30, row_y=None):
        self.width = screen_width
        self.height = screen_height
        self.spacing = spacing
        self.corner_padding = corner_padding
        self.corner_padding_y = corner_padding_y
        self.horizontal_spacing = horizontal_spacing
        self.row_y = row_y if row_y is not None else screen_height // 2

    def compute_positions(self, count: int, zone: Zone, elements: Optional[List[Any]] = None) -> List[tuple]:
        positions = []
        if count == 0:
            return positions

        if zone == Zone.RIGHT_CORNER:
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
                y = self.height - self.corner_padding_y - (count - 1 - i) * self.spacing
                positions.append((int(x), int(y)))
            return positions

        elif zone == Zone.LEFT_CORNER:
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
                y = self.height - self.corner_padding_y - (count - 1 - i) * self.spacing
                positions.append((int(x), int(y)))
            return positions

        elif zone == Zone.TOP_LEFT_CORNER:
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

        elif zone == Zone.TOP_RIGHT_CORNER:
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

        elif zone == Zone.HORIZONTAL_CENTER:
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
            y = self.row_y
            current_x = start_x
            for w in widths:
                x = current_x + w // 2
                positions.append((int(x), int(y)))
                current_x += w + self.horizontal_spacing
            return positions

        else:
            # Zones verticales: CENTER, TOP, BOTTOM, LEFT, RIGHT
            total_height = (count - 1) * self.spacing
            start_y = (self.height // 2) - (total_height // 2)
            for i in range(count):
                y = start_y + i * self.spacing
                if zone == Zone.CENTER:
                    x = self.width // 2
                elif zone == Zone.LEFT:
                    x = self.width * 0.2
                elif zone == Zone.RIGHT:
                    x = self.width * 0.8
                elif zone == Zone.TOP:
                    x = self.width // 2
                    y = 80 + i * self.spacing
                elif zone == Zone.BOTTOM:
                    x = self.width // 2
                    y = self.height - 80 - (count-1-i) * self.spacing
                else:
                    x = self.width // 2  # fallback
                positions.append((int(x), int(y)))
            return positions