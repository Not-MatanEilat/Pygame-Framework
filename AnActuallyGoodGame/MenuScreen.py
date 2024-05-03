import pygame

from AnActuallyGoodGame import Colors
from AnActuallyGoodGame.UI import EditText
from Screen import Screen
from Sprite import Sprite


class MenuScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.game.draw_manager.add_drawable(self.game.player)

        self.init_UI()

    def init_UI(self):
        pass

    def updates(self, events):
        super().updates(events)

    def draw(self):
        super().draw()
