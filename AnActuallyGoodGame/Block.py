from Sprite import Sprite

class Block(Sprite):
    def __init__(self, game_scroll, x, y, width, height):
        super().__init__(game_scroll, x, y, width, height)

    def update(self, keyboard):
        pass