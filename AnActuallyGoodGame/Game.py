import pygame
import Colors
from AnActuallyGoodGame.Sprite import Sprite
from Mouse import Mouse
from Keyboard import Keyboard
from UI import Button
from UI import Image
from UI import EditText
from UI import Text
import abc
from MenuScreen import MenuScreen
from Drawable import DrawManager


pygame.init()


class Game:
    HEIGHT = 600
    WIDTH = 800
    FPS = 60
    BACKGROUND_COLOR = Colors.LIGHTBLUE

    def __init__(self):
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.current_screen = None
        self.screens = []
        self.running = True
        self.draw_manager = DrawManager(self.current_screen)
        self.clock = pygame.time.Clock()
        self.game_scroll = GameScroll()
        self.camera = Camera(self.game_scroll)
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.UI = Ui_Manager(self)



    def run(self):
        self.current_screen = MenuScreen(self)
        self.current_screen.start_screen(MenuScreen)
        pygame.quit()


class Ui_Manager:
    def __init__(self, current_screen):
        self.current_screen = current_screen


    def add_view(self, view):
        self.current_screen.views.append(view)

    def update(self):
        for view in self.current_screen.views:
            view.update()

    def draw(self, screen):
        for view in self.current_screen.views:
            view.draw(screen)

    def remove_view(self, view):
        self.current_screen.views.remove(view)
    def clear(self):
        self.current_screen.views.clear()


class Camera:
    def __init__(self, game_scroll):
        self.game_scroll = game_scroll

        self.sprite_following = None
        self.is_following = False

    def update(self):
        if self.is_following:
            self.game_scroll.x = self.sprite_following.rect.x - Game.WIDTH / 2
            self.game_scroll.y = self.sprite_following.rect.y - Game.HEIGHT / 2

    def follow(self, sprite):
        self.is_following = True

        self.game_scroll.x = sprite.rect.x - Game.WIDTH / 2
        self.game_scroll.y = sprite.rect.y - Game.HEIGHT / 2
        self.sprite_following = sprite

    def stop_following(self):
        self.is_following = False

    def move_x(self, x):
        self.game_scroll.x += x

    def move_y(self, y):
        self.game_scroll.y += y


class GameScroll:
    def __init__(self):
        self.x = 0
        self.y = 0



if __name__ == "__main__":
    game = Game()
    game.run()