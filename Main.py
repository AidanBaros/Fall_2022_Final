from Map import *
from Home import *
from Rooms import *
from Player import *
from Monster import *

import pygame

pygame.init()
pygame.display.set_caption("Wave Function Collapse")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screenX, screenY = screen.get_size()
Running = True

YTC = 10
XTC = int(YTC * 1.5)

roomList = []

grid = makeGrid(screenX, screenY, screen, XTC, YTC)

ranX = random.randint(0, XTC - 1)
ranY = random.randint(0, YTC - 1)

while True:
    if grid[ranY][ranX].tile.sides == [0, 0, 0, 0]:
        ranX = random.randint(0, XTC)
        ranY = random.randint(0, YTC)
    else:
        MapXPos = ranX
        MapYPos = ranY
        break

XPos = screenX // 2
YPos = screenY // 2
PlayerSizeX = 50
PlayerSizeY = 100

PlayerSpeed = int(screenX // 750)

for i in range(YTC):
    roomList.append([])
    for j in range(XTC):
        roomList[i].append(
            room(
                0,
                grid[i][j].tile.sides,
                grid[i][j].tile.ID,
                screenX,
                screenY,
                screen,
                (PlayerSizeX, PlayerSizeY),
            )
        )

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    screen.fill((0, 0, 0))

    roomList[MapYPos][MapXPos].draw()

    pygame.draw.rect(screen, (255, 0, 0), (XPos, YPos, PlayerSizeX, PlayerSizeY))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        while True:
            screen.fill((0, 0, 0))
            start(screenY, XTC, YTC)
            if keys[pygame.K_LSHIFT]:
                break
    if keys[pygame.K_LCTRL]:
        Running = False

    if XPos == 0 and grid[MapYPos][MapXPos].tile.sides[3] == 1:
        MapXPos -= 1
        XPos = screenX - PlayerSizeX - 10
    if XPos == screenX - PlayerSizeX and grid[MapYPos][MapXPos].tile.sides[1] == 1:
        MapXPos += 1
        XPos = 10
    if YPos == 0 and grid[MapYPos][MapXPos].tile.sides[0] == 1:
        MapYPos -= 1
        YPos = screenY - PlayerSizeY - 10
    if YPos == screenY - PlayerSizeY and grid[MapYPos][MapXPos].tile.sides[2] == 1:
        MapYPos += 1
        YPos = 10

    if (
        keys[pygame.K_a]
        and XPos > 0
        and roomList[MapYPos][MapXPos].collision((XPos, YPos)) == False
    ):
        XPos -= PlayerSpeed
    if (
        keys[pygame.K_d]
        and XPos < screenX - PlayerSizeX
        and roomList[MapYPos][MapXPos].collision((XPos, YPos)) == False
    ):
        XPos += PlayerSpeed
    if (
        keys[pygame.K_w]
        and YPos > 0
        and roomList[MapYPos][MapXPos].collision((XPos, YPos)) == False
    ):
        YPos -= PlayerSpeed
    if (
        keys[pygame.K_s]
        and YPos < screenY - PlayerSizeY
        and roomList[MapYPos][MapXPos].collision((XPos, YPos)) == False
    ):
        YPos += PlayerSpeed

    pygame.display.flip()
