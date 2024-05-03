import pygame


class Screen:
    def __init__(self, game):
        self.game = game
        self.game.draw_manager.clear()

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

    def updates(self, events):
        self.game.mouse.update(events)
        self.game.keyboard.update()
        self.game.player.update(self.game.keyboard)
        self.game.UI.update()

    def middleUpdates(self, events):
        pass

    def endUpdates(self, events):
        self.game.camera.update()

    def draw(self):
        self.game.screen.fill(self.game.BACKGROUND_COLOR)
        self.game.draw_manager.draw(self.game.screen)
        pygame.display.flip()

