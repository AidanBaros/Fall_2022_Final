import pygame
import random

pygame.init()


class room:
    def __init__(self, roomtype, screenX, screenY, screen):
        self.roomtype = roomtype
        self.screenX = screenX
        self.screenY = screenY
        self.screen = screen

    def draw(self):
        hallwaySize = self.screenX // 8
        Width = self.screenX // 2 - hallwaySize // 2
        Height = self.screenY // 2 - hallwaySize // 2
        xPoint = self.screenX // 2 + hallwaySize // 2
        yPoint = self.screenY // 2 + hallwaySize // 2
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, Width, Height))
        pygame.draw.rect(self.screen, (0, 0, 0), (xPoint, 0, Width, Height))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, yPoint, Width, Height))
        pygame.draw.rect(self.screen, (0, 0, 0), (xPoint, yPoint, Width, Height))
