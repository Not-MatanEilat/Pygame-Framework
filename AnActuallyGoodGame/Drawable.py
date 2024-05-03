import abc


class DrawManager:
    instance = None

    def __init__(self):
        self.drawables = []
        self.instance = self

    @staticmethod
    def get_instance():
        if DrawManager.instance is None:
            DrawManager.instance = DrawManager()
        return DrawManager.instance

    def add_drawable(self, drawable):
        self.drawables.append(drawable)
        self.drawables = sorted(self.drawables, key=lambda draw: draw.priority)

    def draw(self, screen):
        for drawable in self.drawables:
            drawable.draw(screen)

    def clear(self):
        self.drawables.clear()

    def remove_drawable(self, drawable):
        self.drawables.remove(drawable)


class Drawable:
    def __init__(self, priority=0):
        self.priority = priority
        DrawManager.get_instance().add_drawable(self)


    @abc.abstractmethod
    def draw(self, screen):
        pass
