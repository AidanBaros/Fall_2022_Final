import pygame
import random

pygame.init()


class room:
    def __init__(self, roomtype, hallwayDirection, ID, screenX, screenY, screen):
        self.hallwayDirection = hallwayDirection
        self.roomtype = roomtype
        self.screenX = screenX
        self.screenY = screenY
        self.screen = screen
        self.ID = ID

    def draw(self):
        hallwaySize = self.screenX // 8
        Width = self.screenX // 2 - hallwaySize // 2
        Height = self.screenY // 2 - hallwaySize // 2
        xPoint = self.screenX // 2 + hallwaySize // 2
        yPoint = self.screenY // 2 + hallwaySize // 2
        """self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, Width, Height))
        pygame.draw.rect(self.screen, (0, 0, 0), (xPoint, 0, Width, Height))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, yPoint, Width, Height))
        pygame.draw.rect(self.screen, (0, 0, 0), (xPoint, yPoint, Width, Height))"""
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(
            self.screen, (255, 255, 255), (Width, Height, hallwaySize, hallwaySize)
        )
        if self.hallwayDirection[0] == 1:
            pygame.draw.rect(
                self.screen, (255, 255, 255), (Width, 0, hallwaySize, Height)
            )
        if self.hallwayDirection[1] == 1:
            pygame.draw.rect(
                self.screen, (255, 255, 255), (xPoint, Height, Width, hallwaySize)
            )
        if self.hallwayDirection[2] == 1:
            pygame.draw.rect(
                self.screen, (255, 255, 255), (Width, yPoint, hallwaySize, Height)
            )
        if self.hallwayDirection[3] == 1:
            pygame.draw.rect(
                self.screen, (255, 255, 255), (0, Height, Width, hallwaySize)
            )

        if self.hallwayDirection == [0, 0, 0, 0]:
            pygame.draw.rect(
                self.screen, (0, 0, 0), (Width, Height, hallwaySize, hallwaySize)
            )

        if self.ID == 1 or self.ID == 2 or self.ID == 3 or self.ID == 4:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (200, 200, self.screenX - 400, self.screenY - 400),
            )
        elif self.ID == 11 or self.ID == 12 or self.ID == 13 or self.ID == 14:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (300, 300, self.screenX - 600, self.screenY - 600),
            )
        elif self.ID == 15:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (100, 100, self.screenX - 200, self.screenY - 200),
            )

        # print(self.hallwayDirection)
