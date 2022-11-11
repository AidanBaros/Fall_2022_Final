from Map import *
from Home import *
from Rooms import *
from Player import *
from Monster import *
from startup import *

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screenSize = screen.get_size()
        self.clock = pygame.time.Clock()
        self.Runninf = True

    def run(self):
        while self.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                self.Running = False

            time = self.clock.tick() / 1000
            pygame.display.update()
