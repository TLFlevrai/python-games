import pygame

from core.utilities.colors import Colors
from .core.configs import game_config, scoring_config
from .core.entities import Snake, Food
from .core.managers import CollisionManager, ScoreManager
from .core.interfaces.pause_interface import PauseInterface
from .core.interfaces.game_over_interface import GameOverInterface

class SnakeGame:
    def __init__(self, screen, input_manager):
        self.surface = screen
        self.input = input_manager
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # État du jeu
        self.state = "playing"  # playing, paused, game_over

        # Dimensions de la grille
        self.grid_width = game_config.grid_width
        self.grid_height = game_config.grid_height
        self.cell_size = game_config.cell_size

        # Calculer le décalage pour centrer la grille
        self.grid_offset_x = (self.screen_width - self.grid_width * self.cell_size) // 2
        self.grid_offset_y = (self.screen_height - self.grid_height * self.cell_size) // 2

        # Entités
        self.snake = Snake(self.grid_width, self.grid_height)
        self.food = Food(self.grid_width, self.grid_height)
        # Placer la nourriture en évitant le serpent initial
        self.food.respawn(self.snake.get_body())

        # Gestionnaires
        self.collision_manager = CollisionManager()
        self.score_manager = ScoreManager()

        # Vitesse (frames par mouvement)
        self.move_timer = 0
        self.move_interval = game_config.initial_speed  # nombre de frames avant un mouvement

        # Interfaces
        self.pause_interface = PauseInterface(self.surface, self.input)
        self.game_over_interface = GameOverInterface(self.surface, self.input)

    def reset(self):
        self.state = "playing"
        self.snake = Snake(self.grid_width, self.grid_height)
        self.food.respawn(self.snake.get_body())
        self.score_manager.reset()
        self.move_timer = 0
        self.move_interval = game_config.initial_speed

    def handle_input(self):
        # Changer la direction du serpent
        if self.input.key_just_pressed(pygame.K_UP):
            self.snake.change_direction((0, -1))
        elif self.input.key_just_pressed(pygame.K_DOWN):
            self.snake.change_direction((0, 1))
        elif self.input.key_just_pressed(pygame.K_LEFT):
            self.snake.change_direction((-1, 0))
        elif self.input.key_just_pressed(pygame.K_RIGHT):
            self.snake.change_direction((1, 0))

        # Pause avec Échap
        if self.input.key_just_pressed(pygame.K_ESCAPE):
            self.state = "paused"

    def update(self):
        if self.state == "playing":
            self.handle_input()

            # Gestion du mouvement basé sur le timer
            self.move_timer += 1
            if self.move_timer >= self.move_interval:
                self.move_timer = 0
                self.snake.move()

                # Vérifier les collisions
                head = self.snake.get_head()

                # Collision avec la nourriture
                if self.collision_manager.check_food_collision(head, self.food.get_position()):
                    self.snake.set_grow()
                    self.score_manager.add_food_score()
                    self.food.respawn(self.snake.get_body())

                    # Augmenter la vitesse (diminuer l'intervalle)
                    new_interval = max(game_config.min_speed, self.move_interval - game_config.speed_increment)
                    self.move_interval = new_interval

                # Collision avec les murs
                if self.collision_manager.check_wall_collision(head, self.grid_width, self.grid_height):
                    self.state = "game_over"
                    return

                # Collision avec soi-même
                if self.collision_manager.check_self_collision(self.snake.get_body()):
                    self.state = "game_over"
                    return

        elif self.state == "paused":
            result = self.pause_interface.update()
            if result == "RESUME":
                self.state = "playing"
            elif result == "RESTART":
                self.reset()
            elif result == "MENU":
                return "MENU"

        elif self.state == "game_over":
            result = self.game_over_interface.update(
                self.score_manager.current_score,
                self.score_manager.high_score
            )
            if result == "RESTART":
                self.reset()
            elif result == "MENU":
                self.reset()
                return "MENU"

        return None

    def draw(self, surface):
        # Dessiner le fond
        surface.fill(game_config.background_color)

        # Dessiner la grille (lignes)
        for x in range(self.grid_width + 1):
            start = (self.grid_offset_x + x * self.cell_size, self.grid_offset_y)
            end = (self.grid_offset_x + x * self.cell_size, self.grid_offset_y + self.grid_height * self.cell_size)
            pygame.draw.line(surface, game_config.grid_line_color, start, end, 1)
        for y in range(self.grid_height + 1):
            start = (self.grid_offset_x, self.grid_offset_y + y * self.cell_size)
            end = (self.grid_offset_x + self.grid_width * self.cell_size, self.grid_offset_y + y * self.cell_size)
            pygame.draw.line(surface, game_config.grid_line_color, start, end, 1)

        # Dessiner les entités
        self.snake.draw(surface, self.grid_offset_x, self.grid_offset_y)
        self.food.draw(surface, self.grid_offset_x, self.grid_offset_y)

        # Dessiner le score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score_manager.get_formatted_score()}", True, Colors.WHITE)
        high_text = font.render(f"High: {self.score_manager.get_formatted_high_score()}", True, Colors.WHITE)
        surface.blit(score_text, (10, 10))
        surface.blit(high_text, (10, 50))

        # Dessiner les overlays si nécessaire
        if self.state == "paused":
            self.pause_interface.draw(surface)
        elif self.state == "game_over":
            self.game_over_interface.draw(surface,
                                          self.score_manager.current_score,
                                          self.score_manager.high_score)