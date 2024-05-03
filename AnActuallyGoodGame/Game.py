import pygame
import Colors
from Mouse import Mouse
from Keyboard import Keyboard



pygame.init()


class Game:
    HEIGHT = 600
    WIDTH = 800
    FPS = 60
    BACKGROUND_COLOR = Colors.LIGHTBLUE

    def __init__(self):
        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.game_scroll = GameScroll()
        self.camera = Camera(self.game_scroll)
        self.player = Player(self.game_scroll, 50, 50, 50, 50)
        self.mouse = Mouse()
        self.keyboard = Keyboard()

        self.camera.follow(self.player)

        self.test1 = Sprite(self.game_scroll, 1000, 100, 50, 50)
        self.test2 = Sprite(self.game_scroll, 200, 200, 50, 50)

    def draw(self):
        self.screen.fill(self.BACKGROUND_COLOR)
        self.player.draw(self.screen)
        self.test1.draw(self.screen)
        self.test2.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.mouse.update(events)
            self.keyboard.update()
            self.player.update(self.keyboard)

            self.camera.move_x(1)

            self.camera.update()
            self.draw()

        pygame.quit()


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


class Sprite:
    def __init__(self, game_scroll, x, y, width, height):
        self.game_scroll = game_scroll

        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.RED, pygame.Rect(self.rect.x - self.game_scroll.x, self.rect.y - self.game_scroll.y, self.rect.width, self.rect.height))


class Player(Sprite):
    def __init__(self, game_scroll, x, y, width, height):
        super().__init__(game_scroll, x, y, width, height)

    def update(self, keyboard):
        if keyboard.is_key_down(pygame.K_a):
            self.rect.x -= 5
        if keyboard.is_key_down(pygame.K_d):
            self.rect.x += 5
        if keyboard.is_key_down(pygame.K_w):
            self.rect.y -= 5
        if keyboard.is_key_down(pygame.K_s):
            self.rect.y += 5


if __name__ == "__main__":
    game = Game()
    game.run()