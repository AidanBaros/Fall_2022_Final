import pygame
import random
import copy
import numpy as np

pygame.init()


class Tile:
    def __init__(self, fileName: str, sideValues: list, ID, Weight):
        self.image = pygame.image.load("HalfTiles/" + fileName)
        self.image = self.image.copy()
        self.sides = sideValues
        self.name = fileName
        self.ID = ID
        self.Weight = Weight


TileImages = [
    Tile("Tile0.png", [0, 0, 0, 0], 0, 10),
    Tile("Tile1.png", [1, 1, 0, 1], 1, 4),
    Tile("Tile2.png", [1, 1, 1, 0], 2, 4),
    Tile("Tile3.png", [0, 1, 1, 1], 3, 4),
    Tile("Tile4.png", [1, 0, 1, 1], 4, 4),
    Tile("Tile5.png", [0, 1, 0, 1], 5, 10),
    Tile("Tile6.png", [1, 0, 1, 0], 6, 10),
    Tile("Tile7.png", [1, 1, 0, 0], 7, 2),
    Tile("Tile8.png", [0, 1, 1, 0], 8, 2),
    Tile("Tile9.png", [0, 0, 1, 1], 9, 2),
    Tile("Tile10.png", [1, 0, 0, 1], 10, 2),
    Tile("Tile11.png", [1, 0, 0, 0], 11, 0),
    Tile("Tile12.png", [0, 1, 0, 0], 12, 0),
    Tile("Tile13.png", [0, 0, 1, 0], 13, 0),
    Tile("Tile14.png", [0, 0, 0, 1], 14, 0),
    Tile("Tile15.png", [1, 1, 1, 1], 15, 7),
]


class Space:
    def __init__(self, xpos: int, ypos: int, Yscale: int):
        self.collapsed = False
        self.possibilities = copy.copy(TileImages)
        self.pos = (xpos, ypos)
        self.entropy = len(TileImages)
        self.tile: Tile
        self.Yscale = Yscale
        self.screen = pygame.display.get_surface()
        #self.PlayerMapPos = PlayerMapPos

    def draw(self,i,j,PlayerMapPos: tuple[int,int]):
        if self.collapsed:
            pygame.draw.rect(self.screen,(255,0,0),(self.pos[0],self.pos[1],self.Yscale,self.Yscale))
            self.tile.image = pygame.transform.scale(
                self.tile.image, (self.Yscale, self.Yscale)
            )
            if j == PlayerMapPos[0] and i == PlayerMapPos[1]:
                self.tile.image.set_colorkey((255,255,255))
            else:
                self.tile.image.set_colorkey(None)
            self.screen.blit(self.tile.image, self.pos)

    def collapse(self):
        if len(self.possibilities) != 0:
            self.collapsed = True
            self.tile = self.possibilities[Weights(self.possibilities)]
            return


def determine_possibilities():
    filter = []
    isDone = True
    for i, rows in enumerate(grid):
        for j, tile in enumerate(rows):
            if tile.collapsed == False:
                filter = copy.copy(tile.possibilities)
                isDone = False
                if j == len(grid[i]) - 1:
                    for possibility in tile.possibilities:
                        if possibility.sides[1] == 1:
                            filter.remove(possibility)
                elif j + 1 < len(grid[i]):
                    if grid[i][j + 1].collapsed:
                        for possibility in tile.possibilities:
                            if grid[i][j + 1].tile.sides[3] != possibility.sides[1]:
                                filter.remove(possibility)
                if j == 0:
                    for possibility in tile.possibilities:
                        if possibility.sides[3] == 1:
                            filter.remove(possibility)
                elif j - 1 >= 0:
                    if grid[i][j - 1].collapsed:
                        for possibility in tile.possibilities:
                            if grid[i][j - 1].tile.sides[1] != possibility.sides[3]:
                                filter.remove(possibility)
                if i + 1 == len(grid):
                    for possibility in tile.possibilities:
                        if possibility.sides[2] == 1 and possibility in filter:
                            filter.remove(possibility)
                elif i + 1 < len(grid):
                    if grid[i + 1][j].collapsed:
                        for possibility in tile.possibilities:
                            if grid[i + 1][j].tile.sides[0] != possibility.sides[2]:
                                filter.remove(possibility)
                if i == 0:
                    for possibility in tile.possibilities:
                        if possibility.sides[0] == 1 and possibility in filter:
                            filter.remove(possibility)
                elif i - 1 >= 0:
                    if grid[i - 1][j].collapsed:
                        for possibility in tile.possibilities:
                            if grid[i - 1][j].tile.sides[2] != possibility.sides[0]:
                                filter.remove(possibility)
            tile.possibilities = copy.copy(filter)
            tile.entropy = len(tile.possibilities)
    return isDone


def collapse():
    lowestEntropy = len(TileImages)
    lowestList = []
    for i, rows in enumerate(grid):
        for j, tile in enumerate(rows):
            if tile.collapsed == False:
                if tile.entropy < lowestEntropy:
                    lowestEntropy = tile.entropy
    for i, rows in enumerate(grid):
        for j, tile in enumerate(rows):
            if tile.collapsed == False:
                if tile.entropy == lowestEntropy:
                    lowestList.append(tile)
    if len(lowestList) != 0:
        randomSlot = random.randint(0, len(lowestList) - 1)
        lowestList[randomSlot].collapse()
        return


def Weights(possibilities: list[Tile]):
    Weights = []
    GeneratorNum = 0
    Counter = 0
    for i in possibilities:
        if i.Weight > 0:
            for j in range(i.Weight):
                Weights.append(Counter)
        GeneratorNum += i.Weight
        Counter += 1
    ran = random.randint(0, GeneratorNum)
    if ran <= 0 and len(Weights) != 0:
        return Weights[ran]
    elif len(Weights) != 0:
        return Weights[ran - 1]
    else:
        return 0


def makeGrid(
    screen: pygame.Surface, tileGenRect: tuple[int, int], screenSize: tuple[int, int]
) -> list[Space]:
    global done
    global grid
    done = False
    grid = []
    sizeY = screenSize[1] // tileGenRect[1]
    offset = (screenSize[0] - (sizeY * tileGenRect[0])) // 2
    sizeX = sizeY
    for i in range(tileGenRect[1]):
        grid.append([])
        for j in range(tileGenRect[0]):
            grid[i].append(Space((j * sizeX) + offset, i * sizeY, sizeY))

    while not done:
        done = determine_possibilities()
        collapse()
    return grid


def start(tileGenRect: tuple[int, int],PlayerMapPos: tuple[int, int]):
    for i in range(tileGenRect[1]):
        for j in range(tileGenRect[0]):
            grid[i][j].draw(i,j,PlayerMapPos)
