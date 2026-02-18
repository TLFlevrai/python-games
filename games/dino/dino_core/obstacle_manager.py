import pygame
from games.dino.dino_core.obstacle import Obstacle

class ObstacleManager:
    """
    Gestionnaire d'obstacles pour Dino Runner.
    Spawn automatique, vitesse progressive.
    """

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.obstacles = []

        # ---------- SPAWN TIMING ----------
        self.spawn_timer = 0
        self.spawn_interval = 90  # frames (1.5 sec à 60 FPS)
        self.min_spawn_interval = 50  # Intervalle minimum

        # ---------- VITESSE ----------
        self.initial_speed = 6
        self.speed = self.initial_speed
        self.speed_increment = 0.002  # Augmentation progressive

    # ---------- UPDATE ----------

    def update(self, dino_rect):
        """
        Met à jour tous les obstacles.
        
        Returns:
            bool: True si collision détectée
        """

        collision = False

        # Timer de spawn
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_obstacle()
            self.spawn_timer = 0

        # Mise à jour de chaque obstacle
        for obstacle in self.obstacles[:]:

            obstacle.update()

            # Collision avec le dino
            if obstacle.get_rect().colliderect(dino_rect):
                collision = True

            # Suppression hors écran
            if obstacle.is_offscreen():
                self.obstacles.remove(obstacle)

        # Augmentation progressive de la vitesse
        self.speed += self.speed_increment

        return collision

    # ---------- SPAWN ----------

    def spawn_obstacle(self):
        """Crée un nouvel obstacle"""
        obstacle = Obstacle(self.screen_width, self.screen_height, self.speed)
        self.obstacles.append(obstacle)

    # ---------- DRAW ----------

    def draw(self, surface):
        """Dessine tous les obstacles"""
        for obstacle in self.obstacles:
            obstacle.draw(surface)

    # ---------- RESET ----------

    def reset(self):
        """Réinitialise le gestionnaire"""
        self.obstacles.clear()
        self.spawn_timer = 0
        self.speed = self.initial_speed

    # ---------- DIFFICULTY ----------

    def increase_difficulty(self):
        """Réduit l'intervalle de spawn (plus difficile)"""
        if self.spawn_interval > self.min_spawn_interval:
            self.spawn_interval -= 5