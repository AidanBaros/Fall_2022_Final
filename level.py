import pygame
import numpy
from map import *
from home import *
from rooms import Room
from player import Player
from monster import *
from startup import *


class Level:
    def __init__(self, screenSize: tuple[int, int], tileGenRect: tuple[int, int]):
        self.screen = pygame.display.get_surface()

        self.screenSize = screenSize
        self.tileGenRect = tileGenRect

        self.roomList: list[list[Room]] = []

        self.collisionBoxList: list[pygame.Rect] = []

        self.playerMapPos = ()

        self.setup()

    def setup(self):

        grid: list[list[Space]] = makeGrid(
            self.screen, self.tileGenRect, self.screenSize
        )
        ranX = random.randint(0, self.tileGenRect[0] - 1)
        ranY = random.randint(0, self.tileGenRect[1] - 1)
        while True:
            try:
                if grid[ranY][ranX].tile.ID == 0:
                    ranX = random.randint(0, self.tileGenRect[0])
                    ranY = random.randint(0, self.tileGenRect[1])
                else:
                    break
            except:
                ranX = random.randint(0, self.tileGenRect[0])
                ranY = random.randint(0, self.tileGenRect[1])

        self.playerMapPos = [ranX, ranY]

        self.CheckForIslands(self.playerMapPos, grid)

        for Z in range(self.tileGenRect[1]):
            for V in range(self.tileGenRect[0]):
                print(f"{grid[Z][V].tile.ID}, {grid[Z][V].tile.checked} | ", end="")
            print()



        """if not grid[Z][V].tile.checked and grid[Z][V].tile.ID != 0:
                    print("Goodbye islands")
                    #self.setup()
                    #return
        print("No islands")"""

        self.player = Player(self.screen, self.playerMapPos, self.screenSize)

        for i in range(self.tileGenRect[1]):
            self.roomList.append([])
            for j in range(self.tileGenRect[0]):
                self.roomList[i].append(
                    Room(
                        grid[i][j].tile,
                        self.screenSize,
                        self.screen,
                        (self.player.rect.width, self.player.rect.height),
                    )
                )

    def CheckForIslands(self, Pos: tuple[int, int], grid: list[list[Space]]):
        x = Pos[0]
        left = Pos[0] - 1
        right = Pos[0] + 1
        y = Pos[1]
        up = Pos[1] - 1
        down = Pos[1] + 1

        grid[y][x].tile.checked = True

        if grid[y][x].tile.sides[0] == 1 and not grid[up][x].tile.checked:
            self.CheckForIslands((x, up), grid)

        if grid[y][x].tile.sides[2] == 1 and not grid[down][x].tile.checked:
            self.CheckForIslands((x, down), grid)

        if grid[y][x].tile.sides[1] == 1 and not grid[y][right].tile.checked:
            self.CheckForIslands((right, y), grid)

        if grid[y][x].tile.sides[3] == 1 and not grid[y][left].tile.checked:
            self.CheckForIslands((left, y), grid)

    def run(self, time: float):
        self.screen.fill("black")
        self.collisionBoxList: list[pygame.Rect] = self.roomList[self.playerMapPos[1]][
            self.playerMapPos[0]
        ].update()
        self.player.getCollisionBoxList(self.collisionBoxList)
        self.player.update(time, self.roomList)
