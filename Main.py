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

r1 = room(0, screenX, screenY, screen)

grid = makeGrid(screenX, screenY, screen, XTC, YTC)


while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        while True:
            start(screenY, XTC, YTC)
            if keys[pygame.K_LSHIFT]:
                break
    if keys[pygame.K_LCTRL]:
        Running = False

    r1.draw()
    pygame.display.flip()
