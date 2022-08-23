import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Dragon Game')
        self.clock = pygame.time.Clock()
        self.level = Level()

    # Run method which is responsible for the 'game loop'
    # While the game is open, update. Otherwise, the game quits and shuts down entirely.
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Delta Time
            # dt is passed to the run method of the level class to keep the frames updating
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
