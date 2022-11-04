import pygame
import random

pygame.init()


class room:
    def __init__(
        self,
        roomtype,
        hallwayDirection,
        ID,
        screenX,
        screenY,
        screen,
        playerSize,
    ):
        self.hallwayDirection = hallwayDirection
        self.roomtype = roomtype
        self.screenX = screenX
        self.screenY = screenY
        self.screen = screen
        self.ID = ID
        self.playerSize = playerSize

        self.hallwaySize = self.screenX // 8
        self.WidthNoHallway = self.screenX // 2 - self.hallwaySize // 2
        self.HeightNoHallway = self.screenY // 2 - self.hallwaySize // 2
        self.WidthHallway = self.screenX // 2 + self.hallwaySize // 2
        self.HeightHallway = self.screenY // 2 + self.hallwaySize // 2
        self.offset = 0
        self.color = (255, 255, 255)

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (self.WidthNoHallway, self.HeightNoHallway, self.hallwaySize, self.hallwaySize),
        )
        if self.hallwayDirection[0] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (self.WidthNoHallway, 0, self.hallwaySize, self.HeightNoHallway),
            )
        if self.hallwayDirection[1] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (self.WidthHallway, self.HeightNoHallway, self.WidthNoHallway, self.hallwaySize),
            )
        if self.hallwayDirection[2] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (self.WidthNoHallway, self.HeightHallway, self.hallwaySize, self.HeightNoHallway),
            )
        if self.hallwayDirection[3] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (0, self.HeightNoHallway, self.WidthNoHallway, self.hallwaySize),
            )

        if self.ID == 0:
            self.color = (0, 0, 0)
        elif self.ID == 1 or self.ID == 2 or self.ID == 3 or self.ID == 4:
            self.offset = 200
        elif self.ID == 11 or self.ID == 12 or self.ID == 13 or self.ID == 14:
            self.offset = 300
        elif self.ID == 15:
            self.offset = 100

        if self.ID not in (5, 6, 7, 8, 9, 10):
            pygame.draw.rect(
                self.screen,
                self.color,
                (
                    self.offset,
                    self.offset,
                    self.screenX - (self.offset * 2),
                    self.screenY - (self.offset * 2),
                ),
            )

    def collision(self, playerPos):
        Colliding = False
        if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15):
            if self.hallwayDirection[0] == 1:
                if (
                    (
                        playerPos[1] >= self.offset 
                        and 
                        playerPos[0] >= self.offset
                    ) 
                    or 
                    (
                        playerPos[1] >= 0 
                        and 
                        playerPos[0] >= self.WidthNoHallway 
                        and
                        playerPos[0] + self.playerSize[0] <= self.WidthHallway
                    )
                    or 
                    (
                        playerPos[1] >= self.offset 
                        and 
                        playerPos[0] >= self.WidthHallway 
                        and
                        playerPos[0] + self.playerSize[0] <= self.screenX - self.offset
                    )
                ):
                    Colliding = False
                else:
                    Colliding = True
            if self.hallwayDirection[1] == 1:
                pass
            if self.hallwayDirection[2] == 1:
                pass
            if self.hallwayDirection[3] == 1:
                pass
        else:
            pass
        
        return Colliding



    """def collision(self, playerPos, direction):

        Colliding = False
        print(self.offset)

        if direction == "w":
            if self.hallwayDirection[0] == 1:
                if playerPos[1]:
                    pass
                pass
            if self.hallwayDirection[1] == 1:
                pass
            if self.hallwayDirection[3] == 1:
                pass

            pass
        if direction == "a":
            pass
        if direction == "s":
            pass
        if direction == "d":
            pass

        
        if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15) and playerPos[1] >= self.offset:
                Colliding = False
            elif self.hallwayDirection[0] == 1 and playerPos[1] >= 0:
                Colliding = False
            elif self.hallwayDirection[1] == 1 and playerPos[1] <= self.HeightNoHallway:
                Colliding = False
            elif self.hallwayDirection[2] == 1 and playerPos[1] >= 0:
                Colliding = False
            elif self.hallwayDirection[3] == 1 and playerPos[1] <= self.HeightNoHallway:
                Colliding = False
            else:
                Colliding = True
        

        if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15):
            if (
                playerPos[0] >= self.offset
                and playerPos[1] >= self.offset
                and playerPos[0] + self.playerSize[0] <= self.screenX - self.offset
                and playerPos[1] + self.playerSize[1] <= self.screenY - self.offset
            ):
                Colliding = False
            else:
                Colliding = True
        if self.hallwayDirection[0] == 1:
            if (
                playerPos[0] >= self.WidthNoHallway
                and playerPos[1] >= 0
                and playerPos[0] + self.playerSize[0]
                <= self.WidthNoHallway + self.hallwaySize
                and playerPos[1] + self.playerSize[1] <= self.HeightNoHallway
            ):
                Colliding = False
                print("3")
            else:
                Colliding = True
                print("4")
        if self.hallwayDirection[1] == 1:
            if (
                playerPos[0] >= self.WidthNoHallway + self.hallwaySize
                and playerPos[1] >= self.HeightNoHallway
                and playerPos[0] + self.playerSize[0] <= self.screenX
                and playerPos[1] + self.playerSize[1]
                <= self.HeightNoHallway + self.hallwaySize
            ):
                Colliding = False
                print("5")
            else:
                Colliding = True
                print("6")
        if self.hallwayDirection[2] == 1:
            if (
                playerPos[0] >= self.WidthNoHallway
                and playerPos[1] >= self.HeightNoHallway + self.hallwaySize
                and playerPos[0] + self.playerSize[0]
                <= self.WidthNoHallway + self.hallwaySize
                and playerPos[1] + self.playerSize[1] <= self.screenY
            ):
                Colliding = False
                print("7")
            else:
                Colliding = True
                print("8")
        if self.hallwayDirection[3] == 1:
            if (
                playerPos[0] >= 0
                and playerPos[1] >= self.HeightNoHallway
                and playerPos[0] + self.playerSize[0] <= self.WidthNoHallway
                and playerPos[1] + self.playerSize[1]
                <= self.HeightNoHallway + self.hallwaySize
            ):
                Colliding = False
                print("9")
            else:
                Colliding = True
                print("0")

        return Colliding"""
