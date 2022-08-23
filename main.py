import pygame, sys
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    # Run method which is responsible for the 'game loop'
    # While the game is open, update. Otherwise, the game quits and shuts down entirely.
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
