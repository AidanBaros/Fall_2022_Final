import pygame
import random
from map import Tile
import monster

pygame.init()


class Room:
    def __init__(
        self,
        tile: Tile,
        screenSize: tuple[int, int],
        screen: pygame.Surface,
        playerSize: tuple[int, int],
        playerMapPos: list[int, int],
    ):
        self.hallwayDirection = tile.sides
        self.ID = tile.ID
        self.screenX = screenSize[0]
        self.screenY = screenSize[1]
        self.screenSize = screenSize
        self.screen = screen
        self.playerSize = playerSize
        self.playerMapPos = playerMapPos
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

        monsterSpawnArea:list[tuple[int,int]] = []

        self.w = False
        self.s = False
        self.a = False
        self.d = False

        self.monsterList = []

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
            self.tile1()
        elif self.ID == 2:
            self.tile2()
        elif self.ID == 3:
            self.tile3()
        elif self.ID == 4:
            self.tile4()
        elif self.ID == 5:
            self.tile5()
        elif self.ID == 6:
            self.tile6()
        elif self.ID == 7:
            self.tile7()
        elif self.ID == 8:
            self.tile8()
        elif self.ID == 9:
            self.tile9()
        elif self.ID == 10:
            self.tile10()
        elif self.ID == 11:
            self.tile11()
        elif self.ID == 12:
            self.tile12()
        elif self.ID == 13:
            self.tile13()
        elif self.ID == 14:
            self.tile14()
        elif self.ID == 15:
            self.tile15()

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

        self.monsterGen(screen, playerMapPos, screenSize)

    def monsterGen(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
    ):
        monsterChance = random.randint(0, 15)
        numMonsters = 0
        if monsterChance <= 1:
            numMonsters = random.randint(0, 5)
            for _ in range(numMonsters):
                self.monsterList.append(
                    monster.Spider(self.screen, self.playerMapPos, self.screenSize)
                )

    def tile1(self):
        self.collisionBoxList.append(self.TLT)
        self.collisionBoxList.append(self.TLL)
        self.collisionBoxList.append(self.TRT)
        self.collisionBoxList.append(self.TRR)
        self.collisionBoxList.append(self.BLL)
        self.collisionBoxList.append(self.BRR)
        self.collisionBoxList.append(self.BottomR)

    def tile2(self):
        self.collisionBoxList.append(self.BRR)
        self.collisionBoxList.append(self.BRB)
        self.collisionBoxList.append(self.TRT)
        self.collisionBoxList.append(self.TRR)
        self.collisionBoxList.append(self.BLB)
        self.collisionBoxList.append(self.TLT)
        self.collisionBoxList.append(self.LeftR)

    def tile3(self):
        self.collisionBoxList.append(self.BLL)
        self.collisionBoxList.append(self.BLB)
        self.collisionBoxList.append(self.BRR)
        self.collisionBoxList.append(self.BRB)
        self.collisionBoxList.append(self.TLL)
        self.collisionBoxList.append(self.TRR)
        self.collisionBoxList.append(self.TopR)

    def tile4(self):
        self.collisionBoxList.append(self.TLT)
        self.collisionBoxList.append(self.TLL)
        self.collisionBoxList.append(self.BLL)
        self.collisionBoxList.append(self.BLB)
        self.collisionBoxList.append(self.TRT)
        self.collisionBoxList.append(self.BRB)
        self.collisionBoxList.append(self.RightR)

    def tile5(self):
        self.collisionBoxList.append(self.TopNR)
        self.collisionBoxList.append(self.BottomNR)

    def tile6(self):
        self.collisionBoxList.append(self.LeftNR)
        self.collisionBoxList.append(self.RightNR)

    def tile7(self):
        self.collisionBoxList.append(self.CornerTR)
        self.collisionBoxList.append(self.BottomNR)
        self.collisionBoxList.append(self.LeftNR)

    def tile8(self):
        self.collisionBoxList.append(self.CornerBR)
        self.collisionBoxList.append(self.TopNR)
        self.collisionBoxList.append(self.LeftNR)

    def tile9(self):
        self.collisionBoxList.append(self.CornerBL)
        self.collisionBoxList.append(self.TopNR)
        self.collisionBoxList.append(self.RightNR)

    def tile10(self):
        self.collisionBoxList.append(self.CornerTL)
        self.collisionBoxList.append(self.BottomNR)
        self.collisionBoxList.append(self.RightNR)

    def tile11(self):
        self.collisionBoxList.append(self.TLT)
        self.collisionBoxList.append(self.TRT)
        self.collisionBoxList.append(self.RightR)
        self.collisionBoxList.append(self.LeftR)
        self.collisionBoxList.append(self.BottomR)

    def tile12(self):
        self.collisionBoxList.append(self.BRR)
        self.collisionBoxList.append(self.TRR)
        self.collisionBoxList.append(self.LeftR)
        self.collisionBoxList.append(self.BottomR)
        self.collisionBoxList.append(self.TopR)

    def tile13(self):
        self.collisionBoxList.append(self.BRB)
        self.collisionBoxList.append(self.BLB)
        self.collisionBoxList.append(self.RightR)
        self.collisionBoxList.append(self.LeftR)
        self.collisionBoxList.append(self.TopR)

    def tile14(self):
        self.collisionBoxList.append(self.TLL)
        self.collisionBoxList.append(self.BLL)
        self.collisionBoxList.append(self.RightR)
        self.collisionBoxList.append(self.BottomR)
        self.collisionBoxList.append(self.TopR)

    def tile15(self):
        self.collisionBoxList.append(self.TLT)
        self.collisionBoxList.append(self.TLL)
        self.collisionBoxList.append(self.BRR)
        self.collisionBoxList.append(self.BRB)
        self.collisionBoxList.append(self.TRR)
        self.collisionBoxList.append(self.TRT)
        self.collisionBoxList.append(self.BLL)
        self.collisionBoxList.append(self.BLB)

    def draw(self):
        self.screen.fill((0, 0, 0))
        """for i in range(len(self.collisionBoxList)):
            pygame.draw.rect(
                self.screen,
                (
                    50 + (25*i),
                    50 + (25*i),
                    50 + (25*i),
                ),
                self.collisionBoxList[i],
            )"""
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

    def update(self):
        self.draw()
        return self.collisionBoxList
