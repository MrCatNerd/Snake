__author__ = "Alon B.R."

import json

from os.path import join as join_path


def get_settings() -> dict:
    settings_file_path: str = join_path("data", "settings.json")

    with open(settings_file_path, "r") as settings_file:
        contant: str = settings_file.read()
        data: str = json.loads(contant)

    return data


data = get_settings()


DATA_PATH: str = data["data path"]
TITLE: str = data["title"]
WIDTH: int = data["width"]
HEIGHT: int = data["height"]
FONT_NAME: str = data["font name"]
FONT_SIZE: int = data["font size"]
FONT_PATH: str = join_path(DATA_PATH, data["font path"])
FONT_ANTIALIASING: bool = data["font antialiasing"]
SCALE: int = data["scale"]
FPS: int = data["fps"]
SFX_PATH: bool = join_path(DATA_PATH, data["sfx path"])
SFX_VOLUME: float = data["sfx volume"] / 100
SNAKE_SPEED: int = data["snake speed"]
SNAKE_COLOR: tuple = data["snake color"]
SNAKE_HEAD_COLOR: tuple = data["snake head color"]
APPLE_COLOR: tuple = data["apple color"]
GAME_SPEED: float = data["game speed"]

del get_settings, join_path
