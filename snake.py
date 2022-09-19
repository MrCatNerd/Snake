__author__ = "Alon B.R."

import pygame
import random

from settings import (
    SNAKE_HEAD_COLOR,
    WIDTH,
    HEIGHT,
    SCALE,
    SNAKE_COLOR,
    SNAKE_SPEED,
    SFX,
)

pygame.init()


def draw(pos: pygame.math.Vector2, color: tuple, window: pygame.Surface) -> None:
    pygame.draw.rect(window, color, (pos.x, pos.y, SCALE, SCALE))


class Snake:
    def __init__(self) -> None:
        self.reposition()
        self.trail: list = []

        self.direction: pygame.math.Vector2 = pygame.math.Vector2(0, 0)

        self.score: int = 3

        self.stuck: bool = False

        self.key_pressed: dict = {"w": False, "a": False, "s": False, "d": False}

    def update(
        self,
        keys: pygame.key.get_pressed,
        apple,
        window: pygame.Surface,
        move_sfx: pygame.mixer.Sound,
        channel: pygame.mixer.Channel,
    ):

        # <SPAGHETTI CODE>

        if (
            (keys[pygame.K_w] or keys[pygame.K_UP])
            and not self.key_pressed["w"]
            and self.direction.y != 1
        ):  #     -up
            self.direction.xy = 0, -1
            self.key_pressed["w"] = True

            channel.play(move_sfx)
        elif self.key_pressed["w"] and not (keys[pygame.K_w] or keys[pygame.K_UP]):
            self.key_pressed["w"] = False

        if (
            (keys[pygame.K_a] or keys[pygame.K_LEFT])
            and not self.key_pressed["a"]
            and self.direction.x != 1
        ):  #  -left
            self.direction.xy = -1, 0
            self.key_pressed["a"] = True

            channel.play(move_sfx)
        elif self.key_pressed["a"] and not (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.key_pressed["a"] = False

        if (
            (keys[pygame.K_s] or keys[pygame.K_DOWN])
            and not self.key_pressed["s"]
            and self.direction.y != -1
        ):  #  -down
            self.direction.xy = 0, 1
            self.key_pressed["s"] = True

            channel.play(move_sfx)
        elif self.key_pressed["s"] and not (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            self.key_pressed["s"] = False

        if (
            (keys[pygame.K_d] or keys[pygame.K_RIGHT])
            and not self.key_pressed["d"]
            and self.direction.x != -1
        ):  # -right
            self.direction.xy = 1, 0
            self.key_pressed["d"] = True

            channel.play(move_sfx)

        elif self.key_pressed["d"] and not (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.key_pressed["d"] = False

        # </SPAGHETTI CODE>

        self.update_trail()

        self.pos.x += self.direction.x * SNAKE_SPEED * SCALE
        self.pos.y += self.direction.y * SNAKE_SPEED * SCALE

        self.stick_to_boarder()

        if self.pos.xy == apple.pos.xy:
            apple.reposition()
            self.score += 1

        if self.direction.x != 0 or self.direction.y != 0:
            self.check_dead(apple)

        for peace in self.trail:
            draw(peace, SNAKE_COLOR, window)
        draw(self.pos, SNAKE_HEAD_COLOR, window)

    def check_dead(self, apple) -> bool:
        if self.stuck or any([self.pos.xy == pos for pos in self.trail]):
            self.reposition()
            self.trail = []
            apple.reposition()
            self.score = 3
            self.direction.xy = 0, 0

    def update_trail(self) -> None:
        if self.stuck:
            return

        self.trail.append(self.pos.xy)
        if len(self.trail) >= self.score + 1:
            self.trail.remove(self.trail[0])

    def stick_to_boarder(self) -> bool:
        self.stuck = False
        if self.pos.x > WIDTH - SCALE:
            self.pos.x = WIDTH - SCALE
            self.stuck = True

        if self.pos.x < 0:
            self.pos.x = 0
            self.stuck = True

        if self.pos.y > HEIGHT - SCALE:
            self.pos.y = HEIGHT - SCALE
            self.stuck = True

        if self.pos.y < 0:
            self.pos.y = 0
            self.stuck = True

    def reposition(self) -> None:
        self.pos: pygame.math.Vector2 = pygame.math.Vector2(
            random.randint(1, (WIDTH // SCALE) - 1) * SCALE,
            random.randint(1, (HEIGHT // SCALE) - 1) * SCALE,
        )
