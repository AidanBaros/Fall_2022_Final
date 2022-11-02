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
XPos = 0
YPos = 0

roomList = []

grid = makeGrid(screenX, screenY, screen, XTC, YTC)

for i in range(YTC):
    roomList.append([])
    for j in range(XTC):
        roomList[i].append(room(0,grid[i][j].tile.sides, screenX, screenY, screen))

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    screen.fill((0, 0, 0))

    roomList[YPos][XPos].draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        while True:
            screen.fill((0, 0, 0))
            start(screenY, XTC, YTC)
            if keys[pygame.K_LSHIFT]:
                break
    if keys[pygame.K_LCTRL]:
        Running = False

    if keys[pygame.K_LEFT] and XPos > 0:
        XPos -= 1
    if keys[pygame.K_RIGHT] and XPos < XTC - 1:
        XPos += 1
    if keys[pygame.K_UP] and YPos > 0:
        YPos -= 1
    if keys[pygame.K_DOWN] and YPos < YTC - 1:
        YPos += 1

    

    pygame.display.flip()
