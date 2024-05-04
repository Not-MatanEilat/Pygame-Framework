import pygame

from AnActuallyGoodGame import Colors
from Player import Player
from AnActuallyGoodGame.UI import EditText, Button
from Screen import Screen
from Sprite import Sprite


class GameScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.player = Player(self.game.game_scroll, 50, 50, 50, 50)

        self.init_UI()

    def init_UI(self):
        button = Button(pygame.Rect(0, 0, 100, 50), Colors.RED, "Back", Colors.BLACK, self.game.mouse)
        button.on_click_call_backs.append(lambda: self.back_to_last_screen())
        self.game.UI.add_view(button)

    def updates(self, events):
        super().updates(events)
        self.player.update(self.game.keyboard)

        if self.game.keyboard.is_key_just_pressed(pygame.K_t):
            self.back_to_last_screen()

    def draw(self):
        super().draw()