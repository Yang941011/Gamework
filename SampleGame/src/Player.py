from enum import auto
from os import path

import pygame
from mlgame.utils.enum import StringEnum
from mlgame.view.view_model import create_asset_init_data, create_image_view_data

PLAYER_PATH = path.join(path.dirname(__file__), "..", "asset", "image", "player.png")


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple, play_area_rect: pygame.Rect):
        super().__init__()
        self._play_area_rect = play_area_rect
        self._speed = 5
        self._init_pos = pos
        self.rect = pygame.Rect(*pos, *size)
        self._score = 0
        self._lives = 100

    def update(self, action: list) -> None:
        if "UP" in action and self.rect.top > self._play_area_rect.top:
            self.move_up()
        elif "DOWN" in action and self.rect.bottom < self._play_area_rect.bottom:
            self.move_down()
        elif "LEFT" in action and self.rect.left > self._play_area_rect.left:
            self.move_left()
        elif "RIGHT" in action and self.rect.right < self._play_area_rect.right:
            self.move_right()

    def move_right(self):
        self.rect.centerx += self._speed

    def move_left(self):
        self.rect.centerx -= self._speed

    def move_down(self):
        self.rect.centery += self._speed

    def move_up(self):
        self.rect.centery -= self._speed

    @property
    def score(self):
        return self._score

    @property
    def lives(self):
        return self._lives

    @property
    def xy(self):
        return self.rect.topleft

    def reset(self):
        self.rect.topleft = self._init_pos

    def collide_with_walls(self):
        pass

    def collide_with_mobs(self):
        pass

    def collide_with_bullets(self):
        self._lives -= 10

    @property
    def game_object_data(self):
        return create_image_view_data(image_id="player", x=self.rect.x, y=self.rect.y,
                                      width=self.rect.width, height=self.rect.height, angle=0)

    @property
    def game_init_object_data(self):
        return create_asset_init_data(image_id="player",
                                      width=self.rect.width, height=self.rect.height,
                                      file_path=PLAYER_PATH,
                                      github_raw_url="https://raw.githubusercontent.com/Jesse-Jumbo/GameFramework/main/MyGame/asset/image/player.png")
