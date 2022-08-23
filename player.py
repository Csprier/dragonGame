import pygame
# from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # General setup
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

        # Movement attributes
        self.direction = pygame.math.Vector2() # default value is 0,0 or nothing
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
    def input(self):
        # .get_pressed() returns a list of all the keys that are potentially being pressed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            print('Up')
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            print('Down')
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            print('Left')
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            print('Right')
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos
    def update(self, dt):
        self.input()
        self.move(dt)