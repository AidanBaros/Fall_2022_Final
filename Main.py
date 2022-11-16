from level import *

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screenSize = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.tileGenRect = (15, 10)
        self.level = Level(self.screenSize, self.tileGenRect)
        self.Running = True

    def run(self):
        while self.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                self.Running = False
            if keys[pygame.K_LSHIFT]:
                while True:
                    self.screen.fill((0, 0, 0))
                    start(self.tileGenRect)
                    if keys[pygame.K_LSHIFT]:
                        break

            time = self.clock.tick() / 1000
            self.level.run(time)
            pygame.display.update()
