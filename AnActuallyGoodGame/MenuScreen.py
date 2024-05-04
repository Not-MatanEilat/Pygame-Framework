import pygame

from AnActuallyGoodGame import Colors
from AnActuallyGoodGame.UI import EditText, Button
from Screen import Screen
from Sprite import Sprite
from GameScreen import GameScreen

class MenuScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.init_UI()

    def init_UI(self):
        button = Button(pygame.Rect(150, 150, 100, 50), Colors.RED, "Play", Colors.BLACK, self.game.mouse)
        button.on_click_call_backs.append(lambda: self.start_screen(GameScreen))
        self.game.UI.add_view(button)


    def updates(self, events):
        super().updates(events)

    def draw(self):
        super().draw()
