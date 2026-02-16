import pygame

# core
from games.flappy_bird.flappy_bird_core.entity.bird import Bird
from games.flappy_bird.flappy_bird_core.entity.pipe_manager import PipeManager
from games.flappy_bird.flappy_bird_core.UI.label.flappy_bird_score import Score


class FlappyBirdGame:

    def __init__(self, screen, input_manager):

        self.surface = screen
        self.input = input_manager

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # ---------- GAME STATE ----------
        self.game_over = False

        # ---------- PLAYER ----------
        self.bird = Bird(200, self.screen_height // 2)

        # ---------- PIPES ----------
        self.pipe_manager = PipeManager(self.screen_width, self.screen_height)

        # ---------- SCORE ----------
        self.score_manager = Score(self.screen_width, self.screen_height)

    # ==================================================
    # RESET
    # ==================================================

    def reset(self):

        self.game_over = False
        self.score = 0

        self.bird.reset(200, self.screen_height // 2)
        self.pipe_manager.reset()

        print("🔄 Flappy Bird reset")

    # ==================================================
    # UPDATE
    # ==================================================

    def update(self):

        # ---------- INPUT ----------
        if not self.game_over:

            # Clic souris OU touche Espace
            if self.input.click() or self.input.space_pressed():
                self.bird.flap()

        # ---------- UPDATE PLAYER ----------
        self.bird.update()

        # ---------- UPDATE PIPES ----------
        if not self.game_over:

            collision, scored = self.pipe_manager.update(
                self.bird.get_rect()
            )

            # collision
            if collision:
                self.game_over = True
                self.bird.alive = False

            # scoring
            if scored:
                self.score_manager.add_point()  # ← NOUVEAU

        # ---------- CHECK SCREEN LIMIT ----------
        if self.bird.y < 0 or self.bird.y > self.screen_height:
            self.game_over = True
            self.bird.alive = False

    # ==================================================
    # DRAW
    # ==================================================

    def draw(self, surface):

        # pipes
        self.pipe_manager.draw(surface)

        # bird
        self.bird.draw(surface)

        # score
        self.score_manager.draw(surface)  # ← NOUVEAU