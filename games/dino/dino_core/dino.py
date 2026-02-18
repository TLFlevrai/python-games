import pygame

class Dino:
    """
    Dinosaure joueur pour Dino Runner.
    Peut sauter avec Espace pour éviter les obstacles.
    """

    def __init__(self, ground_y): 

        # ---------- POSITION ----------
        self.x = 100  # Position fixe à gauche
        self.ground_y = ground_y
        self.y = ground_y

        # ---------- DIMENSIONS ----------
        self.width = 40
        self.height = 50

        # ---------- PHYSIQUE ----------
        self.gravity = 0.8
        self.jump_strength = -15
        self.velocity_y = 0

        # ---------- ÉTAT ----------
        self.is_jumping = False
        self.is_alive = True

        # ---------- HITBOX ----------
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # ---------- COULEURS ----------
        self.color = (80, 80, 85)  # Gris foncé

    # ---------- INPUT ----------

    def jump(self):
        """Saute si au sol"""
        if not self.is_jumping and self.is_alive:
            self.velocity_y = self.jump_strength
            self.is_jumping = True

    # ---------- UPDATE ----------

    def update(self):

        if not self.is_alive:
            return

        # Appliquer gravité
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Collision avec le sol
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.velocity_y = 0
            self.is_jumping = False

        # Update hitbox
        self.rect.topleft = (self.x, self.y)

    # ---------- COLLISION ----------

    def get_rect(self):
        """Retourne la hitbox pour détection collision"""
        return self.rect

    def die(self):
        """Tue le dino"""
        self.is_alive = False

    # ---------- DRAW ----------

    def draw(self, surface):
        """Dessine le dino (rectangle simple pour l'instant)"""
        pygame.draw.rect(surface, self.color, self.rect)

        # Debug hitbox (optionnel)
        # pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)

    # ---------- RESET ----------

    def reset(self, ground_y):
        """Réinitialise le dino"""
        self.ground_y = ground_y
        self.y = ground_y
        self.velocity_y = 0
        self.is_jumping = False
        self.is_alive = True
        self.rect.topleft = (self.x, self.y)