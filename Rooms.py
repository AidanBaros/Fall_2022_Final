import pygame
import random

pygame.init()


class room:
    def __init__(
        self,
        tile,
        screenSize,
        screen,
        playerSize,
    ):
        self.hallwayDirection = tile.sides
        self.ID = tile.ID
        self.screenX = screenSize[0]
        self.screenY = screenSize[1]
        self.screen = screen
        self.playerSize = playerSize
        self.collisionBoxList: list[pygame.Rect] = []
        self.RoomYes = [1, 2, 3, 4, 11, 12, 13, 14, 15]
        self.RoomNo = [5, 6, 7, 8, 9, 10]

        self.hallwaySize = self.screenX // 8
        self.WidthNoHallway = self.screenX // 2 - self.hallwaySize // 2
        self.HeightNoHallway = self.screenY // 2 - self.hallwaySize // 2
        self.WidthHallway = self.screenX // 2 + self.hallwaySize // 2
        self.HeightHallway = self.screenY // 2 + self.hallwaySize // 2
        self.offset = 0
        self.color = (255, 255, 255)

        self.w = False
        self.s = False
        self.a = False
        self.d = False

        # SET OFFSET
        if self.ID == 1:
            self.offset = 200
        elif self.ID == 2:
            self.offset = 200
        elif self.ID == 3:
            self.offset = 200
        elif self.ID == 4:
            self.offset = 200
        elif self.ID == 11:
            self.offset = 300
        elif self.ID == 12:
            self.offset = 300
        elif self.ID == 13:
            self.offset = 300
        elif self.ID == 14:
            self.offset = 300
        elif self.ID == 15:
            self.offset = 100

        # COLLISION BOXS
        self.CornerTL = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.CornerTR = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.CornerBR = pygame.Rect(
            self.WidthHallway,
            self.HeightHallway,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
        self.CornerBL = pygame.Rect(
            0,
            self.HeightHallway,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
        self.TopNR = pygame.Rect(
            0,
            0,
            self.screenX,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.BottomNR = pygame.Rect(
            0,
            self.HeightHallway,
            self.screenX,
            self.HeightNoHallway,
        )
        self.LeftNR = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.screenY,
        )
        self.RightNR = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.screenY,
        )

        self.TLT = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.offset - playerSize[1] + (playerSize[1] // 4),
        )
        self.TLL = pygame.Rect(
            0,
            0,
            self.offset,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.TRT = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.offset - playerSize[1] + (playerSize[1] // 4),
        )
        self.TRR = pygame.Rect(
            self.screenX - self.offset,
            0,
            self.offset,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.BRR = pygame.Rect(
            self.screenX - self.offset,
            self.HeightHallway,
            self.offset,
            self.HeightNoHallway,
        )
        self.BRB = pygame.Rect(
            self.WidthHallway,
            self.screenY - self.offset,
            self.WidthNoHallway,
            self.offset,
        )
        self.BLL = pygame.Rect(
            0,
            self.HeightHallway,
            self.offset,
            self.HeightNoHallway,
        )
        self.BLB = pygame.Rect(
            0,
            self.screenY - self.offset,
            self.WidthNoHallway,
            self.offset,
        )
        self.TopR = pygame.Rect(
            0,
            0,
            self.screenX,
            self.offset - playerSize[1] + (playerSize[1] // 4),
        )
        self.BottomR = pygame.Rect(
            0,
            self.screenY - self.offset,
            self.screenX,
            self.offset,
        )
        self.LeftR = pygame.Rect(
            0,
            0,
            self.offset,
            self.screenY,
        )
        self.RightR = pygame.Rect(
            self.screenX - self.offset,
            0,
            self.offset,
            self.screenY,
        )

        if self.ID == 1:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BottomR)
        elif self.ID == 2:
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.LeftR)
        elif self.ID == 3:
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 4:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.RightR)
        elif self.ID == 5:
            self.collisionBoxList.append(self.TopNR)
            self.collisionBoxList.append(self.BottomNR)
        elif self.ID == 6:
            self.collisionBoxList.append(self.LeftNR)
            self.collisionBoxList.append(self.RightNR)
        elif self.ID == 7:
            self.collisionBoxList.append(self.CornerTR)
            self.collisionBoxList.append(self.BottomNR)
            self.collisionBoxList.append(self.LeftNR)
        elif self.ID == 8:
            self.collisionBoxList.append(self.CornerBR)
            self.collisionBoxList.append(self.TopNR)
            self.collisionBoxList.append(self.LeftNR)
        elif self.ID == 9:
            self.collisionBoxList.append(self.CornerBL)
            self.collisionBoxList.append(self.TopNR)
            self.collisionBoxList.append(self.RightNR)
        elif self.ID == 10:
            self.collisionBoxList.append(self.CornerTL)
            self.collisionBoxList.append(self.BottomNR)
            self.collisionBoxList.append(self.RightNR)
        elif self.ID == 11:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.RightR)
            self.collisionBoxList.append(self.LeftR)
            self.collisionBoxList.append(self.BottomR)
        elif self.ID == 12:
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.LeftR)
            self.collisionBoxList.append(self.BottomR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 13:
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.RightR)
            self.collisionBoxList.append(self.LeftR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 14:
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.RightR)
            self.collisionBoxList.append(self.BottomR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 15:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BLB)

        # Playable area rects
        self.center_square = pygame.Rect(
            self.WidthNoHallway,
            self.HeightNoHallway,
            self.hallwaySize,
            self.hallwaySize,
        )
        self.main_room = pygame.Rect(
            self.offset,
            self.offset,
            self.screenX - (self.offset * 2),
            self.screenY - (self.offset * 2),
        )
        self.top_hallway = pygame.Rect(
            self.WidthNoHallway, 0, self.hallwaySize, self.HeightNoHallway
        )
        self.right_hallway = pygame.Rect(
            self.WidthHallway,
            self.HeightNoHallway,
            self.WidthNoHallway,
            self.hallwaySize,
        )
        self.bottom_hallway = pygame.Rect(
            self.WidthNoHallway,
            self.HeightHallway,
            self.hallwaySize,
            self.HeightNoHallway,
        )
        self.left_hallway = pygame.Rect(
            0, self.HeightNoHallway, self.WidthNoHallway, self.hallwaySize
        )

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i in range(len(self.collisionBoxList)):
            pygame.draw.rect(
                self.screen,
                (
                    50 + (25*i),
                    50 + (25*i),
                    50 + (25*i),
                ),
                self.collisionBoxList[i],
            )
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            self.center_square,
        )
        if self.hallwayDirection[0] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.top_hallway,
            )
        if self.hallwayDirection[1] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.right_hallway,
            )
        if self.hallwayDirection[2] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.bottom_hallway,
            )
        if self.hallwayDirection[3] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.left_hallway,
            )
        if self.ID not in (5, 6, 7, 8, 9, 10):
            pygame.draw.rect(
                self.screen,
                self.color,
                self.main_room,
            )

    def collision(self, player: pygame.Rect, PlayerSpeed):
        returnVal = False
        for i in self.collisionBoxList:
            if player.colliderect(i):
                if player.top < i.bottom and (player.top + PlayerSpeed >= i.bottom):
                    player.top = i.bottom
                elif player.left < i.right and (player.left + PlayerSpeed >= i.right):
                    player.left = i.right
                elif player.bottom > i.top and (player.bottom - PlayerSpeed <= i.top):
                    player.bottom = i.top
                elif player.right > i.left and (player.right - PlayerSpeed <= i.left):
                    player.right = i.left
                returnVal = True


        return returnVal
