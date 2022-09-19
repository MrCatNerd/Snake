__author__ = "Alon B.R."

import pygame
import random

from settings import SCALE, WIDTH, HEIGHT, APPLE_COLOR

pygame.init()


class Apple:
    def __init__(self) -> None:
        self.reposition()

    def update(self, window: pygame.Surface) -> None:
        pygame.draw.rect(window, APPLE_COLOR, (self.pos.x, self.pos.y, SCALE, SCALE))

    def reposition(self) -> None:
        self.pos: pygame.math.Vector2 = pygame.math.Vector2(
            random.randint(1, (WIDTH // SCALE) - 1) * SCALE,
            random.randint(1, (HEIGHT // SCALE) - 1) * SCALE,
        )
