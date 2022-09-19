__author__ = "Alon B.R."

import pygame
import sys

from pygame import mixer

from os.path import join as join_path

from settings import *
from apple import Apple
from snake import Snake

pygame.init()
mixer.init()


def load_sound(*paths) -> mixer.Sound:
    return mixer.Sound(join_path(*paths))


FONT = pygame.font.Font(FONT_NAME, FONT_SIZE)


class Main:
    def __init__(self) -> None:
        self.app = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.run = True

        # sfx
        self.sfx_channel = mixer.Channel(0)
        self.sfx_channel.set_volume(SFX_VOLUME)
        self.move_sfx = load_sound("data", "sfx", "move.wav")

        ####################################################
        self.snake = Snake()
        self.apple = Apple()

    def play(self) -> None:
        while self.run:
            keys = pygame.key.get_pressed()
            self.app.fill((0, 0, 0))

            self.snake.update(
                keys, self.apple, self.app, self.move_sfx, self.sfx_channel
            )
            self.apple.update(self.app)

            score_texture = FONT.render(
                f"SCORE: {self.snake.score}", ANTIALIASING, (255, 255, 255)
            )

            if DEBUG_MODE and any(pygame.mouse.get_pressed()):
                self.snake.score += 1

            self.app.blit(score_texture, (50, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    mixer.quit()
                    pygame.quit()
                    sys.exit()

            self.clock.tick(FPS)
            pygame.display.update()


if __name__ == "__main__":
    game = Main()
    game.play()
