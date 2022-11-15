import pygame
from map import *
from home import *
from rooms import Room
from player import Player
from monster import *
from startup import *


class Level:
    def __init__(self, screenSize:tuple[int,int], tileGenRect:tuple[int,int]):
        self.screen = pygame.display.get_surface()

        self.screenSize = screenSize
        self.tileGenRect = tileGenRect

        self.roomList: list[list[Room]] = []

        self.playerMapPos = ()

        self.setup()

    def setup(self):
        grid = makeGrid(self.screen, self.tileGenRect, self.screenSize)

        ranX = random.randint(0, self.tileGenRect[0] - 1)
        ranY = random.randint(0, self.tileGenRect[1] - 1)

        while True:
            try:
                if grid[ranY][ranX].tile.ID == 0:
                    ranX = random.randint(0, self.tileGenRect[0])
                    ranY = random.randint(0, self.tileGenRect[1])
                    print("test")
                else:
                    break
            except:
                ranX = random.randint(0, self.tileGenRect[0])
                ranY = random.randint(0, self.tileGenRect[1])

        self.playerMapPos = (ranX, ranY)

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

    def run(self, time: float):
        self.screen.fill("black")
        self.player.update(time, self.roomList)
        self.roomList[self.playerMapPos[0]][self.playerMapPos[1]].update(self.player.rect)
