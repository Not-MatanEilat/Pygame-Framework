import pygame

from Sprite import Sprite


class Player(Sprite):
    def __init__(self, game_scroll, x, y, width, height):
        super().__init__(game_scroll, x, y, width, height)
        self.lock_all_controls = False

    def update(self, keyboard):
        if not self.lock_all_controls:
            if keyboard.is_key_down(pygame.K_a):
                self.rect.x -= 5
            if keyboard.is_key_down(pygame.K_d):
                self.rect.x += 5
            if keyboard.is_key_down(pygame.K_w):
                self.rect.y -= 5
            if keyboard.is_key_down(pygame.K_s):
                self.rect.y += 5