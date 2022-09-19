__author__ = "Alon B.R."

import json

from os.path import join as join_path


def get_settings() -> dict:
    settings_file_path: str = join_path("data", ".settings.json")

    with open(settings_file_path, "r") as settings_file:
        contant: str = settings_file.read()
        data: str = json.loads(contant)

    return data


data = get_settings()


TITLE: str = data["title"]
FONT_NAME: str = data["font name"]
FONT_SIZE: int = data["font size"]
ANTIALIASING: bool = data["antialiasing"]
WIDTH: int = data["width"]
HEIGHT: int = data["height"]
SCALE: int = data["scale"]
FPS: int = data["fps"]
SFX: bool = data["sfx"]
SFX_VOLUME: float = data["sfx volume"]
SNAKE_SPEED: int = data["snake speed"]
SNAKE_COLOR: tuple = data["snake color"]
SNAKE_HEAD_COLOR: tuple = data["snake head color"]
APPLE_COLOR: tuple = data["apple color"]
DEBUG_MODE: bool = data["debug mode"]

del get_settings, join_path
