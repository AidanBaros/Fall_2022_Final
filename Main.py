"""from map import *
from home import *
from rooms import *
from player import *
from monster import *
from startup import *"""
from level import *

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screenSize = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.SCREENX = self.screenSize[0]
        self.SCREENY = self.screenSize[1]
        self.YTC = 10
        self.XTC = 15
        self.level = Level()
        self.Running = True

    def run(self):
        while self.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                self.Running = False

            time = self.clock.tick() / 1000
            self.level.run()
            pygame.display.update()
