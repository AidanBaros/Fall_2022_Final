import pygame
from player import Player
from map import *
from settings import *
from rooms import Room

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.setup()

        self.roomList: list[Room] = []

        self.playerMapPos = ()


    def setup(self):
        grid = makeGrid(self.screen, XTC, YTC)

        ranX = random.randint(0, XTC - 1)
        ranY = random.randint(0, YTC - 1)

        while True:
            try:
                if grid[ranY][ranX].tile.ID == 0:
                    ranX = random.randint(0, XTC)
                    ranY = random.randint(0, YTC)
                else:
                    break
            except:
                ranX = random.randint(0, XTC)
                ranY = random.randint(0, YTC)

        self.playerMapPos = (ranX,ranY)

        self.player = Player(self.screen, grid[self.playerMapPos[0]][self.playerMapPos[1]])

        for i in range(YTC):
            self.roomList.append([])
            for j in range(XTC):
                self.roomList[i].append(
                    Room(
                        grid[i][j].tile,
                        (SCREENX, SCREENY),
                        self.screen,
                        (Player.rect.width, Player.rect.height),
                    )
                )

    def run(self, time):
        self.screen.fill("black")
        self.player.update(time)