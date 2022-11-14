from map import *
from home import *
from rooms import *
from player import *
from monster import *

import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Wave Function Collapse")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screenX, screenY = screen.get_size()
    Running = True

    YTC = 10
    XTC = 15

    roomList: list[room] = []

    grid = makeGrid(screenX, screenY, screen, XTC, YTC)

    ranX = random.randint(0, XTC - 1)
    ranY = random.randint(0, YTC - 1)

    """
    print(f"{ranY}, {ranX}")

    for i in range(YTC):
        for j in range(XTC):
            print(grid[i][j].tile.ID, end=",")
        print()"""

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

    player = pygame.Rect(screenX // 2 - 25, screenY // 2 - 50, 50, 100)

    PlayerSpeed = int(screenX // 750)
    # PlayerSpeed = 7

    for i in range(YTC):
        roomList.append([])
        for j in range(XTC):
            roomList[i].append(
                room(
                    grid[i][j].tile,
                    (screenX, screenY),
                    screen,
                    (player.width, player.height),
                )
            )

    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        screen.fill((0, 0, 0))

        roomList[MapYPos][MapXPos].draw()

        pygame.draw.rect(screen, (255, 0, 0), player)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            while True:
                screen.fill((0, 0, 0))
                start(screenY, XTC, YTC)
                if keys[pygame.K_LSHIFT]:
                    break
        if keys[pygame.K_LCTRL]:
            Running = False

        if player.x <= 0 and grid[MapYPos][MapXPos].tile.sides[3] == 1:
            MapXPos -= 1
            player.x = screenX - player.w - 10
            player.y = screenY // 2 - player.height // 2
        if player.x >= screenX - player.w and grid[MapYPos][MapXPos].tile.sides[1] == 1:
            MapXPos += 1
            player.x = 10
            player.y = screenY // 2 - player.height // 2
        if player.y <= 0 and grid[MapYPos][MapXPos].tile.sides[0] == 1:
            MapYPos -= 1
            player.x = screenX // 2 - player.width // 2
            player.y = screenY - player.h - 10
        if player.y >= screenY - player.h and grid[MapYPos][MapXPos].tile.sides[2] == 1:
            MapYPos += 1
            player.x = screenX // 2 - player.width // 2
            player.y = 10

        if keys[pygame.K_a] and player.left >= 0:
            player.x -= PlayerSpeed
        if keys[pygame.K_d] and player.right <= screenX:
            player.x += PlayerSpeed
        if keys[pygame.K_w] and player.top >= 0:
            player.y -= PlayerSpeed
        if keys[pygame.K_s] and player.bottom <= screenY:
            player.y += PlayerSpeed

        roomList[MapYPos][MapXPos].collision(player, PlayerSpeed)

        pygame.display.flip()
