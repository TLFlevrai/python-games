import pygame

from games.flappy_bird.flappy_bird_core.flappy_bird_config import FlappyBirdConfig
from games.flappy_bird.flappy_bird_core.entity.pipe import Pipe

class PipeManager:

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.pipes = []

        self.spawn_timer = 0
        self.spawn_interval = FlappyBirdConfig.PIPE_SPAWN_INTERVAL

        self.speed = FlappyBirdConfig.PIPE_SPEED

    # ---------- UPDATE ----------

    def update(self, bird_rect):

        collision = False
        scored = False

        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_pipe()
            self.spawn_timer = 0

        for pipe in self.pipes[:]:

            pipe.update()

            if pipe.collide(bird_rect):
                collision = True

            if pipe.check_score(bird_rect):
                scored = True

            if pipe.is_offscreen():
                self.pipes.remove(pipe)

        return collision, scored

    # ---------- SPAWN ----------

    def spawn_pipe(self):
        pipe = Pipe(self.screen_width, self.screen_height, self.speed)
        self.pipes.append(pipe)

    # ---------- DRAW ----------

    def draw(self, surface):
        for pipe in self.pipes:
            pipe.draw(surface)

    # ---------- RESET ----------

    def reset(self):
        self.pipes.clear()
        self.spawn_timer = 0