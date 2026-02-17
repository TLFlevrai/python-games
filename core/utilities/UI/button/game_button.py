import pygame

class GameButton:
    """
    Bouton de sélection de jeu avec logo.
    Style moderne sobre, coins arrondis.
    Rectangle avec logo centré + nom du jeu en dessous.
    """

    def __init__(self, text, logo_path, position, input_manager):

        self.text = text
        self.input = input_manager

        # ---------- DIMENSIONS ----------
        self.width = 130
        self.height = 160
        self.border_radius = 14
        self.logo_size = 50

        # ---------- RECT ----------
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = position

        # ---------- LOGO ----------
        try:
            raw = pygame.image.load(logo_path).convert_alpha()
            self.logo = pygame.transform.scale(raw, (self.logo_size, self.logo_size))
        except (pygame.error, FileNotFoundError) as e:
            print(f"⚠️ Logo '{logo_path}' not found: {e}")
            self.logo = None

        # ---------- FONT ----------
        self.font = pygame.font.SysFont("Courier New", 16)

        # ---------- STATE ----------
        self.is_hovered = False
        self.is_pressed = False

    # ---------- SET POSITION ----------

    def set_position(self, pos):
        self.rect.center = pos

    # ---------- UPDATE ----------

    def update(self):

        mouse_pos = self.input.get_mouse_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)

        if self.is_hovered:
            self.is_pressed = self.input.pressed()
            if self.input.click():
                return True

        return False

    # ---------- DRAW ----------

    def draw(self, surface):

        mouse_pos = self.input.get_mouse_pos()

        # ---------- COULEURS SELON ÉTAT ----------
        if self.is_pressed:
            bg_color = (25, 25, 28)
            border_color = (80, 80, 85)
        elif self.is_hovered:
            bg_color = (55, 55, 60)
            border_color = (100, 100, 110)
        else:
            bg_color = (35, 35, 38)
            border_color = (60, 60, 65)

        # ---------- FOND ----------
        pygame.draw.rect(surface, bg_color, self.rect, border_radius=self.border_radius)
        pygame.draw.rect(surface, border_color, self.rect, width=1, border_radius=self.border_radius)

        # ---------- LOGO ----------
        if self.logo:
            logo_x = self.rect.centerx - self.logo_size // 2
            logo_y = self.rect.top + 30  # Marge haute
            surface.blit(self.logo, (logo_x, logo_y))
        else:
            # Fallback carré coloré
            fallback = pygame.Rect(
                self.rect.centerx - 25,
                self.rect.top + 30,
                50, 50
            )
            pygame.draw.rect(surface, (70, 70, 75), fallback, border_radius=8)

        # ---------- TEXTE ----------
        label = self.font.render(self.text.upper(), True, 
            (220, 220, 220) if self.is_hovered else (160, 160, 165)
        )
        label_rect = label.get_rect(center=(self.rect.centerx, self.rect.bottom - 25))
        surface.blit(label, label_rect)