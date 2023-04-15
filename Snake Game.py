__author__ = "Alon B.R."

import pygame
import sys
import time

from pygame import mixer

from os.path import join as join_path

from settings import *
from apple import Apple
from snake import Snake

pygame.init()
mixer.init()


def load_sound(*paths) -> mixer.Sound:
    return mixer.Sound(join_path(*paths))


FONT = pygame.font.Font(join_path(FONT_PATH, FONT_NAME), FONT_SIZE)


class Main:
    def __init__(self) -> None:
        self.app = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.run = True

        # sfx
        self.sfx_channel = mixer.Channel(0)
        self.sfx_channel.set_volume(SFX_VOLUME)
        self.move_sfx = load_sound(SFX_PATH, "move.wav")

        ####################################################
        self.snake = Snake()
        self.apple = Apple()

    def play(self) -> None:
        last_time: float = time.time()
        while self.run:
            deltaTime: float = time.time() - last_time
            deltaTime *= GAME_SPEED
            last_time = time.time()

            keys = pygame.key.get_pressed()
            self.app.fill((0, 0, 0))

            score_texture = FONT.render(
                f"SCORE: {self.snake.score}", FONT_ANTIALIASING, (255, 255, 255)
            )

            self.app.blit(score_texture, (50, 50))
            self.snake.update(
                keys, self.apple, self.app, self.move_sfx, self.sfx_channel, deltaTime
            )
            self.apple.update(self.app)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        self.quit()

            self.clock.tick(FPS)
            pygame.display.update()

    def quit(self):
        self.run = False
        mixer.quit()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Main()
    game.play()
