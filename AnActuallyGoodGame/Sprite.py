import pygame
import Colors
from Drawable import Drawable


class Sprite(Drawable):
    def __init__(self, game_sroll, x, y, width, height):
        super().__init__()
        self.game_scroll = game_sroll

        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.RED, pygame.Rect(self.rect.x - self.game_scroll.x, self.rect.y - self.game_scroll.y, self.rect.width, self.rect.height))
