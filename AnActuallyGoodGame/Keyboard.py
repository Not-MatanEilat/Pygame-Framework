from pygame import key as pygame_key


class Keyboard:
    def __init__(self):
        self.keys = {}
        self.last_keys = {}

    def update(self):
        self.last_keys = self.copy_keys()
        self.keys = pygame_key.get_pressed()

    def is_key_down(self, key):
        return self.keys[key]

    def is_key_up(self, key):
        return not self.keys[key]

    def is_key_just_pressed(self, key):
        return self.keys[key] and not self.last_keys[key]

    def is_key_just_released(self, key):
        return not self.keys[key] and self.last_keys[key]

    def copy_keys(self):
        keys = {}
        for key in self.keys:
            keys[key] = self.keys[key]
        return keys