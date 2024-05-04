import pygame
import sys


class Screen:
    def __init__(self, game):
        self.game = game
        self.drawables = []
        self.views = []
        self.game.draw_manager.current_screen = self
        self.game.UI.current_screen = self

    def run(self):
        while self.game.running:
            self.game.clock.tick(self.game.FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.game.running = False

            self.updates(events)
            self.middleUpdates(events)
            self.endUpdates(events)

            self.draw()

        pygame.quit()
        sys.exit()


    def updates(self, events):
        self.game.mouse.update(events)
        self.game.keyboard.update()
        self.game.UI.update()
        self.game.timer_manager.update()

    def middleUpdates(self, events):
        pass

    def endUpdates(self, events):
        self.game.camera.update()

    def init_UI(self):
        pass

    def draw(self):
        self.game.screen.fill(self.game.BACKGROUND_COLOR)
        self.game.draw_manager.draw(self.game.screen)
        pygame.display.flip()

    def start_screen(self, screen):
        screen_to_start = screen(self.game)
        self.game.screens.append(self)
        self.game.current_screen = screen_to_start
        screen_to_start.run()

    def back_to_last_screen(self):
        screen_to_start = self.game.screens.pop()
        self.game.current_screen = screen_to_start
        self.game.draw_manager.current_screen = screen_to_start
        self.game.UI.current_screen = screen_to_start
        screen_to_start.run()
