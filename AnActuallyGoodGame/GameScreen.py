import pygame

from AnActuallyGoodGame import Colors
from AnActuallyGoodGame.Timer import CountdownTimer
from Player import Player
from AnActuallyGoodGame.UI import EditText, Button, Text
from Screen import Screen
from Sprite import Sprite
from Block import Block


class GameScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.player = Player(self.game.game_scroll, 50, 50, 50, 50)
        self.blocks = []

        self.init_UI()
        self.init_blocks()

        self.text_view = Text(pygame.Rect(0, 50, 100, 50), "Time: ", 36, Colors.BLACK, self.game.mouse)
        self.game.UI.add_view(self.text_view)

        self.timer = CountdownTimer(10)
        self.timer.start()
        self.timer.on_finish = lambda: self.back_to_last_screen()

    def init_UI(self):
        button = Button(pygame.Rect(0, 0, 100, 50), Colors.RED, "Back", Colors.BLACK, self.game.mouse)
        button.on_click_call_backs.append(lambda: self.back_to_last_screen())
        self.game.UI.add_view(button)

    def init_blocks(self):
        block1 = Block(self.game.game_scroll, 0, 0, 50, 50)
        block2 = Block(self.game.game_scroll, 250, 400, 50, 50)
        block3 = Block(self.game.game_scroll, 350, 400, 50, 50)
        block4 = Block(self.game.game_scroll, 450, 400, 50, 50)
        block5 = Block(self.game.game_scroll, 220, 400, 50, 50)
        block6 = Block(self.game.game_scroll, 300, 400, 50, 50)

        self.blocks.append(block1)
        self.blocks.append(block2)
        self.blocks.append(block3)
        self.blocks.append(block4)
        self.blocks.append(block5)
        self.blocks.append(block6)

    def updates(self, events):
        super().updates(events)
        self.player.update(self.game.keyboard, self.blocks)
        self.text_view.text = "Time: " + str(int(self.timer.get_time_is_left()))

    def draw(self):
        super().draw()