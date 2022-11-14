import random
import pygame
from map import *
from rooms import *
from player import *
from settings import *


pygame.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

YTC = 10
XTC = 15

roomList: list[Room] = []

grid = makeGrid(screen, XTC, YTC)

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

MapXPos = ranX
MapYPos = ranY

Player()

for i in range(YTC):
    roomList.append([])
    for j in range(XTC):
        roomList[i].append(
            Room(
                grid[i][j].tile,
                (SCREENX, SCREENY),
                screen,
                (Player.rect.width, Player.rect.height),
            )
        )
