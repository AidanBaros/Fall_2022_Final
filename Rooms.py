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

        self.monsterSpawnArea: list[pygame.Rect] = []

        self.w = False
        self.s = False
        self.a = False
        self.d = False

        self.monsterList: list[monster.Monster] = []

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

        if self.ID not in (5, 6, 7, 8, 9, 10):
            self.monsterSpawnArea.append(self.main_room)

        else:
            self.monsterSpawnArea.append(self.center_square)
            if self.hallwayDirection[0] == 1:
                self.monsterSpawnArea.append(self.top_hallway)
            if self.hallwayDirection[1] == 1:
                self.monsterSpawnArea.append(self.right_hallway)
            if self.hallwayDirection[2] == 1:
                self.monsterSpawnArea.append(self.bottom_hallway)
            if self.hallwayDirection[3] == 1:
                self.monsterSpawnArea.append(self.left_hallway)

        self.monsterGen()

    def monsterGen(self):
        monsterChance = random.randint(0, 15)
        numMonsters = 0
        if monsterChance <= 1:
            numMonsters = random.randint(1, 6)
        elif monsterChance <= 3:
            numMonsters = random.randint(1, 4)
        elif monsterChance <= 5:
            numMonsters = random.randint(1, 4)
        elif monsterChance <= 7:
            numMonsters = random.randint(1, 5)
        elif monsterChance <= 9:
            numMonsters = random.randint(5, 11)
        for _ in range(numMonsters):
            if len(self.monsterSpawnArea) > 1:
                indexPos = random.randint(0, len(self.monsterSpawnArea) - 1)
            else:
                indexPos = 0
            spawnX = random.randint(
                self.monsterSpawnArea[indexPos].x + 50,
                (
                    self.monsterSpawnArea[indexPos].x
                    + self.monsterSpawnArea[indexPos].width
                    - 50
                ),
            )
            spawnY = random.randint(
                self.monsterSpawnArea[indexPos].y + 50,
                (
                    self.monsterSpawnArea[indexPos].y
                    + self.monsterSpawnArea[indexPos].height
                    - 50
                ),
            )
            if monsterChance <= 1:
                self.monsterList.append(
                    monster.Spider(
                        self.playerMapPos,
                        self.screenSize,
                        (spawnX, spawnY),
                        self.collisionBoxList,
                    )
                )
            elif monsterChance <= 3:
                self.monsterList.append(
                    monster.Skeleton(
                        self.playerMapPos,
                        self.screenSize,
                        (spawnX, spawnY),
                        self.collisionBoxList,
                    )
                )
            elif monsterChance <= 5:
                self.monsterList.append(
                    monster.Zombie(
                        self.playerMapPos,
                        self.screenSize,
                        (spawnX, spawnY),
                        self.collisionBoxList,
                    )
                )
            elif monsterChance <= 7:
                self.monsterList.append(
                    monster.Slim(
                        self.playerMapPos,
                        self.screenSize,
                        (spawnX, spawnY),
                        self.collisionBoxList,
                    )
                )
            elif monsterChance <= 9:
                self.monsterList.append(
                    monster.Bat(
                        self.playerMapPos,
                        self.screenSize,
                        (spawnX, spawnY),
                        self.collisionBoxList,
                    )
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
        self.screen.fill("grey30")
        for i in range(len(self.collisionBoxList)):
            pygame.draw.rect(
                self.screen,
                ("grey10"),
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

    def update(self, time):
        self.draw()
        for i in self.monsterList:
            i.update(time)
        return self.collisionBoxList
